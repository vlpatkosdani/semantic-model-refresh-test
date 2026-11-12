# Harness run 20261112T152844Z-v00-eda9

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 4275dc69d71f7fcc804b26b1fb112366af0da4b5
- Notebook run: 079f293e-cd92-4ef6-abcc-8e6a588d9327
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261112T152844Z-v00-eda9.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 4275dc6, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                520.0             732.0                 281.0                 389.0              516.0            14452       0
 p20 cold page        5               2111.0            2328.6                1563.0                2956.0             3535.0            56052       0
```

## Log

```
2026-11-12T15:29:28Z run 20261112T152844Z-v00-eda9: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T15:29:33Z F64: workspace already at 4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T15:29:37Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-12T15:29:59Z F64: page p05 done, 25 queries so far
2026-11-12T15:30:54Z F64: page p20 done, 125 queries so far
2026-11-12T15:30:54Z F64: monitoring database Monitoring KQL database
2026-11-12T15:34:01Z F64: 125 of 125 queries found in SemanticModelLogs
```
