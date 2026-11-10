# Harness run 20261110T145027Z-v24-0303

- Task: queries
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
- Notebook run: c2cda5eb-cc94-4732-a7b6-204ff8d0f5b5
- Pages p01,p05,p10,p20,pf, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T145027Z-v24-0303.json

## F64

- 968 queries sent (88 warm-up), 0 failed, 968 found in SemanticModelLogs, 0 throttling retries
- Workspace at e3910b1, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                575.0             607.0                  16.0                  16.0               16.0             4252       0
 p01 cold  seq        5                507.0             621.8                  16.0                  16.0               31.0             3336       0
 p01 warm page        5                525.0             556.4                  16.0                  16.0               16.0             1025       0
 p01 warm  seq        5                504.0             568.0                   0.0                   0.0                0.0             1025       0
 p05 cold page        5                631.0             720.2                 125.0                 189.0              328.0            14452       0
 p05 cold  seq        5               1135.0            1306.0                 125.0                 173.0              219.0            14428       0
 p05 warm page        5                441.0             513.2                  16.0                  16.0               16.0             1025       0
 p05 warm  seq        5                940.0             989.2                  16.0                  16.0               16.0             1025       0
 p10 cold page        5                411.0             667.6                 141.0                 246.0              392.0            14428       0
 p10 cold  seq        5               1803.0            1887.6                 125.0                 236.0              437.0            14455       0
 p10 warm page        5                501.0             608.4                  16.0                  36.0               32.0             1025       0
 p10 warm  seq        5               1669.0            1762.6                  16.0                  32.0               32.0             1025       0
 p20 cold page        5               1275.0            1471.8                 688.0                1454.0             1986.0            56745       0
 p20 cold  seq        5               3941.0            4111.6                 584.0                1145.0             1752.0            56745       0
 p20 warm page        5                666.0             934.0                  16.0                  80.0              111.0             1026       0
 p20 warm  seq        5               3337.0            3488.0                  16.0                  48.0              110.0             1026       0
  pf cold page        5                519.0             711.8                  62.0                 173.0              235.0            11454       0
  pf cold  seq        5               1325.0            1511.2                  47.0                 143.0              265.0            11802       0
  pf warm page        5                472.0             499.0                  16.0                  32.0               63.0             3357       0
  pf warm  seq        5               1226.0            1474.2                  16.0                  52.0               64.0             3357       0
```

## Log

```
2026-11-10T14:53:20Z run 20261110T145027Z-v24-0303: variant=v24-bidirectional data_tag=data-1m-v1 targets=['F64'] expected_commit=e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T14:53:30Z F64: workspace already at e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T14:53:32Z F64: v24-bidirectional is 79e079ab-ca76-4a15-a093-e21d8e5e1818, DataTag reads back data-1m-v1
2026-11-10T14:54:23Z F64: page p01 done, 22 queries so far
2026-11-10T14:55:20Z F64: page p05 done, 132 queries so far
2026-11-10T14:57:32Z F64: page p10 done, 352 queries so far
2026-11-10T15:01:56Z F64: page p20 done, 792 queries so far
2026-11-10T15:03:41Z F64: page pf done, 968 queries so far
2026-11-10T15:06:49Z F64: 968 of 968 queries found in SemanticModelLogs
```
