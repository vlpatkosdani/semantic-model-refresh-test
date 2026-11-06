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
| F2 | 1M | first | refreshed | | | |
| F2 | 1M | second, right after the first | refreshed | | | |

On F64 the peak is 1,405 MB, of which 399 MB is Power Query. The part outside Power Query grows from about 110 MB in the baseline to about 1,000 MB. Unlike the calculated columns, the calculated tables clearly raise the peak. The model grows from 76 MB to 193 MB (backup size in the refresh log). `Sales Copy` takes 8 seconds, `Product Date Grid` 5.5 seconds, `Sales Summary` 4.6 seconds.

On 10M the peak is 13,062 MB, of which 1,202 MB is Power Query. The part outside Power Query is about 11,900 MB, against about 210 MB for the baseline on 10M. The calculated tables scale with the data, about 12 times from 1M to 10M. The model is 1,923 MB (baseline on 10M: 816 MB). This model would need at least F64; it would fail on F2 to F32.
