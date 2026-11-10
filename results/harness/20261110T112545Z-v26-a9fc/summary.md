# Harness run 20261110T112545Z-v26-a9fc

- Task: queries
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: afe63a327a1eaab17562d2a259bcfae0ccab1393
- Notebook run: 03973d0e-1415-4b7b-824e-777b09826e10
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261110T112545Z-v26-a9fc.json

## F64

- 792 queries sent (72 warm-up), 0 failed, 597 found in SemanticModelLogs, 0 throttling retries
- Workspace at afe63a3, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                561.0             578.6                  16.0                  16.0               16.0           5304.0       0
 p01 cold  seq        5                463.0             502.2                  16.0                  16.0               31.0           5240.0       0
 p01 warm page        5                547.0             562.8                   0.0                   0.0                0.0           1024.0       0
 p01 warm  seq        5                477.0             493.4                   0.0                   0.0               16.0           1024.0       0
 p05 cold page        5               8793.0            9151.4                8552.0                8631.0            12187.0        1583179.0       0
 p05 cold  seq        5               9785.0           10370.6                8755.0                8819.0            12515.0        1584361.0       0
 p05 warm page        5               7475.0            7760.8                7255.0                7255.0            10266.0        1263150.0       0
 p05 warm  seq        5               8804.0            9084.2                7676.0                7676.0            10109.0        1263150.0       0
 p10 cold page        5               9623.0           10215.0                9332.0               22630.0            32672.0        1580580.0       0
 p10 cold  seq        5              20846.0           21239.8                8723.0               19121.0            27345.0        1583227.0       0
 p10 warm page        5               8767.0            9039.6                8457.0               19963.0            28126.0        1263126.0       0
 p10 warm  seq        5              19163.0           19919.4                7597.0               17508.0            24719.0        1262677.0       0
 p20 cold page        5              17651.0           18443.0               17165.0               76775.0            99145.0        2718666.0       0
 p20 cold  seq        5              52253.0           54026.2               13349.0               49136.0            70408.0        2449116.0       0
 p20 warm page        5              15251.0           15969.2               14899.0               60547.0            79564.0        2206147.0       0
 p20 warm  seq        5              45855.0           47387.6               12083.0               41718.0            59109.0        2206208.0       0
```

## Log

```
2026-11-10T11:28:02Z run 20261110T112545Z-v26-a9fc: variant=v26-bad-dax data_tag=data-1m-v1 targets=['F64'] expected_commit=afe63a327a1eaab17562d2a259bcfae0ccab1393
2026-11-10T11:28:12Z F64: workspace already at afe63a327a1eaab17562d2a259bcfae0ccab1393
2026-11-10T11:28:14Z F64: v26-bad-dax is 7ba5e6dc-b664-4a7b-93f9-8b8d826d882e, DataTag reads back data-1m-v1
2026-11-10T11:28:56Z F64: page p01 done, 22 queries so far
2026-11-10T11:32:23Z F64: page p05 done, 132 queries so far
2026-11-10T11:37:59Z F64: page p10 done, 352 queries so far
2026-11-10T11:50:20Z F64: page p20 done, 792 queries so far
2026-11-10T12:10:50Z F64: 792 of 792 queries found in SemanticModelLogs
```
