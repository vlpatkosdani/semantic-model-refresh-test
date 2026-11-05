# v99h-staging-buffers

Diagnostic run H for v99-kitchen-sink. It is v99g plus `Table.Buffer` at the end of `stg Sales` and `stg Customer`.

## What changed vs v99g

- `stg Sales` and `stg Customer` end with `Table.Buffer` again, as in v99. Neither query is loaded. `stg Sales` is referenced by `Sales`, `Sales Flat` and `Customer Stats`. `stg Customer` is referenced by `Customer` and `Sales Flat`.

This model is now v99 with `CopyCount = 1` instead of 2, plus the auto date/time tables Desktop created for v99a. The other differences from v99 are metadata only (default summarization, query descriptions, relationship IDs).

## Results so far (F64)

| Run | What it adds | F64 |
|---|---|---|
| v99 | everything | failed, cancelled at 25,599 MB |
| v99a | v99 without calculated tables, flat table, staging buffers, unused query | refreshed |
| v99d first version | v99a plus `Sales Flat`, staging buffers, unused query | failed, cancelled at 25,598 MB |
| v99d | v99a plus unused query | refreshed (3 times) |
| v99e | v99d plus `Sales Flat` loaded | refreshed |
| v99f | v99e plus `Sales Summary`, `Product Date Grid`, `Calendar Auto` | refreshed |
| v99g | v99f plus `Sales Copy`, one copy | refreshed |
| v99h | v99g plus staging buffers | not run yet |

## How to read the result

- If H fails on F64, the two staging buffers are what pushes v99 past 25 GB. Together with the v99d first version failure, that is two independent failures with the buffers and none without them. `mEnginePeakMemoryKB` in the ExecutionMetrics event should show whether the memory is in the Power Query engine or in the semantic model engine.
- If H refreshes, the buffers only fail when combined with something not in v99h. The remaining difference to v99 is the second Sales copy, so the next step is `CopyCount = 2`.
