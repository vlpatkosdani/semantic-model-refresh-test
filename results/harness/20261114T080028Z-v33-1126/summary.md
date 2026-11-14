# Harness run 20261114T080028Z-v33-1126

- Task: queries
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: fa176557-d2cb-43d5-886d-38c13c3497d8
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261114T080028Z-v33-1126.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                500.0             731.2                 125.0                 195.0              328.0            14484       0
 p20 cold page        5               1372.0            1504.4                 797.0                1563.0             1986.0            56110       0
```

## Log

```
2026-11-14T08:02:36Z run 20261114T080028Z-v33-1126: variant=v33-auto-date-time data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-14T08:02:46Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-14T08:02:49Z F64: v33-auto-date-time is 79c2f30d-ee15-45f7-92a8-73654d03e1a1, DataTag reads back data-1m-v1
2026-11-14T08:03:15Z F64: page p05 done, 25 queries so far
2026-11-14T08:04:10Z F64: page p20 done, 125 queries so far
2026-11-14T08:04:10Z F64: monitoring database Monitoring KQL database
2026-11-14T08:07:16Z F64: 125 of 125 queries found in SemanticModelLogs
```
