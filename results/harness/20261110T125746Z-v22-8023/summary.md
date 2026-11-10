# Harness run 20261110T125746Z-v22-8023

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: ee5050bd97225153e7d3e555e414d49995893af6
- Notebook run: d08eabae-346e-4bd1-ac8c-c888ebabe18a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 621 MB, Power Query 270 MB, duration 1 min, CPU 67 s, rows 21,353,868, model 101 MB (Backup step in SemanticModelLogs)
- Refresh request 534c7a2b-1e08-4cdb-a47b-91f4c4dd9ff2, 2026-11-10T12:58:36.11 to 2026-11-10T12:59:21.66, workspace at ee5050b, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v22-dax-calc-columns on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-10T10:09:23Z): peak 621 MB vs 698 MB (-77 MB), Power Query 270 MB vs 419 MB, model 101 MB vs 73 MB.
- Measured peak against per-model limits: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%).

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    98144a3c-be86-49fb-940d-51fa121d9e50 TabularSequencePoint         40.1     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.6    11.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.2    11.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.0    11.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.2     5.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.0     4.0       0
                                                  Sales.Sales Line Label       TabularRefresh          3.3     3.2       0
                                                                                       Commit          3.1     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.6     0.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.5     0.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.5     0.3       0
                                                     Sales.Customer Name       TabularRefresh          1.4     1.1       0
```

## Log

```
2026-11-10T12:58:19Z run 20261110T125746Z-v22-8023: variant=v22-dax-calc-columns data_tag=data-1m-v1 targets=['F64'] expected_commit=ee5050bd97225153e7d3e555e414d49995893af6
2026-11-10T12:58:26Z F64: workspace already at ee5050bd97225153e7d3e555e414d49995893af6
2026-11-10T12:58:30Z F64: v22-dax-calc-columns is 98144a3c-be86-49fb-940d-51fa121d9e50, DataTag reads back data-1m-v1
2026-11-10T12:58:36Z F64: refresh started, request 534c7a2b-1e08-4cdb-a47b-91f4c4dd9ff2
2026-11-10T12:59:46Z F64: refresh refreshed (Completed) 
2026-11-10T13:01:22Z F64: ExecutionMetrics event found
```
