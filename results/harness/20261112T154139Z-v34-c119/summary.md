# Harness run 20261112T154139Z-v34-c119

- Task: queries
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 4275dc69d71f7fcc804b26b1fb112366af0da4b5
- Notebook run: ba687f5a-b71f-4606-973d-b2404dc581f5
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261112T154139Z-v34-c119.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 4275dc6, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                761.0             794.6                 282.0                 406.0              530.0            14499       0
 p20 cold page        5               2338.0            4696.6                1407.0                2858.0             3299.0            55892       0
```

## Log

```
2026-11-12T15:42:46Z run 20261112T154139Z-v34-c119: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 targets=['F64'] expected_commit=4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T15:42:51Z F64: workspace already at 4275dc69d71f7fcc804b26b1fb112366af0da4b5
2026-11-12T15:42:53Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1
2026-11-12T15:43:15Z F64: page p05 done, 25 queries so far
2026-11-12T15:44:10Z F64: page p20 done, 125 queries so far
2026-11-12T15:44:11Z F64: monitoring database Monitoring KQL database
2026-11-12T15:46:17Z F64: 125 of 125 queries found in SemanticModelLogs
```
