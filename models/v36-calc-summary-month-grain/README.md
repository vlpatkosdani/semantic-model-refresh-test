# v36-calc-summary-month-grain

v23-dax-calc-tables with the `Sales Summary` calculated table grouped by month instead of year, on the 10M data.

## What changed vs v23-dax-calc-tables

| Knob | v23 | This run |
|---|---|---|
| Grain in `tables/Sales Summary.tmdl` | `'Date'[Year]` | `'Date'[Year Month]` |
| `DataTag` in `expressions.tmdl` | `data-1m-v1` | `data-10m-v1` |

`Sales Summary` is a `SUMMARIZECOLUMNS` over customer, period and category with three measures (`Sales Amount`, `Total Quantity`, `# Orders`, the last a `DISTINCTCOUNT`). On 10M it has 16.5M rows by year; by month it has more. Everything else is the same as v23.

## Why this run

v35 (four copies of `Sales Copy`) had the same refresh peak as v23 on 10M, about 13 GB: a bigger copy table does not raise the peak. `Sales Summary`, which ran at the same time as `Sales Copy`, is the most likely table to set it. This run makes that table heavier, to see whether the peak follows it and whether it goes past the 25.6 GB of F64. If it fails on F64, it is run on Premium Per User (100 GB per model), to show that PPU refreshes a model that F64 cannot, on the model side and not in Power Query.

## Expected effect

- If `Sales Summary` sets the peak: a higher peak than v23's 13 GB, possibly above 25.6 GB, and then a failure on F64.
- If the peak stays at 13 GB: `Sales Summary` is not the step that sets it either.

## Runs

1. Refresh on F64 with 10M, through Git (harness).
2. Only if F64 fails on the memory limit: refresh on PPU with 10M, measured with the XMLA trace. Open `v36-calc-summary-month-grain.pbip` in Desktop, do not refresh, publish to the PPU workspace, and let the harness refresh it.

## Results

F64, 10M, 2026-11-13, harness run `20261113T132605Z-v36-6c53`:

| Model | Result | Peak | Power Query | Duration | Rows loaded | Model in memory after |
|---|---|---|---|---|---|---|
| v23, 3 harness runs | refreshed | 13,062 to 13,139 MB | 1,707 to 1,870 MB | 7.5 to 8.2 min | 75.9M | 1,379 to 1,387 MB |
| v35, four copies of `Sales Copy` | refreshed | 13,063 MB | 1,601 MB | 17 min | 147.1M | 2,803 MB |
| v36, `Sales Summary` by month | refreshed | 14,759 MB | 1,194 MB | 7 min | 78.9M | 1,406 MB |

By month `Sales Summary` gets about 3M more rows than by year (rows loaded 78.9M against 75.9M; by year it has 16.5M), about 18 % more: most customers buy in only a few months of a year. The peak rose by 1.7 GB, 13 %. v35 added 69M rows to `Sales Copy` and the peak did not move. So the peak follows `Sales Summary`, the `SUMMARIZECOLUMNS` with three measures, not the size of the model or of the largest table.

It still fits F64 (58 % of the 25.6 GB limit), so it was not run on PPU.
