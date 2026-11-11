# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# # Refresh harness
# Runs one variant of the refresh lab: update from Git, check the model and its `DataTag`, full refresh,
# read the monitoring logs (F64 only), compare, and record one row per refresh.
# Started by `harness/run_variant.py` through the Job Scheduler API, or by hand (see `docs/harness.md`).
# Runs as the user who starts it. One variant per run.

# PARAMETERS CELL ********************

variant = "v00-baseline"      # model folder and semantic model name
data_tag = "data-1m-v1"       # DataTag committed in the variant's TMDL; the model must read back the same value
targets = "F64"               # comma separated: F2, F64, PPU. Refreshed one after the other, in this order
expected_commit = ""          # commit the driver pushed; empty means whatever the remote branch has
harness_run_id = ""           # set by the driver; empty means generate one
max_refresh_minutes = "120"   # stop polling the refresh after this many minutes
max_log_wait_minutes = "20"   # stop waiting for the monitoring event after this many minutes
task = "refresh"              # refresh: full refresh cycle. queries: run the query workload
queries_file = ""             # queries task: path under harness_lake Files/ with the variant's query JSON
pages = "p01,p05,p10,p20"     # queries task: pages to render
modes = "cold,warm"           # queries task: cold clears the cache before each repeat; warm renders once unmeasured first
concurrency = "seq,page"      # queries task: seq sends visuals one by one; page sends all visuals of a page at once
repeats = "5"                 # queries task: measured renders per page, mode and concurrency

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "semantic-link-labs==0.18.1"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import datetime as dt
import io
import json
import re
import time
import uuid

import pandas as pd
import sempy.fabric as fabric
import sempy_labs as labs
import notebookutils

# Lab environment. IDs, not secrets.
WORKSPACES = {
    "F2": "58b05b2a-00d2-45df-9034-0a044bb3d162",
    "F64": "a1a434d3-4b0b-46d2-a4a2-147e3aff9e77",
    # Premium Per User, 100 GB per model. Not connected to Git and not a Fabric capacity, so it has no
    # workspace monitoring: the model is published from Desktop, and the refresh is measured with a trace.
    "PPU": "5f59a539-09dd-480f-a4ae-24f374b0e7aa",
}
NO_GIT = {"PPU"}       # targets whose models are published by hand, not synced from Git
TRACED = {"PPU"}       # targets measured with an XMLA trace instead of SemanticModelLogs
HARNESS_WORKSPACE = WORKSPACES["F64"]   # where this notebook and harness_lake live
LAKEHOUSE_NAME = "harness_lake"
# Targets with workspace monitoring. The KQL database is looked up by name at run time, because turning
# monitoring off and on (or a capacity change) recreates it with a new ID.
MONITORED = {"F64"}
MONITORING_DB_NAME = "Monitoring KQL database"
_monitoring_db = {}


def monitoring_db(cap):
    if cap not in _monitoring_db:
        _monitoring_db[cap] = find_item(WORKSPACES[cap], "KQLDatabase", MONITORING_DB_NAME)
    return _monitoring_db[cap]
REFRESH_PARALLELISM = 6   # what the manual service refreshes used, so results compare

# Per-model refresh memory limits in MB. F2 is the measured limit from the error messages.
# F16, F32 and F64 are the documented limits (F64 errors showed 25,592 to 25,593 MB).
LIMITS_MB = {"F2": 3066, "F16": 5120, "F32": 10240, "F64": 25600, "PPU": 102400}
CHANGE_FLAG_PCT = 1.0

fab = fabric.FabricRestClient()
pbi = fabric.PowerBIRestClient()

run_id = harness_run_id or dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:6]
target_list = [t.strip() for t in targets.split(",") if t.strip()]
ctx = notebookutils.runtime.context
notebook_run_id = str(ctx.get("currentRunId") or ctx.get("activityId") or "")


class HarnessStop(Exception):
    """A check failed. Nothing is fixed silently: the run stops and reports."""


def utcnow():
    return dt.datetime.now(dt.timezone.utc)


def iso(t):
    return t.strftime("%Y-%m-%dT%H:%M:%SZ") if t else ""


def ok(resp, what):
    if resp.status_code >= 300:
        raise HarnessStop(f"{what}: HTTP {resp.status_code} {resp.text[:2000]}")
    return resp


def list_items(ws, item_type):
    items, url = [], f"v1/workspaces/{ws}/items?type={item_type}"
    while url:
        body = ok(fab.get(url), f"list {item_type} in {ws}").json()
        items += body.get("value", [])
        token = body.get("continuationToken")
        url = f"v1/workspaces/{ws}/items?type={item_type}&continuationToken={token}" if token else None
    return items


def find_item(ws, item_type, name):
    hits = [i for i in list_items(ws, item_type) if i["displayName"] == name]
    if len(hits) != 1:
        raise HarnessStop(f"{item_type} '{name}' found {len(hits)} times in workspace {ws}")
    return hits[0]["id"]


lake_id = find_item(HARNESS_WORKSPACE, "Lakehouse", LAKEHOUSE_NAME)
LAKE = f"abfss://{HARNESS_WORKSPACE}@onelake.dfs.fabric.microsoft.com/{lake_id}"
RUNS_TABLE = f"{LAKE}/Tables/refresh_runs"
RUN_DIR = f"{LAKE}/Files/harness/runs/{run_id}"
log_lines = []


def note(msg):
    line = f"{iso(utcnow())} {msg}"
    print(line)
    log_lines.append(line)


