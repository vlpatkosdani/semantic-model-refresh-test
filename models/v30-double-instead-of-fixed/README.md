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

Totals against v00-baseline, both on F64 with 1M, 2026-11-13 (DAX query through executeQueries, grand total and per year, 11 rows):

| Measure | v00-baseline (fixed decimal) | v30 (decimal number) | Difference |
|---|---|---|---|
| Sales Amount | 2,298,959,215.6985 | 2,298,959,214.469255 | 1.23 |
| Total Cost | 1,013,993,459.634 | 1,013,993,459.6339607 | 0.00004 |
| Margin | 1,284,965,756.0645 | 1,284,965,754.8352942 | 1.23 |
| Margin % | 0.558933689336496 | 0.5589336891006766 | 0.0000000002 |
| Total Quantity | 7,384,887 | 7,384,887 | 0 |
| # Orders | 980,666 | 980,666 | 0 |

The Total Cost difference is floating point rounding. The Sales Amount difference is not: 4,742 of the 24,212 distinct Net Price values in the source have a fifth decimal (for example 74.24325). Fixed decimal stores four decimals, so the baseline rounds them; decimal number keeps them. The v30 total is the one closer to the source data. On a total of 2.3 billion the difference is 1.23, invisible in any report formatted to whole numbers or two decimals.
