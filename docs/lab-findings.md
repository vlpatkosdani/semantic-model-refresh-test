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

Measured on Premium Per User (100 GB per model) with an XMLA trace on 2026-11-11, the buffer is the last step over the limit, not a large effect on its own. v99g without it peaked at 23,025 MB on F64. v99i, with the Sales buffer, needs 23,893 MB, and v99h, with both buffers, 25,971 MB (runs `20261111T090350Z-v99i-1beb` and `20261111T081746Z-v99h-601b`). The v99i peak is below F64's 25.6 GB limit, yet v99i was cancelled on F64 at 25,604 MB. Either the peak differs between F64 and Premium Per User, or it varies from run to run by more than the 1.7 GB of headroom; with one run on each, the lab cannot tell which. What holds: the model was already at 23 GB before the buffer, and it sits within a few GB of F64's limit with or without it.

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

The size of a calculated table does not decide the refresh peak; how it is calculated does. The four calculated tables are independent of each other: each reads only imported tables (Sales, Customer, Product, Date, Store). The refresh log shows they are not built one after the other: in v35 `Product Date Grid` ran while Sales was still loading, and `Sales Copy` and `Sales Summary` both started at 12:37:07 UTC and ran side by side (99 s for the summary, 448 s for the copy). On 10M (F64, 2026-11-13):

| Model | Change against v23 | Peak | Model in memory after |
|---|---|---|---|
| v23 | | 13,062 to 13,139 MB (3 runs) | 1,379 MB |
| v35 | `Sales Copy` with four copies of the Sales rows, 94.9M rows instead of 23.7M | 13,063 MB | 2,803 MB |
| v36 | `Sales Summary` by month instead of year, about 3M more rows | 14,759 MB | 1,406 MB |

69M more rows in a copy table doubled the model and the refresh time and left the peak unchanged. 3M more rows in the `SUMMARIZECOLUMNS` summary with three measures, one a distinct count, raised it by 1.7 GB. A large calculated table makes the model larger; a summary calculated with measures is what costs refresh memory.

### 8. Power Query has a second, separate limit

v19 builds five analysis tables in Power Query from the 10M data (merges, Group By with distinct counts, rankings, a self join) and loads only small results. On F64 it fails with a different error: "The M evaluation exceeded the memory limit ... Container exited unexpectedly with code 0x0000DEAD". Its peaks at failure were 14.4 to 24.5 GB, below the 25.6 GB model limit. With the self join reduced to 1M data it still fails, and in every failed run the query still running was `PQ Customer RFM`, which ranks all 1.68M customers three times. A single Power Query evaluation has its own memory limit, separate from the model limit. On Premium Per User (100 GB per model) v19 failed with the same error at 22,186 MB (2026-11-13), so this limit does not grow with the model limit. v99 used 25,958 MB of Power Query memory on PPU and refreshed, so the limit is not on the total Power Query memory of a refresh; it fits a limit per evaluation, which `PQ Customer RFM` alone exceeds. Its size was not measured and is not documented.

### 9. Peak memory on a large capacity predicts the result on a small one

For every model run on both F64 and F2, the F64 peak sorted it correctly against the F2 limit of about 3,066 MB:

- Below the limit, refreshed on F2: v00 (785), v18 (1,562), v22 (686), v23 (1,405), v99m (627), v99n (624), v99p (746).
- Above the limit, failed on F2: v99q (3,477), v21 (3,767), v20 (5,229), v99o (5,337), v99l (12,878), v99k (12,992), v99a (16,054).

This gives a practical method: refresh once on a capacity with monitoring, read the peak, and compare it with the per model limit of the target SKU.

### 10. The failure message does not give the real need

"Consumed memory" in a resource governance error is where the engine stopped the refresh, a few MB to about 100 MB over the limit. It is not the memory the refresh would have needed. Example: v99l failed on F2 at 3,146 MB, but its full peak on F64 is 12,878 MB.

### 11. Pro behaves differently

The full kitchen sink model (v99) refreshed on Pro, giving a .pbix of 458 MB. On F2 it failed at 3,319 MB and on F64 it failed at the 25.6 GB limit. This matches the customer case: a model that works on Pro and fails on a Fabric capacity. Only one Pro run was made, and the lab does not establish what limits Pro applies.

On a Premium Per User workspace (100 GB per model) v99 refreshed, and an XMLA trace of the refresh measured its full peak: 26,115 MB, of which 25,958 MB is Power Query, in 20 minutes, with a 622 MB model (harness run `20261110T162110Z-v99-0db3`, 2026-11-10). That is 2 percent over F64's 25.6 GB limit, which is where F64 cancelled it, and 8.5 times F2's limit. Premium Per User runs on shared hardware, so this is recorded as its own capacity, PPU, and not as an F64 number.

