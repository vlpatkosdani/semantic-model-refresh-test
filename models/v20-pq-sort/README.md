# v20-pq-sort

The baseline plus two sorts of the Sales table in Power Query. Nothing else changes.

## What changed vs baseline

In the `Sales` query:

- right after reading the file, the full table is sorted by order date (descending), order number and line number
- after the type step, it is sorted again by customer

The loaded table has the same rows and columns as the baseline. Only the order differs, and the order does not matter to the model.

## Hypothesis

A sort cannot stream. Power Query has to read all 2.35M rows into memory before it returns the first one, which costs about as much as a `Table.Buffer`. In the v99 diagnostic runs, v99o (v99m plus these sorts and a sort of Product) failed on F2 while v99m refreshed. That model also had eight calculated columns, bidirectional relationships and auto date/time. This run tests whether the sorts alone take the clean baseline off F2.

## Expected effect

- Model size: same as baseline.
- Peak refresh memory: higher than baseline, by roughly the size of the decoded Sales table in the mashup engine, once or twice.
- Duration: somewhat higher than baseline.

## How to read the result

- If it fails on F2, one common Power Query step is enough to push a well-built model of this size off the smallest capacity.
- If it refreshes, the sorts only fail F2 together with the rest of v99m.

## Results

| Capacity | Data | Run | Result | Peak MB | Power Query MB | Duration | Details |
|---|---|---|---|---|---|---|---|
| F64 | 1M | manual, 2026-11-06 | refreshed | 5,229 | 4,965 | 8.6 min | service size 72 MB |
| F2 | 1M | manual, 2026-11-06 | failed | | | | consumed memory not recorded |
| F2 | 1M | harness, 2026-11-10 | failed | | | 1.2 min | resource governance: consumed 3,179 MB, limit 3,067 MB, database size before command 4 MB |
| F64 | 1M | harness, 2026-11-10 | refreshed | 5,269 | 5,043 | 1.8 min | service size 72 MB |

The harness run is within 1% of the manual run on F64 (5,269 vs 5,229 MB). On the same day v00 peaked at 623 MB, so the two sorts add about 4,650 MB. The peak is above the F2 limit and just above the documented F16 limit (5,120 MB). The duration differs a lot from the manual run (1.8 vs 8.6 min), the peak does not.

The two sorts alone take the baseline off F2. The loaded table is identical to the baseline, only the row order differs, so the extra memory is used by Power Query during the refresh and none of it stays in the model.
