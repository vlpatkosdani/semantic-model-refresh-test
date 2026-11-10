# Harness run 20261110T121143Z-v27-ada0

- Task: queries
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: afe63a327a1eaab17562d2a259bcfae0ccab1393
- Notebook run: 63920bd3-6b00-4671-b729-e1707758a412
- Pages p01,p05,p10,p20,p27, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T121143Z-v27-ada0.json

## F64

- 902 queries sent (82 warm-up), 0 failed, 902 found in SemanticModelLogs, 0 throttling retries
- Workspace at afe63a3, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                606.0             643.0                  16.0                  16.0               31.0             4252       0
 p01 cold  seq        5                555.0             708.2                  16.0                  16.0               31.0             4252       0
 p01 warm page        5                625.0             673.6                   0.0                   0.0                0.0             1025       0
 p01 warm  seq        5                561.0             598.0                   0.0                   0.0               16.0             1025       0
 p05 cold page        5                456.0             606.6                 141.0                 220.0              250.0            13847       0
 p05 cold  seq        5               1262.0            1447.4                 125.0                 188.0              313.0            14455       0
 p05 warm page        5                510.0             631.2                  16.0                  32.0               16.0             1025       0
 p05 warm  seq        5               1043.0            1074.2                   0.0                   0.0               16.0             1025       0
 p10 cold page        5                532.0             754.6                 141.0                 267.0              439.0            14455       0
 p10 cold  seq        5               1843.0            1930.4                 141.0                 252.0              391.0            14428       0
 p10 warm page        5                498.0             640.4                  16.0                  16.0               48.0             1025       0
 p10 warm  seq        5               1806.0            1828.0                  16.0                  32.0               63.0             1025       0
 p20 cold page        5               1350.0            1524.0                 766.0                1566.0             2079.0            56052       0
 p20 cold  seq        5               4470.0            4962.2                 594.0                1160.0             1800.0            56745       0
 p20 warm page        5                630.0            1483.2                  16.0                  70.0              112.0             1026       0
 p20 warm  seq        5               3523.0            3713.0                  16.0                  80.0              143.0             1026       0
 p27 cold page        5               1726.0            1852.6                1345.0                3830.0             4517.0           236726       0
 p27 cold  seq        5               4372.0            4597.8                1141.0                3002.0             3516.0           251290       0
 p27 warm page        5               1122.0            1468.8                 750.0                2017.0             2033.0            89899       0
 p27 warm  seq        5               3004.0            3655.2                 735.0                1935.0             1938.0            90211       0
```

## Log

```
2026-11-10T12:14:02Z run 20261110T121143Z-v27-ada0: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 targets=['F64'] expected_commit=afe63a327a1eaab17562d2a259bcfae0ccab1393
2026-11-10T12:14:12Z F64: workspace already at afe63a327a1eaab17562d2a259bcfae0ccab1393
2026-11-10T12:14:14Z F64: v27-high-cardinality-visuals is ff8802e6-5a2b-475b-a6be-b56e16fe65ca, DataTag reads back data-1m-v1
2026-11-10T12:15:01Z F64: page p01 done, 22 queries so far
2026-11-10T12:15:57Z F64: page p05 done, 132 queries so far
2026-11-10T12:18:09Z F64: page p10 done, 352 queries so far
2026-11-10T12:22:33Z F64: page p20 done, 792 queries so far
2026-11-10T12:23:48Z F64: page p27 done, 902 queries so far
2026-11-10T12:26:56Z F64: 902 of 902 queries found in SemanticModelLogs
```
