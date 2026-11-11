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

Not run yet.
