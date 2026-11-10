"""Run one variant through the refresh harness notebook and pull the results into the repo.

Usage (from the repo root, after the variant is committed and pushed):

    python harness/run_variant.py v00-baseline --targets F2,F64

Steps:
  1. Read DataTag from the variant's committed TMDL (HEAD, not the working tree).
  2. Check that HEAD is pushed to the remote branch.
  3. Before a 10M run, show the 1M results of the same variant and warn if one is near a limit.
  4. Bring the F64 workspace (where the notebook lives) up to the pushed commit. Stops on
     uncommitted workspace changes or conflicts.
  5. Start the refresh-harness notebook through the Job Scheduler API, wait for it.
  6. Download the run folder from harness_lake, append rows to results/harness-runs.csv,
     save the summary and log extracts under results/harness/<run id>/.

Auth: the signed-in az CLI user. No secrets anywhere.
Python standard library only.
"""
import argparse
import csv
import datetime as dt
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REMOTE = "semantic-model-refresh"
BRANCH = "main"
WORKSPACES = {"F2": "58b05b2a-00d2-45df-9034-0a044bb3d162", "F64": "a1a434d3-4b0b-46d2-a4a2-147e3aff9e77"}
HARNESS_WS = WORKSPACES["F64"]
NOTEBOOK = "refresh-harness"
LAKEHOUSE = "harness_lake"
LIMITS_MB = {"F2": 3066, "F16": 5120, "F32": 10240, "F64": 25600, "PPU": 102400}
NEAR_LIMIT = 0.8
RUNS_CSV = ROOT / "results" / "harness-runs.csv"
FABRIC = "https://api.fabric.microsoft.com/v1"
ONELAKE = "https://onelake.dfs.fabric.microsoft.com"

_tokens = {}


def token(resource):
    if resource not in _tokens or _tokens[resource][1] < time.time() + 300:
        out = subprocess.run(["az", "account", "get-access-token", "--resource", resource, "-o", "json"],
                             capture_output=True, text=True, shell=(sys.platform == "win32"))
        if out.returncode:
            sys.exit(f"az could not get a token for {resource}: {out.stderr.strip()}")
        body = json.loads(out.stdout)
        _tokens[resource] = (body["accessToken"], int(body.get("expires_on") or time.time() + 1800))
    return _tokens[resource][0]


def http(method, url, body=None, resource="https://api.fabric.microsoft.com", headers=None, raw=False):
    h = {"Authorization": "Bearer " + token(resource)}
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        h["Content-Type"] = "application/json"
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                content = r.read()
                return r.status, {k.lower(): v for k, v in r.headers.items()}, (content if raw else (json.loads(content) if content else {}))
        except urllib.error.HTTPError as e:
            return e.code, {k.lower(): v for k, v in e.headers.items()}, e.read().decode(errors="replace")
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:   # network trouble on this side
            print(f"  network error ({e}), retrying in {15 * (attempt + 1)} s")
            time.sleep(15 * (attempt + 1))
    sys.exit(f"{method} {url}: no connection after 5 attempts")


def fabric(method, path, body=None, lro=False):
    status, headers, out = http(method, FABRIC + path, body)
    if status == 202 and lro:
        op = headers.get("location")
        while True:
            time.sleep(int(headers.get("retry-after", 5)))
            status, headers, out = http("GET", op)
            if isinstance(out, dict) and out.get("status") in ("Succeeded", "Failed", "Cancelled"):
                break
        if out.get("status") != "Succeeded":
            sys.exit(f"{method} {path} failed: {json.dumps(out)[:2000]}")
        status, headers, res = http("GET", op.rstrip("/") + "/result")
        return 200, headers, (res if status == 200 else out)
    if status >= 300:
        sys.exit(f"{method} {path}: HTTP {status} {str(out)[:2000]}")
    return status, headers, out


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()


def committed_data_tag(variant):
    path = f"models/{variant}/{variant}.SemanticModel/definition/expressions.tmdl"
    try:
        text = git("show", f"HEAD:{path}")
    except subprocess.CalledProcessError:
        sys.exit(f"{path} is not in HEAD. Commit the variant first.")
    m = re.search(r'expression\s+DataTag\s*=\s*"([^"]+)"', text)
    if not m:
        sys.exit(f"No DataTag parameter in {path}")
    return m.group(1)