note(f"run {run_id}: variant={variant} data_tag={data_tag} targets={target_list} expected_commit={expected_commit or '(remote head)'}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Step 1 and 2: update from Git, check the model and its data tag

# CELL ********************

def git_status(ws):
    r = ok(fab.get(f"v1/workspaces/{ws}/git/status", lro_wait=True), f"git status of {ws}")
    return r.json()


def sync_workspace(cap):
    ws = WORKSPACES[cap]
    if cap in NO_GIT:
        note(f"{cap}: not connected to Git; the model there is the one published by hand")
        return ""
    st = None
    # The remote head can take a moment to show a fresh push. Poll, don't sleep blindly.
    for attempt in range(12):
        st = git_status(ws)
        if not expected_commit or (st.get("remoteCommitHash") or "").startswith(expected_commit):
            break
        time.sleep(10)
    remote, head = st.get("remoteCommitHash"), st.get("workspaceHead")
    if expected_commit and not (remote or "").startswith(expected_commit):
        raise HarnessStop(f"{cap}: the workspace sees remote commit {remote}, not the pushed {expected_commit}")

    changes = st.get("changes", [])
    dirty = [c for c in changes if c.get("workspaceChange") not in (None, "None")]
    conflicts = [c for c in changes if c.get("conflictType") not in (None, "None")]
    if dirty or conflicts:
        lines = [f"  {c['itemMetadata'].get('displayName')} ({c['itemMetadata'].get('itemType')}): "
                 f"workspace {c.get('workspaceChange')}, remote {c.get('remoteChange')}, conflict {c.get('conflictType')}"
                 for c in dirty + conflicts]
        raise HarnessStop(f"{cap}: workspace has uncommitted changes or conflicts. Commit or undo them in "
                          f"Source control first. Nothing was updated.\n" + "\n".join(lines))

    if head != remote:
        note(f"{cap}: update from Git {head} -> {remote}")
        body = {
            "remoteCommitHash": remote,
            "workspaceHead": head,
            # No workspace changes exist (checked above), so this policy has nothing to resolve.
            # If one appeared in between, the workspace version is kept and the tag check below stops the run.
            # allowOverrideItems is the consent Fabric needs to apply incoming changes to existing items.
            "conflictResolution": {"conflictResolutionType": "Workspace", "conflictResolutionPolicy": "PreferWorkspace"},
            "options": {"allowOverrideItems": True},
        }
        ok(fab.post(f"v1/workspaces/{ws}/git/updateFromGit", json=body, lro_wait=True), f"{cap}: update from Git")
        st = git_status(ws)
        if st.get("workspaceHead") != remote:
            raise HarnessStop(f"{cap}: after update from Git the workspace head is {st.get('workspaceHead')}, expected {remote}")
    else:
        note(f"{cap}: workspace already at {remote}")
    return st.get("workspaceHead")


def find_dataset(ws, name):
    """Through the Power BI API, which also lists models in workspaces that are not on a Fabric capacity."""
    hits = [d["id"] for d in ok(pbi.get(f"v1.0/myorg/groups/{ws}/datasets"), f"list datasets in {ws}").json()["value"]
            if d["name"] == name]
    if len(hits) != 1:
        raise HarnessStop(f"semantic model '{name}' found {len(hits)} times in workspace {ws}")
    return hits[0]


def check_model(cap):
    ws = WORKSPACES[cap]
    dataset_id = find_dataset(ws, variant) if cap in NO_GIT else find_item(ws, "SemanticModel", variant)
    params = ok(pbi.get(f"v1.0/myorg/groups/{ws}/datasets/{dataset_id}/parameters"),
                f"{cap}: read parameters of {variant}").json().get("value", [])
    tags = [p.get("currentValue") for p in params if p.get("name") == "DataTag"]
    if not tags:
        raise HarnessStop(f"{cap}: {variant} has no DataTag parameter")
    if tags[0] != data_tag:
        raise HarnessStop(f"{cap}: {variant} reads back DataTag={tags[0]}, the run expects {data_tag}. "
                          f"Was the parameter changed in the service? Change it only in TMDL and commit.")
    note(f"{cap}: {variant} is {dataset_id}, DataTag reads back {tags[0]}")
    return dataset_id, tags[0], {p["name"]: p.get("currentValue") for p in params}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Step 3: full refresh through the enhanced refresh API

# CELL ********************

RG_PATTERN = re.compile(r"consumed memory\s*([\d,\.]+)\s*MB,\s*memory limit\s*([\d,\.]+)\s*MB,\s*"
                        r"database size before command execution\s*([\d,\.]+)\s*MB", re.I)


def num(s):
    return float(s.replace(",", "")) if s else None


def refresh(cap, dataset_id):
    ws = WORKSPACES[cap]
    base = f"v1.0/myorg/groups/{ws}/datasets/{dataset_id}/refreshes"
    body = {"type": "full", "commitMode": "transactional", "maxParallelism": REFRESH_PARALLELISM, "retryCount": 0}
    r = pbi.post(base, json=body)
    if r.status_code != 202:
        raise HarnessStop(f"{cap}: refresh request refused: HTTP {r.status_code} {r.text[:2000]}")
    location = r.headers.get("Location", "")
    request_id = location.rstrip("/").split("/")[-1] if location else r.headers.get("RequestId", "")
    note(f"{cap}: refresh started, request {request_id}")

    deadline = time.time() + float(max_refresh_minutes) * 60
    detail, interval = {}, 10
    while time.time() < deadline:
        time.sleep(interval)
        interval = min(interval + 5, 30)
        g = pbi.get(f"{base}/{request_id}")
        if g.status_code >= 300:
            note(f"{cap}: poll returned HTTP {g.status_code}, retrying")
            continue
        detail = g.json()
        if detail.get("status") not in ("NotStarted", "Unknown", "InProgress", None):
            break
    status = detail.get("status") or "Unknown"
    if status in ("NotStarted", "Unknown", "InProgress"):
        status = "PollTimeout"

    messages = detail.get("messages") or []
    error_text = "\n".join(str(m.get("message", "")) for m in messages if m.get("message"))
    if not error_text and messages:
        error_text = json.dumps(messages)
    out = {
        "refresh_request_id": request_id,
        "refresh_status": status,
        "extended_status": detail.get("extendedStatus", ""),
        "refresh_start": detail.get("startTime"),
        "refresh_end": detail.get("endTime"),
        "error_text": error_text,
        "messages_json": json.dumps(messages),
    }
    m = RG_PATTERN.search(error_text)
    out["consumed_mb_from_error"] = num(m.group(1)) if m else None
    out["limit_mb_from_error"] = num(m.group(2)) if m else None
    out["db_size_before_mb"] = num(m.group(3)) if m else None
    if m:
        out["failure_kind"] = "resource governance"
    elif "M evaluation exceeded the memory limit" in error_text:
        out["failure_kind"] = "M evaluation memory limit"
    elif status == "Completed":
        out["failure_kind"] = ""
    else:
        out["failure_kind"] = "other"
    out["result"] = {"Completed": "refreshed", "Failed": "failed", "Cancelled": "cancelled"}.get(status, status.lower())
    note(f"{cap}: refresh {out['result']} ({status}) {out['failure_kind']}")
    return out

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Steps 4 and 5: monitoring logs (F64 only)
# No request ID reaches `SemanticModelLogs`, so the refresh is matched by model ID and time:
# the `ExecutionMetrics` event of a refresh (it has `tabularConnectionTimeoutMs`) whose `timeStart`
# is within two minutes of the start reported by the refresh API. Queries 1, 3 and 4 are the ones in
# `analysis/refresh-memory.kql`, narrowed to that one refresh.

# CELL ********************

def kql(cap, query):
    return labs.query_kusto(query=query, kql_database=monitoring_db(cap), workspace=WORKSPACES[cap])


def kdt(s):
    return f"datetime({s})"


def wait_for_metrics(cap, dataset_id, start, end):
    q = f"""
SemanticModelLogs
| where Timestamp > {kdt(start)} - 5m and OperationName == "ExecutionMetrics" and ItemId == "{dataset_id}"
| extend m = parse_json(EventText)
| where isnotnull(m.tabularConnectionTimeoutMs)
| extend TimeStart = todatetime(m.timeStart), TimeEnd = todatetime(m.timeEnd)
| where TimeStart between ({kdt(start)} - 2m .. {kdt(start)} + 2m)
| project Timestamp, Model = ItemName, TimeStart, TimeEnd,
          Result         = iff(toint(m.errorCount) > 0, "failed", "refreshed"),
          PeakMemMB      = round(todouble(m.approximatePeakMemConsumptionKB) / 1024, 0),
          MEnginePeakMB  = round(todouble(m.mEnginePeakMemoryKB) / 1024, 0),
          DurationMin    = round(todouble(m.durationMs) / 60000, 2),
          TotalCpuSec    = round(todouble(m.totalCpuTimeMs) / 1000, 0),
          MEngineCpuSec  = round(todouble(m.mEngineCpuTimeMs) / 1000, 0),
          VertipaqCpuSec = round(todouble(m.vertipaqJobCpuTimeMs) / 1000, 0),
          RowsLoaded     = tolong(m.vertipaqTotalRows),
          RefreshParallelism = toint(m.refreshParallelism)
| order by Timestamp desc
| take 1"""
    deadline, interval = time.time() + float(max_log_wait_minutes) * 60, 15
    while time.time() < deadline:
        df = kql(cap, q)
        if len(df):
            note(f"{cap}: ExecutionMetrics event found")
            return df
        time.sleep(interval)
        interval = min(interval + 15, 60)
    note(f"{cap}: no ExecutionMetrics event after {max_log_wait_minutes} min")
    return pd.DataFrame()


def steps_query(dataset_id, start, end):
    return f"""
SemanticModelLogs
| where Timestamp between ({kdt(start)} .. {kdt(end)} + 5s)
    and OperationName == "ProgressReportEnd" and ItemId == "{dataset_id}"
| extend Object = strcat_array(array_slice(split(XmlaObjectPath, "."), -2, -1), ".")
| summarize DurationSec = round(sum(DurationMs) / 1000.0, 1),
            CpuSec = round(sum(CpuTimeMs) / 1000.0, 1),
            Rows = max(ProgressCounter)
  by Object, OperationDetailName
| order by DurationSec desc"""


def failed_steps_query(dataset_id, start, end):
    return f"""
SemanticModelLogs
| where Timestamp between ({kdt(start)} .. {kdt(end)} + 5s)
    and OperationName in ("ProgressReportBegin", "ProgressReportEnd") and ItemId == "{dataset_id}"
| summarize Began     = minif(Timestamp, OperationName == "ProgressReportBegin"),
            Ended     = maxif(Timestamp, OperationName == "ProgressReportEnd"),
            EndStatus = take_anyif(Status, OperationName == "ProgressReportEnd")
  by XmlaObjectPath, OperationDetailName
| where isnull(Ended) or EndStatus != "Succeeded"
| extend Object = strcat_array(array_slice(split(XmlaObjectPath, "."), -2, -1), ".")
| project Object, OperationDetailName, Began, Ended, EndStatus
| order by Began asc"""


# Targets without workspace monitoring (PPU) are measured with an XMLA trace that runs during the refresh.
# The trace delivers the same ExecutionMetrics event the monitoring logs get, as JSON in its text column.
TRACE_COLUMNS = {
    "ProgressReportEnd": ["EventClass", "EventSubclass", "CurrentTime", "StartTime", "EndTime", "Duration",
                          "CpuTime", "ObjectName", "ObjectPath", "IntegerData", "TextData", "Success"],
    "CommandEnd": ["EventClass", "EventSubclass", "CurrentTime", "StartTime", "EndTime", "Duration", "CpuTime",
                   "TextData", "Success", "Error"],
    "Error": ["EventClass", "CurrentTime", "TextData"],
    "ExecutionMetrics": ["EventClass", "TextData"],   # event 136 has no CurrentTime column (2026-11-10)
}
# Fallbacks if the trace API refuses a column or an event; the summary says which one was used.
TRACE_SCHEMAS = [
    ("full", TRACE_COLUMNS),
    ("minimal columns", {e: ["EventClass", "TextData"] for e in TRACE_COLUMNS}),
    ("without ExecutionMetrics", {e: c for e, c in TRACE_COLUMNS.items() if e != "ExecutionMetrics"}),
]


def norm_cols(df):
    df = df.copy()
    df.columns = [re.sub(r"[^a-z]", "", str(c).lower()) for c in df.columns]
    return df


def metrics_from_trace(df):
    if not len(df) or "textdata" not in df or "eventclass" not in df:
        return pd.DataFrame()
    rows = []
    for _, r in df[df["eventclass"].astype(str).str.contains("ExecutionMetrics|136", regex=True)].iterrows():
        try:
            m = json.loads(r["textdata"])
        except Exception:
            continue
        if "approximatePeakMemConsumptionKB" not in m or "mEnginePeakMemoryKB" not in m:
            continue   # a query's metrics, not the refresh's
        rows.append({
            "Timestamp": r.get("currenttime"), "Model": variant,
            "TimeStart": m.get("timeStart"), "TimeEnd": m.get("timeEnd"),
            "Result": "failed" if int(m.get("errorCount") or 0) > 0 else "refreshed",
            "PeakMemMB": round(float(m["approximatePeakMemConsumptionKB"]) / 1024, 0),
            "MEnginePeakMB": round(float(m.get("mEnginePeakMemoryKB") or 0) / 1024, 0),
            "DurationMin": round(float(m.get("durationMs") or 0) / 60000, 2),
            "TotalCpuSec": round(float(m.get("totalCpuTimeMs") or 0) / 1000, 0),
            "MEngineCpuSec": round(float(m.get("mEngineCpuTimeMs") or 0) / 1000, 0),
            "VertipaqCpuSec": round(float(m.get("vertipaqJobCpuTimeMs") or 0) / 1000, 0),
            "RowsLoaded": float(m.get("vertipaqTotalRows") or 0),
            "RefreshParallelism": float(m.get("refreshParallelism") or 0),
        })
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows).sort_values("PeakMemMB", ascending=False).head(1).reset_index(drop=True)


