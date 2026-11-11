# v25-many-to-many

The baseline plus one table, `Customer Segment`, with one row per customer and year, related to Sales many-to-many on `CustomerKey` only.

## What changed vs baseline

- New table `Customer Segment` built in Power Query from `customer.parquet`: `CustomerKey`, `Year` (2016 to 2025) and `Segment`. 104,990 customers times 10 years is 1,049,900 rows. `CustomerKey` is not unique in it.
- The segments are synthetic: each customer is Bronze, Silver or Gold, and moves to the next segment every four years (2016 to 2019, 2020 to 2023, 2024 and 2025). A real model would derive them from spend; synthetic segments keep the refresh from reading Sales a second time.
- New relationship `Sales[CustomerKey]` to `'Customer Segment'[CustomerKey]`, many-to-many, single direction (Customer Segment filters Sales).

## Why this run

A segment that changes over time belongs to a customer and a year, but a relationship can use only one column. Joining on `CustomerKey` alone is the usual shortcut, and Power BI accepts it as a many-to-many relationship. Filtering on a segment then selects every Sales row of every customer who was in that segment in any year. The questions are what this costs at query time and what number the report shows.

## Expected effect

- Refresh: one more table of about a million rows, so a somewhat higher peak and a larger model than the baseline. No numbers until measured.
- Pages p01 to p20 and pf: same as baseline, they do not use the new table.
- Page pm (Segment filtered, Gold selected): slower than the same visuals without a filter, because the filter goes through a many-to-many join with about a million rows. Sales Amount for Gold is larger than the Gold sales in the years the customers were Gold. No numbers until measured.

## Runs

1. Open in Power BI Desktop and capture the Performance Analyzer queries of page pm.
2. Refresh on F64 with 1M.
3. Query workload on F64 with 1M, pages p01 to p20, pf and pm. Compare with v00-baseline.
4. Check with DAX what Gold returns through the relationship against the year-matched answer.

## Results

Not run yet.
