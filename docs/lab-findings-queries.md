# Query workload lab: findings

The second half of the lab. `docs/lab-findings.md` covers refresh memory; this file covers what the same models cost when a report queries them: time, CPU and memory per query, and what fails on a small capacity.

## The question

Which model design choices make report queries slower or heavier, and when does a report stop working on a small capacity even though the model refreshes?

## Setup

- Models: the same Contoso star schema variants as the refresh lab, on 1M data (2.35M sales rows) unless noted, and v00 on 10M (23.7M sales rows).
- Workload: one spec (`reports/spec.yaml`, see `reports/README.md`) defines a pool of 20 visuals and pages that show the first 1, 5, 10 and 20 of them (p01, p05, p10, p20). Some variants add a page of their own: pf (a filtered page, 8 visuals), po (the Orders table of v24a and v24b), pm (the segment table of v25), p27 (high-cardinality visuals of v27). The DAX of each visual is the DAX Power BI Desktop sends, checked against Performance Analyzer captures (`reports/validation/`).
- Modes: cold (cache cleared before each render) and warm; visuals sent one by one or all at once, as a report page does. 5 repeats, medians reported.
- Measurement: the harness sends each query through the executeQueries REST API and reads `QueryEnd` and `ExecutionMetrics` from workspace monitoring (`SemanticModelLogs`) on F64. F2 has no monitoring; there the `xmla` task sends chosen queries through XMLA under a trace (`docs/harness.md`).
- Numbers used below: "slowest visual" is the slowest single query of a page render (what the user waits for when all visuals load at once), "CPU" is the CPU time of all queries of the page, "peak per query" is the largest `approximatePeakMemConsumptionKB` of one query, in MB of 1,048,576 bytes.

Unless noted, results are for p20, cold cache, all visuals at once, on F64 with 1M. The baseline there: slowest visual 672 to 719 ms, CPU 1,890 to 2,172 ms, peak per query 58 MB (three runs on 2026-11-10).

## Main findings

### 1. On F2 a single query fails at 1 GB

F2 limits the memory of one query to 1,024 MB, a third of what a refresh may use there. A query over the limit fails with:

> Resource Governance: This query uses more memory than the configured limit. [...] More details: consumed memory 1024 MB, memory limit 1024 MB.

v26-bad-dax refreshes on F2 without a problem, and four of its visuals fail on F2 with this error. Each of them needed more than 1,024 MB per query on F64 (1,276 to 2,655 MB); every visual below that succeeded on F2. As with refresh memory, the peak per query measured on a large capacity predicts the result on a small one.

v00 on 10M has no visual over the limit, but comes close. Its heaviest query, the matrix v20 (Orders by category and continent, a distinct count), needs about 860 MB on both F64 and F2, 84 % of the limit; it ran on F2 in 19 to 25 s. A little more data or a few more columns in that matrix would make the report fail on F2 while the model still refreshes.

### 2. Bad DAX is the largest query cost in the lab

v26-bad-dax rewrites five of the six measures in common bad patterns, returning the same numbers. Refresh is unchanged. Queries:

| Page | Slowest visual v00 | Slowest visual v26 | CPU v00 | CPU v26 | Peak per query v00 | Peak per query v26 |
|---|---|---|---|---|---|---|
| p05 | 141 ms | 8,552 ms | 328 ms | 12,187 ms | 14 MB | 1,546 MB |
| p20 | 672 ms | 17,165 ms | 2,033 ms | 99,145 ms | 58 MB | 2,655 MB |

- `Margin` as `SUMX` over two measures is the expensive pattern: a context transition per Sales row, up to 2.6 GB for a query that returns 4 rows. `Margin %` inherits it.
- `# Orders` with `FILTER` over `VALUES ( Sales[Order Number] )` costs seconds and hundreds of MB.
- `FILTER ( Sales, Sales[Quantity] > 0 )` in `Sales Amount` costs nothing measurable: the engine turns it into a column filter.
- A warm cache does not help: p20 still took 15.3 s warm against 0.7 s for the baseline. The extra work is in the formula engine, and the cache keeps only storage engine results.

### 3. Ten times the data, about 26 times the wait and 15 times the memory

v00 on 10M against 1M (F64, 2026-11-12):

| Page | Slowest visual 1M | Slowest visual 10M | CPU 1M | CPU 10M | Peak per query 1M | Peak per query 10M |
|---|---|---|---|---|---|---|
| p05 | 125 to 141 ms | 3,737 ms | 313 to 328 ms | 18,125 ms | 14 MB | 415 MB |
| p20 | 672 to 719 ms | 18,545 ms | 1,890 to 2,172 ms | 102,611 ms | 58 MB | 861 MB |

