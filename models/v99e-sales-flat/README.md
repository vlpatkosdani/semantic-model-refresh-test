# v99e-sales-flat

Diagnostic run E for v99-kitchen-sink. It is v99d plus one change: `Sales Flat` is loaded into the model.

## What changed vs v99d

- `Sales Flat` is loaded: Sales merged with Customer, Product, Store and Date in Power Query, 2.35M rows, 30 columns. Most columns stay text, and `Order Line Key` is a concatenated text key with one distinct value per row. The query sorts and buffers the full result before loading.
- Auto date/time is on, so `Sales Flat[Order Date]` gets its own local date table.

The staging queries `stg Sales` and `stg Customer` stay unbuffered, as in v99a and v99d.

## Why this run

The first version of v99d loaded `Sales Flat` and also buffered the staging queries. It failed on F64, cancelled at 25,598 MB. v99d without both refreshed. This run puts back only `Sales Flat`.

## How to read the result

- If E fails on F64, loading `Sales Flat` alone pushes refresh memory past 25 GB.
- If E refreshes, the staging buffers caused the earlier failure, or only the combination did. Peak of E minus peak of v99d is then the cost of the flat table.
- Duration and CU of E minus v99d show the Power Query cost of the merges, sort and buffer.