def check_pushed():
    if git("status", "--porcelain", "--", "models", "harness", "reports"):
        sys.exit("models/ or harness/ has uncommitted changes. Commit and push first.")
    git("fetch", REMOTE, BRANCH)
    head, remote = git("rev-parse", "HEAD"), git("rev-parse", f"{REMOTE}/{BRANCH}")
    if head != remote:
        sys.exit(f"HEAD {head[:7]} is not what {REMOTE}/{BRANCH} has ({remote[:7]}). Push first.")
    return head


def read_runs():
    if not RUNS_CSV.exists():
        return []
    with RUNS_CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def warn_before_10m(variant, data_tag, targets):
    if "10m" not in data_tag:
        return
    small = [r for r in read_runs() if r["variant"] == variant and "1m" in r["data_tag"]]
    if not small:
        print(f"WARNING: no 1M harness run of {variant} yet. Run 1M first unless the 10M run is the point.")
        return
    for r in small[-4:]:
        line = f"  1M on {r['capacity']}: {r['result']}, peak {r['peak_mb'] or 'n/a'} MB"
        print(line)
    for r in small:
        if r["result"] != "refreshed":
            print(f"WARNING: {variant} already failed on 1M on {r['capacity']}.")
        try:
            peak = float(r["peak_mb"])
        except (TypeError, ValueError):
            continue
        for cap in targets:
            lim = LIMITS_MB.get(cap)
            if lim and peak >= NEAR_LIMIT * lim:
                print(f"WARNING: on 1M {variant} peaked at {peak:,.0f} MB, {peak / lim:.0%} of the {cap} limit. "
                      f"10M will need more.")


def sync_harness_workspace(commit):
    _, _, st = fabric("GET", f"/workspaces/{HARNESS_WS}/git/status", lro=True)
    for _ in range(12):
        if (st.get("remoteCommitHash") or "").startswith(commit):
            break
        time.sleep(10)
        _, _, st = fabric("GET", f"/workspaces/{HARNESS_WS}/git/status", lro=True)
    if not (st.get("remoteCommitHash") or "").startswith(commit):
        sys.exit(f"F64 workspace sees remote {st.get('remoteCommitHash')}, not {commit}")
    bad = [c for c in st.get("changes", [])
           if c.get("workspaceChange") not in (None, "None") or c.get("conflictType") not in (None, "None")]
    if bad:
        for c in bad:
            print(f"  {c['itemMetadata'].get('displayName')}: workspace {c.get('workspaceChange')}, "
                  f"remote {c.get('remoteChange')}, conflict {c.get('conflictType')}")
        sys.exit("F64 workspace has uncommitted changes or conflicts. Commit or undo them in Source control, then rerun.")
    if st.get("workspaceHead") != st.get("remoteCommitHash"):
        print(f"F64: update from Git {str(st.get('workspaceHead'))[:7]} -> {st['remoteCommitHash'][:7]}")
        fabric("POST", f"/workspaces/{HARNESS_WS}/git/updateFromGit", {
            "remoteCommitHash": st["remoteCommitHash"], "workspaceHead": st.get("workspaceHead"),
            "conflictResolution": {"conflictResolutionType": "Workspace", "conflictResolutionPolicy": "PreferWorkspace"},
            "options": {"allowOverrideItems": True}}, lro=True)
    else:
        print(f"F64: workspace already at {commit[:7]}")


def item_id(ws, item_type, name):
    _, _, out = fabric("GET", f"/workspaces/{ws}/items?type={item_type}")
    hits = [i["id"] for i in out.get("value", []) if i["displayName"] == name]
    if len(hits) != 1:
        sys.exit(f"{item_type} {name} found {len(hits)} times in {ws}")
    return hits[0]


