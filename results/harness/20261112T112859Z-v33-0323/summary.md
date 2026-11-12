# Harness run 20261112T112859Z-v33-0323

- Task: queries
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 77500603-6548-4ea0-8d36-7ade74ef7454
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T112859Z-v33-0323.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 5c382cc, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                593.0             622.2                  31.0                  31.0               31.0             4300       0
 p01 cold  seq        5                548.0             609.0                  16.0                  16.0               31.0             3171       0
 p01 warm page        5                586.0             685.0                  16.0                  16.0               16.0             1024       0
 p01 warm  seq        5                523.0             533.0                   0.0                   0.0                0.0             1024       0
 p05 cold page        5                613.0             639.0                 172.0                 235.0              344.0            14504       0
 p05 cold  seq        5               1275.0            1436.0                 156.0                 220.0              313.0            13895       0
 p05 warm page        5                455.0             528.2                  16.0                  28.0               32.0             1024       0
 p05 warm  seq        5               1025.0            1138.0                  16.0                  32.0               48.0             1024       0
 p10 cold page        5                540.0             705.4                 141.0                 330.0              530.0            14476       0
 p10 cold  seq        5               1947.0            2003.4                 157.0                 292.0              408.0            14173       0
 p10 warm page        5                467.0             538.0                  16.0                  48.0               64.0             1024       0
 p10 warm  seq        5               1716.0            1783.0                  16.0                  16.0               63.0             1024       0
 p20 cold page        5               1464.0            1542.6                 798.0                1738.0             2125.0            55871       0
 p20 cold  seq        5               4604.0            5027.6                 735.0                1440.0             1749.0            59113       0
 p20 warm page        5                681.0            2537.4                  16.0                  80.0              157.0             1035       0
 p20 warm  seq        5               3444.0            3823.6                  16.0                  64.0              173.0             1035       0
```

## Log

```
2026-11-12T11:29:36Z run 20261112T112859Z-v33-0323: variant=v33-auto-date-time data_tag=data-1m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:29:42Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:29:43Z F64: v33-auto-date-time is 79c2f30d-ee15-45f7-92a8-73654d03e1a1, DataTag reads back data-1m-v1
2026-11-12T11:30:27Z F64: page p01 done, 22 queries so far
2026-11-12T11:31:23Z F64: page p05 done, 132 queries so far
2026-11-12T11:33:35Z F64: page p10 done, 352 queries so far
2026-11-12T11:37:59Z F64: page p20 done, 792 queries so far
2026-11-12T11:37:59Z F64: monitoring database Monitoring KQL database
2026-11-12T11:40:06Z F64: 792 of 792 queries found in SemanticModelLogs
```
