# v99c-crossjoin-only

Diagnostic run C for v99-kitchen-sink.

v99 failed on F64: the refresh was cancelled at 25,599 MB against a 25,593 MB limit. Runs A, B and C split v99 into parts so each part's peak refresh memory can be measured on F64.

## What changed vs v99

Run A plus the full Product x Date crossjoin (10.1M rows). Sales Copy is empty.

| Knob | v99 | This run |
|---|---|---|
| `CopyCount` in `tables/Sales Copy.tmdl` | 2 | 0 |
| `FirstYear` in `tables/Product Date Grid.tmdl` | 2016 | 2016 |

A knob of 0 copies or a first year of 2099 leaves the table in the model with zero rows. The model structure is otherwise identical to v99.

## How to read the result

- Peak of B minus peak of A: the cost of one Sales copy.
- Peak of C minus peak of A: the cost of the 10.1M row crossjoin.
- If A fails on F64 by itself, the main cost is somewhere else in v99.

Same Desktop steps as v99 before publishing: refresh once so the calculated tables get their columns, and toggle auto date/time off and on.
