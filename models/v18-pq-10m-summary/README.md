# v18-pq-10m-summary

The baseline plus one small table that is aggregated in Power Query from a much larger source.

## What changed vs baseline

- New not-loaded query `stg Sales 10M`: reads the full `sales.parquet` of the 10M release (23.5M rows, 443 MB file) and keeps four columns.
- New loaded table `Store Year Summary`: a Group By of `stg Sales 10M` by store and year. Roughly 740 rows.
- New parameter `SummaryDataTag` (default `data-10m-v1`) picks the release for this query only. The star schema still loads `DataTag` (1M by default).
- `fnLoadParquet` takes an optional second argument for the release tag. The base URL is still the static literal.

## Hypothesis

A common belief is that only what you load costs memory: "the query isn't loaded and the table has 740 rows, so it is cheap". But the source is not foldable, so Power Query has to download the whole file, decode it and group every row during the refresh.

The v99 diagnostic runs suggest that Power Query memory counts against the semantic model's memory limit: both 25 GB failures were cancelled as "Data source error" while data was still being read. This variant tests that with a realistic pattern instead of `Table.Buffer`.

## Expected effect

- Model size: same as baseline. The new table adds a few KB.
- Peak refresh memory: if Power Query memory counts, well above baseline (the 443 MB file is held in memory by `Binary.Buffer`, plus the grouping). If it does not count, about the same as baseline.
- Duration and CU: clearly higher than baseline, mostly download and Power Query CPU.

## How to read the result

- Compare `approximatePeakMemConsumptionKB` and `mEnginePeakMemoryKB` with the baseline run.
- If it fails on F2 while the baseline refreshes there, a table of 740 rows is enough to push a model off the smallest capacity.
- Setting `SummaryDataTag` to `data-1m-v1` gives the same model on a 10 times smaller source, which shows how the cost scales.
