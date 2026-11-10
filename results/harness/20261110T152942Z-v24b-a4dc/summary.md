# Harness run 20261110T152942Z-v24b-a4dc

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
- Notebook run: 1d5dd6f2-6b14-4231-ae77-985b5b28d90f
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,102 MB, Power Query 1,003 MB, duration 1 min, CPU 105 s, rows 3,541,806, model 103 MB (Backup step in SemanticModelLogs)
- Refresh request 8d2c90f7-c7df-4354-ba6f-bbfd6b4a2e81, 2026-11-10T15:31:20.527 to 2026-11-10T15:32:29.367, workspace at e3910b1, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v24b-second-fact-bidirectional on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-10T10:09:23Z): peak 1,102 MB vs 698 MB (+404 MB), Power Query 1,003 MB vs 419 MB, model 103 MB vs 73 MB.
- Measured peak against per-model limits: F2 3,066 MB: fits (36%); F16 5,120 MB: fits (22%); F32 10,240 MB: fits (11%); F64 25,600 MB: fits (4%).

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  36b073b1-f4a7-44e2-a114-d74d899ff5bd TabularSequencePoint         61.0     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.5    16.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.6    16.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         58.3    16.0 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         15.2     4.3       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         13.9     4.3       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         12.1     4.2  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.6     8.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.5     7.4       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.2     1.5       0
                                                                     Commit          4.5     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.8     1.4       0
```

## Log

```
2026-11-10T15:31:06Z run 20261110T152942Z-v24b-a4dc: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 targets=['F64'] expected_commit=e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T15:31:11Z F64: workspace already at e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T15:31:13Z F64: v24b-second-fact-bidirectional is 36b073b1-f4a7-44e2-a114-d74d899ff5bd, DataTag reads back data-1m-v1
2026-11-10T15:31:20Z F64: refresh started, request 8d2c90f7-c7df-4354-ba6f-bbfd6b4a2e81
2026-11-10T15:32:31Z F64: refresh refreshed (Completed) 
2026-11-10T15:34:06Z F64: ExecutionMetrics event found
```
