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
LIMITS_MB = {"F2": 3066, "F16": 5120, "F32": 10240, "F64": 25600}
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
    try:
        with urllib.request.urlopen(req) as r:
            content = r.read()
            return r.status, {k.lower(): v for k, v in r.headers.items()}, (content if raw else (json.loads(content) if content else {}))
    except urllib.error.HTTPError as e:
        return e.code, {k.lower(): v for k, v in e.headers.items()}, e.read().decode(errors="replace")


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
    if git("status", "--porcelain", "--", "models", "harness"):
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
    print(f"Notebook job {job_id} started")
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


def pull_results(run_id, job_id):
    lake_id = item_id(HARNESS_WS, "Lakehouse", LAKEHOUSE)
    names = onelake_files(lake_id, f"harness/runs/{run_id}")
    if not names:
        print("No result files in harness_lake for this run. Check the notebook run in the F64 workspace.")
        return None
    out_dir = ROOT / "results" / "harness" / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    rows_text = None
    for name in names:
        content = download(name)
        base = name.rsplit("/", 1)[-1]
        (out_dir / base).write_bytes(content)
        if base == "rows.csv":
            rows_text = content.decode("utf-8")
    if rows_text:
        new_rows = list(csv.DictReader(rows_text.splitlines()))
        fields = ["job_instance_id"] + list(new_rows[0].keys())
        existing = read_runs()
        if existing and list(existing[0].keys()) != fields:
            sys.exit(f"{RUNS_CSV} has different columns. Not touching it; rows are in {out_dir / 'rows.csv'}.")
        write_header = not RUNS_CSV.exists()
        with RUNS_CSV.open("a", newline="", encoding="utf-8") as f:   # append only, never rewrite
            w = csv.DictWriter(f, fieldnames=fields)
            if write_header:
                w.writeheader()
            for r in new_rows:
                w.writerow({"job_instance_id": job_id, **r})
        (out_dir / "rows.csv").unlink()   # the rows live in harness-runs.csv
        print(f"Appended {len(new_rows)} row(s) to {RUNS_CSV.relative_to(ROOT)}")
    summary = out_dir / "summary.md"
    return summary if summary.exists() else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("variant")
    ap.add_argument("--targets", default="F64", help="comma separated, run in this order: F2,F64")
    args = ap.parse_args()
    targets = [t.strip() for t in args.targets.split(",") if t.strip()]
    if not (ROOT / "models" / args.variant).is_dir():
        sys.exit(f"models/{args.variant} does not exist")

    data_tag = committed_data_tag(args.variant)
    commit = check_pushed()
    print(f"{args.variant}: DataTag {data_tag} at {commit[:7]}, targets {', '.join(targets)}")
    warn_before_10m(args.variant, data_tag, targets)
    sync_harness_workspace(commit)

    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + args.variant.split("-")[0] + "-" + uuid.uuid4().hex[:4]
    job_id, job = run_notebook({"variant": args.variant, "data_tag": data_tag, "targets": ",".join(targets),
                                "expected_commit": commit, "harness_run_id": run_id})
    if job.get("status") != "Completed":
        print(f"Notebook job ended {job.get('status')}: {json.dumps(job.get('failureReason'))[:1500]}")
    summary = pull_results(run_id, job_id)
    if summary:
        print("\n" + summary.read_text(encoding="utf-8"))
        print(f"\nSummary saved to {summary.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
