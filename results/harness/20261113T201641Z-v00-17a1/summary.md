# Harness run 20261113T201641Z-v00-17a1

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: c1699d19-f033-4a1b-8aa6-6f8ddd02f197
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T201641Z-v00-17a1.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                756.0            1129.8                 250.0                 359.0              484.0            14461       0
 p20 cold page        5               1986.0            2134.8                1393.0                2803.0             3550.0            56761       0
```

## Log

```
2026-11-13T20:17:16Z run 20261113T201641Z-v00-17a1: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:17:23Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:17:25Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-13T20:17:47Z F64: page p05 done, 25 queries so far
2026-11-13T20:18:41Z F64: page p20 done, 125 queries so far
2026-11-13T20:18:41Z F64: monitoring database Monitoring KQL database
2026-11-13T20:20:47Z F64: 125 of 125 queries found in SemanticModelLogs
```
