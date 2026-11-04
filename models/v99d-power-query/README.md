# v99d-power-query

Diagnostic run D for v99-kitchen-sink: v99a plus the Power Query antipatterns that v99a removed. No calculated tables.

## What changed vs v99a

- `Sales Flat` is loaded again: Sales merged with every dimension in Power Query, 2.35M rows, 30 columns, most of them text, with the concatenated `Order Line Key`.
- `Table.Buffer` is back in `stg Sales` and `stg Customer`.
- `Unused Heavy Query` has its original body again. It is still not loaded and nothing references it.
- Auto date/time stays on, so `Sales Flat[Order Date]` gets its own local date table.

Everything else is identical to v99a. The calculated tables `Sales Copy`, `Sales Summary`, `Product Date Grid` and `Calendar Auto` stay out.

## How to read the result

- Peak of D minus peak of A: the cost of loading `Sales Flat` into the model. The buffers and the unused query run in the mashup engine, so they should show up in duration and CU, not in peak memory.
- Duration and CU of D minus A: the cost of the Power Query work, mostly the merges, sorts and buffers that build `Sales Flat`.
- If D stays under 25 GB, v99's failure on F64 came from the calculated tables.
