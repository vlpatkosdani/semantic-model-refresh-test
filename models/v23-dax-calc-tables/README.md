# v23-dax-calc-tables

The baseline plus four calculated tables. Power Query is the same as in the baseline.

## What changed vs baseline

New calculated tables, the same as in v99g:

| Table | DAX pattern | Rows on 1M |
|---|---|---|
| `Sales Copy` | `ADDCOLUMNS ( Sales, ...six RELATED columns )`, repeated `CopyCount` times with `GENERATE` | 2.35M per copy |
| `Sales Summary` | `SUMMARIZECOLUMNS` by customer, year and category with three measures | about 1M |
| `Product Date Grid` | `CROSSJOIN` of all products and all days | 10.1M |
| `Calendar Auto` | `CALENDARAUTO ()` with year and month | a few thousand |

None of them has a relationship. Nothing else changes: no auto date/time, no bidirectional relationships.

## Why this run

v99f added three of these tables to v99e and the F64 peak did not change (22,889 to 22,752 MB). v99g added `Sales Copy` and the peak rose 270 MB. Those peaks were set by Power Query, so the tables fit underneath it. Here Power Query is light (baseline peak 785 MB on F64), so anything above that comes from the calculated tables.

## Knobs

| Knob | Where | Default | Effect |
|---|---|---|---|
| `CopyCount` | `VAR` in `Sales Copy` | 1 | each extra copy adds 2.35M rows on 1M |
| `FirstYear` | `VAR` in `Product Date Grid` | 2016 | 2021 keeps about half the rows |
| `DataTag` | parameter | `data-1m-v1` | `data-10m-v1` makes Sales and `Sales Copy` 23.5M rows |

## Expected effect

- Model size: clearly larger than baseline. `Sales Copy` alone is about the size of Sales.
- Peak refresh memory: higher than baseline. A calculated table is built in memory in full before it is compressed. No number this time.
- Duration: higher than baseline.

## Practical notes

- The calculated tables have no column definitions in the TMDL. Desktop computes them when you open the file and refresh. Publish after that refresh.

## Runs

1. F64 with 1M, then F64 with 10M. Compare `PeakMemMB` and `MEnginePeakMB` with v00 on the same data. The difference between them is the model side.
2. F2 with 1M.
3. Refresh the same model twice in a row, on F64 and F2. During a full refresh the old data stays in memory until the new data is committed, so the second refresh should need more than the first.

## Results

| Capacity | Data | Run | Result | Peak MB | Power Query MB | Duration |
|---|---|---|---|---|---|---|
| F64 | 1M | first | refreshed | 1,405 | 399 | 0.9 min |
| F64 | 10M | first | refreshed | 13,062 | 1,202 | 8.6 min |
| F2 | 1M | first | refreshed | n/a | n/a | n/a |
| F2 | 1M | second, right after the first | refreshed | n/a | n/a | n/a |

F2 has no workspace monitoring, so the two F2 runs have a result but no peak or duration (n/a). Both refreshed: the model needs about 1.4 GB on 1M, well under the F2 limit of about 3 GB, even with the first copy still in memory. Whether the copy in memory counts in the peak was measured on 10M instead (the three runs on 2026-11-12 below): it does not.

On F64 the peak is 1,405 MB, of which 399 MB is Power Query. The part outside Power Query grows from about 110 MB in the baseline to about 1,000 MB. Unlike the calculated columns, the calculated tables clearly raise the peak. The model grows from 73 MB to 184 MB (backup size in the refresh log, MB of 1,048,576 bytes). `Sales Copy` takes 8 seconds, `Product Date Grid` 5.5 seconds, `Sales Summary` 4.6 seconds.

On 10M the peak is 13,062 MB, of which 1,202 MB is Power Query. The part outside Power Query is about 11,900 MB, against about 210 MB for the baseline on 10M. The calculated tables scale with the data, about 12 times from 1M to 10M. The model is 1,833 MB (baseline on 10M: 778 MB). This model would need at least F64; it would fail on F2 to F32.

### Harness runs, F64, 1M, 2026-11-10

Refresh (run `20261110T131904Z-v23-8705`): peak 1,406 MB, Power Query 721 MB, 1 min, model 184 MB. The peak repeats the first measurement (1,405 MB).

Query workload (run `20261110T132552Z-v23-ac2c`, all 792 queries succeeded), compared with v00-baseline (run `20261110T103141Z-v00-5b3b`). Medians over 5 repeats, cold cache, all visuals at once:

| Page | Slowest visual v00 | Slowest visual v23 | CPU v00 | CPU v23 | Peak per query v00 | Peak per query v23 |
|---|---|---|---|---|---|---|
| p01 | 21 ms | 16 ms | 31 ms | 31 ms | 4 MB | 4 MB |
| p05 | 141 ms | 125 ms | 328 ms | 327 ms | 14 MB | 14 MB |
| p10 | 141 ms | 141 ms | 360 ms | 422 ms | 14 MB | 14 MB |
| p20 | 672 ms | 672 ms | 2,033 ms | 2,001 ms | 58 MB | 58 MB |

The calculated tables cost memory at refresh and in the model, but nothing measurable at query time for visuals that do not use them: the baseline's queries ran as fast as on v00.

### Harness runs, F64, 10M, 2026-11-12: does the model already in memory count?

Three full refreshes of the same model in a row, with the model size in memory measured before each one (INFO.STORAGETABLECOLUMNSEGMENTS plus dictionaries, by DAX):

| Run | Harness run | Model in memory before | Peak MB | Power Query MB | Duration | Model after |
|---|---|---|---|---|---|---|
| from empty | `20261112T114059Z-v23-16be` | 0 MB | 13,064 | 1,708 | 8 min | 1,379 MB |
| model loaded, right after the first | `20261112T115659Z-v23-fb5a` | 1,379 MB | 13,139 | 1,707 | 8 min | 1,381 MB |
| loaded, then cleared first (`clearValues`) | `20261112T121228Z-v23-dfc6` | 1,381 MB, 0.1 MB after clearing | 13,062 | 1,870 | 7 min | 1,387 MB |

The peak is the same in all three runs (13,062 to 13,139 MB, and 13,062 MB in the first 10M run on 2026-11-10). With 1,379 MB already loaded, the peak rose by 75 MB, not by 1,379 MB. So the peak in ExecutionMetrics does not include the copy of the model that stays in memory during a full refresh, and the second refresh did not need more than the first. Run 3 in the list above expected it would.

That matches the command memory limit as Chris Webb describes it: the limit for a refresh is the SKU maximum minus the size of the model before the command. The peak counts what the refresh itself uses, and the model already in memory is taken off the limit instead. For this model on F64 that is 25,600 MB minus 1,379 MB, 24,221 MB, against a peak of about 13,100 MB.

Clearing the model first did not lower the peak. It only raises the limit by the size of the model, here by 1,379 MB, at the cost of the model being empty while the refresh runs. On a SKU where the peak is just over the limit, that can be the difference; on F64 it does not matter for this model.

The model size here is measured by DAX in the service. The backup size in the refresh log on 2026-11-10 was 1,833 MB for the same model, so the two sources differ.