def steps_from_trace(df):
    if not len(df) or "eventclass" not in df:
        return pd.DataFrame()
    p = df[df["eventclass"].astype(str).str.contains("ProgressReportEnd|^6$", regex=True)].copy()
    if not len(p):
        return pd.DataFrame()
    obj = p["objectpath"].astype(str) if "objectpath" in p else p.get("objectname", pd.Series("", index=p.index)).astype(str)
    p["Object"] = obj.str.split(".").str[-2:].str.join(".")
    p["OperationDetailName"] = p["eventsubclass"].astype(str) if "eventsubclass" in p else ""
    for c in ("duration", "cputime", "integerdata"):
        p[c] = pd.to_numeric(p[c], errors="coerce") if c in p else np.nan
    return (p.groupby(["Object", "OperationDetailName"], as_index=False)
             .agg(DurationSec=("duration", lambda s: round(s.sum() / 1000, 1)),
                  CpuSec=("cputime", lambda s: round(s.sum() / 1000, 1)),
                  Rows=("integerdata", "max"))
             .sort_values("DurationSec", ascending=False))


def traced_refresh(cap, dataset_id):
    """Start a trace on the model, run the same enhanced refresh as everywhere else, stop the trace."""
    ws = WORKSPACES[cap]
    out = {"metrics": pd.DataFrame(), "steps": pd.DataFrame(), "failed_steps": pd.DataFrame(), "trace": pd.DataFrame()}
    try:
        conn = fabric.create_trace_connection(dataset_id, workspace=ws)
    except Exception as e:
        raise HarnessStop(f"{cap}: could not open a trace connection to {variant} (semantic-link opens it "
                          f"read/write, so the workspace's XMLA endpoint must allow read/write): "
                          f"{type(e).__name__}: {str(e)[:1500]}")
    with conn:
        # The server checks the columns only when the trace starts, so each schema is tried up to start().
        trace, used = None, None
        for name, schema in TRACE_SCHEMAS:
            t = None
            try:
                t = conn.create_trace(schema, f"lab-{run_id}-{len(name)}")
                t.start()
                trace, used = t, name
                break
            except Exception as e:
                note(f"{cap}: trace schema '{name}' refused: {str(e)[:300]}")
                if t is not None:
                    try:
                        t.drop()
                    except Exception:
                        pass
        if trace is None:
            raise HarnessStop(f"{cap}: could not start a trace on {variant}")
        with trace:
            note(f"{cap}: trace started ({used})")
            ref = refresh(cap, dataset_id)
            time.sleep(30)   # the ExecutionMetrics event comes a little after the refresh ends
            raw = trace.stop()
    raw = norm_cols(raw if isinstance(raw, pd.DataFrame) else pd.DataFrame(raw))
    note(f"{cap}: trace captured {len(raw)} events: " +
         ", ".join(f"{k} {v}" for k, v in raw["eventclass"].astype(str).value_counts().items()) if len(raw) else
         f"{cap}: trace captured no events")
    out["trace"] = raw
    out["metrics"] = metrics_from_trace(raw)
    out["steps"] = steps_from_trace(raw)
    if not len(out["metrics"]):
        note(f"{cap}: no refresh ExecutionMetrics event in the trace")
    return ref, out


