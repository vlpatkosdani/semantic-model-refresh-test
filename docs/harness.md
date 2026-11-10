# Refresh harness

The harness runs one variant from this repo on the lab capacities and records what happened. It replaces the manual cycle of publishing, refreshing in the service, running the KQL queries and copying numbers into READMEs.

## What is in the repo

| Path | What it is |
|---|---|
| `harness/refresh-harness.Notebook/` | The Fabric notebook (PySpark). Git integration creates it in the F64 workspace, where it runs. |
| `harness/harness_lake.Lakehouse/` | The Lakehouse for the results, in the F64 workspace. |
| `harness/run_variant.py` | The local driver. Starts the notebook and pulls its results into the repo. Python standard library only. |
| `results/harness-runs.csv` | One row per refresh, appended by the driver. Never rewritten. |
| `results/harness/<run id>/` | Run summary (`summary.md`) and the log extracts of that run (`f64-metrics.csv`, `f64-steps.csv`, `f64-failed_steps.csv`). |

## One cycle

1. Build or change the variant in `models/<variant>/`. Commit and push.
2. `python harness/run_variant.py <variant> --targets F2,F64`
3. Read the summary it prints. Update the variant README and `docs/lab-findings.md` from it.
4. Commit the new rows and the run folder.

What the driver does:

1. Reads `DataTag` from the variant's TMDL in the commit (HEAD), not from the working tree and not from the service.
2. Checks that HEAD is pushed. It does not push.
3. Before a 10M run, prints the 1M results of the same variant and warns if one of them failed or peaked at 80% or more of a target's limit.
4. Brings the F64 workspace up to the pushed commit, so the notebook that runs is the committed one. It stops if the workspace has uncommitted changes or conflicts.
5. Starts the notebook through the Job Scheduler API (`RunNotebook`) with the parameters below, and polls the job every 30 seconds.
6. Downloads the run folder from `harness_lake` (OneLake), appends the rows to `results/harness-runs.csv` with the job instance ID, and saves the summary.

What the notebook does, per target:

1. Git status of the workspace. Stops on uncommitted changes or conflicts, and if the workspace does not see the pushed commit. Otherwise runs Update from Git. It never resolves a conflict: the check runs before the update, so the only thing the update replaces is the previous committed version of an item. Fabric needs explicit consent for that (`allowOverrideItems`), which the harness gives.
2. Finds the semantic model by name and reads `DataTag` back through the REST parameters API. Stops if it differs from the committed value.
3. All targets pass steps 1 and 2 before any refresh starts. Then the targets refresh one after the other.
4. Full refresh through the enhanced refresh API: `type full`, transactional, `maxParallelism 6` (what the service used for the manual runs), no retries. Polls until it ends. Records the request ID, start, end, status and the full error text. From the error text it reads consumed memory, memory limit and database size, and whether it is the Power Query error "The M evaluation exceeded the memory limit".
5. F64 only: polls `SemanticModelLogs` until the `ExecutionMetrics` event of that refresh arrives (up to 20 minutes), then runs queries 1, 3 and 4 of `analysis/refresh-memory.kql` narrowed to that refresh.
6. Compares the run with the previous harness run of the same variant, capacity and data, and with the latest refreshed v00-baseline on the same capacity and data. A peak change of more than 1% or a changed result is flagged. A measured peak is set against the per-model limits: F2 3,066 MB, F16 5,120 MB, F32 10,240 MB, F64 25,600 MB.
7. Appends one row to the Delta table `refresh_runs` and writes `rows.csv`, the log extracts and `summary.md` to `Files/harness/runs/<run id>/`.

If a check fails, the notebook writes a summary with the reason and ends as failed. No refresh has started at that point.

## Parameters

| Parameter | Default | Meaning |
|---|---|---|
| `variant` | `v00-baseline` | Model folder and semantic model name |
| `data_tag` | `data-1m-v1` | The `DataTag` the model must read back |
| `targets` | `F64` | `F2`, `F64` or `F2,F64`, refreshed in that order |
| `expected_commit` | empty | Commit the workspaces must see. Empty means whatever the remote branch has |
| `harness_run_id` | empty | Run folder name. Empty means generate one |
| `max_refresh_minutes` | `120` | When to stop polling a refresh |
| `max_log_wait_minutes` | `20` | When to stop waiting for the monitoring event |

## How the refresh is matched in the logs

The request ID of the refresh API does not appear in `SemanticModelLogs`, and the table has no `XmlaRequestId` column. The notebook matches by model ID (`ItemId`) and time: the `ExecutionMetrics` event with `tabularConnectionTimeoutMs` whose `timeStart` is within two minutes of the start the refresh API reports. Only one refresh per model runs at a time, so this is unambiguous as long as nobody refreshes the same model by hand during a harness run.

## What is measured where

