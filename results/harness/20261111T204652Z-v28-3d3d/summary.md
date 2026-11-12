# Harness run 20261111T204652Z-v28-3d3d

- Task: queries
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 7c87ac648b9c75b83006c9aaf05fa1d3c8d7970f
- Notebook run: 770d20c1-2f3b-465c-86be-b50570103ea0
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261111T204652Z-v28-3d3d.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 7c87ac6, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                613.0             651.0                  31.0                  31.0               47.0             4257       0
 p01 cold  seq        5                600.0             656.6                  31.0                  31.0               31.0             2258       0
 p01 warm page        5                607.0             609.4                   0.0                   0.0                0.0             1024       0
 p01 warm  seq        5                577.0             647.8                  16.0                  16.0               16.0             1024       0
 p05 cold page        5                744.0             754.6                 250.0                 360.0              469.0            14414       0
 p05 cold  seq        5               1439.0            1596.0                 250.0                 359.0              469.0            14388       0
 p05 warm page        5                460.0             658.6                  16.0                  16.0               63.0             1024       0
 p05 warm  seq        5               1044.0            1092.0                  16.0                  16.0               47.0             1024       0
 p10 cold page        5                550.0             755.8                 266.0                 548.0              736.0            14088       0
 p10 cold  seq        5               1981.0            2209.4                 266.0                 486.0              626.0            13826       0
 p10 warm page        5                656.0            1044.6                  16.0                  16.0              140.0             1024       0
 p10 warm  seq        5               1849.0            2108.0                  16.0                  64.0              111.0             1024       0
 p20 cold page        5               1715.0            2011.4                1047.0                2408.0             3096.0            28534       0
 p20 cold  seq        5               4818.0            5180.4                 953.0                2051.0             2549.0            27637       0
 p20 warm page        5                507.0             840.6                  16.0                 121.0              239.0             1030       0
 p20 warm  seq        5               3411.0            3543.0                  16.0                  96.0              143.0             1030       0
```

## Log

```
2026-11-11T20:47:32Z run 20261111T204652Z-v28-3d3d: variant=v28-types-all-text data_tag=data-1m-v1 targets=['F64'] expected_commit=7c87ac648b9c75b83006c9aaf05fa1d3c8d7970f
2026-11-11T20:47:37Z F64: workspace already at 7c87ac648b9c75b83006c9aaf05fa1d3c8d7970f
2026-11-11T20:47:38Z F64: v28-types-all-text is bc793114-53e1-4476-8e50-c4b0c5b15603, DataTag reads back data-1m-v1
2026-11-11T20:48:14Z F64: page p01 done, 22 queries so far
2026-11-11T20:49:11Z F64: page p05 done, 132 queries so far
2026-11-11T20:51:23Z F64: page p10 done, 352 queries so far
2026-11-11T20:55:47Z F64: page p20 done, 792 queries so far
2026-11-11T20:55:47Z F64: monitoring database Monitoring KQL database
2026-11-11T20:58:54Z F64: 792 of 792 queries found in SemanticModelLogs
```
