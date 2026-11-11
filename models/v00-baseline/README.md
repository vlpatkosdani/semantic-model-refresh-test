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

## Results

| Capacity | Data | Result | Peak MB | Power Query MB | Duration | Model size |
|---|---|---|---|---|---|---|
| F2 | 1M | refreshed | | | 2 min | |
| F64 | 1M | refreshed (2026-11-04) | 785 | 677 | 0.7 min | 73 MB |
| F64 | 1M | refreshed (2026-11-07, harness) | 551 | 312 | 0.7 min | 73 MB |
| F2 | 1M | refreshed (2026-11-10, harness) | | | 1.1 min | 93 MB (DAX) |
| F64 | 1M | refreshed (2026-11-10, harness) | 623 | 599 | 0.6 min | 73 MB |
| F64 | 10M | refreshed (2026-11-06) | 2,040 | 1,832 | 6 min | 778 MB |
| F2 | 10M | refreshed (2026-11-10, harness) | | | 26 min | 700 MB (DAX) |
| F64 | 10M | refreshed (2026-11-10, harness) | 2,116 | 1,584 | 6 min | 778 MB |
| F64 | 1M | refreshed (2026-11-11, harness, new F64 workspace, model empty before) | 543 | 270 | 1 min | 73 MB |
| F64 | 1M | refreshed (2026-11-11, harness, model loaded: 92.7 MB in memory before) | 545 | 374 | 1 min | 73 MB |
| F64 | 1M | refreshed (2026-11-11, harness, clearValues first: 0 MB before) | 608 | 335 | 1 min | 73 MB |
| F2 | 1M | refreshed (2026-11-11, harness, 10M data still loaded: 626 MB before) | | | 1 min | 93 MB (DAX) |

Model size is the backup size in the refresh log, in MB of 1,048,576 bytes. On 1M the model is 73 MB, a bit above the 40 to 60 MB expected. On 10M the peak stays below the 3 GB limit of F2 (2,040 and 2,116 MB in two runs), and the harness run on 2026-11-10 confirmed it: the clean star schema with 23.7M sales rows refreshed on F2. It took 26 minutes there, against 6 minutes on F64.

Sizes marked (DAX) are from a DAX query in the service over `INFO.STORAGETABLECOLUMNSEGMENTS` and the column dictionaries, a different measure from the backup size. On 1M it is above the backup size (93 vs 73 MB), on 10M below it (700 vs 778 MB).

The 1M runs on F64 peaked at 543 to 785 MB with the same rows and parallelism. The spread comes almost entirely from Power Query (270 to 677 MB).

Clearing the model first (`clearValues`, then the full refresh) made no measurable difference on 1M: 545 MB with the 92.7 MB model in memory, 608 MB after clearing. A 93 MB model is small against a spread of more than 200 MB between runs, so this neither shows nor rules out that the old copy counts in the peak; a larger model is needed (v23 on 10M).

The refresh on F2 on 2026-11-11 started with the 10M data still in memory (626 MB). Its command memory limit was therefore 3,066 - 626 = 2,440 MB rather than about 3 GB. The 1M refresh needs far less and went through.

The VertiPaq size in memory was 92.7 MB right after each refresh, the same as DAX Studio on the model in Desktop (97,198,262 bytes). The same model read 66.2 MB a day after its refresh, when the service had reloaded it from storage; the difference is all in the dictionaries.
