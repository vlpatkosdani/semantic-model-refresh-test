# Harness run 20261110T194546Z-v00-cdd8

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: b2070490d6cdd6d46f96e9292bc1688abcf54fcb
- Notebook run: bbf203f6-e874-4f6c-b255-a7318dfb4e25
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T194546Z-v00-cdd8.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at b207049, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                550.0             592.8                  16.0                  16.0               31.0             4252       0
 p01 cold  seq        5                480.0             495.6                  16.0                  16.0               16.0             3237       0
 p01 warm page        5                524.0             561.8                   0.0                   0.0                0.0             1025       0
 p01 warm  seq        5                456.0             520.4                  16.0                  16.0               16.0             1025       0
 p05 cold page        5                536.0             581.8                 125.0                 189.0              313.0            14428       0
 p05 cold  seq        5               1067.0            1233.8                 125.0                 172.0              282.0            14161       0
 p05 warm page        5                424.0             434.4                   0.0                   0.0               16.0             1025       0
 p05 warm  seq        5                928.0             966.8                   0.0                   0.0               16.0             1025       0
 p10 cold page        5                522.0            1607.4                 156.0                 307.0              455.0            14428       0
 p10 cold  seq        5               1721.0            2014.6                 125.0                 230.0              361.0            14161       0
 p10 warm page        5                366.0             498.0                  16.0                  16.0               64.0             1025       0
 p10 warm  seq        5               1565.0            1602.0                  16.0                  44.0               48.0             1025       0
 p20 cold page        5               1267.0            1444.4                 719.0                1471.0             1890.0            59070       0
 p20 cold  seq        5               3984.0            4411.4                 688.0                1195.0             1737.0            56745       0
 p20 warm page        5                557.0             657.0                  16.0                  96.0              143.0             1026       0
 p20 warm  seq        5               3122.0            3153.6                  16.0                  48.0               94.0             1026       0
```

## Log

```
2026-11-10T19:46:46Z run 20261110T194546Z-v00-cdd8: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=b2070490d6cdd6d46f96e9292bc1688abcf54fcb
2026-11-10T19:46:55Z F64: workspace already at b2070490d6cdd6d46f96e9292bc1688abcf54fcb
2026-11-10T19:46:57Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-10T19:47:33Z F64: page p01 done, 22 queries so far
2026-11-10T19:48:28Z F64: page p05 done, 132 queries so far
2026-11-10T19:50:40Z F64: page p10 done, 352 queries so far
2026-11-10T19:55:05Z F64: page p20 done, 792 queries so far
2026-11-10T19:57:10Z F64: 792 of 792 queries found in SemanticModelLogs
```
