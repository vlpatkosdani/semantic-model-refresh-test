# Harness run 20261113T204543Z-v00-0b01

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: 3a46b64a-5c6b-40c7-ba9c-e451fdff2a45
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T204543Z-v00-0b01.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                552.0             591.2                 250.0                 361.0              485.0            14169       0
 p20 cold page        5               1875.0            2039.6                1283.0                2563.0             3140.0            55844       0
```

## Log

```
2026-11-13T20:46:20Z run 20261113T204543Z-v00-0b01: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:46:26Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:46:28Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-13T20:46:49Z F64: page p05 done, 25 queries so far
2026-11-13T20:47:44Z F64: page p20 done, 125 queries so far
2026-11-13T20:47:45Z F64: monitoring database Monitoring KQL database
2026-11-13T20:49:50Z F64: 125 of 125 queries found in SemanticModelLogs
```
