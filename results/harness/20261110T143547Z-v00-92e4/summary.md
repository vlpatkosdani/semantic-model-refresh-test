# Harness run 20261110T143547Z-v00-92e4

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
- Notebook run: 16c54dda-a20f-4c30-b3d9-09971a4ad76a
- Pages pf, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T143547Z-v00-92e4.json

## F64

- 176 queries sent (16 warm-up), 0 failed, 176 found in SemanticModelLogs, 0 throttling retries
- Workspace at e3910b1, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
  pf cold page        5                513.0            4452.2                  63.0                 173.0              220.0            11803       0
  pf cold  seq        5               1555.0            1715.6                  62.0                 157.0              235.0            11582       0
  pf warm page        5                480.0             627.4                  16.0                  16.0               47.0             3357       0
  pf warm  seq        5               1403.0            1453.0                  16.0                  48.0               78.0             3357       0
```

## Log

```
2026-11-10T14:37:59Z run 20261110T143547Z-v00-92e4: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T14:38:10Z F64: workspace already at e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T14:38:14Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-10T14:40:08Z F64: page pf done, 176 queries so far
2026-11-10T14:42:14Z F64: 176 of 176 queries found in SemanticModelLogs
```
