# Refresh memory lab: findings

A summary of the lab in this repository, written as input for an article on how semantic model design drives peak refresh memory and the Fabric capacity a model needs. Every number below comes from a measured run. Details per model are in `models/<model>/README.md`.

## The question

A customer had a semantic model of 124 MB. It refreshed on a Pro workspace but failed on F2, F4 and F8, where a model may use at most about 3 GB during refresh. The lab set out to reproduce that and to find which design choices drive refresh memory.

## Setup

- Data: Contoso sales data as Parquet files in GitHub releases. `data-1m-v1` has 2.35M sales rows, `data-10m-v1` has 23.7M.
- Source: `Web.Contents` to github.com plus `Parquet.Document`. This source cannot fold, so every Power Query step runs in the Power Query engine.
- Baseline (v00): a clean star schema. Sales fact, Customer, Product, Store, Date, Currency Exchange. Typed columns, no calculated columns or tables, single direction relationships, auto date/time off.
- Variants: each model folder changes one thing, or a small set of things, against the baseline or against a diagnostic parent. Each has a README with the change and its results.
- Capacities: an F2 workspace and an F64 workspace. One Pro run.
- Measurement on F64: Fabric workspace monitoring (`SemanticModelLogs`). The `ExecutionMetrics` event of each refresh gives `approximatePeakMemConsumptionKB` (peak of the whole refresh) and `mEnginePeakMemoryKB` (peak of the Power Query engine), plus duration and CPU. The `Backup` step gives the size of the committed model in bytes. Queries are in `analysis/refresh-memory.kql`.
- Measurement on F2: pass or fail only. F2 cannot carry workspace monitoring. A failure message reports "consumed memory", "memory limit" and "database size before command execution".
- Units: MB is 1,048,576 bytes and GB is 1,024 MB everywhere, for peaks, limits and model sizes. Peaks come in KB from the engine; model sizes are the `Backup` bytes divided by 1,048,576.
- Observed limits: F2 3,065 to 3,067 MB per model, F64 25,592 to 25,593 MB per model.

## Main findings

### 1. Power Query memory counts against the semantic model memory limit

In every run where Power Query does heavy work (sorts, Group By, buffers, merges), the Power Query engine accounts for 93 to 99 percent of the peak refresh memory. Failed refreshes report "Data source error" with "Resource Governance ... consumed memory". The model limit covers the whole refresh, not only what ends up in the model.

### 2. Model size does not predict refresh memory

| Model | Change vs baseline | Model size | F64 peak |
|---|---|---|---|
| v00 | none | 73 MB | 785 MB |
| v20 | two sorts of Sales in Power Query | 72 MB | 5,229 MB |
| v21 | one summary table built with Group By in Power Query | 85 MB | 3,767 MB |

v20 loads exactly the same table as the baseline. Only the row order differs. It needs almost 7 times the memory, and it fails on F2.

### 3. One common Power Query step is enough to take a clean model off F2

On the clean baseline:

- v20, two sorts of the 2.35M row fact: fails on F2, refreshes on F64.
- v21, one Group By over the fact into a small summary table: fails on F2, refreshes on F64.

A sort or a Group By has to read the whole input before it returns its first row. Steps that work row by row do not raise memory:

- v99n, every column converted to text and converted back late: peak about the same as without it (624 vs 627 MB).
- v99p, two high cardinality columns added in Power Query: 746 MB.

### 4. Row by row steps cost time and CPU instead

| Model | Duration | Total CPU |
|---|---|---|
| v99m (no Power Query antipatterns) | 0.8 min | 73 s |
| v99n (text staging) | 5.3 min | 339 s |
| v20 (sorts on the baseline) | 8.6 min, vs 0.7 for the baseline | 739 s, vs 64 for the baseline |

### 5. Antipatterns combine to more than their sum

Measured alone on top of the same model: text staging adds almost nothing, sorts reach 5.3 GB, the Group By 3.5 GB. Combined in one model, where the sorts and the Group By run on text and two tables read the same staging query (v99k), the peak is 13.0 GB.

### 6. Table.Buffer on a large staging query is the extreme case

