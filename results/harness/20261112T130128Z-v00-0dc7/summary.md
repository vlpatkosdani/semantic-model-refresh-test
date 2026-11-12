# Harness run 20261112T130128Z-v00-0dc7

- Task: queries
- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: 6bbfb2927c8f84faaa5079ff221dbf194f7def02
- Notebook run: bdfa9688-7b97-49cd-a411-5622d70c6e20
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T130128Z-v00-0dc7.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 6bbfb29, DataTag read back data-10m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                644.0             726.2                  63.0                  63.0              547.0            14801       0
 p01 cold  seq        5                710.0             891.4                  63.0                  63.0              422.0            16204       0
 p01 warm page        5                751.0             856.6                  16.0                  16.0               16.0             1025       0
 p01 warm  seq        5                542.0             558.4                  16.0                  16.0               16.0             1025       0
 p05 cold page        5               4030.0            4193.6                3737.0                4299.0            18125.0           424570       0
 p05 cold  seq        5               5395.0            6100.0                4050.0                4253.0            18032.0           424574       0
 p05 warm page        5                488.0             517.2                  16.0                  32.0               62.0             1025       0
 p05 warm  seq        5               1268.0            1316.0                  16.0                  32.0               48.0             1025       0
 p10 cold page        5               4106.0            4445.0                3770.0                4766.0            20049.0           424557       0
 p10 cold  seq        5               5671.0            5968.0                3721.0                4111.0            19424.0           424565       0
 p10 warm page        5                594.0            1008.2                  16.0                  64.0               95.0             1025       0
 p10 warm  seq        5               1825.0            1941.2                  16.0                  32.0               79.0             1025       0
 p20 cold page        5              19135.0           20054.8               18545.0               83314.0           102611.0           881432       0
 p20 cold  seq        5              31655.0           32141.0               18151.0               28504.0           124266.0           881386       0
 p20 warm page        5                659.0             680.2                  16.0                  90.0              112.0             1026       0
 p20 warm  seq        5               3751.0            4033.4                  16.0                 101.0              175.0             1026       0
```

## Log

```
2026-11-12T13:04:02Z run 20261112T130128Z-v00-0dc7: variant=v00-baseline data_tag=data-10m-v1 targets=['F64'] expected_commit=6bbfb2927c8f84faaa5079ff221dbf194f7def02
2026-11-12T13:04:12Z F64: workspace already at 6bbfb2927c8f84faaa5079ff221dbf194f7def02
2026-11-12T13:04:14Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-10m-v1
2026-11-12T13:05:02Z F64: page p01 done, 22 queries so far
2026-11-12T13:06:19Z F64: page p05 done, 132 queries so far
2026-11-12T13:08:31Z F64: page p10 done, 352 queries so far
2026-11-12T13:15:26Z F64: page p20 done, 792 queries so far
2026-11-12T13:15:26Z F64: monitoring database Monitoring KQL database
2026-11-12T13:17:33Z F64: 792 of 792 queries found in SemanticModelLogs
```
