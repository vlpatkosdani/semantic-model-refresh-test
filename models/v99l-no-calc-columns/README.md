# v99l-no-calc-columns

Diagnostic run L for v99-kitchen-sink. It is v99k without the eight calculated columns on Sales.

## What changed vs v99k

Removed from `Sales`:

- `Customer Name`, `Customer Country`, `Product Name`, `Product Category`, `Store Name` (RELATED)
- `Product Price Rank` (RANKX)
- `Sales Line Label` (text concatenation)
- `Customer Lifetime Sales` (CALCULATE with ALLEXCEPT)

No measure or visual uses them. `Date[End of Month]` stays as a DAX calculated column. It has 4,018 rows, so it does not matter here.

Everything else is identical to v99k:

- staging queries that turn every column into text, with types converted late
- full-table sorts in `Sales` and `Product`, and the Group By in `Customer Stats`
- high-cardinality columns `Sales[Order Line]` and `Sales[Order DateTime]`
- bidirectional relationships, many-to-many to `Customer Stats`, auto date/time
- no `Table.Buffer` in any query that refresh evaluates

## Why this run

v99k failed on F2 without any `Table.Buffer`, and refreshed on F64. L and M split what is left in two: L removes the calculated columns, M removes the Power Query antipatterns.

## How to read the result

| L on F2 | M on F2 | Meaning |
|---|---|---|
| refreshes | fails | the calculated columns push the refresh over 3 GB |
| fails | refreshes | the Power Query steps push the refresh over 3 GB |
| refreshes | refreshes | neither alone is enough, the two together are |
| fails | fails | the cause is in what both keep: relationships, auto date/time, or the remaining columns |

## Results

| Capacity | Result | Details |
|---|---|---|
| F2 | not run yet | |