| Number | F64 | F2 |
|---|---|---|
| Peak memory, Power Query peak, CPU, rows | `ExecutionMetrics` | not available (no monitoring) |
| Duration | `ExecutionMetrics` | start and end from the refresh API |
| Model size | `Backup` step in the logs | DAX over `INFO.STORAGETABLECOLUMNSEGMENTS` and dictionaries, only if refreshed |
| Memory at cancellation | error text | error text |

The two model sizes are not the same measure. The column `model_size_source` says which one a row has.

## 1M and 10M

The data size is the `DataTag` parameter in the variant's TMDL (`expressions.tmdl`). To run 10M:

1. Change `DataTag` to `data-10m-v1` in TMDL and commit ("v00 to 10M").
2. Push and run the driver. It warns if the 1M run was near a limit.
3. Change it back to `data-1m-v1` and commit ("v00 back to 1M"), push, so the default stays 1M.

Never change the parameter in the service settings. The workspace would then differ from Git, and the next Update from Git either fails or overwrites it. The notebook stops when the read-back value differs from the committed one.

The read-back value is in every row (`data_tag_readback`).

## Setup (once)

1. Both workspaces clean in Source control (nothing uncommitted).
2. Git folders: F64 syncs the repo root (`/`), F2 syncs `/models` only. F2 cannot hold Fabric items such as notebooks, Lakehouses or KQL querysets ("The user is not allowed to create this fabric item"), and an Update from Git is all or nothing, so one such folder in its scope blocks every update. Keep everything that is not a Power BI item outside `models/`.
3. Commit and push the `harness/` folder. The driver brings F64 up to date, which creates the notebook and the Lakehouse there.
4. Local: `az login` as yourself, in the lab tenant. The driver uses `az account get-access-token` for the Fabric API and OneLake.

## Permissions

Everything runs as Dani. No service principal, no secrets in the repo.

| Call | Needs |
|---|---|
| Git status and Update from Git | Contributor or higher on both workspaces, and access to the GitHub connection |
| Read parameters, enhanced refresh | Write permission on the semantic models (owner or workspace member) |
| `SemanticModelLogs` | Viewer on the F64 workspace (the Monitoring KQL database) |
| Write to `harness_lake`, run the notebook | Contributor on the F64 workspace |
| Driver | The same user signed in with `az login` |

## Running by hand

1. Open `refresh-harness` in the F64 workspace.
2. Set the parameters in the parameters cell (at least `variant`, `data_tag` and `targets`). Leave `expected_commit` empty.
3. Run all. The summary prints at the end and is in `harness_lake` under `Files/harness/runs/<run id>/`.
4. To bring the results into the repo, download the run folder and append the row by hand, or run the driver next time. The Delta table `refresh_runs` has every row either way.

Make sure the workspaces are updated from Git first, or leave that to the notebook (step 1 above).

## Cost

The notebook runs on the F64 capacity. A run starts a Spark session and installs semantic-link-labs (about a minute), then mostly waits. A refresh on F2 uses F2 capacity units, as a manual refresh would. Nothing scales, pauses, resumes or creates a capacity. One variant per run; there is no loop that keeps refreshing.

## Library choices

| Need | Used | Why |
|---|---|---|
| Git status, Update from Git, items | Fabric REST through `sempy.fabric.FabricRestClient` (`lro_wait=True`) | `semantic-link-labs` has `update_from_git`, but its `get_git_status` returns no workspace head or remote commit when there are no changes, and both are needed for the update |
| Read `DataTag` back | Power BI REST `datasets/{id}/parameters` through `PowerBIRestClient` | Plain REST, works on F2 and F64 without XMLA |
| Refresh | Power BI enhanced refresh REST through `PowerBIRestClient` | `sempy.fabric.refresh_dataset` wraps the same API, but the harness needs the request ID, the raw messages and its own polling with a timeout |
| KQL | `sempy_labs.query_kusto` (0.18.1) | Uses the notebook user's token for the Eventhouse and takes the KQL database ID |
| Model size on F2 | `sempy_labs.get_semantic_model_size` | DAX `INFO` functions, no XMLA write needed |
| Driver | Python standard library and the az CLI token | Nothing to install locally |

Versions: semantic-link-labs is pinned to 0.18.1 in the first code cell. `sempy` is the version in the Fabric runtime (0.14.3 when this was written).

## Known limits

- F2 has no monitoring, so an F2 row has a peak only when the refresh fails with a resource governance error, and that number is where the engine stopped it.
- A peak for a failed refresh is a lower bound.
- If the `ExecutionMetrics` event does not arrive within 20 minutes, the row is recorded with numbers from the refresh API only (`metrics_source` says so).
- The comparison uses harness runs only. The earlier manual runs are in the READMEs and `results/monitoring-*.csv`.

## Notebook source format

Fabric rewrites a notebook it does not fully like and then shows it as modified, which stops the harness. Keep `notebook-content.py` the way Fabric stores it:

- no magic commands (`%pip`); the install is a `pip` call through `subprocess`
- no blank lines inside a markdown cell
- a `# METADATA` block after every code cell, including the last one

After editing the notebook, run it once by hand and compare with `getDefinition` if F64 shows it as modified.
