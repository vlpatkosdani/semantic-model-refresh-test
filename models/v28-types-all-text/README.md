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

F64, 1M, 2026-11-11 and 2026-11-12. Refresh run `20261111T204204Z-v28-3f3b`, query run `20261111T204652Z-v28-3d3d` (all 792 queries succeeded). Query numbers are medians over 5 repeats, cold cache, all visuals of the page at once. The v00 column is the range over its six refreshes and three query runs on F64 with 1M.

| | v00-baseline | v28-types-all-text |
|---|---|---|
| Refresh peak | 543 to 698 MB | 777 MB |
| Power Query peak | 270 to 599 MB | 629 MB |
| Duration | 0.6 to 0.8 min | 0.9 min |
| CPU | 55 to 71 s | 108 s |
| Model, backup size in the refresh log | 72.7 MB | 69.1 MB |
| Model in memory right after the refresh | 92.7 MB | 171.5 MB |
| p05 cold, slowest visual | 125 to 141 ms | 250 ms |
| p05 cold, CPU | 313 to 328 ms | 469 ms |
| p20 cold, slowest visual | 672 to 719 ms | 1,047 ms |
| p20 cold, CPU | 1,890 to 2,172 ms | 3,096 ms |
| p20 cold, peak per query | 58 MB | 28 MB |

- Model: almost twice the baseline in memory (171.5 MB against 92.7 MB). The backup size in the refresh log is slightly smaller (69.1 MB against 72.7 MB), so the two measures disagree in direction. The size in memory is what the capacity holds.
- Refresh: CPU about 1.5 to 2 times the baseline, peak 777 MB, above the baseline range by 79 MB. One run.
- Queries: clearly slower. On p20 the slowest visual takes 1,047 ms against 672 to 719 ms, CPU is about 1.5 times, and p05 is about twice as slow. The peak per query is half the baseline (28 MB against 58 MB); v29 shows the same, so it comes from the text keys.
