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

F64, 1M, 2026-11-12. Refresh run `20261112T134438Z-v34-9a21`, query run `20261112T134925Z-v34-85a1` (all 792 queries succeeded). Query numbers are medians over 5 repeats, cold cache, all visuals of the page at once.

| | v00-baseline | v33 (Date marked) | v34 (Date not marked) |
|---|---|---|---|
| Refresh peak | 543 to 698 MB | 619 MB | 707 MB |
| Power Query peak | 270 to 599 MB | 423 MB | 421 MB |
| CPU | 55 to 71 s | 59 s | 99 s |
| Model, backup size in the refresh log | 72.7 MB | 73.8 MB | 74 MB |
| Model in memory right after the refresh | 92.7 MB | 96.2 MB | 96.9 MB |
| p20 cold, peak per query | 58 MB | 55 MB | 55 MB |

- Model: the two extra local date tables add 0.7 MB in memory over v33. With the fact date columns related to the Date table, Auto date/time costs a few MB whether the Date table is marked or not.
- Refresh: the peak is 9 MB above the baseline range, and CPU (99 s) is high. A v00-baseline refresh 20 minutes later also used 99 s of CPU, so the CPU says more about the capacity at that time than about the model.
- Queries: p20 slowest visual 1,486 ms, CPU 3,346 ms. A control run of v00-baseline 35 minutes later was just as slow (1,424 ms, CPU 3,673 ms), so the capacity was slower at that time and these times cannot be compared with the earlier runs. An interleaved run with v00 is needed. The peak per query is the same as the baseline.