v99i adds one `Table.Buffer` to the Sales staging query, which three tables reference. It fails on F64 at the 25.6 GB limit. The same buffer on the Customer staging query (v99j, 105K rows) changes nothing. This pattern is rare in practice, so the article should treat it as an extreme example rather than the typical cause.

### 7. Calculated columns are cheap, calculated tables are not, and they scale with data

| Model | Data | F64 peak | Outside Power Query | Model size |
|---|---|---|---|---|
| v00 baseline | 1M | 785 MB | about 110 MB | 73 MB |
| v22, 8 calculated columns on Sales | 1M | 686 MB | about 260 MB | 101 MB |
| v23, 4 calculated tables | 1M | 1,405 MB | about 1,000 MB | 184 MB |
| v00 baseline | 10M | 2,040 MB | about 210 MB | 778 MB |
| v23, 4 calculated tables | 10M | 13,062 MB | about 11,900 MB | 1,833 MB |

- Each calculated column takes 0.6 to 3.5 seconds to compute on 2.35M rows. Removing all eight from a heavy model changed its peak by 114 MB.
- The calculated tables (a full copy of Sales with six RELATED columns, a SUMMARIZECOLUMNS summary, a product by day CROSSJOIN, CALENDARAUTO) add about 900 MB on 1M and about 11.7 GB on 10M. On 10M that model needs F64, while the clean baseline on the same data peaks at 2 GB.
- "Outside Power Query" is the total peak minus the Power Query peak. The two peaks may not happen at the same moment, so treat it as an approximation.

### 8. Power Query has a second, separate limit

v19 builds five analysis tables in Power Query from the 10M data (merges, Group By with distinct counts, rankings, a self join) and loads only small results. On F64 it fails with a different error: "The M evaluation exceeded the memory limit ... Container exited unexpectedly with code 0x0000DEAD". Its peaks at failure were 14.4 to 24.5 GB, below the 25.6 GB model limit. With the self join reduced to 1M data it still fails, and in every failed run the query still running was `PQ Customer RFM`, which ranks all 1.68M customers three times. A single Power Query evaluation has its own memory limit, separate from the model limit. Its size was not measured and is not documented in this lab.

### 9. Peak memory on a large capacity predicts the result on a small one

For every model run on both F64 and F2, the F64 peak sorted it correctly against the F2 limit of about 3,066 MB:

- Below the limit, refreshed on F2: v00 (785), v18 (1,562), v22 (686), v23 (1,405), v99m (627), v99n (624), v99p (746).
- Above the limit, failed on F2: v99q (3,477), v21 (3,767), v20 (5,229), v99o (5,337), v99l (12,878), v99k (12,992), v99a (16,054).

This gives a practical method: refresh once on a capacity with monitoring, read the peak, and compare it with the per model limit of the target SKU.

### 10. The failure message does not give the real need

"Consumed memory" in a resource governance error is where the engine stopped the refresh, a few MB to about 100 MB over the limit. It is not the memory the refresh would have needed. Example: v99l failed on F2 at 3,146 MB, but its full peak on F64 is 12,878 MB.

### 11. Pro behaves differently

The full kitchen sink model (v99) refreshed on Pro, giving a .pbix of 458 MB. On F2 it failed at 3,319 MB and on F64 it failed at the 25.6 GB limit. This matches the customer case: a model that works on Pro and fails on a Fabric capacity. Only one Pro run was made, and the lab does not establish what limits Pro applies.

## Diagnostic path, for the narrative

1. v99, a kitchen sink of antipatterns, fails on F2 and F64 and refreshes on Pro.
2. Removing the large calculated tables and the flat table (v99a) brings it to 16 GB: refreshes on F64, fails on F2.
3. Adding parts back one by one (v99d to v99j) shows that one `Table.Buffer` on the Sales staging query is what pushes it past 25.6 GB.
4. Without any `Table.Buffer` (v99k) it still needs 13 GB.
5. Splitting v99k: without calculated columns (v99l) still 12.9 GB; with the baseline Power Query (v99m) only 627 MB. The Power Query half is the cause.
6. Adding back one Power Query part at a time to v99m (v99n to v99q): the sorts and the Group By each fail F2, text staging and extra columns do not.
7. The same sort and Group By on the clean baseline (v20, v21) still fail F2.

