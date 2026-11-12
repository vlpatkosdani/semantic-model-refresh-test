# Harness run 20261112T092209Z-v29-a76d

- Task: queries
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 8a56d9c8-9002-42e9-b7f4-456906de61c4
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T092209Z-v29-a76d.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 5c382cc, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                594.0             682.8                  16.0                  16.0               31.0             4252       0
 p01 cold  seq        5                484.0             663.6                  16.0                  16.0               31.0             4252       0
 p01 warm page        5                575.0             667.2                   0.0                   0.0                0.0             1025       0
 p01 warm  seq        5                476.0             490.6                   0.0                   0.0                0.0             1025       0
 p05 cold page        5                539.0             655.6                 141.0                 205.0              297.0            14401       0
 p05 cold  seq        5               1198.0            1339.4                 125.0                 172.0              344.0            14384       0
 p05 warm page        5                432.0            1143.8                  16.0                  16.0               31.0             1025       0
 p05 warm  seq        5                978.0            1054.4                  16.0                  16.0               16.0             1025       0
 p10 cold page        5                572.0            1241.4                 125.0                 267.0              407.0            14384       0
 p10 cold  seq        5               1930.0            2311.0                 141.0                 262.0              437.0            14083       0
 p10 warm page        5                442.0             854.2                  16.0                  32.0               78.0             1025       0
 p10 warm  seq        5               1653.0            1688.8                   0.0                   0.0               62.0             1025       0
 p20 cold page        5               1070.0            1255.6                 594.0                1317.0             1737.0            28527       0
 p20 cold  seq        5               4020.0            4162.4                 547.0                1067.0             1658.0            28530       0
 p20 warm page        5                616.0             671.0                  16.0                  64.0              112.0             1026       0
 p20 warm  seq        5               3362.0            4012.8                  16.0                  32.0               64.0             1026       0
```

## Log

```
2026-11-12T09:24:52Z run 20261112T092209Z-v29-a76d: variant=v29-keys-as-text data_tag=data-1m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T09:25:04Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T09:25:06Z F64: v29-keys-as-text is 8a2beb05-98b9-4e44-92de-799777abce23, DataTag reads back data-1m-v1
2026-11-12T09:25:54Z F64: page p01 done, 22 queries so far
2026-11-12T09:26:50Z F64: page p05 done, 132 queries so far
2026-11-12T09:29:02Z F64: page p10 done, 352 queries so far
2026-11-12T09:33:26Z F64: page p20 done, 792 queries so far
2026-11-12T09:33:26Z F64: monitoring database Monitoring KQL database
2026-11-12T09:35:33Z F64: 792 of 792 queries found in SemanticModelLogs
```
