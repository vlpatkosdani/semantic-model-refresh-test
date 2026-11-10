# v26-bad-dax

The baseline with five of its six measures rewritten in common bad DAX patterns. The tables, relationships and Power Query are the same as in the baseline, and every measure returns the same numbers.

## What changed vs baseline

| Measure | Baseline | v26 | Pattern |
|---|---|---|---|
| `Sales Amount` | `SUMX ( Sales, Sales[Quantity] * Sales[Net Price] )` | `SUMX ( FILTER ( Sales, Sales[Quantity] > 0 ), Sales[Quantity] * Sales[Net Price] )` | `FILTER` over the whole fact table instead of a column filter |
| `Total Cost` | `SUMX ( Sales, Sales[Quantity] * Sales[Unit Cost] )` | `SUMX ( Sales, Sales[Quantity] * IF ( Sales[Unit Cost] > 0, Sales[Unit Cost], 0 ) )` | `IF` inside an iterator, which the storage engine has to call back to the formula engine for |
| `Margin` | `[Sales Amount] - [Total Cost]` | `SUMX ( Sales, [Sales Amount] - [Total Cost] )` | measures inside an iterator: a context transition for every Sales row |
| `Margin %` | `DIVIDE ( [Margin], [Sales Amount] )` | `IFERROR ( [Margin] / [Sales Amount], BLANK () )` | `IFERROR` instead of `DIVIDE`, on top of the expensive `Margin` |
| `# Orders` | `DISTINCTCOUNT ( Sales[Order Number] )` | `COUNTROWS ( FILTER ( VALUES ( Sales[Order Number] ), CALCULATE ( COUNTROWS ( Sales ) ) > 0 ) )` | a context transition for every order |
| `Total Quantity` | `SUM ( Sales[Quantity] )` | unchanged | control |

Why the results are the same: on the 1M data every Sales row has a quantity and a unit cost above 0, and order number plus line number is unique (checked on 2026-11-10: 2,349,091 rows, 980,666 orders). The `FILTER` and `IF` conditions are therefore always true, and a context transition on a Sales row selects exactly that row.

## Why this run

Refresh memory is not affected: measures are not computed during refresh. The question is query time. Measures are where most report authors write DAX, and these patterns appear in real models. The workload pages are the same as for the baseline, so the difference per page is the cost of the measures.

## Expected effect

- Model size and refresh peak: same as baseline.
- Query time and CPU: much higher on every visual that uses `Margin`, `Margin %` or `# Orders`, likely seconds instead of milliseconds. `Total Quantity` visuals (v09, v13, v17) should stay at baseline level. No numbers until measured.
- Query memory: higher where the formula engine materializes the rows it iterates.

## Runs

1. Refresh on F64 with 1M (the harness deploys and refreshes it).
2. Check that the measures return the same totals as the baseline.
3. Query workload on F64 with 1M. Compare with v00-baseline (`analysis/query-perf.kql`, query 4).

## Results

| Capacity | Data | Run | Result | Peak MB | Power Query MB | Duration | Model size |
|---|---|---|---|---|---|---|---|
| F64 | 1M | harness, 2026-11-10 | refreshed | 715 | 689 | 0.6 min | 73 MB |

Refresh is the same as the baseline, as expected: the peak is inside the baseline's range on F64 (551 to 785 MB over four runs) and the model is the same size.

Same results: all six measures by `Date[Year]` (11 years) returned identical values on v00-baseline and v26 on 2026-11-10.

### Query workload, F64, 1M

Harness run `20261110T112545Z-v26-a9fc`, compared with v00-baseline run `20261110T103141Z-v00-5b3b`. Medians over 5 repeats. "Slowest visual" is the slowest single query on the page, "CPU" the CPU time of all queries of the page, "peak" the largest `approximatePeakMemConsumptionKB` of one query.

Cold cache, all visuals of the page at once:

| Page | Slowest visual v00 | Slowest visual v26 | CPU v00 | CPU v26 | Peak per query v00 | Peak per query v26 |
|---|---|---|---|---|---|---|
| p01 | 21 ms | 16 ms | 31 ms | 16 ms | 4 MB | 5 MB |
| p05 | 141 ms | 8,552 ms | 328 ms | 12,187 ms | 14 MB | 1,546 MB |
| p10 | 141 ms | 9,332 ms | 360 ms | 32,672 ms | 14 MB | 1,544 MB |
| p20 | 672 ms | 17,165 ms | 2,033 ms | 99,145 ms | 58 MB | 2,655 MB |

The p20 page took 17.7 s to load on v26 (median, all visuals at once) against 1.5 s on v00. With a warm cache it still took 15.3 s, against 0.7 s: the extra work is in the formula engine, and the cache keeps only storage engine results.

Per visual, cold, p20, all at once (median server time, largest peak):

| Visual | Measures | v00 | v26 | Peak v00 | Peak v26 |
|---|---|---|---|---|---|
| v01, v02, v03, v04, v06, v16 | `Sales Amount` | 15 to 31 ms | 16 to 45 ms | 2 to 6 MB | 3 to 4 MB |
| v09, v13, v17 | `Total Quantity` (v13 also `Sales Amount`) | 0 to 31 ms | 16 to 47 ms | 0 to 3 MB | 0 to 3 MB |
| v11 | `Total Cost` | 10 ms | 125 ms | 3 MB | 2 MB |
| v07 | `# Orders` | 0 ms | 1,642 ms | 0 MB | 89 MB |
| v14 | `# Orders` | 136 ms | 1,782 ms | 14 MB | 93 MB |
| v18 | `Sales Amount`, `# Orders` | 172 ms | 3,188 ms | 27 MB | 131 MB |
| v20 | `# Orders` | 672 ms | 7,800 ms | 58 MB | 509 MB |
| v10, v19 | `Margin` | 16 ms | 6,066 ms | 4 to 5 MB | 926 MB |
| v08 | `Margin %` | 16 ms | 9,410 ms | 3 MB | 1,276 MB |
| v12 | `Margin %` | 31 ms | 10,865 ms | 4 MB | 1,513 MB |
| v05 | `Sales Amount`, `Margin`, `# Orders` | 157 ms | 12,147 ms | 14 MB | 1,544 MB |
| v15 | `Sales Amount`, `Margin %` | 0 ms | 17,165 ms | 5 MB | 2,655 MB |

What this shows:

- `FILTER ( Sales, Sales[Quantity] > 0 )` in `Sales Amount` cost nothing measurable. The engine turned it into a column filter, the same as the baseline.
- The `IF` in `Total Cost` made the card about 10 times slower, but it stayed at about 0.1 s.
- `Margin` as `SUMX` over measures is the expensive one: one context transition per Sales row, up to 2.6 GB for a single query that returns 4 rows. `Margin %` inherits it.
- `# Orders` with `FILTER` over `VALUES ( Sales[Order Number] )` costs seconds and hundreds of MB, less than `Margin`.

All 792 queries succeeded. Workspace monitoring stored no `ExecutionMetrics` event for 195 of them, still missing 40 minutes after the run, so the peak column is the largest of the queries that have one. Every visual has at least one measured peak. The v00 and v27 runs had metrics for every query.
