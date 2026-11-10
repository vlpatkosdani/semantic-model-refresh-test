# v99-kitchen-sink

The baseline with every antipattern from the test list combined. It is built to look harmless on Pro and fail on small Fabric capacities.

## Design targets (1M data)

- Final model size well under Pro's 1 GB limit, ideally a few hundred MB.
- Peak refresh memory clearly above 3 GB, so the refresh fails on F2, F4 and F8.
- Peak low enough to refresh on F64 (25 GB), so the real peak can be measured.

## What changed vs baseline

Power Query

- Staging queries `stg Sales`, `stg Customer`, `stg Product`, `stg Store`, `stg Date`. They are not loaded and they turn every column into text.
- `stg Sales` is referenced by `Sales`, `Sales Flat` and `Customer Stats`, so it is evaluated three times. `stg Customer`, `stg Product`, `stg Store` and `stg Date` are each evaluated twice.
- Loaded queries convert types late, after sorts and buffers. `Sales Flat` leaves most columns as text.
- `Sales Flat`: Sales merged with every dimension in Power Query and loaded next to the star. Parquet does not fold, so the joins run in the mashup engine.
- Needless `Table.Sort` and `Table.Buffer` on the full fact, twice in `Sales` and once in `Sales Flat`.
- `Customer Stats`: a Group By over the full fact (customer and year).
- `Unused Heavy Query`: merges, sorts and buffers orders and order rows. It is not loaded and nothing references it, so it should cost nothing.

Model

- Auto date/time on (see the Desktop step below).
- High-cardinality columns: `Sales[Order Line]` (line-level integer key), `Sales[Order DateTime]` (datetime with time), `Sales Flat[Order Line Key]` (concatenated text key).
- Calculated columns on `Sales`: five RELATED columns, `Customer Lifetime Sales` (CALCULATE with context transition), `Product Price Rank` (RANKX), `Sales Line Label` (text concatenation).
- Calculated tables:
  - `Sales Copy`: ADDCOLUMNS over all of Sales plus RELATED columns, repeated `CopyCount` times.
  - `Sales Summary`: SUMMARIZECOLUMNS by customer, year and category.
  - `Product Date Grid`: CROSSJOIN of Product and Date.
  - `Calendar Auto`: a second date table from CALENDARAUTO.
- Relationships: bidirectional between Sales and Customer, Product and Store. Many-to-many between Sales and `Customer Stats` on CustomerKey. `Calendar Auto` relates to `Sales Flat` only, so no filter path is ambiguous.
- `Date[End of Month]` stays a DAX calculated column (the baseline builds it in Power Query).

## Knobs

Each knob is marked with `===== KNOB =====` in the DAX:

| Knob | Where | Default | Effect |
|---|---|---|---|
| `CopyCount` | `tables/Sales Copy.tmdl` | 2 | Number of Sales copies. Each copy adds about 40 to 60 MB of model size and 1.2 to 1.8 GB of peak memory. |
| `FirstYear` | `tables/Product Date Grid.tmdl` | 2016 | Start of the crossjoin date range. 2016 keeps all 10.1M rows, 2021 about half. |
| Summary grain | `tables/Sales Summary.tmdl` | Year | `Year Month` instead of `Year` roughly doubles the rows. |

Do not add Store or Customer to the crossjoin. Product x Date x Store is 750M rows and would fail on any capacity.

This variant is tuned for the 1M data. On `data-10m-v1` every Sales-sized object is ten times larger. Set `CopyCount` to 1 and expect it to fail below F64.

## Expected effect per element (1M data, full refresh)

These are estimates with roughly 50% error each way. The point of the lab is to replace them with measured numbers.

