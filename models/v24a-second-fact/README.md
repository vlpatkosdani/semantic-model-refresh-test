# v24a-second-fact

The baseline plus a second fact table, Orders, with one row per order. All relationships filter in one direction, as in the baseline. This is the control for v24b-second-fact-bidirectional.

## What changed vs baseline

- New table `Orders` from `orders.parquet` in the same data release: `Order Number`, `Order Date`, `Delivery Date`, `CustomerKey`, `StoreKey`, `Currency Code`. On 1M data it has 980,666 rows, one per order in Sales.
- New measure `Orders[Order Count] = COUNTROWS ( Orders )`.
- New relationships, many to one, single direction: `Orders[CustomerKey]` to `Customer`, `Orders[StoreKey]` to `Store`, `Orders[Order Date]` to `Date`.

Orders and Sales share Customer, Store and Date, so the model has two facts on the same dimensions, a common shape in real models (for example sales and budget, or orders and returns). There is no relationship between Orders and Sales.

## Why this run

It isolates the cost of the second fact table itself, so v24b can show what the bidirectional relationship adds on top. It also shows what a second fact does to refresh: one more table to load, compress and relate.

## Expected effect

- Refresh: a higher peak and a larger model than the baseline, from one more table of about a million rows. No numbers until measured.
- Pages p01 to p20 and pf: same as baseline, the visuals do not use Orders.
- Page po (Orders filtered): the Category slicer does not filter the Orders visuals, because Product has no path to Orders. The Country slicer does, through Customer.

## Runs

1. Refresh on F64 with 1M.
2. Query workload on F64 with 1M, pages p01 to p20, pf and po.

## Results

Not run yet.
