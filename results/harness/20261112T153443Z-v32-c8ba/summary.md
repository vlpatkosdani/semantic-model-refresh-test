# Harness run 20261112T153443Z-v32-c8ba

- Task: queries
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 4275dc69d71f7fcc804b26b1fb112366af0da4b5
- Notebook run: 7e3ca4d5-a082-40f9-963c-bbd791077c48
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261112T153443Z-v32-c8ba.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 4275dc6, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                619.0             811.8                 281.0                 416.0              516.0            14489       0
 p20 cold page        5               2174.0            2396.0                1580.0                3175.0             3831.0            56769       0
```

## Log

```
2026-11-12T15:36:51Z run 20261112T153443Z-v32-c8ba: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 targets=['F64'] expected_commit=4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T15:37:01Z F64: workspace already at 4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T15:37:03Z F64: v32-calc-columns-aggregate is 5c599620-07a4-4f5a-9f50-07e7127ad6ba, DataTag reads back data-1m-v1
2026-11-12T15:37:32Z F64: page p05 done, 25 queries so far
2026-11-12T15:38:28Z F64: page p20 done, 125 queries so far
2026-11-12T15:38:28Z F64: monitoring database Monitoring KQL database
2026-11-12T15:40:33Z F64: 125 of 125 queries found in SemanticModelLogs
```
