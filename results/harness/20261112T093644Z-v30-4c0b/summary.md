# Harness run 20261112T093644Z-v30-4c0b

- Task: queries
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: b4282c6b-4a78-4261-9c44-098035fee1cf
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T093644Z-v30-4c0b.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 5c382cc, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                531.0             641.4                  16.0                  16.0               16.0             4218       0
 p01 cold  seq        5                468.0             552.6                  16.0                  16.0               31.0             4444       0
 p01 warm page        5                538.0             563.0                   0.0                   0.0                0.0             1025       0
 p01 warm  seq        5                503.0             531.0                   0.0                   0.0                0.0             1025       0
 p05 cold page        5                384.0             600.2                 141.0                 219.0              298.0            14163       0
 p05 cold  seq        5               1189.0            1599.8                 156.0                 189.0              312.0            14454       0
 p05 warm page        5                462.0             525.6                  16.0                  16.0               48.0             1025       0
 p05 warm  seq        5               1028.0            1207.4                  16.0                  16.0               32.0             1025       0
 p10 cold page        5                636.0             649.2                 141.0                 252.0              423.0            14427       0
 p10 cold  seq        5               1800.0            1983.8                 141.0                 268.0              375.0            13849       0
 p10 warm page        5                466.0             548.2                   0.0                   0.0               31.0             1025       0
 p10 warm  seq        5               1717.0            1969.2                  16.0                  16.0               16.0             1025       0
 p20 cold page        5               1230.0            1405.4                 657.0                1502.0             1955.0            59070       0
 p20 cold  seq        5               4169.0            4275.6                 641.0                1213.0             1784.0            56745       0
 p20 warm page        5                601.0             767.6                  16.0                  62.0               95.0             1026       0
 p20 warm  seq        5               3302.0            3395.8                  16.0                  48.0              110.0             1026       0
```

## Log

```
2026-11-12T09:39:00Z run 20261112T093644Z-v30-4c0b: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T09:39:10Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T09:39:12Z F64: v30-double-instead-of-fixed is 82a0b18f-7fcc-4d91-84c8-ad3d394d13f0, DataTag reads back data-1m-v1
2026-11-12T09:39:55Z F64: page p01 done, 22 queries so far
2026-11-12T09:40:51Z F64: page p05 done, 132 queries so far
2026-11-12T09:43:03Z F64: page p10 done, 352 queries so far
2026-11-12T09:47:27Z F64: page p20 done, 792 queries so far
2026-11-12T09:47:27Z F64: monitoring database Monitoring KQL database
2026-11-12T09:49:34Z F64: 792 of 792 queries found in SemanticModelLogs
```
