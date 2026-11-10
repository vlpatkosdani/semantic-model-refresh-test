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

Not run yet.
