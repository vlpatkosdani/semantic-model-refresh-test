# v27-high-cardinality-visuals

The baseline model unchanged, with an extra report page of visuals that group by columns with many distinct values. The change is in the report, not in the model.

## What changed vs baseline

The workload report has a fifth page, `p27` (High cardinality), defined in `reports/spec.yaml`:

| Visual | Type | Grouped by | Groups on 1M |
|---|---|---|---|
| h01 Orders | table | `Sales[Order Number]` | 980,666 |
| h02 Customers | table | `Customer[Name]`, `Customer[City]` | about 105,000 |
| h03 Order lines | table | `Sales[Order Number]`, `Sales[Line Number]`, `Product[Product Name]` | 2,349,091 |
| h04 Customers by year | matrix | `Customer[Name]` by `Date[Year]` | about 99,000 rows |
| h05 Sales by product | bar chart | `Product[Product Name]` | 2,517 |

Power BI shows only the first rows of a table (a window of 502), but the engine still has to group all of them to find those rows and the total.

The semantic model is a copy of the baseline, so its refresh results should match the baseline.

## Why this run

Users often ask for "all orders" or "all customers" in a table. These visuals are where single queries need the most memory, because the result is grouped over the whole fact table before it is cut to the visible rows. Per-query memory (`approximatePeakMemConsumptionKB` of the query's `ExecutionMetrics` event) is recorded for every query. This is the page to watch for it.

## Expected effect

- Pages p01 to p20: same as baseline.
- Page p27: far higher query time, CPU and memory per query than any baseline page. h03 should be the heaviest. No numbers until measured.

## Runs

1. Refresh on F64 with 1M.
2. Query workload on F64 with 1M, all pages. Compare p27 with the baseline's p20.
3. Later: p27 on F2, to see whether a single query reaches a limit there.

## Results

| Capacity | Data | Run | Result | Peak MB | Power Query MB | Duration | Model size |
|---|---|---|---|---|---|---|---|
| F64 | 1M | harness, 2026-11-10 | refreshed | 616 | 336 | 0.7 min | 73 MB |

The refresh matches the baseline (551 to 785 MB over four runs), as it should for an unchanged model.

### Query workload, F64, 1M

Harness run `20261110T121143Z-v27-ada0`, compared with v00-baseline run `20261110T103141Z-v00-5b3b`. Medians over 5 repeats. All 902 queries succeeded.

Pages p01 to p20 match the baseline. On p20, cold, all visuals at once: slowest visual 766 ms (v00: 672 ms), CPU 2,079 ms (v00: 2,033 ms), largest query 55 MB (v00: 58 MB).

Page p27:

| Mode | Visuals | Page load | Slowest visual | CPU | Peak per query |
|---|---|---|---|---|---|
| cold | all at once | 1,726 ms | 1,345 ms | 4,517 ms | 231 MB |
| cold | one by one | 4,372 ms | 1,141 ms | 3,516 ms | 245 MB |
| warm | all at once | 1,122 ms | 750 ms | 2,033 ms | 88 MB |
| warm | one by one | 3,004 ms | 735 ms | 1,938 ms | 88 MB |

Baseline p20 for comparison, cold, all at once: page load 1,457 ms, slowest visual 672 ms, CPU 2,033 ms, peak 58 MB.

Per visual, cold, all at once (median server time, largest peak):

| Visual | Server time | Peak per query |
|---|---|---|
| h01 Orders | 1,235 ms | 140 MB |
| h02 Customers | 344 ms | 51 MB |
| h03 Order lines | 1,344 ms | 231 MB |
| h04 Customers by year | 891 ms | 99 MB |
| h05 Sales by product | 31 ms | 2 MB |

h03 is the heaviest, as expected. A single high-cardinality table needs about 4 times the memory of the heaviest baseline visual (v20, 58 MB), and a warm cache does not remove it: p27 still took 1.1 s with up to 88 MB per query, against 0.7 s and 1 MB on baseline p20. For scale, the worst v26-bad-dax query needed 2,655 MB on the same data.
