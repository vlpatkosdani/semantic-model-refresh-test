# Harness run 20261110T101053Z-v00-edb2

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 325f2600d506c145498e21caff3f23c451fed8d3
- Notebook run: ee70797f-5d48-47de-b7ad-7cdb6a875883
- Pages p01,p05, modes cold, concurrency page, repeats 1, queries from harness/queries/20261110T101053Z-v00-edb2.json

## F64

- 7 queries sent (0 warm-up), 3 failed, 7 found in SemanticModelLogs, 0 throttling retries
- Workspace at 325f260, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        1                552.0             552.0                  16.0                  32.0               32.0             2191       2
 p05 cold page        1                648.0             648.0                 156.0                 204.0              281.0            13847       1
```

Failed queries (first 10):

```
page visual mode conc  rep                                                                                                                         client_error
 p01    v01 cold page    1 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p01    v01 cold page    1 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p05    v01 cold page    1 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
```

## Log

```
2026-11-10T10:11:49Z run 20261110T101053Z-v00-edb2: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=325f2600d506c145498e21caff3f23c451fed8d3
2026-11-10T10:11:56Z F64: workspace already at 325f2600d506c145498e21caff3f23c451fed8d3
2026-11-10T10:11:58Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-10T10:12:14Z F64: page p01 done, 1 queries so far
2026-11-10T10:12:16Z F64: page p05 done, 6 queries so far
2026-11-10T10:14:22Z F64: 7 of 6 queries found in SemanticModelLogs
```

Smoke test of the query runner (before two fixes): the matrix query v01 counted as failed because REST returns one result set, and p01 v01 appears twice because the query had two ExecutionMetrics events. Rows moved here from results/query-*.csv.
