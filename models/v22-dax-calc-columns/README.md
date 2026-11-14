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
| F64 | 1M | first | refreshed | 686 | 430 | 0.8 min |
| F64 | 10M | first | not run yet | | | |
| F2 | 1M | first | refreshed | | | |
| F2 | 1M | second, right after the first | refreshed | | | |

On F64 the peak is 686 MB, of which 430 MB is Power Query. The baseline peaks at 785 MB with 677 MB in Power Query. The part outside Power Query grows from about 110 MB to about 260 MB. Each calculated column takes 0.6 to 1.2 seconds to compute, `Sales Line Label` 3.5 seconds. The model grows from 73 MB to 101 MB (backup size in the refresh log, MB of 1,048,576 bytes).

### Harness runs, F64, 1M, 2026-11-10

Refresh (run `20261110T125746Z-v22-8023`): peak 621 MB, Power Query 270 MB, 1 min, model 101 MB. The baseline's four harness and manual runs on F64 1M peaked at 551 to 785 MB, so the calculated columns do not raise the peak measurably on 1M.

Query workload (run `20261110T130235Z-v22-817d`, all 792 queries succeeded), compared with v00-baseline (run `20261110T103141Z-v00-5b3b`). Medians over 5 repeats, cold cache:

| Page | Visuals | Slowest visual v00 | Slowest visual v22 | CPU v00 | CPU v22 | Peak per query v00 | Peak per query v22 |
|---|---|---|---|---|---|---|---|
| p01 | all at once | 21 ms | 16 ms | 31 ms | 16 ms | 4 MB | 4 MB |
| p05 | all at once | 141 ms | 141 ms | 328 ms | 328 ms | 14 MB | 14 MB |
| p10 | all at once | 141 ms | 156 ms | 360 ms | 407 ms | 14 MB | 14 MB |
| p20 | all at once | 672 ms | 1,047 ms | 2,033 ms | 2,625 ms | 58 MB | 58 MB |
| p20 | one by one | 641 ms | 782 ms | 1,906 ms | 2,236 ms | 58 MB | 58 MB |

The slowest visual on p20 is v20 (orders by category and continent) on both models. It took 1,047 ms on v22 against 672 ms on v00 when all 20 visuals ran at once, and 782 ms against 641 ms one by one. The other visuals that group over Sales (v05, v14, v18) were also 50 to 100 ms slower when run at once. No visual uses the calculated columns. For comparison, v27, an unchanged copy of the baseline, measured 766 ms for v20 on the same page. This is one run per model, so a repeat run of v00 and v22 is needed before calling the difference an effect of the wider Sales table.

Repeat runs on 2026-11-10 (v00 `20261110T194546Z-v00-cdd8`, v22 `20261110T195815Z-v22-cca3`), slowest visual on p20, cold cache, median of 5 repeats:

| Run | v00 all at once | v22 all at once | v00 one by one | v22 one by one |
|---|---|---|---|---|
| first | 672 ms | 1,047 ms | 641 ms | 782 ms |
| repeat | 719 ms | 750 ms | 688 ms | 625 ms |

In the repeat v22 is as fast as v00, so the first run's 1,047 ms was run-to-run spread, not an effect of the calculated columns. Calculated columns that no visual uses do not change query time here. The repeat's per-page summary file was not downloaded (the sign-in token expired during the download, and the F64 workspace lost its capacity afterwards); the per-query rows are in `results/query-runs.csv` and `results/query-pages.csv`.

### Query runs alternating with v00-baseline, F64, 1M, 2026-11-13

The first two runs that day failed: v22 had never been refreshed in the new F64 workspace (2026-11-11), so it held no data ("The expression referenced a relationship ... which does not hold any data because it needs to be recalculated"). After a refresh (run `20261113T173653Z-v22-df42`: peak 794 MB, Power Query 469 MB, 132.6 MB in memory right after), pages p05 and p20, cold, all visuals at once:

| Time (UTC) | Model | p05 slowest visual | p20 slowest visual | p20 CPU | p20 peak per query |
|---|---|---|---|---|---|
| 18:02 | v00-baseline | 250 ms | 1,392 ms | 3,736 ms | 55 MB |
| 18:55 | v22 | 156 ms | 813 ms | 1,985 ms | 55 MB |
| 19:00 | v00-baseline | 234 ms | 1,344 ms | 3,204 ms | 55 MB |
| 19:07 | v22 | 156 ms | 828 ms | 2,142 ms | 55 MB |
| 20:16 | v00-baseline | 250 ms | 1,393 ms | 3,550 ms | 55 MB |

Query time on F64 has a fast and a slow state per model, about two times apart, that last for hours and change by themselves (`docs/lab-findings-queries.md`, finding 7). Memory per query does not change with it. Here v00 was in the slow state and v22 was not, so these runs do not show the effect of the calculated columns. All three v22 runs (813 to 1,047 ms) are inside the baseline's two states. Not confirmed either way.
