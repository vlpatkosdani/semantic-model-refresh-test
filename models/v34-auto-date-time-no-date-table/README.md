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
- Queries: p20 slowest visual 1,486 ms, CPU 3,346 ms. A control run of v00-baseline 35 minutes later was just as slow (1,424 ms, CPU 3,673 ms), so the capacity was slower at that time and these times cannot be compared with the earlier runs. The interleaved runs below show no difference from the baseline. The peak per query is the same as the baseline.

### Interleaved query runs, F64, 1M, 2026-11-12

v00-baseline, v32 and v34 back to back, twice, between 14:42 and 15:48 UTC (round 2 started 15:28, after a network drop): pages p05 and p20, cold cache, all visuals of the page at once, medians over 5 repeats. All 750 queries succeeded.

| Round | Model | p05 slowest visual | p05 CPU | p20 slowest visual | p20 CPU | p20 peak per query |
|---|---|---|---|---|---|---|
| 1 | v00-baseline | 266 ms | 515 ms | 1,516 ms | 3,736 ms | 55 MB |
| 1 | v32-calc-columns-aggregate | 282 ms | 547 ms | 1,454 ms | 3,643 ms | 55 MB |
| 1 | v34-auto-date-time-no-date-table | 281 ms | 485 ms | 1,470 ms | 3,627 ms | 55 MB |
| 2 | v00-baseline | 281 ms | 516 ms | 1,563 ms | 3,535 ms | 55 MB |
| 2 | v32-calc-columns-aggregate | 281 ms | 516 ms | 1,580 ms | 3,831 ms | 55 MB |
| 2 | v34-auto-date-time-no-date-table | 282 ms | 530 ms | 1,407 ms | 3,299 ms | 55 MB |

Runs: v00 `20261112T144321Z-v00-7624`, `20261112T152844Z-v00-eda9`; v32 `20261112T145014Z-v32-e5da`, `20261112T153443Z-v32-c8ba`; v34 `20261112T145703Z-v34-b6c0`, `20261112T154139Z-v34-c119`.

Run back to back, the three models give the same query times, CPU and memory, within about 10 % between rounds. Neither the 30 aggregating calculated columns nor Auto date/time without a marked date table changes the cost of the report's queries.