def read_logs(cap, dataset_id, ref):
    out = {"metrics": pd.DataFrame(), "steps": pd.DataFrame(), "failed_steps": pd.DataFrame()}
    if cap not in MONITORED or not ref.get("refresh_start"):
        return out
    metrics = wait_for_metrics(cap, dataset_id, ref["refresh_start"], ref.get("refresh_end") or iso(utcnow()))
    out["metrics"] = metrics
    if not len(metrics):
        return out
    start, end = str(metrics.iloc[0]["TimeStart"]), str(metrics.iloc[0]["TimeEnd"])
    # Progress events can land a little after ExecutionMetrics. On a refreshed model, wait for the Backup step.
    for attempt in range(8):
        steps = kql(cap, steps_query(dataset_id, start, end))
        if ref["result"] != "refreshed" or (steps["OperationDetailName"] == "Backup").any():
            break
        time.sleep(15)
    out["steps"] = steps
    if metrics.iloc[0]["Result"] == "failed":
        out["failed_steps"] = kql(cap, failed_steps_query(dataset_id, start, end))
    return out

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Steps 6 and 7: compare and record

# CELL ********************

from pyspark.sql.types import StructType, StructField, StringType, DoubleType

ROW_SCHEMA = StructType(
    [StructField(c, StringType()) for c in [
        "timestamp_utc", "harness_run_id", "notebook_run_id", "variant", "data_tag", "data_tag_readback",
        "capacity", "workspace_head", "result", "failure_kind"]]
    + [StructField(c, DoubleType()) for c in [
        "peak_mb", "pq_peak_mb", "consumed_mb_from_error", "limit_mb_from_error", "db_size_before_mb",
        "duration_min", "total_cpu_sec", "mengine_cpu_sec", "vertipaq_cpu_sec", "rows_loaded",
        "refresh_parallelism", "model_size_mb"]]
    + [StructField(c, StringType()) for c in [
        "model_size_source", "metrics_source", "refresh_request_id", "refresh_start_utc", "refresh_end_utc",
        "error_text"]]
)
COLUMNS = [f.name for f in ROW_SCHEMA.fields]


