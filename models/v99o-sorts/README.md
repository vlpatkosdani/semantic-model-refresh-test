# v99o-sorts

Diagnostic run O for v99-kitchen-sink. It is v99m plus the sorts from v99k.

## What changed vs v99m

- `Sales` sorts the full table by order date, order number and line number right after reading the file, and sorts it again by customer at the end.
- `Product` sorts by product name before the type step.

The sorts run on typed columns here. In v99k they ran on text.

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
| F64 | refreshed | |
| F2 | failed | consumed memory not recorded |

Results of the whole split on F2: n refreshed, o failed, p refreshed, q failed. All four refreshed on F64.

The sorts alone and `Customer Stats` alone are each enough to push v99m over 3 GB. Text staging and the high-cardinality columns are not. Sorting and grouping are the two steps here that cannot stream: Power Query has to read the whole Sales table into memory before it returns the first row, which has the same effect as a `Table.Buffer`.