v99h also failed on F64 and refreshed on PPU (peak 25,971 MB). So PPU refreshes models that F64 cannot, but in this lab only by a small margin above the F64 limit, and only for models whose peak is Power Query memory. A larger model side peak was not reached: v35 and v36 tried to push the calculated tables past 25.6 GB and stayed at 13.1 and 14.8 GB (finding 7). Power Query memory per evaluation is not raised by PPU at all (finding 8).

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
- The model already in memory does not count in the measured peak. v23 on 10M peaked at 13,064 MB from empty, 13,139 MB with its 1,379 MB model loaded, and 13,062 MB after `clearValues` (F64, 2026-11-12). It counts against the limit instead: the command memory limit is the SKU maximum minus the model size before the refresh.
- The 124 MB customer model was not reproduced exactly. The lab shows the mechanism with models of 72 to 114 MB that need 3.5 to 5.3 GB.
- Peak figures are the engine's approximate peak, not an operating system measurement.

## All runs

Peaks are from F64 unless noted. All sizes are in MB of 1,048,576 bytes.

The same model has a different size depending on where you look:

- Service size: the `Backup` step in the F64 refresh log, the size of the committed model in the service. Measured for every model that refreshed on F64.
- Downloaded .pbix: the file size of the model downloaded from the service with its data (REST API Export report, `downloadType=IncludeModel`, 2026-11-11), the size a user sees on disk. The same as refreshing in Desktop and saving: v99 downloaded from Premium Per User is 448.3 MB, and the .pbix saved after the Pro refresh was 447.6 MB (458,321 KB). Only models whose last refresh in that workspace completed with the 1M data (10M for the second v00 row) are listed; a failed refresh leaves a file of about 1 MB.
- In memory after refresh: the VertiPaq size in the service right after a successful refresh, measured by the harness with a DAX query over `INFO.STORAGETABLECOLUMNSEGMENTS` and the column dictionaries (the same storage numbers DAX Studio reads). This is what the capacity holds for the model. Measured from 2026-11-11 on; older runs have no value. The same model reads 10 to 30 % smaller once the service reloads it from storage.
- DAX Studio size: Advanced > View Metrics (VertiPaq Analyzer) in DAX Studio, total size, connected to the model open in Desktop. The in-memory size of the data, dictionaries, hierarchies and relationships.

For v00 on 1M the service size is 73 MB, and a DAX query in the service over `INFO.STORAGETABLECOLUMNSEGMENTS` and the column dictionaries gave 93 MB (harness run on F2, 2026-11-10). The DAX Studio column is filled from DAX Studio connected to the model in Desktop: for v00 on 1M the six tables add up to 97,198,262 bytes, 92.7 MB. Sizes marked (file) are from the .pbix downloaded from F64 (or PPU, where marked) and opened in Desktop without a refresh. A model loaded from a file reads smaller than right after a refresh, mostly in the dictionaries: v00 in the service read 92.7 MB right after a refresh and 66.2 MB once reloaded from storage. So a (file) size compares with the reloaded v00, about 66 MB, not with 92.7 MB.

