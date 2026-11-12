# Harness run 20261112T145014Z-v32-e5da

- Task: queries
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 4275dc69d71f7fcc804b26b1fb112366af0da4b5
- Notebook run: 7225b9ba-f560-430c-8384-332b9b7757f5
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261112T145014Z-v32-e5da.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 4275dc6, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                541.0             737.6                 282.0                 407.0              547.0            14489       0
 p20 cold page        5               2025.0            2109.2                1454.0                2876.0             3643.0            55855       0
```

## Log

```
2026-11-12T14:52:42Z run 20261112T145014Z-v32-e5da: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 targets=['F64'] expected_commit=4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T14:52:52Z F64: workspace already at 4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T14:52:57Z F64: v32-calc-columns-aggregate is 5c599620-07a4-4f5a-9f50-07e7127ad6ba, DataTag reads back data-1m-v1
2026-11-12T14:53:26Z F64: page p05 done, 25 queries so far
2026-11-12T14:54:22Z F64: page p20 done, 125 queries so far
2026-11-12T14:54:22Z F64: monitoring database Monitoring KQL database
2026-11-12T14:56:28Z F64: 125 of 125 queries found in SemanticModelLogs
```