The heavy queries are the ones with a distinct count over many rows: the matrix v20 (861 MB) and the tables v18 and v05 (413 MB each), then a bar chart of orders by gender (108 MB). Every other visual stays at 25 MB or less on 10M.

### 4. High-cardinality visuals need several times the memory

v27 adds a page of visuals grouped by columns with many distinct values (orders, order lines, customers). The heaviest, a table of order lines, needs 231 MB per query, 4 times the heaviest baseline visual, and takes 1.3 s. A warm cache still leaves up to 88 MB per query. The model is unchanged; the cost is in the report.

### 5. Relationships: little time, wrong numbers

- A bidirectional relationship on a single star (v24) costs nothing measurable beyond a slicer that now goes through Sales.
- With a second fact table (v24a, v24b), turning Sales to Customer bidirectional makes a Category slicer reach Orders through Customer. The Orders page got slower (slowest visual 16 to 78 ms on 1M), but the bigger effect is the numbers: "Computers" gives 966,183 orders, the orders of customers who ever bought a computer, while 422,638 orders contain a computer. No error, no warning.
- A many-to-many relationship to a customer segment table by year (v25) makes every segment show the total of all sales, because every customer was in every segment in some year. The segment page takes 609 ms cold for its slowest visual, and the join with the 1M row segment table is not removed by a warm cache.

### 6. What costs refresh memory or model size does not cost query time

Calculated columns and tables that the visuals do not use, Auto date/time, and a different numeric type left the report queries unchanged:

| Model | Change | Model in memory | p20 slowest visual | p20 CPU | Peak per query |
|---|---|---|---|---|---|
| v00-baseline | | 92.7 MB | 672 to 719 ms | 1,890 to 2,172 ms | 58 MB |
| v23 | 4 calculated tables | | 672 ms | 2,001 ms | 58 MB |
| v30 | decimal number instead of fixed decimal | 92.9 MB | 657 ms | 1,955 ms | 58 MB |
| v31 | 32 row-level calculated columns | 316.8 MB | 703 ms | 1,926 ms | 58 MB |
| v32 | 30 aggregating calculated columns | 367.9 MB | same as v00, run alternating (see 7) | | 55 MB |
| v34 | Auto date/time, Date table not marked | 96.9 MB | same as v00, run alternating (see 7) | | 55 MB |

A model three to four times larger in memory answered the same queries in the same time. Model size matters for refresh memory and for what fits on a capacity at rest, not for queries that do not touch the extra columns.

Text keys are the exception in the other direction: with the key columns as text (v28, v29) the largest query needed 28 MB instead of 58 MB, in every run. Whether text keys also change query time is not settled (see the v28 caveat below).

### 7. Query time on the capacity drifts; memory does not

On the afternoon of 2026-11-12 the F64 capacity ran the unchanged baseline about twice as slowly as on 2026-11-10 (p20 slowest visual 1,424 to 1,563 ms, CPU 3,535 to 3,736 ms). Runs of v32 and v34 made that afternoon looked twice as slow as the baseline until a baseline run next to them showed the same. The peak per query did not change.

Run back to back, alternating, the three models gave the same results:

| Round | Model | p05 slowest visual | p20 slowest visual | p20 CPU | p20 peak per query |
|---|---|---|---|---|---|
| 1 | v00-baseline | 266 ms | 1,516 ms | 3,736 ms | 55 MB |
| 1 | v32 | 282 ms | 1,454 ms | 3,643 ms | 55 MB |
| 1 | v34 | 281 ms | 1,470 ms | 3,627 ms | 55 MB |
| 2 | v00-baseline | 281 ms | 1,563 ms | 3,535 ms | 55 MB |
| 2 | v32 | 281 ms | 1,580 ms | 3,831 ms | 55 MB |
| 2 | v34 | 282 ms | 1,407 ms | 3,299 ms | 55 MB |

So query times are only comparable between runs made close together, with a baseline run between them. Memory per query can be compared across days.

## Method notes

- The executeQueries REST API returns one result set. A matrix with column headers returns two, and the API reports `DaxResultsetCountNotSupported` even though the engine finished the query. On F64 the harness checks the server log and counts such a query as a success; on F2 it cannot, so the matrices v01 and v20 show as failed there. The `xmla` task gets around this.
- On F64 the XMLA trace and workspace monitoring gave the same peak for the same query (v00 10M, v20: 860 and 861 MB).
- Workspace monitoring does not always store every event: for v26, 195 of 792 queries had no `ExecutionMetrics` event 40 minutes after the run, and for v24b none of the p10 queries sent all at once. The peak columns use the queries that have one.
- On F2, for v20's second and third runs, the client waited 60 to 65 s while the engine reported 20 to 25 s. Something on F2 held those queries for about 40 s outside the engine's own time; the trace does not show what.

