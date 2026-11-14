# Harness run 20261114T082105Z-v00-dd57

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: 10c7f117-eb8c-4e48-ac9c-a5eef1980388
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261114T082105Z-v00-dd57.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                660.0             813.6                 281.0                 378.0              516.0            14463       0
 p20 cold page        5               2098.0            2393.4                1548.0                3065.0             3847.0            56067       0
```

## Log

```
2026-11-14T08:23:19Z run 20261114T082105Z-v00-dd57: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-14T08:23:28Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-14T08:23:32Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-14T08:23:58Z F64: page p05 done, 25 queries so far
2026-11-14T08:24:54Z F64: page p20 done, 125 queries so far
2026-11-14T08:24:54Z F64: monitoring database Monitoring KQL database
2026-11-14T08:28:01Z F64: 125 of 125 queries found in SemanticModelLogs
```
