# v99a-no-big-calc-tables

Diagnostic run A for v99-kitchen-sink.

v99 failed on F64: the refresh was cancelled at 25,599 MB against a 25,593 MB limit. This variant strips v99 down to find out how much of that peak comes from the calculated tables and the flat table.

## What changed vs v99

Removed or disabled:

- Calculated tables `Sales Copy`, `Sales Summary`, `Product Date Grid` and `Calendar Auto` are removed from the model.
- `Sales Flat` is no longer loaded. Its query stays in the file as a not-loaded query, so it is never evaluated.
- `Table.Buffer` is removed from `stg Sales` and `stg Customer`.
- `Unused Heavy Query` is commented out and returns 1.

Kept from v99:

- Staging queries that turn every column into text, with types converted late.
- Sort and `Table.Buffer` on the full fact in `Sales`, and the Group By in `Customer Stats`.
- High-cardinality columns `Sales[Order Line]` and `Sales[Order DateTime]`.
- All eight calculated columns on `Sales` (RELATED, CALCULATE, RANKX, text concatenation) and `Date[End of Month]`.
- Bidirectional relationships from Sales to Customer, Product and Store, and the many-to-many to `Customer Stats`.
- Auto date/time on. Desktop created local date tables for `Customer[Birthday]`, `Sales[Order DateTime]`, `Store[Open Date]` and `Store[Close Date]`.

## How to read the result

- If A refreshes on F64, its peak is the cost of everything except the removed tables. v99's 25.6 GB or more minus this peak is the cost of the calculated tables and the flat table together.
- If A also refreshes on F2, the calculated columns, relationships and Power Query steps alone do not push the peak past 3 GB.
- If A fails on F64, the main cost is in what is left, most likely the calculated columns on Sales.

## Results

| Capacity | Result | Details |
|---|---|---|
| F64 | refreshed | |
| F2 | failed | cancelled at 3,099 MB, limit 3,065 MB, database size before command 6 MB |

v99d to v99j all contain everything in v99a, so they are expected to fail on F2 as well. They were not run there.

v99a still has two `Table.Buffer` steps in loaded queries: after the sort in `Sales` and at the start of `Customer Stats`.
