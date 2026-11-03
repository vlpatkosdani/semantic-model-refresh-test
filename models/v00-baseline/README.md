# v00-baseline

The reference model. Every other variant is measured against this one.

## What it is

A clean star schema on Contoso V2:

- Fact: `Sales` (one row per order line, 2.35M rows on the 1M data).
- Dimensions: `Customer`, `Product`, `Store`, `Date`.
- `Currency Exchange` (daily rates, related to `Date`).
- Single direction, one-to-many relationships. `Sales[Delivery Date]` to `Date` is inactive.
- Correct data types, only the columns the model needs.
- No calculated columns, no calculated tables. `Date[End of Month]` is built in Power Query.
- Auto date/time off.
- Measures: Sales Amount, Total Cost, Margin, Margin %, Total Quantity, # Orders.

`orders.parquet` and `orderrows.parquet` are not loaded. They hold the same rows as `sales.parquet`, split into header and detail.

## Data access

- Parameter `DataTag` picks the release: `data-1m-v1` (default) or `data-10m-v1`. Changing it switches every table.
- Function `fnLoadParquet(FileName)` loads one file. Every table query calls it, so variants only differ where they mean to.
- The URL is `Web.Contents("https://github.com", [RelativePath = ...])`. The base is a static literal and the tag and file name are in RelativePath, so the service sees one static data source and can refresh without a gateway.
- Credentials in the service: Anonymous, privacy level Public.
- The function wraps the download in `Binary.Buffer`. Parquet needs random access to the file, and without the buffer the engine can download it more than once.

## Hypothesis

None. This is the control. It sets the reference numbers for model size, peak refresh memory, refresh duration and CU.

## Expected numbers (1M data)

- Model size: about 40 to 60 MB.
- Peak refresh memory: a few hundred MB, roughly two to four times the model size during a full refresh.
- Should refresh on every capacity, F2 included.
