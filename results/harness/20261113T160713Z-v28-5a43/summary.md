# Harness run 20261113T160713Z-v28-5a43

- Task: queries
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: 85988033-6ab7-4860-a99e-adb1609af75a
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T160713Z-v28-5a43.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                588.0             676.2                 125.0                 189.0              266.0            14096       0
 p20 cold page        5               1102.0            1275.4                 563.0                1281.0             1813.0            28546       0
```

## Log

```
2026-11-13T16:09:22Z run 20261113T160713Z-v28-5a43: variant=v28-types-all-text data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T16:09:32Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T16:09:34Z F64: v28-types-all-text is bc793114-53e1-4476-8e50-c4b0c5b15603, DataTag reads back data-1m-v1
2026-11-13T16:10:02Z F64: page p05 done, 25 queries so far
2026-11-13T16:10:56Z F64: page p20 done, 125 queries so far
2026-11-13T16:10:56Z F64: monitoring database Monitoring KQL database
2026-11-13T16:13:01Z F64: 125 of 125 queries found in SemanticModelLogs
```