## Caveats

- The source cannot fold. With a SQL source, sorts and Group By steps that fold run in the database and do not cost refresh memory. The findings apply to non folding sources (files, web, APIs) and to steps that break folding.
- Most models were refreshed once or a few times, so most peaks are single measurements. Repeated runs can differ a lot. v00 on 1M peaked at 785 MB on 2026-11-04 and at 551 MB on 2026-11-07, with the same rows loaded and the same parallelism; almost all of the difference is Power Query (677 vs 312 MB). v99d, on the other hand, stayed within 1 percent over three runs (16,005 to 16,056 MB). Failed runs vary more, since the peak depends on when the engine stops. Differences of a few hundred MB between single runs are not evidence of a design effect; the large effects in this document (several times the baseline) are well beyond that spread.
- F2 results are pass or fail only.
- A second refresh right after the first, with the old data still in memory, passed on F2 for v22 and v23 on 1M data. Those models peak far below the limit, so this does not test how much the old copy adds.
- The 124 MB customer model was not reproduced exactly. The lab shows the mechanism with models of 72 to 114 MB that need 3.5 to 5.3 GB.
- Peak figures are the engine's approximate peak, not an operating system measurement.

## All runs

Peaks are from F64 unless noted. All sizes are in MB of 1,048,576 bytes.

The same model has a different size depending on where you look:

- Service size: the `Backup` step in the F64 refresh log, the size of the committed model in the service. Measured for every model that refreshed on F64.
- Desktop file size: what a user sees on disk after refreshing in Power BI Desktop. For a .pbix it is the file size; for a PBIP project it is `.pbi/cache.abf` in the semantic model folder. Often the only size a user ever sees.
- DAX Studio size: Advanced > View Metrics (VertiPaq Analyzer) in DAX Studio, total size, connected to the model open in Desktop. The in-memory size of the data, dictionaries, hierarchies and relationships.

For v00 on 1M the service size is 73 MB, and a DAX query in the service over `INFO.STORAGETABLECOLUMNSEGMENTS` and the column dictionaries gave 93 MB (harness run on F2, 2026-11-10). The Desktop columns are filled in by hand from Desktop measurements.

| Model | What it is | F64 result | F64 peak MB | Power Query MB | F2 result | Service size | Desktop file size | DAX Studio size |
|---|---|---|---|---|---|---|---|---|
| v00-baseline | clean star schema, 1M | refreshed | 785 | 677 | refreshed | 73 MB |  |  |
| v00-baseline | same, 10M | refreshed | 2,040 | 1,832 | not run | 778 MB |  |  |
| v18-pq-10m-summary | baseline plus a 590 row summary grouped from the 10M file | refreshed | 1,562 | 1,372 | refreshed | 73 MB |  |  |
| v19-pq-heavy-10m | baseline plus five Power Query analyses on 10M | failed, Power Query limit | 14,366 to 24,464 at failure | | failed at 3,242 | |  |  |
| v20-pq-sort | baseline plus two sorts of Sales | refreshed | 5,229 | 4,965 | failed | 72 MB |  |  |
| v21-pq-group-by | baseline plus a Group By summary table | refreshed | 3,767 | 3,604 | failed | 85 MB |  |  |
| v22-dax-calc-columns | baseline plus 8 calculated columns | refreshed | 686 | 430 | refreshed twice | 101 MB |  |  |
| v23-dax-calc-tables | baseline plus 4 calculated tables, 1M | refreshed | 1,405 | 399 | refreshed twice | 184 MB |  |  |
| v23-dax-calc-tables | same, 10M | refreshed | 13,062 | 1,202 | not run | 1,833 MB |  |  |
| v99-kitchen-sink | everything | failed at 25.6 GB | | | failed at 3,319 |  | 458 MB (.pbix of the Pro run) |  |
| v99a | v99 without big calculated tables and flat table | refreshed | 16,054 | 15,932 | failed at 3,099 | 185 MB |  |  |
| v99d | v99a plus an unused heavy query | refreshed | 16,010 | 15,925 | not run | 185 MB |  |  |
| v99e | v99d plus the flat table loaded | refreshed | 22,889 | 22,766 | not run | 323 MB |  |  |
| v99f | v99e plus three calculated tables | refreshed | 22,752 | 22,600 | not run | 361 MB |  |  |
| v99g | v99f plus a copy of Sales | refreshed | 23,025 | 22,899 | not run | 533 MB |  |  |
| v99h | v99g plus two staging buffers | failed at 25.6 GB | | | not run | |  |  |
| v99i | v99g plus the Sales staging buffer | failed at 25.6 GB | | | not run | |  |  |
| v99j | v99g plus the Customer staging buffer | refreshed | 22,894 | 22,789 | not run | 533 MB |  |  |
| v99k | v99a without any Table.Buffer | refreshed | 12,992 | 12,892 | failed | 185 MB |  |  |
| v99l | v99k without calculated columns | refreshed | 12,878 | 12,760 | failed at 3,146 | 158 MB |  |  |
| v99m | v99k with the baseline Power Query | refreshed | 627 | 272 | refreshed | 102 MB |  |  |
| v99n | v99m plus text staging | refreshed | 624 | 294 | refreshed | 92 MB |  |  |
| v99o | v99m plus sorts | refreshed | 5,337 | 5,048 | failed | 99 MB |  |  |
| v99p | v99m plus high cardinality columns | refreshed | 746 | 335 | refreshed | 175 MB |  |  |
| v99q | v99m plus the Group By table | refreshed | 3,477 | 3,243 | failed | 114 MB |  |  |

