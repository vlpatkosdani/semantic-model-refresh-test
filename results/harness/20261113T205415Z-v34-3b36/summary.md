# Harness run 20261113T205415Z-v34-3b36

- Task: queries
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: 214ec627-e3d8-4645-baef-8c691afbe444
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T205415Z-v34-3b36.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                478.0             685.0                 125.0                 188.0              297.0            14243       0
 p20 cold page        5               1230.0            1333.0                 703.0                1407.0             2031.0            59150       0
```

## Log

```
2026-11-13T20:54:38Z run 20261113T205415Z-v34-3b36: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:54:44Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:54:46Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1
2026-11-13T20:55:05Z F64: page p05 done, 25 queries so far
2026-11-13T20:56:00Z F64: page p20 done, 125 queries so far
2026-11-13T20:56:00Z F64: monitoring database Monitoring KQL database
2026-11-13T20:58:06Z F64: 125 of 125 queries found in SemanticModelLogs
```
