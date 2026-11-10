# Harness run 20261110T151413Z-v24a-c285

- Task: queries
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
- Notebook run: bacc71d2-decf-4a9b-8e95-f522d49c07a3
- Pages p01,p05,p10,p20,pf,po, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T151413Z-v24a-c285.json

## F64

- 1100 queries sent (100 warm-up), 0 failed, 1100 found in SemanticModelLogs, 0 throttling retries
- Workspace at e3910b1, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                574.0             611.4                  16.0                  16.0               31.0             4262       0
 p01 cold  seq        5                547.0             581.6                  16.0                  16.0               31.0             4262       0
 p01 warm page        5                550.0             583.0                  16.0                  16.0               16.0             1027       0
 p01 warm  seq        5                527.0             534.6                   0.0                   0.0                0.0             1027       0
 p05 cold page        5                555.0             606.2                 141.0                 204.0              282.0            14435       0
 p05 cold  seq        5               1138.0            1371.6                 110.0                 173.0              313.0            14462       0
 p05 warm page        5                484.0             631.0                  16.0                  16.0               32.0             1027       0
 p05 warm  seq        5               1039.0            1083.6                  16.0                  16.0               31.0             1027       0
 p10 cold page        5                616.0             654.2                 125.0                 251.0              360.0            14171       0
 p10 cold  seq        5               1900.0            1970.4                 125.0                 252.0              343.0            14171       0
 p10 warm page        5                391.0             624.4                  16.0                  16.0               47.0             1027       0
 p10 warm  seq        5               1813.0            1925.2                  16.0                  18.0               48.0             1027       0
 p20 cold page        5               1357.0            1594.2                 719.0                1578.0             2017.0            56061       0
 p20 cold  seq        5               3984.0            4480.0                 594.0                1159.0             1704.0            56754       0
 p20 warm page        5                650.0             794.0                  16.0                  58.0              174.0             1028       0
 p20 warm  seq        5               3479.0            3492.6                  16.0                  51.0               80.0             1028       0
  pf cold page        5                502.0             628.0                  62.0                 156.0              233.0            11812       0
  pf cold  seq        5               1319.0            1376.6                  62.0                 157.0              188.0            11811       0
  pf warm page        5                504.0             730.0                  16.0                  32.0               32.0             3369       0
  pf warm  seq        5               1598.0            1828.4                  16.0                  32.0               48.0             3369       0
  po cold page        5                317.0             336.4                  16.0                  32.0               48.0             6151       0
  po cold  seq        5                840.0             975.8                  31.0                  63.0               78.0             5023       0
  po warm page        5                373.0             513.0                  16.0                  16.0               32.0             2787       0
  po warm  seq        5                868.0             877.0                  16.0                  16.0               32.0             2787       0
```

## Log

```
2026-11-10T15:15:07Z run 20261110T151413Z-v24a-c285: variant=v24a-second-fact data_tag=data-1m-v1 targets=['F64'] expected_commit=e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T15:15:16Z F64: workspace already at e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T15:15:18Z F64: v24a-second-fact is 66e6aaee-ac4c-4400-9842-b68895f2d6f7, DataTag reads back data-1m-v1
2026-11-10T15:15:58Z F64: page p01 done, 22 queries so far
2026-11-10T15:16:54Z F64: page p05 done, 132 queries so far
2026-11-10T15:19:06Z F64: page p10 done, 352 queries so far
2026-11-10T15:23:30Z F64: page p20 done, 792 queries so far
2026-11-10T15:25:16Z F64: page pf done, 968 queries so far
2026-11-10T15:26:35Z F64: page po done, 1100 queries so far
2026-11-10T15:28:41Z F64: 1100 of 1100 queries found in SemanticModelLogs
```