def history():
    try:
        return spark.read.format("delta").load(RUNS_TABLE).toPandas()
    except Exception:
        return pd.DataFrame(columns=COLUMNS)


def model_size(cap, dataset_id, logs, ref):
    steps = logs["steps"]
    if len(steps):
        backup = steps[steps["OperationDetailName"] == "Backup"]
        if len(backup):
            where = "XMLA trace" if cap in TRACED else "SemanticModelLogs"
            return round(float(backup["Rows"].max()) / 1048576, 1), f"Backup step in {where}"
    if ref["result"] == "refreshed":
        try:
            return round(labs.get_semantic_model_size(dataset=dataset_id, workspace=WORKSPACES[cap]) / 1048576, 1), \
                "INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX)"
        except Exception as e:
            note(f"{cap}: model size query failed: {e}")
    return None, ""


def build_row(cap, head, tag_readback, dataset_id, ref, logs):
    def dur():
        if ref.get("refresh_start") and ref.get("refresh_end"):
            a = pd.Timestamp(ref["refresh_start"]); b = pd.Timestamp(ref["refresh_end"])
            return round((b - a).total_seconds() / 60, 2)
        return None
    row = {c: None for c in COLUMNS}
    row.update({
        "timestamp_utc": iso(utcnow()), "harness_run_id": run_id, "notebook_run_id": notebook_run_id,
        "variant": variant, "data_tag": data_tag, "data_tag_readback": tag_readback, "capacity": cap,
        "workspace_head": head, "result": ref["result"], "failure_kind": ref["failure_kind"],
        "consumed_mb_from_error": ref["consumed_mb_from_error"], "limit_mb_from_error": ref["limit_mb_from_error"],
        "db_size_before_mb": ref["db_size_before_mb"], "refresh_request_id": ref["refresh_request_id"],
        "refresh_start_utc": ref.get("refresh_start") or "", "refresh_end_utc": ref.get("refresh_end") or "",
        "error_text": ref["error_text"], "duration_min": dur(), "metrics_source": "refresh API",
    })
    met = logs["metrics"]
    if len(met):
        m = met.iloc[0]
        row.update({
            "peak_mb": float(m["PeakMemMB"]), "pq_peak_mb": float(m["MEnginePeakMB"]),
            "duration_min": float(m["DurationMin"]), "total_cpu_sec": float(m["TotalCpuSec"]),
            "mengine_cpu_sec": float(m["MEngineCpuSec"]), "vertipaq_cpu_sec": float(m["VertipaqCpuSec"]),
            "rows_loaded": float(m["RowsLoaded"]), "refresh_parallelism": float(m["RefreshParallelism"]),
            "metrics_source": "SemanticModelLogs ExecutionMetrics",
        })
    row["model_size_mb"], row["model_size_source"] = model_size(cap, dataset_id, logs, ref)
    return row


def fmt(v, unit=" MB"):
    return "n/a" if v is None or pd.isna(v) else f"{v:,.0f}{unit}"


def compare(row, hist):
    """Lines for the summary. Only measured numbers; nothing is estimated."""
    lines = []
    peak = row["peak_mb"]
    same_tag = hist[(hist["data_tag"] == row["data_tag"]) & (hist["capacity"] == row["capacity"])]

    prev = same_tag[same_tag["variant"] == row["variant"]].sort_values("timestamp_utc")
    if len(prev):
        p = prev.iloc[-1]
        lines.append(f"- Previous harness run of {row['variant']} on {row['capacity']} {row['data_tag']}: "
                     f"{p['result']}, peak {fmt(p['peak_mb'])} ({p['timestamp_utc']}).")
        if peak is not None and pd.notna(p["peak_mb"]) and p["peak_mb"]:
            pct = (peak - p["peak_mb"]) / p["peak_mb"] * 100
            flag = " **FLAG: peak changed by more than 1%**" if abs(pct) > CHANGE_FLAG_PCT else ""
            lines.append(f"  - Peak change: {peak - p['peak_mb']:+,.0f} MB ({pct:+.1f}%).{flag}")
        if p["result"] != row["result"]:
            lines.append(f"  - **FLAG: result changed from {p['result']} to {row['result']}**")
    else:
        lines.append(f"- No earlier harness run of {row['variant']} on {row['capacity']} {row['data_tag']}.")

    if row["variant"] != "v00-baseline":
        base = same_tag[(same_tag["variant"] == "v00-baseline") & (same_tag["result"] == "refreshed")]
        base = base.sort_values("timestamp_utc")
        if len(base) and peak is not None and pd.notna(base.iloc[-1]["peak_mb"]):
            b = base.iloc[-1]
            lines.append(f"- Against v00-baseline on {row['capacity']} {row['data_tag']} ({b['timestamp_utc']}): "
                         f"peak {fmt(peak)} vs {fmt(b['peak_mb'])} ({peak - b['peak_mb']:+,.0f} MB), "
                         f"Power Query {fmt(row['pq_peak_mb'])} vs {fmt(b['pq_peak_mb'])}, "
                         f"model {fmt(row['model_size_mb'])} vs {fmt(b['model_size_mb'])}.")
        else:
            lines.append(f"- No v00-baseline harness run with a measured peak on {row['capacity']} {row['data_tag']} to compare with.")

    if peak is not None:
        fits = [f"{cap} {lim:,} MB: {'fits' if peak <= lim else 'OVER'} ({peak / lim:.0%})" for cap, lim in LIMITS_MB.items()]
        lines.append("- Measured peak against per-model limits: " + "; ".join(fits) + ".")
    elif row["consumed_mb_from_error"] is not None:
        lines.append(f"- Engine cancelled at {fmt(row['consumed_mb_from_error'])} against a limit of "
                     f"{fmt(row['limit_mb_from_error'])} (database size before the command {fmt(row['db_size_before_mb'])}).")
    else:
        lines.append("- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).")
    return lines


