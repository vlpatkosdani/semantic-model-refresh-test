# v36-calc-summary-month-grain

v23-dax-calc-tables with the `Sales Summary` calculated table grouped by month instead of year, on the 10M data.

## What changed vs v23-dax-calc-tables

| Knob | v23 | This run |
|---|---|---|
| Grain in `tables/Sales Summary.tmdl` | `'Date'[Year]` | `'Date'[Year Month]` |
| `DataTag` in `expressions.tmdl` | `data-1m-v1` | `data-10m-v1` |

`Sales Summary` is a `SUMMARIZECOLUMNS` over customer, period and category with three measures (`Sales Amount`, `Total Quantity`, `# Orders`, the last a `DISTINCTCOUNT`). On 10M it has 16.5M rows by year; by month it has more. Everything else is the same as v23.

## Why this run

v35 (four copies of `Sales Copy`) had the same refresh peak as v23 on 10M, about 13 GB: the calculated tables do not add up in the peak, the single most expensive one sets it. `Sales Summary` is the most likely one. This run makes that table heavier, to see whether the peak follows it and whether it goes past the 25.6 GB of F64. If it fails on F64, it is run on Premium Per User (100 GB per model), to show that PPU refreshes a model that F64 cannot, on the model side and not in Power Query.

## Expected effect

- If `Sales Summary` sets the peak: a higher peak than v23's 13 GB, possibly above 25.6 GB, and then a failure on F64.
- If the peak stays at 13 GB: `Sales Summary` is not the step that sets it either.

## Runs

1. Refresh on F64 with 10M, through Git (harness).
2. Only if F64 fails on the memory limit: refresh on PPU with 10M, measured with the XMLA trace. Open `v36-calc-summary-month-grain.pbip` in Desktop, do not refresh, publish to the PPU workspace, and let the harness refresh it.

## Results

Not run yet.
