# Harness run 20261110T130235Z-v22-817d

- Task: queries
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: ee5050bd97225153e7d3e555e414d49995893af6
- Notebook run: 07162466-3b8b-43a6-8919-df6de92168ac
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T130235Z-v22-817d.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at ee5050b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                583.0             640.6                  16.0                  16.0               16.0             4261       0
 p01 cold  seq        5                541.0             651.8                  16.0                  16.0               16.0             4261       0
 p01 warm page        5                655.0             670.0                   0.0                   0.0                0.0             1027       0
 p01 warm  seq        5                559.0             615.6                   0.0                   0.0                0.0             1026       0
 p05 cold page        5                516.0             548.8                 141.0                 218.0              328.0            14437       0
 p05 cold  seq        5               1218.0            1405.8                 125.0                 189.0              297.0            14437       0
 p05 warm page        5                458.0             621.2                   0.0                   0.0               31.0             1026       0
 p05 warm  seq        5               1113.0            1605.6                  16.0                  16.0               32.0             1026       0
 p10 cold page        5                650.0             651.8                 156.0                 313.0              407.0            13856       0
 p10 cold  seq        5               1834.0            2093.2                 141.0                 252.0              391.0            14437       0
 p10 warm page        5                538.0             638.2                  16.0                  32.0               48.0             1026       0
 p10 warm  seq        5               1773.0            1887.4                  16.0                  32.0               47.0             1026       0
 p20 cold page        5               1619.0            1808.2                1047.0                2219.0             2625.0            59077       0
 p20 cold  seq        5               4815.0            4996.0                 782.0                1381.0             2236.0            59077       0
 p20 warm page        5                624.0             720.0                  16.0                  68.0              126.0             1026       0
 p20 warm  seq        5               3797.0            3904.4                  16.0                  63.0              126.0             1027       0
```

## Log

```
2026-11-10T13:06:18Z run 20261110T130235Z-v22-817d: variant=v22-dax-calc-columns data_tag=data-1m-v1 targets=['F64'] expected_commit=ee5050bd97225153e7d3e555e414d49995893af6
2026-11-10T13:06:29Z F64: workspace already at ee5050bd97225153e7d3e555e414d49995893af6
2026-11-10T13:06:31Z F64: v22-dax-calc-columns is 98144a3c-be86-49fb-940d-51fa121d9e50, DataTag reads back data-1m-v1
2026-11-10T13:07:21Z F64: page p01 done, 22 queries so far
2026-11-10T13:08:17Z F64: page p05 done, 132 queries so far
2026-11-10T13:10:29Z F64: page p10 done, 352 queries so far
2026-11-10T13:14:53Z F64: page p20 done, 792 queries so far
2026-11-10T13:18:01Z F64: 792 of 792 queries found in SemanticModelLogs
```
