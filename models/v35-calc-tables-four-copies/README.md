# v35-calc-tables-four-copies

v23-dax-calc-tables with four copies of the Sales rows in `Sales Copy` instead of one, on the 10M data. A model whose refresh needs more than the 25.6 GB of F64 in the model itself, not in Power Query.

## What changed vs v23-dax-calc-tables

| Knob | v23 | This run |
|---|---|---|
| `CopyCount` in `tables/Sales Copy.tmdl` | 1 | 4 |
| `DataTag` in `expressions.tmdl` | `data-1m-v1` | `data-10m-v1` |

With the 10M data, `Sales Copy` has 4 x 23.7M = 94.9M rows. Everything else is the same as v23, which is the baseline plus four calculated tables.

## Why this run

The tests so far showed that Premium Per User (100 GB per model) refreshes models that fail on F64, but only by a small margin: v99 failed on F64 at 25,599 MB and peaked at 26,115 MB on PPU, almost all of it Power Query. v19 showed that the Power Query limit does not grow on PPU at all. This run tests the model side: calculated tables need no Power Query, and are built in memory in full before they are compressed.

v23 on 10M peaks at about 13 GB in four runs, of which 1.2 to 1.9 GB is Power Query. Most of the rest is the calculated tables, and `Sales Copy` is the largest of them.

## Expected effect

- F64: fails on the model memory limit, if each copy adds several GB as the v23 runs suggest. No number until measured.
- PPU: refreshes, with a peak above 25.6 GB.
- If F64 refreshes, four copies were not enough, and the result says how much one copy costs.

## Runs

1. Refresh on F64 with 10M, through Git (harness).
2. Refresh on PPU with 10M, measured with the XMLA trace. The PPU workspace is not connected to Git: open `v35-calc-tables-four-copies.pbip` in Desktop, do not refresh, and publish to the PPU workspace. The harness then refreshes it there with the committed parameters.

## Results

F64, 10M, 2026-11-13, harness run `20261113T122445Z-v35-6ea1`:

| Model | Result | Peak | Power Query | Duration | CPU | Model in memory after |
|---|---|---|---|---|---|---|
| v23 (1 copy), 3 harness runs on 10M | refreshed | 13,062 to 13,139 MB | 1,707 to 1,870 MB | 7.5 to 8.2 min | 809 to 878 s | 1,379 to 1,387 MB |
| v35 (4 copies) | refreshed | 13,063 MB | 1,601 MB | 17 min | 1,827 s | 2,803 MB |

Four copies did not raise the peak at all. The model doubled (2,803 MB against 1,379 MB), `Sales Copy` took 448 s instead of 99 s for its 94.9M rows, but the peak stayed at 13,063 MB. So the calculated tables do not add up in the peak: they are built one after the other, and a table's working memory is released before the next one starts. The peak is set by the single most expensive step.

That step is most likely `Sales Summary`, a `SUMMARIZECOLUMNS` over customer, year and category with three measures, one of them a `DISTINCTCOUNT`, 16.5M rows on 10M. The refresh log gives one peak for the whole refresh, not one per table, so this is not proven.

The model did not exceed the F64 limit, so it was not run on PPU.