| Model | What it is | F64 result | F64 peak MB | Power Query MB | F2 result | Service size | In memory after refresh | Downloaded .pbix | DAX Studio size |
|---|---|---|---|---|---|---|---|---|---|
| v00-baseline | clean star schema, 1M | refreshed | 785 | 677 | refreshed | 73 MB | 92.7 MB | 49.2 MB | 92.7 MB |
| v00-baseline | same, 10M | refreshed | 2,040 | 1,832 | refreshed, 26 min | 778 MB | 700 MB | 473.6 MB | 625.7 MB (file) |
| v18-pq-10m-summary | baseline plus a 590 row summary grouped from the 10M file | refreshed | 1,562 | 1,372 | refreshed | 73 MB |  | 49.2 MB |  |
| v19-pq-heavy-10m | baseline plus five Power Query analyses on 10M | failed, Power Query limit (PPU: same error, peak 22,186) | 14,366 to 24,464 at failure |  | failed at 3,242 |  |  |  |  |
| v20-pq-sort | baseline plus two sorts of Sales | refreshed | 5,229 | 4,965 | failed | 72 MB |  | 51.7 MB | 65.3 MB (file) |
| v21-pq-group-by | baseline plus a Group By summary table | refreshed | 3,767 | 3,604 | failed | 85 MB |  | 57.4 MB |  |
| v22-dax-calc-columns | baseline plus 8 calculated columns | refreshed | 686 | 430 | refreshed twice | 101 MB |  | 72.5 MB |  |
| v23-dax-calc-tables | baseline plus 4 calculated tables, 1M | refreshed | 1,405 | 399 | refreshed twice | 184 MB |  | 115.1 MB |  |
| v23-dax-calc-tables | same, 10M | refreshed | 13,062 | 1,202 | not run | 1,833 MB | 1,379 MB |  |  |
| v35-calc-tables-four-copies | v23 with four copies in Sales Copy, 10M | refreshed | 13,063 | 1,601 | not run |  | 2,803 MB |  |  |
| v36-calc-summary-month-grain | v23 with Sales Summary by month, 10M | refreshed | 14,759 | 1,194 | not run |  | 1,406 MB |  |  |
| v24-bidirectional | Sales to Customer filters in both directions | refreshed | 608 | 335 | not run | 73 MB |  | 49.2 MB |  |
| v24a-second-fact | baseline plus a second fact table, Orders | refreshed | 933 | 911 | not run | 103 MB |  | 66.2 MB |  |
| v24b-second-fact-bidirectional | v24a with Sales to Customer in both directions | refreshed | 1,102 | 1,003 | not run | 103 MB |  | 66.2 MB |  |
| v25-many-to-many | baseline plus Customer Segment, many-to-many to Sales | refreshed | 614 | 457 | not run | 79 MB | 98.1 MB |  |  |
| v26-bad-dax | five measures in common bad DAX patterns | refreshed | 715 | 689 | refreshed | 73 MB | 92.7 MB on F2 | 49.2 MB |  |
| v27-high-cardinality-visuals | baseline model, report page with high-cardinality visuals | refreshed | 616 | 336 | not run | 73 MB |  | 49.2 MB |  |
| v28-types-all-text | almost every column loaded as text | refreshed | 777 | 629 | not run | 69 MB | 171.5 MB |  |  |
| v29-keys-as-text | key columns as text | refreshed | 665 to 1,735 (3 runs) | 398 to 1,720 | not run | 69 MB | 141.9 MB |  |  |
| v30-double-instead-of-fixed | prices and costs as decimal number instead of fixed decimal | refreshed | 550 | 270 | not run | 73 MB | 92.9 MB |  |  |
| v31-calc-columns-row | 32 row-level calculated columns on Sales | refreshed | 913 | 334 | not run | 223 MB | 316.8 MB |  | 233.5 MB (file) |
| v32-calc-columns-aggregate | 30 aggregating calculated columns | refreshed | 631 | 595 | not run | 221 MB | 367.9 MB |  |  |
| v33-auto-date-time | Auto date/time on, Date table marked | refreshed | 619 | 423 | not run | 74 MB | 96.2 MB |  |  |
| v34-auto-date-time-no-date-table | Auto date/time on, Date table not marked | refreshed | 707 | 421 | not run | 74 MB | 96.9 MB |  |  |
| v99-kitchen-sink | everything | failed at 25.6 GB (PPU: refreshed, peak 26,115) |  | 25,958 on PPU | failed at 3,319 | 622 MB on PPU |  | 448.3 MB on PPU (Pro run: 447.6 MB) | 626.4 MB (file, PPU) |
| v99a | v99 without big calculated tables and flat table | refreshed | 16,054 | 15,932 | failed at 3,099 | 185 MB |  | 134.7 MB |  |
| v99d | v99a plus an unused heavy query | refreshed | 16,010 | 15,925 | not run | 185 MB |  | 134.7 MB |  |
| v99e | v99d plus the flat table loaded | refreshed | 22,889 | 22,766 | not run | 323 MB |  | 233.4 MB |  |
| v99f | v99e plus three calculated tables | refreshed | 22,752 | 22,600 | not run | 361 MB |  | 248.2 MB |  |
| v99g | v99f plus a copy of Sales | refreshed | 23,025 | 22,899 | not run | 533 MB |  | 376.8 MB |  |
| v99h | v99g plus two staging buffers | failed at 25.6 GB (PPU: refreshed, peak 25,971) |  | 25,814 on PPU | not run | 534 MB on PPU |  | 376.8 MB on PPU | 540.6 MB (file, PPU) |
| v99i | v99g plus the Sales staging buffer | failed at 25.6 GB (PPU: refreshed, peak 23,893) |  | 23,700 on PPU | not run | 534 MB on PPU |  | 376.8 MB on PPU | 540.6 MB (file, PPU) |
| v99j | v99g plus the Customer staging buffer | refreshed | 22,894 | 22,789 | not run | 533 MB |  | 376.8 MB | 540.5 MB (file) |
| v99k | v99a without any Table.Buffer | refreshed | 12,992 | 12,892 | failed | 185 MB |  | 134.7 MB |  |
| v99l | v99k without calculated columns | refreshed | 12,878 | 12,760 | failed at 3,146 | 158 MB |  | 112.6 MB |  |
| v99m | v99k with the baseline Power Query | refreshed | 627 | 272 | refreshed | 102 MB |  | 72.7 MB |  |
| v99n | v99m plus text staging | refreshed | 624 | 294 | refreshed | 92 MB |  | 66.7 MB |  |
| v99o | v99m plus sorts | refreshed | 5,337 | 5,048 | failed | 99 MB |  | 74.1 MB |  |
| v99p | v99m plus high cardinality columns | refreshed | 746 | 335 | refreshed | 175 MB |  | 122.2 MB |  |
| v99q | v99m plus the Group By table | refreshed | 3,477 | 3,243 | failed | 114 MB |  | 80.9 MB |  |

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
| `f2-v20-pq-sort-resource-governance.png` | v20 on F2: consumed 3,179 MB, limit 3,067 MB, database size before command 4 MB |
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
