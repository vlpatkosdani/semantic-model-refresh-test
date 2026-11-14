# Harness run 20261113T205029Z-v33-9750

- Task: queries
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: 920d2f92-0a51-477f-af59-55ba8625a724
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T205029Z-v33-9750.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                537.0             798.4                 251.0                 376.0              516.0            14512       0
 p20 cold page        5               2081.0            2187.8                1346.0                2706.0             3519.0            55886       0
```

## Log

```
2026-11-13T20:51:04Z run 20261113T205029Z-v33-9750: variant=v33-auto-date-time data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:51:10Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:51:12Z F64: v33-auto-date-time is 79c2f30d-ee15-45f7-92a8-73654d03e1a1, DataTag reads back data-1m-v1
2026-11-13T20:51:32Z F64: page p05 done, 25 queries so far
2026-11-13T20:52:28Z F64: page p20 done, 125 queries so far
2026-11-13T20:52:28Z F64: monitoring database Monitoring KQL database
2026-11-13T20:53:32Z F64: 125 of 125 queries found in SemanticModelLogs
```
