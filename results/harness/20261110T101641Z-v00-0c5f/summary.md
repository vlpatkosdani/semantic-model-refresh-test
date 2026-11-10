# Harness run 20261110T101641Z-v00-0c5f

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 8c45cbd6398223e6114cd8e2e3b72a0ca4e872dc
- Notebook run: 912603dd-8b88-4994-becd-1ca705278d7c
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T101641Z-v00-0c5f.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 792 found in SemanticModelLogs, 0 throttling retries
- Workspace at 8c45cbd, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                584.0             646.0                  31.0                  31.0               31.0             4252       0
 p01 cold  seq        5                376.0             514.8                  23.0                  23.0               47.0             4252       0
 p01 warm page        5                647.0             767.6                   0.0                   0.0               16.0             1025       0
 p01 warm  seq        5                517.0             535.2                  16.0                  16.0               16.0             1025       0
 p05 cold page        5               1454.0            1631.8                 141.0                 220.0              313.0            14455       0
 p05 cold  seq        5               1272.0            1661.0                 141.0                 220.0              328.0            14161       0
 p05 warm page        5               3019.0            3188.2                  16.0                  16.0               32.0             1025       0
 p05 warm  seq        5               1084.0            2171.8                  16.0                  16.0               16.0             1025       0
 p10 cold page        5               4533.0            4872.2                 156.0                 282.0              407.0            14161       0
 p10 cold  seq        5               4339.0            4414.0                 172.0                 314.0              439.0            14161       0
 p10 warm page        5               6053.0            6206.4                  16.0                  32.0               48.0             1025       0
 p10 warm  seq        5               6000.0            6010.8                  16.0                  32.0               64.0             1025       0
 p20 cold page        5              10029.0           10536.0                 704.0                1394.0             2172.0            59070       0
 p20 cold  seq        5              10425.0           10688.6                 719.0                1379.0             2017.0            56745       0
 p20 warm page        5              11796.0           12438.0                  16.0                  66.0              126.0             1026       0
 p20 warm  seq        5              11951.0           12072.0                  16.0                  63.0              110.0             1026       0
```

## Log

```
2026-11-10T10:19:01Z run 20261110T101641Z-v00-0c5f: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=8c45cbd6398223e6114cd8e2e3b72a0ca4e872dc
2026-11-10T10:19:10Z F64: workspace already at 8c45cbd6398223e6114cd8e2e3b72a0ca4e872dc
2026-11-10T10:19:12Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-10T10:20:00Z F64: page p01 done, 22 queries so far
2026-11-10T10:20:57Z F64: page p05 done, 132 queries so far
2026-11-10T10:23:09Z F64: page p10 done, 352 queries so far
2026-11-10T10:27:33Z F64: page p20 done, 792 queries so far
2026-11-10T10:29:39Z F64: 792 of 792 queries found in SemanticModelLogs
```

Note: page_wall_ms in this run is not valid. The rate limiter released one query at a time once its burst of 20 was used, so the client wall time of a page mostly measures waiting for the limiter (warm p20: 12 s for 66 ms of server time). The server-side numbers (server_ms, cpu_ms, peak_mem_kb, result_rows) are not affected. Fixed in the next commit: a page takes all its tokens before it starts.