## Caveats

- Most models had one query run. Only v00, v32 and v34 were run alternating. Three models were slower than the baseline's range in a single run each, and are not confirmed: v22 (p20 1,047 ms; its run on 2026-11-10 at 13:02 falls between two baseline runs that day at 672 and 719 ms, so this one is more likely real), v28 (1,047 ms, on 2026-11-11 with no baseline run near it) and v33 (798 ms).
- 1M rows is small. Differences that are a few ms on 1M can be seconds on 10M, as finding 3 shows for the baseline itself. Only v00 was run on 10M.
- The data is synthetic (Contoso). Real data with more distinct values, or more skew, changes the size of each effect.
- F64 is a trial capacity. Query times on other capacities, and on the same capacity at another time (finding 7), differ; memory per query should not.

## All query runs

F64, 1M, cold cache, all visuals at once, medians over 5 repeats, unless noted. Run IDs are in `results/query-summary.csv`, per query in `results/query-runs.csv`, XMLA runs in `results/query-xmla.csv`.

| Model | Date | p05 slowest | p20 slowest | p20 CPU | p20 peak per query | Note |
|---|---|---|---|---|---|---|
| v00-baseline | 2026-11-10, 3 runs | 125 to 141 ms | 672 to 719 ms | 1,890 to 2,172 ms | 58 MB | |
| v00-baseline | 2026-11-12, 3 runs | 266 to 281 ms | 1,424 to 1,563 ms | 3,535 to 3,736 ms | 55 MB | capacity slower that afternoon |
| v00-baseline, 10M | 2026-11-12 | 3,737 ms | 18,545 ms | 102,611 ms | 861 MB | |
| v00-baseline, 10M, F2 (xmla, 3 visuals, one at a time) | 2026-11-13 | | v20 19.1 to 24.8 s | v20 72.9 to 74.8 s | v20 860 MB | fits the 1,024 MB limit |
| v22-dax-calc-columns | 2026-11-10 | 141 ms | 1,047 ms | 2,625 ms | 58 MB | one run, between two normal v00 runs |
| v23-dax-calc-tables | 2026-11-10 | 125 ms | 672 ms | 2,001 ms | 58 MB | |
| v24-bidirectional | 2026-11-10 | 125 ms | 688 ms | 1,986 ms | 55 MB | |
| v24a-second-fact | 2026-11-10 | 141 ms | 719 ms | 2,017 ms | 55 MB | po 16 ms |
| v24b-second-fact-bidirectional | 2026-11-10 | 125 ms | 688 ms | 1,954 ms | 58 MB | po 78 ms, different numbers |
| v25-many-to-many | 2026-11-11 | 188 ms | 877 ms | 2,267 ms | 55 MB | pm 609 ms, wrong totals |
| v26-bad-dax | 2026-11-10 | 8,552 ms | 17,165 ms | 99,145 ms | 2,655 MB | 4 visuals fail on F2 |
| v27-high-cardinality-visuals | 2026-11-10 | 141 ms | 766 ms | 2,079 ms | 55 MB | p27 1,345 ms, 231 MB |
| v28-types-all-text | 2026-11-11 | 250 ms | 1,047 ms | 3,096 ms | 28 MB | one run, time not confirmed |
| v29-keys-as-text | 2026-11-12 | 141 ms | 594 ms | 1,737 ms | 28 MB | |
| v30-double-instead-of-fixed | 2026-11-12 | 141 ms | 657 ms | 1,955 ms | 58 MB | |
| v31-calc-columns-row | 2026-11-12 | 125 ms | 703 ms | 1,926 ms | 58 MB | |
| v32-calc-columns-aggregate | 2026-11-12, 4 runs | 281 to 297 ms | 1,454 to 1,580 ms | 3,613 to 3,831 ms | 55 MB | same as v00 alongside |
| v33-auto-date-time | 2026-11-12 | 172 ms | 798 ms | 2,125 ms | 55 MB | one run |
| v34-auto-date-time-no-date-table | 2026-11-12, 3 runs | 281 to 282 ms | 1,407 to 1,486 ms | 3,299 to 3,627 ms | 55 MB | same as v00 alongside |

Each model's README has the per-visual numbers and the warm cache and one-by-one modes.
