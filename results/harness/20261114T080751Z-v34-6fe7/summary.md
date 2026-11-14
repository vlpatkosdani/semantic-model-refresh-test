# Harness run 20261114T080751Z-v34-6fe7

- Task: queries
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: da88c5c3-6299-48bd-923c-185d5fdf539b
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261114T080751Z-v34-6fe7.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                569.0             730.2                 266.0                 375.0              484.0            13929       0
 p20 cold page        5               2069.0            3813.4                1251.0                2580.0             3114.0            56132       0
```

## Log

```
2026-11-14T08:08:28Z run 20261114T080751Z-v34-6fe7: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-14T08:08:34Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-14T08:08:38Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1
2026-11-14T08:08:58Z F64: page p05 done, 25 queries so far
2026-11-14T08:09:54Z F64: page p20 done, 125 queries so far
2026-11-14T08:09:55Z F64: monitoring database Monitoring KQL database
2026-11-14T08:13:01Z F64: 125 of 125 queries found in SemanticModelLogs
```
