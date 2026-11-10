# Harness run 20261110T150725Z-v24a-f994

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
- Notebook run: a8e550ee-8547-4c50-9722-758124f7b9d4
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 933 MB, Power Query 911 MB, duration 1 min, CPU 69 s, rows 3,541,806, model 103 MB (Backup step in SemanticModelLogs)
- Refresh request 382b62a6-0ba1-4a2f-ad44-9f7690f94127, 2026-11-10T15:10:03.323 to 2026-11-10T15:10:44.22, workspace at e3910b1, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v24a-second-fact on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-10T10:09:23Z): peak 933 MB vs 698 MB (+235 MB), Power Query 911 MB vs 419 MB, model 103 MB vs 73 MB.
- Measured peak against per-model limits: F2 3,066 MB: fits (30%); F16 5,120 MB: fits (18%); F32 10,240 MB: fits (9%); F64 25,600 MB: fits (4%).

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  66e6aaee-ac4c-4400-9842-b68895f2d6f7 TabularSequencePoint         36.1     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.7    11.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.7    11.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.4    11.3 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh          8.9     3.2       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process          7.9     3.2       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData          6.8     3.1  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.8     5.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.7     4.7       0
                                                                     Commit          3.0     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.4     0.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.7     0.9       0
```

## Log

```
2026-11-10T15:09:40Z run 20261110T150725Z-v24a-f994: variant=v24a-second-fact data_tag=data-1m-v1 targets=['F64'] expected_commit=e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T15:09:50Z F64: workspace already at e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T15:09:52Z F64: v24a-second-fact is 66e6aaee-ac4c-4400-9842-b68895f2d6f7, DataTag reads back data-1m-v1
2026-11-10T15:10:03Z F64: refresh started, request 382b62a6-0ba1-4a2f-ad44-9f7690f94127
2026-11-10T15:10:49Z F64: refresh refreshed (Completed) 
2026-11-10T15:13:26Z F64: ExecutionMetrics event found
```
