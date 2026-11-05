# v99n-text-staging

Diagnostic run N for v99-kitchen-sink. It is v99m plus the text staging queries from v99k.

## What changed vs v99m

- New not-loaded queries `stg Sales`, `stg Customer`, `stg Product`, `stg Store` and `stg Date`. Each reads its Parquet file and turns every column into text.
- `Sales`, `Customer`, `Product`, `Store` and `Date` read from the staging queries and convert the types back at the end, with the en-US culture.
- `Date[End of Month]` is a DAX calculated column, as in v99k, because the Date query is the v99k one. It has 4,018 rows.

No sorts, no `Order Line` or `Order DateTime`, no `Customer Stats`.

## Why this run

v99m (v99k with the baseline Power Query) refreshed on F2. v99l (v99k without the calculated columns) failed on F2 at 3,146 MB. So the Power Query half of v99k is enough to fail F2. v99n to v99q each start from v99m and add back one of its four parts:

| Model | Adds back |
|---|---|
| v99n-text-staging | staging queries that turn every column into text, types converted late |
| v99o-sorts | full sorts of Sales and the sort of Product |
| v99p-high-cardinality | `Sales[Order Line]` and `Sales[Order DateTime]` with its local date table |
| v99q-customer-stats | `Customer Stats`, a Group By over the full Sales fact, and its many-to-many relationship |

All four keep what v99m has: the eight calculated columns on Sales, bidirectional relationships, auto date/time and `Binary.Buffer` in `fnLoadParquet`.

## How to read the result

- If exactly one of n to q fails on F2, that part alone is enough to push this model over 3 GB.
- If several fail, each of them is enough on its own.
- If none fails, it takes a combination. In v99k, `stg Sales` (text) feeds both `Sales` and `Customer Stats`, and the sorts and new columns run on text, so the parts make each other more expensive.

## Results

| Capacity | Result | Details |
|---|---|---|
| F2 | not run yet | |
