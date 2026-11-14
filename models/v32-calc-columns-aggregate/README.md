# v32-calc-columns-aggregate

The baseline plus 30 calculated columns that aggregate: per customer, product, store and date, and per row of Sales.

## What changed vs baseline

| Table | Columns | Patterns |
|---|---|---|
| Customer (104,990 rows) | 8 | `SUMX ( RELATEDTABLE ( Sales ), ... )` for sales and margin, `COUNTROWS ( RELATEDTABLE ( Sales ) )`, `CALCULATE ( DISTINCTCOUNT ( ... ) )`, `MINX` and `MAXX` over the customer's sales, average order, customers in the same city (`CALCULATE` with `ALLEXCEPT`) |
| Product (2,517) | 6 | sales and quantity over `RELATEDTABLE`, distinct customers, `RANKX ( ALL ( 'Product' ), ... )`, products in the same subcategory (`COUNTROWS ( FILTER ( ALL ( 'Product' ), ... EARLIER ( ... ) ) )`), share of category (`SUMX` over `FILTER` with `EARLIER`) |
| Store (74) | 4 | sales, distinct orders, distinct customers, `RANKX` |
| Date (4,018) | 3 | sales, distinct orders, running total (`SUMX ( FILTER ( ALL ( 'Date' ), 'Date'[Date] <= EARLIER ( 'Date'[Date] ) ), ... )`) |
| Sales (2.3M) | 9 | order total (`CALCULATE` with `ALLEXCEPT` on the order number), line share of order, customer and product totals via `RELATED`, line share of customer and product, store rank via `RELATED`, `RANKX ( ALL ( Sales[Net Price] ), ... )`, days since the customer's first order |

Measures, Power Query and relationships are the same as in the baseline.

Two patterns are left out on purpose:

- More than one calculated column with a context transition (`CALCULATE`, or a measure reference) on Sales. Sales has no unique key column, so a second such column makes a circular dependency, which Power BI reports as an error. On the dimension tables the key is unique (the one side of a relationship), so several are allowed.
- `FILTER` with `EARLIER` over all of Sales on each Sales row: 2.3M times 2.3M row comparisons, hours of refresh on 1M data. The same pattern is used on Product and Date, where it is still realistic.

## Why this run

Aggregating calculated columns are a common way to add customer or product statistics to a model. They run during refresh and need the data of the whole fact table for every row of the table they are on.

## Expected effect

- Refresh: longer and a higher peak than v31, which has more columns but none that aggregate. No numbers until measured.
- Model size: smaller growth than v31, since most columns are on small dimension tables.
- Queries: unchanged, the visuals do not use the new columns.

## Runs

1. Refresh on F64 with 1M, model sizes.
2. Query workload on F64 with 1M, pages p01 to p20.
3. If the effect is large: 10M on F64, and F2.

## Results

F64, 1M, 2026-11-11 and 2026-11-12. Refresh run `20261112T110213Z-v32-ae1e`, query run `20261112T110702Z-v32-9843` (all 792 queries succeeded). Query numbers are medians over 5 repeats, cold cache, all visuals of the page at once. The v00 column is the range over its six refreshes and three query runs on F64 with 1M.

| | v00-baseline | v32-calc-columns-aggregate |
|---|---|---|
| Refresh peak | 543 to 698 MB | 631 MB |
| Power Query peak | 270 to 599 MB | 595 MB |
| Duration | 0.6 to 0.8 min | 1.1 min |
| CPU | 55 to 71 s | 121 s |
| Model, backup size in the refresh log | 72.7 MB | 220.7 MB |
| Model in memory right after the refresh | 92.7 MB | 367.9 MB |
| p05 cold, slowest visual | 125 to 141 ms | 297 ms |
| p05 cold, CPU | 313 to 328 ms | 517 ms |
| p20 cold, slowest visual | 672 to 719 ms | 1,486 ms |
| p20 cold, CPU | 1,890 to 2,172 ms | 3,613 ms |
| p20 cold, peak per query | 58 MB | 55 MB |

- Model: about 3 times the baseline (220.7 MB backup size, 367.9 MB in memory), the same as v31 with two fewer columns.
- Refresh: the peak (631 MB) is inside the baseline range, and the Power Query peak (595 MB) is at the top of it. CPU doubles (121 s) and the refresh takes 1.1 min. The aggregating columns cost time, not peak memory. The slowest single column is `Sales[Line Share Of Customer]` at 3.8 s.
- Queries: inconclusive. Two runs (11:07 and 12:33 UTC) were about twice as slow as the baseline on p05 and p20 (p20 slowest visual 1,486 and 1,516 ms, CPU 3,613 and 3,739 ms). A control run of v00-baseline at 14:24 UTC on the same day was just as slow (1,424 ms, CPU 3,673 ms), so the capacity was slower that day, not the model. Query times from different times of day cannot be compared here. The interleaved runs below show no difference from the baseline. The peak per query (55 MB) is the same as the baseline.

### Interleaved query runs, F64, 1M, 2026-11-12

v00-baseline, v32 and v34 back to back, twice, between 14:42 and 15:48 UTC (round 2 started 15:28, after a network drop): pages p05 and p20, cold cache, all visuals of the page at once, medians over 5 repeats. All 750 queries succeeded.

| Round | Model | p05 slowest visual | p05 CPU | p20 slowest visual | p20 CPU | p20 peak per query |
|---|---|---|---|---|---|---|
| 1 | v00-baseline | 266 ms | 515 ms | 1,516 ms | 3,736 ms | 55 MB |
| 1 | v32-calc-columns-aggregate | 282 ms | 547 ms | 1,454 ms | 3,643 ms | 55 MB |
| 1 | v34-auto-date-time-no-date-table | 281 ms | 485 ms | 1,470 ms | 3,627 ms | 55 MB |
| 2 | v00-baseline | 281 ms | 516 ms | 1,563 ms | 3,535 ms | 55 MB |
| 2 | v32-calc-columns-aggregate | 281 ms | 516 ms | 1,580 ms | 3,831 ms | 55 MB |
| 2 | v34-auto-date-time-no-date-table | 282 ms | 530 ms | 1,407 ms | 3,299 ms | 55 MB |

Runs: v00 `20261112T144321Z-v00-7624`, `20261112T152844Z-v00-eda9`; v32 `20261112T145014Z-v32-e5da`, `20261112T153443Z-v32-c8ba`; v34 `20261112T145703Z-v34-b6c0`, `20261112T154139Z-v34-c119`.

Run back to back, the three models give the same results: the slowest visual on p20 is 1,407 to 1,580 ms, CPU 3,299 to 3,831 ms and the peak per query 55 MB for all three, and the spread within one model across the two rounds is as large as the spread between models. Neither the 30 aggregating calculated columns nor Auto date/time without a marked date table changes the cost of the report's queries.

### Note added 2026-11-14

Query time on F64 has a fast and a slow state per model, about two times apart, that last for hours and change by themselves (`docs/lab-findings-queries.md`, finding 7). Memory per query does not change with it. The interleaved runs above found v00, v32 and v34 all in the slow state, which is why they compare fairly. v32 was not run in the fast state.
