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

Not run yet.
