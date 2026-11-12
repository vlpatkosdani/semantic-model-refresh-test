# Harness run 20261112T144321Z-v00-7624

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 4275dc69d71f7fcc804b26b1fb112366af0da4b5
- Notebook run: 0d5385a3-f282-41a3-b469-a57f4e2e86d5
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261112T144321Z-v00-7624.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 4275dc6, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                516.0             598.8                 266.0                 375.0              515.0            14452       0
 p20 cold page        5               2344.0            2441.6                1516.0                2971.0             3736.0            55828       0
```

## Log

```
2026-11-12T14:45:32Z run 20261112T144321Z-v00-7624: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T14:45:41Z F64: workspace already at 4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T14:45:43Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-12T14:46:12Z F64: page p05 done, 25 queries so far
2026-11-12T14:47:07Z F64: page p20 done, 125 queries so far
2026-11-12T14:47:07Z F64: monitoring database Monitoring KQL database
2026-11-12T14:49:13Z F64: 125 of 125 queries found in SemanticModelLogs
```
