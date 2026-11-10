# Harness run 20261110T103141Z-v00-5b3b

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: b6e6f4f732f8478f0f24c57834f52ab992f45c22
- Notebook run: bf266000-f097-47b5-8c06-376c05d8897e
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T103141Z-v00-5b3b.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at b6e6f4f, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                588.0             625.8                  21.0                  21.0               31.0             4252       0
 p01 cold  seq        5                580.0             741.2                  16.0                  16.0               31.0             4252       0
 p01 warm page        5                572.0             605.0                   0.0                   0.0               16.0             1025       0
 p01 warm  seq        5                491.0             502.2                   0.0                   0.0                0.0             1025       0
 p05 cold page        5                527.0             643.2                 141.0                 219.0              328.0            14428       0
 p05 cold  seq        5               1192.0            1563.6                 141.0                 189.0              328.0            14428       0
 p05 warm page        5                437.0             507.2                  16.0                  16.0               32.0             1025       0
 p05 warm  seq        5               1041.0            1067.4                   0.0                   0.0               16.0             1025       0
 p10 cold page        5                679.0             731.4                 141.0                 237.0              360.0            14162       0
 p10 cold  seq        5               1983.0            2223.2                 141.0                 237.0              406.0            14428       0
 p10 warm page        5                419.0             577.4                  16.0                  16.0               47.0             1025       0
 p10 warm  seq        5               1584.0            1814.2                  16.0                  16.0               63.0             1025       0
 p20 cold page        5               1457.0            4691.6                 672.0                1441.0             2033.0            59070       0
 p20 cold  seq        5               4641.0            4729.6                 641.0                1196.0             1906.0            59070       0
 p20 warm page        5                702.0             836.6                  16.0                  70.0               96.0             1026       0
 p20 warm  seq        5               3398.0            3621.6                  16.0                  64.0               80.0             1026       0
```

## Log

```
2026-11-10T10:34:01Z run 20261110T103141Z-v00-5b3b: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=b6e6f4f732f8478f0f24c57834f52ab992f45c22
2026-11-10T10:34:12Z F64: workspace already at b6e6f4f732f8478f0f24c57834f52ab992f45c22
2026-11-10T10:34:14Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-10T10:34:58Z F64: page p01 done, 22 queries so far
2026-11-10T10:35:54Z F64: page p05 done, 132 queries so far
2026-11-10T10:38:06Z F64: page p10 done, 352 queries so far
2026-11-10T10:42:30Z F64: page p20 done, 792 queries so far
2026-11-10T10:44:36Z F64: 792 of 792 queries found in SemanticModelLogs
```
