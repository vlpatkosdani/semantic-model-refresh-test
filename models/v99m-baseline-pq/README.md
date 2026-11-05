# v99m-baseline-pq

Diagnostic run M for v99-kitchen-sink. It is v99k with the Power Query of the baseline.

## What changed vs v99k

- `Sales`, `Customer`, `Product`, `Store` and `Date` load with the same queries as v00-baseline: read the Parquet file, rename, select, set types. No conversion to text, no sorts, no late types.
- The staging queries `stg Sales`, `stg Customer`, `stg Product`, `stg Store` and `stg Date` are removed. So are the not-loaded `Sales Flat` and `Unused Heavy Query`.
- `Sales[Order Line]` and `Sales[Order DateTime]` are removed, together with the local date table of `Order DateTime`.
- `Customer Stats` and its many-to-many relationship to Sales are removed. It is a Group By in Power Query, so it belongs to this half of the split.
- `Date[End of Month]` comes from Power Query, as in the baseline.

Kept from v99k:

- all eight calculated columns on Sales (RELATED, RANKX, text concatenation, CALCULATE with ALLEXCEPT). None of them uses the removed columns.
- bidirectional relationships from Sales to Customer, Product and Store
- auto date/time, with local date tables for `Customer[Birthday]`, `Store[Open Date]` and `Store[Close Date]`
- `Binary.Buffer` in `fnLoadParquet`, as in the baseline

## Why this run

See v99l. L removes the calculated columns, M removes the Power Query antipatterns. Run both on F2 and read them together.

## How to read the result

| L on F2 | M on F2 | Meaning |
|---|---|---|
| refreshes | fails | the calculated columns push the refresh over 3 GB |
| fails | refreshes | the Power Query steps push the refresh over 3 GB |
| refreshes | refreshes | neither alone is enough, the two together are |
| fails | fails | the cause is in what both keep: relationships, auto date/time, or the remaining columns |

If M refreshes, part of the difference also comes from the two high-cardinality columns, because they are created in Power Query and removed here.

## Results

| Capacity | Result | Details |
|---|---|---|
| F2 | not run yet | |
