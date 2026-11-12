# Harness run 20261112T123353Z-v32-4e1f

- Task: queries
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 6bbfb2927c8f84faaa5079ff221dbf194f7def02
- Notebook run: af7ef438-b32d-4ee0-be19-8d542682ace0
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T123353Z-v32-4e1f.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 6bbfb29, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                662.0             692.8                  31.0                  31.0               47.0             3156       0
 p01 cold  seq        5                581.0             692.6                  47.0                  47.0               63.0             3156       0
 p01 warm page        5                586.0             604.8                  16.0                  16.0               16.0             1024       0
 p01 warm  seq        5                526.0             566.2                  16.0                  16.0               16.0             1024       0
 p05 cold page        5                590.0             712.0                 297.0                 437.0              563.0            13880       0
 p05 cold  seq        5               1448.0            1795.4                 266.0                 391.0              501.0            14486       0
 p05 warm page        5                494.0             668.0                  16.0                  32.0               48.0             1024       0
 p05 warm  seq        5               1121.0            1169.2                  16.0                  32.0               48.0             1024       0
 p10 cold page        5                590.0             712.2                 297.0                 579.0              720.0            14158       0
 p10 cold  seq        5               2120.0            2268.0                 250.0                 501.0              642.0            14461       0
 p10 warm page        5                472.0             536.0                  16.0                  48.0              110.0             1024       0
 p10 warm  seq        5               1786.0            1878.8                  16.0                  48.0               78.0             1024       0
 p20 cold page        5               2158.0            2327.4                1516.0                2969.0             3739.0            55855       0
 p20 cold  seq        5               5593.0            5925.4                1439.0                2658.0             3284.0            56769       0
 p20 warm page        5                671.0            1198.0                  16.0                 128.0              253.0             1027       0
 p20 warm  seq        5               3684.0            3861.4                  16.0                  96.0              160.0             1027       0
```

## Log

```
2026-11-12T12:34:36Z run 20261112T123353Z-v32-4e1f: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 targets=['F64'] expected_commit=6bbfb2927c8f84faaa5079ff221dbf194f7def02
2026-11-12T12:34:42Z F64: workspace already at 6bbfb2927c8f84faaa5079ff221dbf194f7def02
2026-11-12T12:34:44Z F64: v32-calc-columns-aggregate is 5c599620-07a4-4f5a-9f50-07e7127ad6ba, DataTag reads back data-1m-v1
2026-11-12T12:35:23Z F64: page p01 done, 22 queries so far
2026-11-12T12:36:21Z F64: page p05 done, 132 queries so far
2026-11-12T12:38:33Z F64: page p10 done, 352 queries so far
2026-11-12T12:42:57Z F64: page p20 done, 792 queries so far
2026-11-12T12:42:57Z F64: monitoring database Monitoring KQL database
2026-11-12T12:45:03Z F64: 792 of 792 queries found in SemanticModelLogs
```
