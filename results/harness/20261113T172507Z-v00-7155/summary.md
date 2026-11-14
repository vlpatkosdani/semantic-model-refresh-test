# Harness run 20261113T172507Z-v00-7155

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: cf297160-3c8f-450e-909d-d01a070a4b52
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T172507Z-v00-7155.json

## F64

- 125 queries sent (0 warm-up), 0 failed, 125 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                625.0             848.0                 234.0                 358.0              470.0            14463       0
 p20 cold page        5               1856.0            2008.0                1298.0                2676.0             3566.0            56067       0
```

## Log

```
2026-11-13T17:25:46Z run 20261113T172507Z-v00-7155: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T17:25:52Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T17:25:54Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-13T17:26:15Z F64: page p05 done, 25 queries so far
2026-11-13T17:27:10Z F64: page p20 done, 125 queries so far
2026-11-13T17:27:10Z F64: monitoring database Monitoring KQL database
2026-11-13T17:30:17Z F64: 125 of 125 queries found in SemanticModelLogs
```
