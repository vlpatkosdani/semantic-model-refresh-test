# v99i-buffer-stg-sales

Diagnostic run I for v99-kitchen-sink. It is v99g plus `Table.Buffer` at the end of `stg Sales` only.

## Why this run

v99h (v99g plus `Table.Buffer` in both `stg Sales` and `stg Customer`) failed on F64, while v99g refreshed. Runs I and J split the two buffers to find which one causes it.

`stg Sales` (2.35M rows, every column text) is referenced by `Sales`, `Sales Flat` and `Customer Stats`. If each of them evaluates its own buffered copy, that is three full copies of the fact table held as text at the same time.

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
| v99i | v99g plus `Table.Buffer` in `stg Sales` only | failed, cancelled at 25,604 MB |
| v99j | v99g plus `Table.Buffer` in `stg Customer` only | refreshed |

## Premium Per User (100 GB per model)

Refreshed on 2026-11-11, 1M data, measured with an XMLA trace (harness run `20261111T090350Z-v99i-1beb`): peak 23,893 MB, Power Query 23,700 MB, 20 min, 38,422,496 rows, model 534 MB. For comparison, v99g (the same model without the staging buffers) peaked at 23,025 MB on F64. Premium Per User runs on shared hardware, so this is recorded as its own capacity, PPU. The peak is below F64's 25.6 GB limit, yet this model was cancelled on F64 at 25,604 MB. With one run on each, the lab cannot tell whether the peak differs between the two platforms or varies between runs by more than the 1.7 GB of headroom.

## How to read the result

- If I fails, buffering the shared fact staging query is enough on its own. The cost scales with the size of the fact table and the number of queries that reference it.
- If I and J both refresh, only the combination fails.
- `approximatePeakMemConsumptionKB` and `mEnginePeakMemoryKB` from the ExecutionMetrics event show whether the memory sits in the semantic model engine or in the Power Query engine.
