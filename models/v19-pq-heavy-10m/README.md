# v19-pq-heavy-10m

The baseline plus five analytical Power Query reports built on the 10M data. Each report loads only a small result table. Nothing is buffered.

## What changed vs baseline

- `fnLoadParquet` takes an optional release tag and has no `Binary.Buffer`. No query in this variant uses `Table.Buffer` or `Binary.Buffer`.
- Not-loaded source queries `src Sales Heavy`, `src Customer Heavy`, `src Product Heavy`, `src Orders Heavy` and `src OrderRows Heavy` read the 10M files.
- Five loaded tables, each one a typical analysis that someone might build in Power Query instead of in the model:

| Table | What Power Query does (10M data) | Rows loaded |
|---|---|---|
| `PQ Customer Segments` | merges 23.5M sales lines with all customers, groups by country, gender, age band and year with distinct counts | about 1,300 |
| `PQ Customer RFM` | groups 23.5M lines by customer, ranks all customers three times, scores them into quintiles, groups by segment | up to 125 |
| `PQ Top Products by Year` | groups by year and product, sorts each year, keeps the top 10 | 110 |
| `PQ Delivery Days` | joins 23.5M order lines with 9.8M order headers, groups by store and delivery days | about 1,000 |
| `PQ Basket Pairs` | joins order lines to themselves on the order number (about 78M intermediate rows), groups by subcategory pair | up to 1,024 |

The star schema still loads the 1M data, so the model stays the size of the baseline plus a few thousand rows.

## Hypothesis

The diagnostic runs on v99 showed that Power Query work can push a refresh past the memory limit even when it loads nothing large. Those runs used `Table.Buffer`. This variant tests the same thing with ordinary operations that cannot fold on a file source: merges, Group By with distinct counts, ranking, sorting and a self-join. None of them is unusual on its own, but each has to hold large intermediate results in memory.

## Design target

Fail on F2, F4 and F8. Whether it also fails on F64 is open.

## Knobs

| Parameter | Default | Effect |
|---|---|---|
| `HeavyDataTag` | `data-10m-v1` | Release for the first four reports. `data-1m-v1` makes them 10 times smaller. |
| `BasketDataTag` | `data-10m-v1` | Release for `PQ Basket Pairs`, the heaviest single query. `data-1m-v1` drops the self-join from about 78M to 7.8M rows. |

Removing a report table also removes its cost, since the source queries are only evaluated through the reports.

## Expected effect

- Model size: same as baseline.
- Peak refresh memory: well above baseline. I don't give a number this time, my estimates for Power Query memory have been unreliable. Compare `approximatePeakMemConsumptionKB` and `mEnginePeakMemoryKB` with the baseline.
- Duration and CU: much higher than baseline. Each report reads the 10M files again, so the 443 MB Sales file is downloaded and decoded several times. Without `Binary.Buffer` the engine may also download a file more than once within one query.

## Practical notes

- Refreshing in Desktop downloads more than 1 GB several times over and can take a long time. If you only want to publish, set both tags to `data-1m-v1` in Desktop, apply, publish, then set them back to `data-10m-v1` in the semantic model settings in the service.
- If the refresh is very slow even on F64, `Binary.Buffer` in `fnLoadParquet` is the first thing to put back.

## Results

| Capacity | Data | Result | Peak memory | Duration | CU |
|---|---|---|---|---|---|
| F64 | star 1M, reports 10M | refreshed | not read yet | not read yet | not read yet |
| F2 | star 1M, reports 10M | failed, cancelled at 3,242 MB (limit 3,067 MB, database size before command 4 MB) | | | |
| Pro | star 1M, reports 10M | not run yet | | | |
