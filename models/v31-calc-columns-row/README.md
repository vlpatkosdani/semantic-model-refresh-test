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

Not run yet.