| Element | Model size | Peak refresh memory | Duration and CU |
|---|---|---|---|
| Old copy kept in memory during full refresh | 0 | +1x model size | 0 |
| `Sales Copy`, 2 copies | +80 to 120 MB | +2.5 to 3.5 GB | high (FE materialization) |
| `Product Date Grid`, 10.1M rows | +20 to 30 MB | +0.7 to 1.2 GB | medium |
| `Sales Flat` | +90 to 130 MB | +0.4 to 0.7 GB | high (mashup joins and sort) |
| Sales calculated columns | +25 to 35 MB | +0.2 to 0.4 GB | medium |
| High-cardinality Sales columns | +20 MB | +0.1 GB | low |
| `Sales Summary` | +10 to 20 MB | +0.1 to 0.2 GB | low |
| Auto date/time | +5 to 20 MB | +0.05 to 0.1 GB | low |
| `Calendar Auto` | under 1 MB | about 0 | low |
| Bidirectional relationships | 0 | about 0 | 0 at refresh, cost shows at query time |
| Many-to-many relationship | about 0 | about 0 | 0 at refresh, cost shows at query time |
| Text types, sorts, Table.Buffer, Group By, shared staging | 0 to 10 MB | about 0 in the engine (wrong, see below) | high (mashup CPU and memory) |
| `Unused Heavy Query` | 0 | 0 | 0 |

Expected totals: model size about 250 to 400 MB, peak refresh memory about 3.5 to 6 GB. The two Sales copies dominate, then the crossjoin, then the old copy and the flat table. If the engine computes the calculated tables one at a time instead of in parallel, the peak lands at the low end.

Power Query work happens in the mashup engine, which is a separate process from the semantic model. It shows up in refresh duration and CU, not in `approximatePeakMemConsumptionKB`. It can still fail on its own if the mashup container runs out of memory.

The `Customer Lifetime Sales` column uses `ALLEXCEPT ( Sales, Sales[CustomerKey] )`, so the engine can compute one value per customer and look it up. A bare `[Sales Amount]` in a calculated column would be much heavier, because context transition then filters on every column of the row. Only one column on Sales may use CALCULATE or a measure. Two such columns depend on each other and fail with a circular dependency.

## Steps in Desktop before the first publish

1. Open `v99-kitchen-sink.pbip` and refresh. The calculated tables have no columns in TMDL yet. The engine creates them on the first refresh.
2. Auto date/time: the model annotation is set to on, but TMDL cannot reliably create the hidden `LocalDateTable_*` tables. Go to File, Options and settings, Options, Current file, Data load, Time intelligence. Turn Auto date/time off and on again, then check that `LocalDateTable_*` tables appear in the TMDL folder after saving.
3. Save, then publish.

## Results

| Capacity | Result | Details |
|---|---|---|
| Pro (shared) | refreshed | downloaded .pbix 458,321 KB |
| F2 | failed | cancelled at 3,319 MB, limit 3,065 MB |
| F64 | failed | cancelled at 25,599 MB, limit 25,593 MB |
| PPU (Premium Per User, 100 GB per model) | refreshed | peak 26,115 MB, Power Query 25,958 MB, 20 min, 40,515,912 rows, model 622 MB (XMLA trace, harness run `20261110T162110Z-v99-0db3`, 2026-11-10, 1M data) |

The full peak, measured on Premium Per User, is 26,115 MB: just above F64's 25.6 GB limit, and 99 percent of it is Power Query. The same model refreshes on Pro and fails on F64. Pro does not behave like a small Fabric capacity: the per-model memory governance that cancels the refresh on F SKUs did not stop it on shared capacity.

## Measured so far

The estimates above were wrong in one important place. The diagnostic runs v99a to v99j split v99 into parts and refreshed them on F64:

- Every calculated table, the flat table and all calculated columns refresh together on F64 (v99g).
- Adding `Table.Buffer` to the not-loaded staging queries `stg Sales` and `stg Customer` makes the same model fail at over 25.6 GB (v99h).
- Splitting the two buffers: `stg Customer` alone refreshes (v99j), `stg Sales` alone fails at over 25.6 GB (v99i).

So the biggest single cause of v99's refresh memory is one `Table.Buffer` step at the end of `stg Sales`, a staging query that is never loaded. It holds all 2.35M Sales rows with every column as text, and three loaded queries reference it (`Sales`, `Sales Flat`, `Customer Stats`). See the README of each diagnostic run for the full results table.
