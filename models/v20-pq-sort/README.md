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

| Capacity | Result | Details |
|---|---|---|
| F2 | not run yet | |
