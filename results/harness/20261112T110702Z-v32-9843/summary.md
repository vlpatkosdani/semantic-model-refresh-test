# Harness run 20261112T110702Z-v32-9843

- Task: queries
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 9e79132d-b797-44cd-8857-329e0514953f
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T110702Z-v32-9843.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 5c382cc, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                657.0             675.4                  36.0                  36.0               63.0             4285       0
 p01 cold  seq        5                562.0             780.8                  31.0                  31.0               31.0             4285       0
 p01 warm page        5                588.0             635.6                   3.0                   3.0               16.0             1024       0
 p01 warm  seq        5                572.0             595.4                   7.0                   7.0               16.0             1024       0
 p05 cold page        5                553.0             900.6                 297.0                 423.0              517.0            13880       0
 p05 cold  seq        5               1587.0            1710.4                 297.0                 387.0              516.0            14486       0
 p05 warm page        5                495.0             616.4                  16.0                  48.0               79.0             1024       0
 p05 warm  seq        5               1145.0            1188.8                  16.0                  32.0               48.0             1024       0
 p10 cold page        5                627.0             756.6                 281.0                 579.0              736.0            14488       0
 p10 cold  seq        5               2238.0            2705.6                 282.0                 582.0              830.0            14486       0
 p10 warm page        5                519.0             672.8                  16.0                  48.0               80.0             1024       0
 p10 warm  seq        5               1813.0            1849.8                  16.0                  64.0              111.0             1024       0
 p20 cold page        5               2165.0            2464.0                1486.0                2848.0             3613.0            56769       0
 p20 cold  seq        5               5784.0            6002.0                1408.0                2657.0             3394.0            56078       0
 p20 warm page        5                611.0             816.0                  16.0                 144.0              222.0             1027       0
 p20 warm  seq        5               3594.0            3765.2                  16.0                 118.0              205.0             1027       0
```

## Log

```
2026-11-12T11:09:53Z run 20261112T110702Z-v32-9843: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:10:03Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:10:05Z F64: v32-calc-columns-aggregate is 5c599620-07a4-4f5a-9f50-07e7127ad6ba, DataTag reads back data-1m-v1
2026-11-12T11:10:54Z F64: page p01 done, 22 queries so far
2026-11-12T11:11:50Z F64: page p05 done, 132 queries so far
2026-11-12T11:14:03Z F64: page p10 done, 352 queries so far
2026-11-12T11:18:26Z F64: page p20 done, 792 queries so far
2026-11-12T11:18:27Z F64: monitoring database Monitoring KQL database
2026-11-12T11:20:33Z F64: 792 of 792 queries found in SemanticModelLogs
```
