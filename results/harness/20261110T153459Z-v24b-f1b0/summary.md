# Harness run 20261110T153459Z-v24b-f1b0

- Task: queries
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
- Notebook run: 958c17fc-8c4e-4193-8519-8335d983abf0
- Pages p01,p05,p10,p20,pf,po, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T153459Z-v24b-f1b0.json

## F64

- 1100 queries sent (100 warm-up), 10 failed, 1000 found in SemanticModelLogs, 0 throttling retries
- Workspace at e3910b1, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                513.0             543.2                  16.0                  16.0               16.0           2263.0       0
 p01 cold  seq        5                501.0             612.0                  16.0                  16.0               16.0           3247.0       0
 p01 warm page        5                535.0             540.6                   0.0                   0.0                0.0           1027.0       0
 p01 warm  seq        5                491.0             528.0                  16.0                  16.0               16.0           1027.0       0
 p05 cold page        5                539.0             565.0                 125.0                 189.0              328.0          14463.0       0
 p05 cold  seq        5               1224.0            1334.0                 125.0                 173.0              313.0          14438.0       0
 p05 warm page        5                449.0             542.8                  16.0                  16.0               48.0           1027.0       0
 p05 warm  seq        5               1000.0            1013.4                  16.0                  16.0               16.0           1027.0       0
 p10 cold page        5                485.0             677.8                   NaN                   0.0                0.0              NaN       5
 p10 cold  seq        5               1733.0            1783.4                 126.0                 221.0              392.0          14438.0       0
 p10 warm page        5                362.0             481.6                  16.0                   0.0                0.0           1027.0       4
 p10 warm  seq        5               1652.0            1729.4                  16.0                  16.0               48.0           1027.0       0
 p20 cold page        5               1189.0            1691.6                 688.0                1453.0             1954.0          59080.0       0
 p20 cold  seq        5               3993.0            4162.6                 609.0                1161.0             1858.0          56754.0       0
 p20 warm page        5                573.0             709.0                  16.0                  48.0               64.0           1028.0       0
 p20 warm  seq        5               3152.0            3426.0                  16.0                  48.0               80.0           1028.0       0
  pf cold page        5                554.0             628.0                  47.0                 174.0              266.0          11811.0       0
  pf cold  seq        5               1412.0            1547.8                  47.0                 148.0              251.0          11530.0       0
  pf warm page        5                435.0             599.0                  16.0                  22.0               48.0           3369.0       0
  pf warm  seq        5               1186.0            1417.8                  16.0                  32.0               48.0           3369.0       0
  po cold page        5                309.0             442.6                  78.0                 235.0              281.0           7154.0       0
  po cold  seq        5               1024.0            1069.4                  74.0                 204.0              297.0           8281.0       0
  po warm page        5                264.0             288.2                  47.0                  94.0               94.0           3964.0       0
  po warm  seq        5                849.0             863.8                  31.0                  78.0               94.0           3964.0       0
```

Failed queries (first 10):

```
page visual mode conc  rep                                                                                                                         client_error
 p10    v01 cold page    1 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 cold page    2 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 cold page    3 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 cold page    4 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 cold page    5 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 warm page    0 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 warm page    1 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 warm page    2 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 warm page    3 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p10    v01 warm page    4 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
```

## Log

```
2026-11-10T15:38:43Z run 20261110T153459Z-v24b-f1b0: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 targets=['F64'] expected_commit=e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T15:38:53Z F64: workspace already at e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T15:38:54Z F64: v24b-second-fact-bidirectional is 36b073b1-f4a7-44e2-a114-d74d899ff5bd, DataTag reads back data-1m-v1
2026-11-10T15:39:42Z F64: page p01 done, 22 queries so far
2026-11-10T15:40:37Z F64: page p05 done, 132 queries so far
2026-11-10T15:42:49Z F64: page p10 done, 352 queries so far
2026-11-10T15:47:13Z F64: page p20 done, 792 queries so far
2026-11-10T15:48:59Z F64: page pf done, 968 queries so far
2026-11-10T15:50:18Z F64: page po done, 1100 queries so far
2026-11-10T16:10:50Z F64: 1000 of 1100 queries found in SemanticModelLogs
```
