# v24-bidirectional

The baseline with one relationship changed: Sales to Customer filters in both directions. Everything else is the same as in the baseline.

## What changed vs baseline

| Relationship | Baseline | v24 |
|---|---|---|
| `Sales[CustomerKey]` to `Customer[CustomerKey]` | single direction (Customer filters Sales) | both directions (Sales also filters Customer) |

With both directions, a filter on Product reaches Customer through Sales. On the filtered page (`pf` in `reports/spec.yaml`), the Country slicer then lists only countries with Computers sales, and the Cities table only cities whose customers bought Computers.

## Why this run

Bidirectional relationships are a common fix for "my slicer shows items with no data". The question is what they cost at query time. Refresh should not change: the relationship is built the same way whichever direction it filters.

## Expected effect

- Refresh peak and model size: same as baseline.
- Pages p01 to p20: same as baseline, because no filter there has to travel from Sales to Customer.
- Page pf: more storage engine queries and more time for the visuals that group by Customer columns (the Country slicer, f04 Cities). No numbers until measured.

## Runs

1. Refresh on F64 with 1M.
2. Query workload on F64 with 1M, pages p01 to p20 and pf. Compare with v00-baseline's pf.

## Results

Not run yet.
