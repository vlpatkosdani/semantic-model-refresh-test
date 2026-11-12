# v33-auto-date-time

The baseline with Auto date/time switched on, saved in Power BI Desktop. The Date table is still marked as a date table.

## What changed vs baseline

- Power BI Desktop, File > Options and settings > Options > Current file > Data load > Auto date/time: on. In TMDL this is `annotation __PBI_TimeIntelligenceEnabled = 1` in `model.tmdl` (the baseline has `0`).
- With the setting on, Desktop added a hidden `DateTableTemplate_...` and one hidden calculated table `LocalDateTable_...` per eligible date column, each `Calendar ( first day of the first year, last day of the last year )` of that column, with year, quarter, month and day columns and a hierarchy, related to the column with `joinOnDateBehavior: datePartOnly`.

Desktop created local date tables for three of the seven date columns:

| Date column | Local date table | Why |
|---|---|---|
| `Customer[Birthday]` | yes | not related to the Date table |
| `Store[Open Date]` | yes | not related to the Date table |
| `Store[Close Date]` | yes | not related to the Date table |
| `Sales[Order Date]` | no | related to the marked Date table |
| `Sales[Delivery Date]` | no | related to the marked Date table (inactive relationship) |
| `Currency Exchange[Date]` | no | related to the marked Date table |
| `Date[End of Month]` | no | column of the marked Date table |

The model was copied from the baseline and saved by Desktop on 2026-11-12. The logical IDs in `.platform` were replaced afterwards, since a copy keeps the baseline's IDs and two items with the same ID break the update from Git.

Auto date/time is a different thing from a calendar table built with `CALENDARAUTO` (as `Calendar Auto` in v99f): CALENDARAUTO is one table the author adds on purpose; Auto date/time adds one hidden table per date column without being asked.

## Why this run

Auto date/time is on by default in Power BI Desktop and is a common cause of model bloat. With a marked date table that the date columns relate to, its reach is limited; v34-auto-date-time-no-date-table tests the case without one.

## Expected effect

- Model size: a little larger. The Birthday table covers 1935 to 2002 (68 years, about 24,800 days), the two store tables 2005 to 2019 and 2013 to 2019.
- Refresh: three more calculated tables; small. No numbers until measured.
- Queries: unchanged, the visuals do not use the new tables.

## Runs

1. Refresh on F64 with 1M, model sizes.
2. Query workload on F64 with 1M, pages p01 to p20.

## Results

F64, 1M, 2026-11-11 and 2026-11-12. Refresh run `20261112T112137Z-v33-27b3`, query run `20261112T112859Z-v33-0323` (all 792 queries succeeded). Query numbers are medians over 5 repeats, cold cache, all visuals of the page at once. The v00 column is the range over its six refreshes and three query runs on F64 with 1M.

| | v00-baseline | v33-auto-date-time |
|---|---|---|
| Refresh peak | 543 to 698 MB | 619 MB |
| Power Query peak | 270 to 599 MB | 423 MB |
| Duration | 0.6 to 0.8 min | 0.6 min |
| CPU | 55 to 71 s | 59 s |
| Model, backup size in the refresh log | 72.7 MB | 73.8 MB |
| Model in memory right after the refresh | 92.7 MB | 96.2 MB |
| p05 cold, slowest visual | 125 to 141 ms | 172 ms |
| p05 cold, CPU | 313 to 328 ms | 344 ms |
| p20 cold, slowest visual | 672 to 719 ms | 798 ms |
| p20 cold, CPU | 1,890 to 2,172 ms | 2,125 ms |
| p20 cold, peak per query | 58 MB | 55 MB |

- Model: 1.1 MB more in the backup size, 3.5 MB more in memory. The three local date tables are small.
- Refresh: inside the baseline range.
- Queries: p20 slowest visual 798 ms and p05 172 ms, slightly above the baseline range; CPU within or just above it. One run, not a clear effect.

With a marked date table that the fact dates relate to, Auto date/time costs almost nothing. v34 tests the model without a marked date table.
