# v99f-calc-tables

Diagnostic run F for v99-kitchen-sink. It is v99e plus three of v99's four calculated tables. `Sales Copy` is left out on purpose.

## What changed vs v99e

- `Sales Summary`: SUMMARIZECOLUMNS by customer, year and category with three measures. Roughly 1M rows.
- `Product Date Grid`: CROSSJOIN of all 2,517 products and all 4,018 dates, 10.1M rows. Knob `FirstYear` is 2016, which keeps all of it.
- `Calendar Auto`: second date table from CALENDARAUTO, related to `Sales Flat[Order Date]` as in v99. Because that column is now on the many side of a relationship, it no longer gets a local date table.

The DAX is unchanged from v99. `Sales Summary` and `Product Date Grid` have no columns in TMDL, so refresh once in Desktop before publishing so the engine creates them.

## Results so far

| Run | What it adds | F64 |
|---|---|---|
| v99 | everything | failed, cancelled at 25,599 MB |
| v99a | v99 without calculated tables, flat table, staging buffers, unused query | refreshed |
| v99d first version | v99a plus `Sales Flat`, staging buffers, unused query | failed, cancelled at 25,598 MB |
| v99d | v99a plus unused query | refreshed (3 times) |
| v99e | v99d plus `Sales Flat` loaded | refreshed |
| v99f | v99e plus three calculated tables | refreshed |

## How to read the result

- If F fails on F64, one of these three tables, most likely the crossjoin, costs more than the headroom v99e left.
- If F refreshes, the remaining parts of v99 are `Sales Copy` and the staging buffers. The next run adds `Sales Copy` with `CopyCount = 1`.
- Peak of F minus peak of v99e is the cost of the three tables together.
