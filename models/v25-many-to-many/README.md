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

F64, 1M, harness runs on 2026-11-11 (new F64 workspace).

Refresh (run `20261111T195122Z-v25-009e`): peak 614 MB, Power Query 457 MB, 1 min, 3,611,040 rows, model 79 MB (Backup step), 98 MB in memory right after the refresh. Inside the baseline's range on F64 (543 to 785 MB).

### What Gold returns

Checked with DAX on 2026-11-11:

| Sales Amount | Value |
|---|---|
| All sales | 2,298,959,216 |
| Gold through the many-to-many relationship | 2,298,959,216 |
| Silver through the relationship | 2,298,959,216 |
| Bronze through the relationship | 2,298,959,216 |
| Gold in the years the customer was Gold (`TREATAS` on customer and year) | 769,523,321 (33.5%) |

Through the relationship every segment returns all sales. A filter on Gold selects every customer who was Gold in any year, and with these synthetic segments every customer with sales (86,908) is in all three segments at some point. The report shows the same total for each segment without any warning. The size of the error here comes from the synthetic segments, which move every customer through all three; with real segments that change less often the error is smaller, but of the same kind: sales from years when the customer was not in the segment are counted.

### Query workload

Run `20261111T195607Z-v25-f02f`, 1,100 queries, none failed. Medians over 5 repeats, all visuals at once:

| Page | Mode | Slowest visual | CPU | Peak per query |
|---|---|---|---|---|
| p20 | cold | 877 ms | 2,267 ms | 55 MB |
| pf | cold | 63 ms | 250 ms | 11 MB |
| pm (Segment filtered) | cold | 609 ms | 1,094 ms | 62 MB |
| pm | warm | 172 ms | 438 ms | 28 MB |

p20 and pf are in the range of the baseline (v00 p20 slowest visual 672 to 719 ms over two runs, pf 63 ms). On pm, the Categories table (Sales Amount and # Orders by category) is the slowest visual at 609 ms cold and 125 ms warm, and the Segment by year matrix takes 203 ms cold and 172 ms warm. The other visuals take 16 to 47 ms. Every visual on the page filters Sales through a join with the 1,049,900-row segment table, which a warm cache does not remove.
