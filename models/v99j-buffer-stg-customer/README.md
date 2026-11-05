# v99j-buffer-stg-customer

Diagnostic run J for v99-kitchen-sink. It is v99g plus `Table.Buffer` at the end of `stg Customer` only.

## Why this run

v99h (v99g plus `Table.Buffer` in both `stg Sales` and `stg Customer`) failed on F64, while v99g refreshed. Runs I and J split the two buffers to find which one causes it.

`stg Customer` (105k rows, every column text) is small. It is referenced by `Customer` and by `Sales Flat`, which merges all 2.35M Sales rows against it.

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
| v99h | v99g plus `Table.Buffer` in `stg Sales` and `stg Customer` | failed, cancelled at 25,603 MB |
| v99i | v99g plus `Table.Buffer` in `stg Sales` only | not run yet |
| v99j | v99g plus `Table.Buffer` in `stg Customer` only | not run yet |

## How to read the result

- If J fails, the problem is not the size of the buffered table but how `Sales Flat` joins against it. A buffered right-hand side may change the join from a hash join to something far more expensive.
- If I and J both refresh, only the combination fails.
- `approximatePeakMemConsumptionKB` and `mEnginePeakMemoryKB` from the ExecutionMetrics event show whether the memory sits in the semantic model engine or in the Power Query engine.