def screenshot_hint(row):
    if row["result"] == "refreshed":
        return None
    short = {"resource governance": "resource-governance", "M evaluation memory limit": "m-evaluation-memory"}.get(
        row["failure_kind"], "refresh-error")
    return (f"Screenshot: the refresh error of {row['variant']} on {row['capacity']} in the service "
            f"(semantic model > Refresh history > error details), saved as "
            f"docs/screenshots/{row['capacity'].lower()}-{row['variant']}-{short}.png")


def spark_row(row):
    out = []
    for f in ROW_SCHEMA.fields:
        v = row.get(f.name)
        if v is None or (isinstance(v, float) and pd.isna(v)):
            out.append(None)
        else:
            out.append(float(v) if isinstance(f.dataType, DoubleType) else str(v))
    return out


def md_table(df):
    try:
        return df.to_markdown(index=False)
    except ImportError:   # tabulate missing
        return "```\n" + df.to_string(index=False) + "\n```"


def write_text(path, text):
    notebookutils.fs.put(path, text, True)


def write_csv(path, df):
    write_text(path, df.to_csv(index=False))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Query workload (task = queries)
# Sends the DAX of each visual through the executeQueries REST API, page by page, and reads back what the engine logged.
# Every query starts with an unused variable, VAR __LabTag = "run=...;page=...;visual=...;mode=...;conc=...;rep=...".
# Comments do not reach SemanticModelLogs, the variable does. All events of one query share an OperationId.

# CELL ********************

import threading
from concurrent.futures import ThreadPoolExecutor

import numpy as np


class TokenBucket:
    """executeQueries allows about 120 queries per minute per user. Bursts of a whole page are allowed,
    the average rate stays under the limit."""

    def __init__(self, per_minute=100, burst=20):
        self.rate, self.capacity, self.tokens = per_minute / 60.0, burst, float(burst)
        self.last, self.lock = time.time(), threading.Lock()

    def take(self, n=1):
        """Wait until n tokens are there and take them together. A page takes all its tokens before it
        starts, so the queries of one render are never held back and the waiting is not measured."""
        while True:
            with self.lock:
                now = time.time()
                self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
                self.last = now
                if self.tokens >= n:
                    self.tokens -= n
                    return
                wait = (n - self.tokens) / self.rate
            time.sleep(wait)


BUCKET = TokenBucket()
_local = threading.local()


def thread_pbi():
    if not hasattr(_local, "client"):
        _local.client = fabric.PowerBIRestClient()
    return _local.client


def tagged(dax, tag):
    head = f'DEFINE\n\tVAR __LabTag = "{tag}"\n'
    s = dax.lstrip()
    return head + (s[len("DEFINE"):].lstrip("\n") if s.upper().startswith("DEFINE") else s)


def exec_query(ws, dataset_id, dax, tag):
    q, retries = tagged(dax, tag), 0
    while True:
        if retries:
            BUCKET.take()   # a retry after throttling needs a token of its own
        t0 = time.time()
        try:
            r = thread_pbi().post(f"v1.0/myorg/groups/{ws}/datasets/{dataset_id}/executeQueries",
                                  json={"queries": [{"query": q}], "serializerSettings": {"includeNulls": True}})
            status, text = r.status_code, None
        except Exception as e:          # the client may raise on HTTP errors
            r, status, text = None, getattr(getattr(e, "response", None), "status_code", -1), str(e)
        t1 = time.time()
        if status == 429 and retries < 6:
            retries += 1
            time.sleep(float((r.headers.get("Retry-After") if r is not None else None) or 10))
            continue
        break
    rows, err = None, ""
    if status == 200:
        res = r.json().get("results", [{}])[0]
        if "error" in res:
            err = json.dumps(res["error"])[:2000]
        else:
            rows = len(res["tables"][0]["rows"])
    else:
        err = f"HTTP {status} {(r.text if r is not None else text)[:2000]}"
    return {"tag": tag, "client_start_utc": dt.datetime.fromtimestamp(t0, dt.timezone.utc).isoformat(),
            "client_ms": round((t1 - t0) * 1000), "http_status": status, "rows_first_result": rows,
            "retries": retries, "client_error": err}


def render_page(ws, dataset_id, qdef, page, mode, conc, rep):
    vids = qdef["pages"][page]["visuals"]
    tag = lambda v: f"run={run_id};page={page};visual={v};mode={mode};conc={conc};rep={rep}"
    BUCKET.take(len(vids))
    t0 = time.time()
    if conc == "seq":
        res = [exec_query(ws, dataset_id, qdef["visuals"][v]["dax"], tag(v)) for v in vids]
    else:
        with ThreadPoolExecutor(max_workers=len(vids)) as ex:
            res = list(ex.map(lambda v: exec_query(ws, dataset_id, qdef["visuals"][v]["dax"], tag(v)), vids))
    wall = round((time.time() - t0) * 1000)
    for v, r in zip(vids, res):
        r.update({"page": page, "visual": v, "visual_type": qdef["visuals"][v]["type"], "mode": mode,
                  "conc": conc, "rep": rep, "page_wall_ms": wall})
    return res


def run_workload(cap, dataset_id):
    ws = WORKSPACES[cap]
    qdef = json.loads(notebookutils.fs.head(f"{LAKE}/Files/{queries_file}", 50_000_000))
    if qdef["variant"] != variant:
        raise HarnessStop(f"{queries_file} is for {qdef['variant']}, not {variant}")
    page_list = [p.strip() for p in pages.split(",") if p.strip()]
    for p in page_list:
        if p not in qdef["pages"]:
            raise HarnessStop(f"page {p} not in {queries_file}")
    started, sent = utcnow(), []
    for page in page_list:
        for conc in [c.strip() for c in concurrency.split(",") if c.strip()]:
            for mode in [m.strip() for m in modes.split(",") if m.strip()]:
                if mode == "warm":
                    sent += render_page(ws, dataset_id, qdef, page, mode, conc, 0)   # warm-up, not measured
                for rep in range(1, int(repeats) + 1):
                    if mode == "cold":
                        labs.clear_cache(dataset=dataset_id, workspace=ws)
                    sent += render_page(ws, dataset_id, qdef, page, mode, conc, rep)
        note(f"{cap}: page {page} done, {len(sent)} queries so far")
    return started, pd.DataFrame(sent)


