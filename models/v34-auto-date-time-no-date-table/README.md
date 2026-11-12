# v34-auto-date-time-no-date-table

The baseline with Auto date/time switched on and the Date table not marked as a date table. Compare with v33-auto-date-time, which has the same setting with the Date table marked.

## What changed vs baseline

- Power BI Desktop, File > Options and settings > Options > Current file > Data load > Auto date/time: on. In TMDL `annotation __PBI_TimeIntelligenceEnabled = 1` in `model.tmdl`.
- The Date table is not marked as a date table: `dataCategory: Time` is removed from `Date.tmdl`. The relationships to it are unchanged.
- With the setting on, Desktop added a hidden `DateTableTemplate_...` and one hidden calculated table `LocalDateTable_...` per eligible date column, related to the column with `joinOnDateBehavior: datePartOnly`.

Desktop created local date tables for five of the eight date columns, two more than in v33:

| Date column | Local date table | Why |
|---|---|---|
| `Customer[Birthday]` | yes | not related to the Date table |
| `Store[Open Date]` | yes | not related to the Date table |
| `Store[Close Date]` | yes | not related to the Date table |
| `Date[Date]` | yes, new vs v33 | the Date table is not marked |
| `Date[End of Month]` | yes, new vs v33 | the Date table is not marked |
| `Sales[Order Date]` | no | key column of a relationship to `Date[Date]` |
| `Sales[Delivery Date]` | no | key column of a relationship to `Date[Date]` (inactive relationship) |
| `Currency Exchange[Date]` | no | key column of a relationship to `Date[Date]` |

Desktop did not add the two new tables when the Date table was only unmarked and saved. They appeared after Auto date/time was switched off and on again in the options, and the file was saved.

The model was copied from v33 and saved by Desktop on 2026-11-12 with its own logical IDs.

## Why this run

Auto date/time adds the most tables when no date table is marked. In this model the fact date columns are relationship keys and still get no local table, so the effect is limited to the Date table's own two date columns. A model without a Date table at all, where the fact dates are not related to anything, would get a local table per fact date column; that is not tested here.

## Expected effect

- Model size: slightly larger than v33. The two new tables each cover the years of the Date table (2016 to 2026).
- Refresh: two more calculated tables; small. No numbers until measured.
- Queries: unchanged, the visuals do not use the new tables.

## Runs

1. Refresh on F64 with 1M, model sizes.
2. Query workload on F64 with 1M, pages p01 to p20.

## Results

Not run yet.
