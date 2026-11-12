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

Not run yet.