def query_logs_kql(dataset_id, start):
    return f"""
let Start = {kdt(start)} - 5m;
let Q = SemanticModelLogs
| where Timestamp > Start and ItemId == "{dataset_id}" and OperationName == "QueryEnd" and EventText contains "run={run_id};"
| extend tag = extract(@'__LabTag\\s*=\\s*"([^"]+)"', 1, EventText)
| project OperationId, server_end_utc = Timestamp, server_ms = DurationMs, cpu_ms = CpuTimeMs,
          server_status = Status, status_code = StatusCode, tag;
let M = SemanticModelLogs
| where Timestamp > Start and ItemId == "{dataset_id}" and OperationName == "ExecutionMetrics"
| extend j = parse_json(EventText)
| where isnull(j.tabularConnectionTimeoutMs)
// A query can have more than one ExecutionMetrics event (one with zeros); keep one row per query.
| summarize peak_mem_kb = max(tolong(j.approximatePeakMemConsumptionKB)), result_rows = max(tolong(j.queryResultRows)),
            execution_delay_ms = max(tolong(j.executionDelayMs)), vertipaq_cpu_ms = max(tolong(j.vertipaqJobCpuTimeMs)),
            formula_cpu_ms = max(tolong(j.queryProcessingCpuTimeMs))
  by OperationId;
let SE = SemanticModelLogs
| where Timestamp > Start and ItemId == "{dataset_id}" and OperationName startswith "VertiPaqSEQuery"
| summarize se_queries = countif(OperationName == "VertiPaqSEQueryEnd" and OperationDetailName == "VertiPaqScan"),
            se_cache_hits = countif(OperationName == "VertiPaqSEQueryCacheMatch"),
            se_ms = sumif(DurationMs, OperationName == "VertiPaqSEQueryEnd" and OperationDetailName == "VertiPaqScan")
  by OperationId;
let E = SemanticModelLogs
| where Timestamp > Start and ItemId == "{dataset_id}" and OperationName == "Error"
| summarize server_error = take_any(EventText) by OperationId;
Q
| join kind=leftouter M on OperationId
| join kind=leftouter SE on OperationId
| join kind=leftouter E on OperationId
| project-away OperationId1, OperationId2, OperationId3"""


def read_query_logs(cap, dataset_id, start, expected):
    deadline, interval, df = time.time() + float(max_log_wait_minutes) * 60, 20, pd.DataFrame()
    while time.time() < deadline:
        df = kql(cap, query_logs_kql(dataset_id, iso(start)))
        complete = len(df) >= expected and (df["peak_mem_kb"].notna().sum() >= expected if len(df) else False)
        if complete:
            break
        time.sleep(interval)
        interval = min(interval + 20, 60)
    note(f"{cap}: {len(df)} of {expected} queries found in SemanticModelLogs")
    return df


def p90(s):
    s = pd.to_numeric(s, errors="coerce").dropna()
    return float(np.percentile(s, 90)) if len(s) else None


def summarise_queries(q):
    meas = q[q["rep"] > 0]
    per_page = meas.groupby(["page", "mode", "conc", "rep"]).agg(
        visuals=("visual", "count"), page_wall_ms=("page_wall_ms", "first"),
        server_sum_ms=("server_ms", "sum"), server_max_ms=("server_ms", "max"), cpu_sum_ms=("cpu_ms", "sum"),
        peak_mem_max_kb=("peak_mem_kb", "max"), errors=("failed", "sum")).reset_index()
    summary = per_page.groupby(["page", "mode", "conc"]).agg(
        repeats=("rep", "count"), visuals=("visuals", "first"),
        page_wall_median_ms=("page_wall_ms", "median"), page_wall_p90_ms=("page_wall_ms", p90),
        server_max_median_ms=("server_max_ms", "median"), server_max_p90_ms=("server_max_ms", p90),
        server_sum_median_ms=("server_sum_ms", "median"), cpu_sum_median_ms=("cpu_sum_ms", "median"),
        peak_mem_max_kb=("peak_mem_max_kb", "max"), errors=("errors", "sum")).reset_index()
    return per_page, summary


def run_queries_task(cap, head, tag, dataset_id):
    started, client = run_workload(cap, dataset_id)
    if cap in MONITORED:
        logs = read_query_logs(cap, dataset_id, started, len(client))
        q = client.merge(logs, on="tag", how="left")
    else:
        q = client.copy()
        for c in ("server_ms", "cpu_ms", "peak_mem_kb", "result_rows", "execution_delay_ms", "server_error"):
            q[c] = None
    # The REST API returns only one result set. A matrix with columns has two (headers and body): the engine
    # runs the whole query and the API then reports DaxResultsetCountNotSupported. That is not a failed query.
    server_ok = q.get("server_status", pd.Series(index=q.index, dtype=object)).fillna("") == "Succeeded"
    rest_only = q["client_error"].fillna("").str.contains("DaxResultsetCountNotSupported") & server_ok
    q["note"] = np.where(rest_only, "REST returned one of two result sets; server completed the query", "")
    q.loc[rest_only, "client_error"] = ""
    q["failed"] = (q["client_error"].fillna("") != "") |         (q.get("server_status", pd.Series(index=q.index, dtype=object)).fillna("Succeeded") != "Succeeded")
    meta = {"harness_run_id": run_id, "notebook_run_id": notebook_run_id, "variant": variant, "data_tag": data_tag,
            "data_tag_readback": tag, "capacity": cap, "workspace_head": head}
    for k, v in reversed(list(meta.items())):
        q.insert(0, k, v)
    per_page, summary = summarise_queries(q)
    for df in (per_page, summary):
        for k, v in reversed(list(meta.items())):
            df.insert(0, k, v)
    return q, per_page, summary

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Run

# CELL ********************

