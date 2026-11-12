# Harness run 20261112T134925Z-v34-85a1

- Task: queries
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: b1660a09614e780473f21788f5ae8523db531ca7
- Notebook run: b90a2741-8c0e-4615-8730-a0a43740c669
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261112T134925Z-v34-85a1.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at b1660a0, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                671.0             779.0                  32.0                  32.0               31.0             3197       0
 p01 cold  seq        5                660.0             700.6                  47.0                  47.0               63.0             4326       0
 p01 warm page        5                624.0             668.8                   0.0                   0.0               16.0             1026       0
 p01 warm  seq        5                573.0             642.4                   0.0                   0.0               16.0             1026       0
 p05 cold page        5                571.0             808.8                 282.0                 421.0              516.0            13921       0
 p05 cold  seq        5               1527.0            1690.2                 297.0                 390.0              470.0            14501       0
 p05 warm page        5                459.0             559.2                  16.0                  16.0               47.0             1026       0
 p05 warm  seq        5               1094.0            1235.8                  16.0                  16.0               31.0             1026       0
 p10 cold page        5                558.0             808.0                 283.0                 516.0              656.0            13920       0
 p10 cold  seq        5               2250.0            2832.8                 267.0                 485.0              611.0            13920       0
 p10 warm page        5                547.0             636.2                  16.0                  64.0               96.0             1026       0
 p10 warm  seq        5               1833.0            1924.4                  16.0                  62.0              126.0             1026       0
 p20 cold page        5               2052.0            3389.2                1486.0                2782.0             3346.0            55892       0
 p20 cold  seq        5               6408.0            6930.6                1376.0                2574.0             3128.0            56804       0
 p20 warm page        5                732.0             782.4                  16.0                 140.0              189.0             1058       0
 p20 warm  seq        5               3664.0            3829.6                  16.0                 112.0              221.0             1058       0
```

## Log

```
2026-11-12T13:51:35Z run 20261112T134925Z-v34-85a1: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 targets=['F64'] expected_commit=b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T13:51:45Z F64: workspace already at b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T13:51:47Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1
2026-11-12T13:52:35Z F64: page p01 done, 22 queries so far
2026-11-12T13:53:31Z F64: page p05 done, 132 queries so far
2026-11-12T13:55:43Z F64: page p10 done, 352 queries so far
2026-11-12T14:00:07Z F64: page p20 done, 792 queries so far
2026-11-12T14:00:08Z F64: monitoring database Monitoring KQL database
2026-11-12T14:02:16Z F64: 792 of 792 queries found in SemanticModelLogs
```
