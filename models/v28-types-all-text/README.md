# v28-types-all-text

The baseline with almost every column loaded as text. The usual result of skipping the type step in Power Query, or of a source that delivers everything as text.

## What changed vs baseline

These columns are text in the model (Power Query `type text`, TMDL `dataType: string`) instead of whole number, fixed decimal, decimal number, date or true/false:

| Table | Columns now text |
|---|---|
| Sales | Order Number, Line Number, Order Date, Delivery Date, CustomerKey, StoreKey, ProductKey, Unit Price, Currency Code, Exchange Rate |
| Customer | CustomerKey, Birthday, Age |
| Product | ProductKey, Weight, Unit Cost, Unit Price, Subcategory Code, Category Code |
| Store | StoreKey, Store Code, Square Meters, Open Date, Close Date |
| Date | Date, Year, Year Quarter Number, Year Month Number, Month Number, Day of Week Number, Working Day, Working Day Number |
| Currency Exchange | Date, Exchange |

Three columns stay numeric: `Sales[Quantity]`, `Sales[Net Price]` and `Sales[Unit Cost]`. The measures aggregate them, and `SUM` over a text column is an error, so making them text would also mean rewriting the measures. The measures are unchanged.

The relationships now join text to text, including the Date relationship. The Date table is no longer marked as a date table, because a date table needs a date key.

Two further changes keep the Date table usable, as a model author would have to:

- The number columns the month, weekday, quarter and year-month labels were sorted by are text now, which would sort "1", "10", "11", "12", "2". Four hidden whole-number columns, `Year Quarter Sort`, `Year Month Sort`, `Month Sort` and `Day of Week Sort`, are added in Power Query after the type step, and the labels sort by them. The text number columns stay in the model.
- `End of Month` was computed from `[Date]` after the type step, which fails once `[Date]` is text. It is now computed before the type step and converted to text with the other columns.

## Why this run

"Use the right data type" is one of the most common pieces of advice for reducing model size. v99n tested text only in staging queries, with the types restored before loading, and found no effect on refresh memory (but a refresh 6 times slower). This run keeps the text in the model.

## Expected effect

- Model size: larger. Text columns need a dictionary entry per distinct value and cannot use value encoding.
- Refresh: some extra memory and time for the larger dictionaries. No numbers until measured.
- Queries: relationships on text keys and visuals on text years; possibly slower.

## Runs

1. Refresh on F64 with 1M. Model size in the service right after the refresh, and the downloaded .pbix.
2. Query workload on F64 with 1M, pages p01 to p20. Compare with v00-baseline.

## Results

Not run yet.
