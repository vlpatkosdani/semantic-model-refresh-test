# Harness run 20261112T142436Z-v00-5975

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: b1660a09614e780473f21788f5ae8523db531ca7
- Notebook run: f9362d60-15b7-43c1-92ac-39a162b46393
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T142436Z-v00-5975.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at b1660a0, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                612.0             670.0                  31.0                  31.0               63.0             2193       0
 p01 cold  seq        5                631.0             957.2                  31.0                  31.0               47.0             2253       0
 p01 warm page        5                605.0             619.2                   0.0                   0.0               31.0             1025       0
 p01 warm  seq        5                550.0             614.6                   0.0                   0.0               16.0             1025       0
 p05 cold page        5                695.0             706.0                 266.0                 360.0              531.0            14428       0
 p05 cold  seq        5               1509.0            1797.4                 250.0                 359.0              454.0            14161       0
 p05 warm page        5                479.0             493.2                  16.0                  16.0               47.0             1025       0
 p05 warm  seq        5               1118.0            1214.2                  16.0                  32.0               63.0             1025       0
 p10 cold page        5                731.0             771.4                 266.0                 500.0              720.0            13847       0
 p10 cold  seq        5               2134.0            2238.0                 250.0                 485.0              610.0            14161       0
 p10 warm page        5                551.0             691.0                  16.0                  96.0               96.0             1025       0
 p10 warm  seq        5               1890.0            1946.4                  16.0                  48.0               95.0             1025       0
 p20 cold page        5               2078.0            2305.8                1424.0                2896.0             3673.0            56052       0
 p20 cold  seq        5               5705.0            5999.2                1393.0                2567.0             3221.0            56052       0
 p20 warm page        5                632.0             894.0                  16.0                 128.0              112.0             1026       0
 p20 warm  seq        5               3572.0            3954.8                  16.0                  80.0              174.0             1026       0
```

## Log

```
2026-11-12T14:26:54Z run 20261112T142436Z-v00-5975: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T14:27:02Z F64: workspace already at b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T14:27:04Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-12T14:27:49Z F64: page p01 done, 22 queries so far
2026-11-12T14:28:45Z F64: page p05 done, 132 queries so far
2026-11-12T14:30:57Z F64: page p10 done, 352 queries so far
2026-11-12T14:35:21Z F64: page p20 done, 792 queries so far
2026-11-12T14:35:21Z F64: monitoring database Monitoring KQL database
2026-11-12T14:37:28Z F64: 792 of 792 queries found in SemanticModelLogs
```
