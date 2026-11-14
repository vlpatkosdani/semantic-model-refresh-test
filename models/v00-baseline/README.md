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
| F64 | 10M | refreshed (2026-11-12, harness, 66.2 MB in memory before) | 1,979 | 1,391 | 10 min | 778 MB |
| F2 | 10M | refreshed (2026-11-12, harness, 66.2 MB in memory before) | | | 12 min | 700 MB (DAX) |

Model size is the backup size in the refresh log, in MB of 1,048,576 bytes. On 1M the model is 73 MB, a bit above the 40 to 60 MB expected. On 10M the peak stays below the 3 GB limit of F2 (2,040 and 2,116 MB in two runs), and the harness run on 2026-11-10 confirmed it: the clean star schema with 23.7M sales rows refreshed on F2. It took 26 minutes there, against 6 minutes on F64.

Sizes marked (DAX) are from a DAX query in the service over `INFO.STORAGETABLECOLUMNSEGMENTS` and the column dictionaries, a different measure from the backup size. On 1M it is above the backup size (93 vs 73 MB), on 10M below it (700 vs 778 MB).

The 1M runs on F64 peaked at 543 to 785 MB with the same rows and parallelism. The spread comes almost entirely from Power Query (270 to 677 MB).

Clearing the model first (`clearValues`, then the full refresh) made no measurable difference on 1M: 545 MB with the 92.7 MB model in memory, 608 MB after clearing. A 93 MB model is small against a spread of more than 200 MB between runs, so this neither shows nor rules out that the old copy counts in the peak; a larger model is needed (v23 on 10M).

The refresh on F2 on 2026-11-11 started with the 10M data still in memory (626 MB). Its command memory limit was therefore 3,066 - 626 = 2,440 MB rather than about 3 GB. The 1M refresh needs far less and went through.

The VertiPaq size in memory was 92.7 MB right after each refresh, the same as DAX Studio on the model in Desktop (97,198,262 bytes). The same model read 66.2 MB a day after its refresh, when the service had reloaded it from storage; the difference is all in the dictionaries.

### Queries on 10M, 2026-11-12

The query workload on 10M, to see how much memory a single query needs and whether the heaviest one fits under the 1,024 MB per-query limit of F2.

F64, run `20261112T130128Z-v00-0dc7`, all 792 queries succeeded. Medians over 5 repeats, cold cache, all visuals of the page at once, against the 1M runs:

| Page | Slowest visual 1M | Slowest visual 10M | CPU 1M | CPU 10M | Peak per query 1M | Peak per query 10M |
|---|---|---|---|---|---|---|
| p01 | 16 to 31 ms | 63 ms | 31 ms | 547 ms | 4 MB | 14 MB |
| p05 | 125 to 141 ms | 3,737 ms | 313 to 328 ms | 18,125 ms | 14 MB | 415 MB |
| p20 | 672 to 719 ms | 18,545 ms | 1,890 to 2,172 ms | 102,611 ms | 58 MB | 861 MB |

Ten times the rows makes the slowest visual on p05 and p20 about 26 times slower and their CPU about 50 times higher. The heaviest single queries on p20:

| Visual | Type | Peak per query | Slowest run | CPU |
|---|---|---|---|---|
| v20 | matrix | 861 MB | 18,545 ms | 69,953 ms |
| v18 | table | 413 MB | 5,864 ms | 11,766 ms |
| v05 | table | 411 MB | 3,955 ms | 9,578 ms |
| v14 | bar chart | 108 MB | 2,300 ms | 7,281 ms |

The matrix v20 needs 861 MB, under the 1,024 MB per query of F2 but close to it.

F2, run `20261112T133725Z-v00-4050`, pages p05 and p20, cold cache, all visuals at once, 3 repeats. F2 has no workspace monitoring, so these are times at the client from the REST API (`executeQueries`) only, with no server time, CPU or memory. 66 of 75 queries succeeded and none failed on memory. The page p20 took 22.3 s (median), against 19.1 s on F64; the matrix v20 was the slowest visual at 22.2 s.

The 9 failures are the visuals v01 on p05 and p20 and v20 on p20, with `DaxResultsetCountNotSupported`: the REST API returns one result set, and these visuals return more than one. The same 9 failed on 1M. v20 ran for about 22 s on F2 before the error came back, which suggested the query completed within the memory limit, but the API does not show that. The XMLA runs below confirm it.


### Query control run, F64, 1M, 2026-11-12

Run `20261112T142436Z-v00-5975`, all 792 queries succeeded. p20 cold, all visuals at once: slowest visual 1,424 ms, CPU 3,673 ms, peak per query 55 MB. The three runs on 2026-11-10 gave 672 to 719 ms and CPU 1,890 to 2,172 ms. The model and the queries are the same. Later runs (2026-11-13 and 14) showed that this is a state of the model on the service, fast or slow, about two times apart, lasting for hours and changing by itself, and not the capacity as a whole: two models a few minutes apart were in different states. The peak per query did not change. See `docs/lab-findings-queries.md`, finding 7, for all 12 runs.

### Heaviest queries through XMLA, 10M, F64 and F2, 2026-11-13

The three heaviest p20 visuals sent through XMLA (harness task `xmla`), one at a time, cold cache, 3 repeats each, with an XMLA trace for server time, CPU and peak memory. F64 run `20261113T084411Z-v00-4f8b`, F2 run `20261113T090703Z-v00-4b85`. All 18 queries succeeded.

| Visual | F64 server time | F64 CPU | F2 server time | F2 CPU | Peak per query (both) |
|---|---|---|---|---|---|
| v20 matrix | 9.0 to 14.3 s | 46.6 to 49.8 s | 19.1 to 24.8 s | 72.9 to 74.8 s | 855 to 860 MB |
| v18 table | 1.9 s | 9.9 to 10.7 s | 3.7 to 3.9 s | 15.8 to 17.2 s | 413 MB |
| v05 table | 1.9 to 2.0 s | 10.4 to 10.9 s | 3.7 to 4.1 s | 17.0 to 17.9 s | 413 to 415 MB |

The matrix v20 fits on F2: it needs about 860 MB against the 1,024 MB per-query limit, 84 % of it. A query needs the same memory on both capacities; F2 takes about twice the time and 1.5 times the CPU. On F64 the trace gave the same peak as the workspace logs for the same query a day earlier (861 MB).

For v20's second and third runs on F2 the client waited 60 to 65 s while the engine reported 20 to 25 s. The Capacity Metrics app shows why: F2 went into the overloaded state with interactive delay at 09:11 UTC, after the first v20 run and before the second, and stayed there for 47 minutes. The service delays interactive queries while a capacity is overloaded (`docs/lab-findings-queries.md`, finding 8).

