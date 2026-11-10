# Harness run 20261110T132552Z-v23-ac2c

- Task: queries
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: ee5050bd97225153e7d3e555e414d49995893af6
- Notebook run: 3ba763f1-e74c-4eaa-bf2c-4860f42e5286
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T132552Z-v23-ac2c.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at ee5050b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                606.0             625.0                  16.0                  16.0               31.0             4170       0
 p01 cold  seq        5                557.0             773.0                  16.0                  16.0               31.0             4170       0
 p01 warm page        5                594.0             979.8                   0.0                   0.0                0.0             1031       0
 p01 warm  seq        5                502.0             531.2                   0.0                   0.0                0.0             1031       0
 p05 cold page        5                457.0            2048.4                 125.0                 173.0              327.0            14208       0
 p05 cold  seq        5               1274.0            1589.2                 125.0                 188.0              251.0            14474       0
 p05 warm page        5                575.0             695.2                  16.0                  32.0               32.0             1031       0
 p05 warm  seq        5               1121.0            1196.2                   0.0                   0.0                0.0             1031       0
 p10 cold page        5                738.0            4431.8                 141.0                 252.0              422.0            14501       0
 p10 cold  seq        5               2057.0            2266.8                 125.0                 252.0              453.0            14474       0
 p10 warm page        5                539.0             640.0                  16.0                  48.0               48.0             1031       0
 p10 warm  seq        5               1766.0            1851.2                  16.0                  48.0               48.0             1031       0
 p20 cold page        5               1343.0            1467.6                 672.0                1470.0             2001.0            59116       0
 p20 cold  seq        5               4734.0            4992.8                 719.0                1475.0             2063.0            59116       0
 p20 warm page        5                662.0            2457.6                  16.0                  64.0              142.0             1039       0
 p20 warm  seq        5               3475.0            3769.4                  16.0                  79.0              127.0             1039       0
```

## Log

```
2026-11-10T13:28:18Z run 20261110T132552Z-v23-ac2c: variant=v23-dax-calc-tables data_tag=data-1m-v1 targets=['F64'] expected_commit=ee5050bd97225153e7d3e555e414d49995893af6
2026-11-10T13:28:27Z F64: workspace already at ee5050bd97225153e7d3e555e414d49995893af6
2026-11-10T13:28:29Z F64: v23-dax-calc-tables is c0fbb6a6-e33c-4f6b-809e-9fc48ad57573, DataTag reads back data-1m-v1
2026-11-10T13:29:21Z F64: page p01 done, 22 queries so far
2026-11-10T13:30:21Z F64: page p05 done, 132 queries so far
2026-11-10T13:32:34Z F64: page p10 done, 352 queries so far
2026-11-10T13:36:58Z F64: page p20 done, 792 queries so far
2026-11-10T13:38:03Z F64: 792 of 792 queries found in SemanticModelLogs
```