def run_notebook(params):
    nb = item_id(HARNESS_WS, "Notebook", NOTEBOOK)
    body = {"executionData": {"parameters": {k: {"value": str(v), "type": "string"} for k, v in params.items()}}}
    status, headers, out = fabric("POST", f"/workspaces/{HARNESS_WS}/items/{nb}/jobs/instances?jobType=RunNotebook", body)
    loc = headers.get("location")
    job_id = loc.rstrip("/").split("/")[-1]
    print(f"Notebook job {job_id} started, run {params.get('harness_run_id')}")
    print(f"If this driver stops, pick the job up again with: --attach {job_id} --run-id {params.get('harness_run_id')}")
    return wait_for_job(loc)


def wait_for_job(loc):
    job_id = loc.rstrip("/").split("/")[-1]
    start, last = time.time(), None
    while True:
        time.sleep(30)
        s, _, job = http("GET", loc)
        if s >= 300:
            print(f"  poll HTTP {s}, retrying")
            continue
        if job.get("status") != last:
            last = job.get("status")
            print(f"  {dt.datetime.now():%H:%M:%S} {last} ({(time.time() - start) / 60:.1f} min)")
        if last in ("Completed", "Failed", "Cancelled", "Deduped"):
            return job_id, job


def onelake_files(lake_id, folder):
    url = (f"{ONELAKE}/{HARNESS_WS}?resource=filesystem&recursive=false&directory="
           + urllib.parse.quote(f"{lake_id}/Files/{folder}"))
    s, _, out = http("GET", url, resource="https://storage.azure.com", headers={"x-ms-version": "2023-11-03"})
    if s >= 300:
        return []
    return [p["name"] for p in out.get("paths", []) if p.get("isDirectory") != "true"]


def download(name):
    s, _, content = http("GET", f"{ONELAKE}/{HARNESS_WS}/{urllib.parse.quote(name)}",
                         resource="https://storage.azure.com", headers={"x-ms-version": "2023-11-03"}, raw=True)
    if s >= 300:
        sys.exit(f"download {name}: HTTP {s} {content}")
    return content


# Result files the notebook writes, and the repo CSV each one is appended to.
APPEND_TO = {
    "rows.csv": RUNS_CSV,
    "query-queries.csv": ROOT / "results" / "query-runs.csv",
    "query-pages.csv": ROOT / "results" / "query-pages.csv",
    "query-summary.csv": ROOT / "results" / "query-summary.csv",
}


def append_csv(target, text, job_id):
    """Append rows with the job instance ID in front. Append only, never rewrite."""
    new_rows = list(csv.DictReader(text.splitlines()))
    if not new_rows:
        return 0
    fields = ["job_instance_id"] + list(new_rows[0].keys())
    if target.exists():
        with target.open(newline="", encoding="utf-8") as f:
            header = next(csv.reader(f), [])
        if header != fields:
            sys.exit(f"{target} has different columns. Not touching it; the rows are in the run folder.")
    write_header = not target.exists()
    with target.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            w.writeheader()
        for r in new_rows:
            w.writerow({"job_instance_id": job_id, **r})
    return len(new_rows)


def pull_results(run_id, job_id):
    lake_id = item_id(HARNESS_WS, "Lakehouse", LAKEHOUSE)
    names = onelake_files(lake_id, f"harness/runs/{run_id}")
    if not names:
        print("No result files in harness_lake for this run. Check the notebook run in the F64 workspace.")
        return None
    out_dir = ROOT / "results" / "harness" / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in names:
        content = download(name)
        base = name.rsplit("/", 1)[-1]
        if base in APPEND_TO:   # these rows live in the repo CSVs, not in the run folder
            n = append_csv(APPEND_TO[base], content.decode("utf-8"), job_id)
            print(f"Appended {n} row(s) to {APPEND_TO[base].relative_to(ROOT)}")
        else:
            (out_dir / base).write_bytes(content)
    summary = out_dir / "summary.md"
    return summary if summary.exists() else None


