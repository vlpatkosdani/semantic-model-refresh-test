# Harness run 20261113T190713Z-v22-8902

- Task: queries
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: aff53178-75a5-499b-b1df-ae537b65a3a5
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T190713Z-v22-8902.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                421.0             467.8                 156.0                 235.0              343.0            14178       0
 p20 cold page        5               1341.0            1468.4                 828.0                1705.0             2142.0            56075       0
```

## Log

```
2026-11-13T19:07:54Z run 20261113T190713Z-v22-8902: variant=v22-dax-calc-columns data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T19:07:59Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T19:08:01Z F64: v22-dax-calc-columns is 683e80a5-7d57-493c-a708-3a0b8ce5350c, DataTag reads back data-1m-v1
2026-11-13T19:08:20Z F64: page p05 done, 25 queries so far
2026-11-13T19:09:16Z F64: page p20 done, 125 queries so far
2026-11-13T19:09:16Z F64: monitoring database Monitoring KQL database
2026-11-13T19:11:21Z F64: 125 of 125 queries found in SemanticModelLogs
```
