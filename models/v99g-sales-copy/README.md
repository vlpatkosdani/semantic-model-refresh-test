# v99g-sales-copy

Diagnostic run G for v99-kitchen-sink. It is v99f plus `Sales Copy` with one copy.

## What changed vs v99f

- `Sales Copy`: ADDCOLUMNS over all of Sales, including its eight calculated columns, plus six RELATED columns. Knob `CopyCount` is 1, so 2.35M rows. v99 used 2.

The DAX is otherwise unchanged from v99. `Sales Copy` has no columns in TMDL, so refresh once in Desktop before publishing so the engine creates them. With auto date/time on, Desktop may also add local date tables for its three date columns.

After this run, the only difference between this model and v99 is `CopyCount` (1 here, 2 in v99) and the `Table.Buffer` steps in `stg Sales` and `stg Customer`.

## Results so far

| Run | What it adds | F64 |
|---|---|---|
| v99 | everything | failed, cancelled at 25,599 MB |
| v99a | v99 without calculated tables, flat table, staging buffers, unused query | refreshed |
| v99d first version | v99a plus `Sales Flat`, staging buffers, unused query | failed, cancelled at 25,598 MB |
| v99d | v99a plus unused query | refreshed (3 times) |
| v99e | v99d plus `Sales Flat` loaded | refreshed |
| v99f | v99e plus `Sales Summary`, `Product Date Grid`, `Calendar Auto` | refreshed |
| v99g | v99f plus `Sales Copy`, one copy | refreshed |

## How to read the result

- If G fails on F64, one copy of Sales as a calculated table needs more than the headroom v99f left.
- If G refreshes, the next step is v99g plus the staging buffers. If that fails, the buffers were behind both 25 GB failures, and `Sales Copy` was not.