rows, sections, stop_reason = [], [], None
query_frames = {"queries": [], "pages": [], "summary": []}
try:
    if task not in ("refresh", "queries"):
        raise HarnessStop(f"unknown task {task}")
    if task == "queries" and not queries_file:
        raise HarnessStop("task queries needs queries_file")
    prepared = {}
    for cap in target_list:                      # all checks pass before any refresh or query starts
        if cap not in WORKSPACES:
            raise HarnessStop(f"unknown target {cap}; known: {', '.join(WORKSPACES)}")
        head = sync_workspace(cap)
        dataset_id, tag, params = check_model(cap)
        prepared[cap] = (head, dataset_id, tag, params)

    hist = history()
    for cap in (target_list if task == "queries" else []):
        head, dataset_id, tag, params = prepared[cap]
        q, per_page, summary_df = run_queries_task(cap, head, tag, dataset_id)
        for k, df in (("queries", q), ("pages", per_page), ("summary", summary_df)):
            query_frames[k].append(df)
        spark.createDataFrame(q.astype(str)).write.format("delta").mode("append") \
            .option("mergeSchema", "true").save(f"{LAKE}/Tables/query_runs")   # append only
        failed = int(q["failed"].sum())
        found = int(q["peak_mem_kb"].notna().sum()) if "peak_mem_kb" in q else 0
        sections += [f"## {cap}", "",
                     f"- {len(q)} queries sent ({int((q['rep'] == 0).sum())} warm-up), {failed} failed, "
                     f"{found} found in SemanticModelLogs, {int(q['retries'].sum())} throttling retries",
                     f"- Workspace at {head[:7] if head else '?'}, DataTag read back {tag}", "",
                     "Median and p90 over the repeats, per page:", "",
                     md_table(summary_df[["page", "mode", "conc", "repeats", "page_wall_median_ms", "page_wall_p90_ms",
                                          "server_max_median_ms", "server_sum_median_ms", "cpu_sum_median_ms",
                                          "peak_mem_max_kb", "errors"]]), ""]
        if failed:
            errs = q[q["failed"]][["page", "visual", "mode", "conc", "rep", "client_error"]].head(10)
            sections += ["Failed queries (first 10):", "", md_table(errs), ""]

    for cap in (target_list if task == "refresh" else []):
        head, dataset_id, tag, params = prepared[cap]
        if cap in TRACED:
            ref, logs = traced_refresh(cap, dataset_id)
        else:
            ref = refresh(cap, dataset_id)
            logs = read_logs(cap, dataset_id, ref)
        row = build_row(cap, head, tag, dataset_id, ref, logs)
        if cap in TRACED and len(logs["metrics"]):
            row["metrics_source"] = "XMLA trace ExecutionMetrics"
        rows.append(row)

        prefix = f"{RUN_DIR}/{cap.lower()}"
        for name in ("metrics", "steps", "failed_steps", "trace"):
            if len(logs.get(name, [])):
                write_csv(f"{prefix}-{name}.csv", logs[name])
        spark.createDataFrame([spark_row(row)], ROW_SCHEMA) \
            .write.format("delta").mode("append").save(RUNS_TABLE)   # append only, never overwrite

        sec = [f"## {cap}", "",
               f"- Result: **{row['result']}** {('(' + row['failure_kind'] + ')') if row['failure_kind'] else ''}",
               f"- Peak {fmt(row['peak_mb'])}, Power Query {fmt(row['pq_peak_mb'])}, duration {fmt(row['duration_min'], ' min')}, "
               f"CPU {fmt(row['total_cpu_sec'], ' s')}, rows {fmt(row['rows_loaded'], '')}, model {fmt(row['model_size_mb'])} "
               f"({row['model_size_source'] or 'no size'})",
               f"- Refresh request {row['refresh_request_id']}, {row['refresh_start_utc']} to {row['refresh_end_utc']}, "
               f"workspace at {head[:7] if head else '?'}, DataTag read back {tag}",
               f"- Numbers from: {row['metrics_source']}"]
        sec += compare(row, hist)
        if row["error_text"]:
            sec += ["", "Error text:", "", "```", row["error_text"], "```"]
        if len(logs["failed_steps"]):
            sec += ["", "Steps running or failed when it stopped:", "", md_table(logs["failed_steps"])]
        if len(logs["steps"]):
            sec += ["", "Slowest steps:", "", md_table(logs["steps"].head(12))]
        hint = screenshot_hint(row)
        if hint:
            sec += ["", f"**{hint}**"]
        sections += sec + [""]
        hist = pd.concat([hist, pd.DataFrame([row], columns=COLUMNS)], ignore_index=True)
except HarnessStop as e:
    stop_reason = str(e)
    note(f"STOPPED: {stop_reason}")
except Exception as e:   # anything unexpected still ends in a summary with the traceback
    import traceback
    stop_reason = f"unexpected error: {type(e).__name__}: {e}\n\n{traceback.format_exc()[-4000:]}"
    note(f"STOPPED: {type(e).__name__}: {str(e)[:500]}")

summary = [f"# Harness run {run_id}", "",
           f"- Task: {task}", f"- Variant: {variant}", f"- Data tag: {data_tag}", f"- Targets: {', '.join(target_list)}",
           f"- Expected commit: {expected_commit or '(remote head)'}", f"- Notebook run: {notebook_run_id}"]
summary += ([f"- Refresh parallelism requested: {REFRESH_PARALLELISM}", ""] if task == "refresh" else
            [f"- Pages {pages}, modes {modes}, concurrency {concurrency}, repeats {repeats}, queries from {queries_file}", ""])
if stop_reason:
    summary += ["**Stopped before finishing:**", "", "```", stop_reason, "```", ""]
summary += sections + ["## Log", "", "```"] + log_lines + ["```", ""]
summary_text = "\n".join(summary)

write_text(f"{RUN_DIR}/summary.md", summary_text)
if rows:
    write_csv(f"{RUN_DIR}/rows.csv", pd.DataFrame(rows, columns=COLUMNS))
for k, frames in query_frames.items():
    if frames:
        write_csv(f"{RUN_DIR}/query-{k}.csv", pd.concat(frames, ignore_index=True))
write_text(f"{RUN_DIR}/status.json", json.dumps({"run_id": run_id, "stopped": stop_reason, "rows": len(rows)}))
print(summary_text)

if stop_reason:
    raise Exception(f"Harness stopped: {stop_reason}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