## Evidence files

### Monitoring exports (F64 workspace, `SemanticModelLogs`)

Exported from the KQL queryset with the queries in `analysis/refresh-memory.kql`, on 2026-11-06.

| File | Query | Content |
|---|---|---|
| `results/monitoring-refreshes.csv` | 1 | one row per refresh on F64: model, result, peak, Power Query peak, duration, CPU, rows loaded |
| `results/monitoring-peak-latest.csv` | 2 | latest refresh per model, including the 10M runs of v00 and v23 |
| `results/monitoring-peak-latest-before-10m-runs.csv` | 2 | same, before the 10M runs (v00 and v23 on 1M) |
| `results/monitoring-steps-per-table-latest.csv` | 3 | time, CPU and rows per table and step, latest refresh per model (v00 and v23 on 10M) |
| `results/monitoring-steps-per-table-before-10m-runs.csv` | 3 | same, with v00 and v23 on 1M |
| `results/monitoring-failed-steps.csv` | 4 | steps still running when each failed F64 refresh was stopped |

Reading notes: the `Backup` step in the per-table files gives the committed model size in bytes. `ReadData` rows give the rows delivered per partition.

### Screenshots (`docs/screenshots/`)

| File | Shows |
|---|---|
| `f2-v99-kitchen-sink-resource-governance.png` | v99 on F2: consumed 3,319 MB, limit 3,065 MB, database size before command 6 MB |
| `f64-v99d-first-version-resource-governance.png` | v99d (first version, with staging buffers) on F64: consumed 25,598 MB, limit 25,593 MB |
| `f64-v99h-staging-buffers-resource-governance.png` | v99h on F64: consumed 25,603 MB, limit 25,592 MB |
| `f64-v99i-buffer-stg-sales-resource-governance.png` | v99i on F64: consumed 25,604 MB, limit 25,592 MB |
| `v19-parameters-last-runs.png` | parameters of v19 for the runs from 09:55 on 2026-11-06 |

### Error texts received as text only

v99l on F2, 2026-11-05 15:06 UTC:

> Data source error Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. [...] More details: consumed memory 3146 MB, memory limit 3066 MB, database size before command execution 5 MB.

v19 on F64, 2026-11-06 10:33:54 UTC (the Power Query limit, finding 8):

> Data source error The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 27004. Used features: (none).

The F2 failures of v99a (3,099 MB, limit 3,065 MB) and v19 (3,242 MB, limit 3,067 MB) were also received as text; their numbers are in the tables above. v20, v21, v99k, v99o and v99q were reported as failed on F2 without the error text.
