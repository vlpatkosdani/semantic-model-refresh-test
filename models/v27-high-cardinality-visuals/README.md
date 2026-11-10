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
