# Harness run 20261113T185531Z-v22-9ed9

- Task: queries
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: 6be22537-bcd9-46bd-9018-9819c4545d27
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T185531Z-v22-9ed9.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                486.0             734.0                 156.0                 220.0              283.0            13864       0
 p20 cold page        5               1335.0            1533.6                 813.0                1566.0             1985.0            56075       0
```

## Log

```
2026-11-13T18:56:10Z run 20261113T185531Z-v22-9ed9: variant=v22-dax-calc-columns data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T18:56:17Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T18:56:19Z F64: v22-dax-calc-columns is 683e80a5-7d57-493c-a708-3a0b8ce5350c, DataTag reads back data-1m-v1
2026-11-13T18:56:39Z F64: page p05 done, 25 queries so far
2026-11-13T18:57:34Z F64: page p20 done, 125 queries so far
2026-11-13T18:57:34Z F64: monitoring database Monitoring KQL database
2026-11-13T18:59:40Z F64: 125 of 125 queries found in SemanticModelLogs
```
