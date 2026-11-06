# v22-dax-calc-columns

The baseline plus eight calculated columns on Sales. Power Query is the same as in the baseline.

## What changed vs baseline

New calculated columns on `Sales`, the same as in v99k:

| Column | DAX pattern |
|---|---|
| `Customer Name`, `Customer Country`, `Product Name`, `Product Category`, `Store Name` | `RELATED` text from a dimension |
| `Product Price Rank` | `RANKX` over all product prices |
| `Sales Line Label` | text concatenation of category, brand, country and month, so almost every row is distinct |
| `Customer Lifetime Sales` | `CALCULATE ( [Sales Amount], ALLEXCEPT ( Sales, Sales[CustomerKey] ) )`, a context transition per row |

Nothing else changes: no auto date/time, no bidirectional relationships.

## Why this run

In the v99 runs, Power Query set peaks of 13 to 23 GB and the calculated columns fit underneath. Removing them from v99k (giving v99l) changed the peak by 114 MB. That shows they did not raise a Power Query-heavy peak, not what they cost on their own. Here Power Query is light (baseline peak 785 MB on F64), so anything above that comes from the model side.

## Knobs

| Parameter | Default | Effect |
|---|---|---|
| `DataTag` | `data-1m-v1` | `data-10m-v1` makes Sales 23.5M rows. Calculated columns are computed per row, so their cost should grow with it. |

## Expected effect

- Model size: larger than baseline, mostly from `Sales Line Label` and the text columns, which compress poorly.
- Peak refresh memory: some hundreds of MB above baseline on 1M. Unknown on 10M, which is the point of the 10M run.
- Duration: higher than baseline. `Customer Lifetime Sales` and `Product Price Rank` are evaluated row by row.

## Runs

1. F64 with 1M, then F64 with 10M. Compare `PeakMemMB` and `MEnginePeakMB` with v00 on the same data. The difference between them is the model side.
2. F2 with 1M.
3. Refresh the same model twice in a row, on F64 and F2. The second refresh starts with the data already in memory ("database size before command execution" in the error message, if it fails).

## Results

| Capacity | Data | Run | Result | Peak MB | Power Query MB | Duration |
|---|---|---|---|---|---|---|
| F64 | 1M | first | not run yet | | | |
| F64 | 10M | first | not run yet | | | |
| F2 | 1M | first | not run yet | | | |
