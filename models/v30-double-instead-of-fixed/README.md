# v30-double-instead-of-fixed

The baseline with the price and cost columns as decimal number instead of fixed decimal.

## What changed vs baseline

| Table | Columns now decimal number (`double`) instead of fixed decimal (`decimal`, Currency.Type) |
|---|---|
| Sales | Unit Price, Net Price, Unit Cost |
| Product | Unit Cost, Unit Price |

Measures and everything else are the same.

## Why this run

Fixed decimal stores a value as a scaled 64-bit integer with 4 decimal places, which the engine can value-encode. Decimal number is a floating point value and often ends up hash encoded. The advice is to use fixed decimal for amounts. Results can differ in the last decimals because of floating point arithmetic.

## Expected effect

- Model size: somewhat larger for the three Sales columns.
- Refresh and queries: little difference. No numbers until measured.

## Runs

1. Refresh on F64 with 1M, model sizes.
2. Query workload on F64 with 1M, pages p01 to p20, and a check that the measures return the same totals as the baseline.

## Results

F64, 1M, 2026-11-11 and 2026-11-12. Refresh run `20261112T082436Z-v30-ccac`, query run `20261112T093644Z-v30-4c0b` (all 792 queries succeeded). Query numbers are medians over 5 repeats, cold cache, all visuals of the page at once. The v00 column is the range over its six refreshes and three query runs on F64 with 1M.

| | v00-baseline | v30-double-instead-of-fixed |
|---|---|---|
| Refresh peak | 543 to 698 MB | 550 MB |
| Power Query peak | 270 to 599 MB | 270 MB |
| Duration | 0.6 to 0.8 min | 0.5 min |
| CPU | 55 to 71 s | 51 s |
| Model, backup size in the refresh log | 72.7 MB | 72.8 MB |
| Model in memory right after the refresh | 92.7 MB | 92.9 MB |
| p05 cold, slowest visual | 125 to 141 ms | 141 ms |
| p05 cold, CPU | 313 to 328 ms | 298 ms |
| p20 cold, slowest visual | 672 to 719 ms | 657 ms |
| p20 cold, CPU | 1,890 to 2,172 ms | 1,955 ms |
| p20 cold, peak per query | 58 MB | 58 MB |

No measurable difference from the baseline in model size, refresh or queries. At 1M, decimal number instead of fixed decimal for the five price and cost columns costs nothing here.

The check that the measures return the same totals as the baseline has not been done yet.