def upload(lake_id, path, content):
    """Write one file to harness_lake Files/ through the OneLake DFS API."""
    url = f"{ONELAKE}/{HARNESS_WS}/{lake_id}/Files/{urllib.parse.quote(path)}"
    h = {"x-ms-version": "2023-11-03"}
    steps = [("PUT", url + "?resource=file", None),
             ("PATCH", url + "?action=append&position=0", content),
             ("PATCH", url + f"?action=flush&position={len(content)}", None)]
    for method, u, data in steps:
        req = urllib.request.Request(u, data=data if data is not None else b"", method=method,
                                     headers={"Authorization": "Bearer " + token("https://storage.azure.com"), **h})
        try:
            urllib.request.urlopen(req).read()
        except urllib.error.HTTPError as e:
            sys.exit(f"upload {path}: {method} HTTP {e.code} {e.read().decode(errors='replace')[:500]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("variant")
    ap.add_argument("--targets", default="F64", help="comma separated, run in this order: F2,F64")
    ap.add_argument("--task", choices=["refresh", "queries"], default="refresh")
    ap.add_argument("--pages", default="p01,p05,p10,p20", help="queries task")
    ap.add_argument("--modes", default="cold,warm", help="queries task")
    ap.add_argument("--concurrency", default="seq,page", help="queries task")
    ap.add_argument("--repeats", default="5", help="queries task")
    ap.add_argument("--attach", metavar="JOB_ID", help="wait for a job that is already running and pull its results")
    ap.add_argument("--run-id", help="with --attach: the harness run id of that job")
    args = ap.parse_args()
    if args.attach:
        nb = item_id(HARNESS_WS, "Notebook", NOTEBOOK)
        job_id, job = wait_for_job(f"{FABRIC}/workspaces/{HARNESS_WS}/items/{nb}/jobs/instances/{args.attach}")
        if job.get("status") != "Completed":
            print(f"Notebook job ended {job.get('status')}: {json.dumps(job.get('failureReason'))[:1500]}")
        run_id = args.run_id
        if not run_id:   # the newest run folder; run ids start with their UTC start time
            lake_id = item_id(HARNESS_WS, "Lakehouse", LAKEHOUSE)
            url = (f"{ONELAKE}/{HARNESS_WS}?resource=filesystem&recursive=false&directory="
                   + urllib.parse.quote(f"{lake_id}/Files/harness/runs"))
            _, _, out = http("GET", url, resource="https://storage.azure.com", headers={"x-ms-version": "2023-11-03"})
            run_id = sorted(p["name"].rsplit("/", 1)[-1] for p in out.get("paths", []))[-1]
            print(f"Newest run folder: {run_id}")
        summary = pull_results(run_id, job_id)
        if summary:
            print(summary.read_text(encoding="utf-8"))
        return
    targets = [t.strip() for t in args.targets.split(",") if t.strip()]
    if not (ROOT / "models" / args.variant).is_dir():
        sys.exit(f"models/{args.variant} does not exist")

    data_tag = committed_data_tag(args.variant)
    commit = check_pushed()
    print(f"{args.variant}: DataTag {data_tag} at {commit[:7]}, targets {', '.join(targets)}")
    if args.task == "refresh":
        warn_before_10m(args.variant, data_tag, targets)
    sync_harness_workspace(commit)

    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + args.variant.split("-")[0] + "-" + uuid.uuid4().hex[:4]
    params = {"variant": args.variant, "data_tag": data_tag, "targets": ",".join(targets),
              "expected_commit": commit, "harness_run_id": run_id, "task": args.task}
    if args.task == "queries":
        qpath = f"reports/queries/{args.variant}.json"
        try:
            qtext = git("show", f"HEAD:{qpath}")   # the committed queries, not the working tree
        except subprocess.CalledProcessError:
            sys.exit(f"{qpath} is not committed. Run reports/generate.py {args.variant} and commit.")
        lake_id = item_id(HARNESS_WS, "Lakehouse", LAKEHOUSE)
        upload(lake_id, f"harness/queries/{run_id}.json", qtext.encode("utf-8"))
        params.update({"queries_file": f"harness/queries/{run_id}.json", "pages": args.pages,
                       "modes": args.modes, "concurrency": args.concurrency, "repeats": args.repeats})
    job_id, job = run_notebook(params)
    if job.get("status") != "Completed":
        print(f"Notebook job ended {job.get('status')}: {json.dumps(job.get('failureReason'))[:1500]}")
    summary = pull_results(run_id, job_id)
    if summary:
        print("\n" + summary.read_text(encoding="utf-8"))
        print(f"\nSummary saved to {summary.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
