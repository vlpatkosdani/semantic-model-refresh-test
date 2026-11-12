# Harness run 20261112T095010Z-v31-c5bc

- Task: queries
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 89c00e96-b1da-46f7-9a46-4159ccc54bee
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T095010Z-v31-c5bc.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 5c382cc, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                604.0             608.2                  16.0                  16.0               16.0             4287       0
 p01 cold  seq        5                552.0             656.0                  16.0                  16.0               31.0             4287       0
 p01 warm page        5                535.0             618.0                   0.0                   0.0                0.0             1026       0
 p01 warm  seq        5                538.0             687.8                   0.0                   0.0                0.0             1026       0
 p05 cold page        5                460.0             594.8                 125.0                 179.0              282.0            14464       0
 p05 cold  seq        5               1213.0            1442.8                 125.0                 189.0              280.0            14464       0
 p05 warm page        5                375.0             501.2                  16.0                  16.0               16.0             1026       0
 p05 warm  seq        5               1017.0            1119.0                  16.0                  16.0               16.0             1026       0
 p10 cold page        5                609.0             677.4                 157.0                 335.0              454.0            14488       0
 p10 cold  seq        5               1914.0            2305.2                 125.0                 252.0              391.0            14464       0
 p10 warm page        5                404.0             494.2                  16.0                  32.0               48.0             1026       0
 p10 warm  seq        5               1740.0            2210.6                  16.0                  16.0               32.0             1026       0
 p20 cold page        5               1256.0            1382.2                 703.0                1456.0             1926.0            59097       0
 p20 cold  seq        5               4496.0            4821.6                 656.0                1285.0             1969.0            56769       0
 p20 warm page        5                711.0             747.0                  16.0                  34.0              110.0             1029       0
 p20 warm  seq        5               3454.0            4214.4                  16.0                  96.0              112.0             1029       0
```

## Log

```
2026-11-12T09:52:34Z run 20261112T095010Z-v31-c5bc: variant=v31-calc-columns-row data_tag=data-1m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T09:52:42Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T09:52:44Z F64: v31-calc-columns-row is 3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18, DataTag reads back data-1m-v1
2026-11-12T09:53:32Z F64: page p01 done, 22 queries so far
2026-11-12T09:54:28Z F64: page p05 done, 132 queries so far
2026-11-12T09:56:40Z F64: page p10 done, 352 queries so far
2026-11-12T10:01:05Z F64: page p20 done, 792 queries so far
2026-11-12T10:01:05Z F64: monitoring database Monitoring KQL database
2026-11-12T10:04:14Z F64: 792 of 792 queries found in SemanticModelLogs
```
