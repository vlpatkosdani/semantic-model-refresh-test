# v31-calc-columns-row

The baseline plus 32 calculated columns on Sales that work row by row, without aggregating.

## What changed vs baseline

| Pattern | Columns |
|---|---|
| `RELATED` text from a dimension | 12: customer name, city, country, continent, gender; product name, brand, category, subcategory, color; store name, country |
| `LOOKUPVALUE` | 5: exchange rate by order date and currency (from `Currency Exchange`), customer age, product list price, year-month of the order date, store size |
| Arithmetic | 6: line amount, line cost, line margin, discount, discount %, amount in USD |
| `IF` and `SWITCH` | 4: quantity band, margin band, is discounted, price band |
| Date functions | 4: order year, order month, weekday, delivery days (`DATEDIFF`) |
| Text concatenation | 1: order line key (`Order Number & "-" & Line Number`, unique per row) |

Measures, Power Query and relationships are the same as in the baseline. v22 tested 8 calculated columns of mixed kinds; this run tests many cheap ones.

## Why this run

Calculated columns are computed during refresh, after the data is loaded, and stored like imported columns. With many of them on the fact table, both refresh memory and model size can grow. The `RELATED` columns repeat dimension text on 2.3M rows; the order line key has a distinct value per row.

## Expected effect

- Model size: clearly larger, most from the order line key and the text columns.
- Refresh: longer and a higher peak than the baseline. No numbers until measured.
- Queries: unchanged, the visuals do not use the new columns.

## Runs

1. Refresh on F64 with 1M, model sizes.
2. Query workload on F64 with 1M, pages p01 to p20.
3. If the effect is large: 10M on F64, and F2.

## Results

F64, 1M, 2026-11-11 and 2026-11-12. Refresh run `20261112T082856Z-v31-5697`, query run `20261112T095010Z-v31-c5bc` (all 792 queries succeeded). Query numbers are medians over 5 repeats, cold cache, all visuals of the page at once. The v00 column is the range over its six refreshes and three query runs on F64 with 1M.

| | v00-baseline | v31-calc-columns-row |
|---|---|---|
| Refresh peak | 543 to 698 MB | 913 MB |
| Power Query peak | 270 to 599 MB | 334 MB |
| Duration | 0.6 to 0.8 min | 0.8 min |
| CPU | 55 to 71 s | 91 s |
| Model, backup size in the refresh log | 72.7 MB | 223 MB |
| Model in memory right after the refresh | 92.7 MB | 316.8 MB |
| p05 cold, slowest visual | 125 to 141 ms | 125 ms |
| p05 cold, CPU | 313 to 328 ms | 282 ms |
| p20 cold, slowest visual | 672 to 719 ms | 703 ms |
| p20 cold, CPU | 1,890 to 2,172 ms | 1,926 ms |
| p20 cold, peak per query | 58 MB | 58 MB |

- Model: about 3 times the baseline (223 MB backup size, 316.8 MB in memory). The largest model change of the data type and calculated column runs.
- Refresh: the peak of 913 MB is above the baseline range, while Power Query stays at the baseline level, so the extra memory comes from the model side, the calculated columns. CPU is about 1.5 times. One run.
- Queries: the same as the baseline. The visuals do not use the new columns.
