# Harness run 20261110T111306Z-v26-d200

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 10c16c38a89d0f2e8a8e67a3194e2559eb728b54
- Notebook run: f5039f84-4153-46b0-ac4e-0b3e5fa00681
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 715 MB, Power Query 689 MB, duration 1 min, CPU 56 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 16e8200f-a45c-44f1-afbd-1b1aae29a156, 2026-11-10T11:14:05.967 to 2026-11-10T11:14:44.77, workspace at 10c16c3, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v26-bad-dax on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-10T10:09:23Z): peak 715 MB vs 698 MB (+17 MB), Power Query 689 MB vs 419 MB, model 73 MB vs 73 MB.
- Measured peak against per-model limits: F2 3,066 MB: fits (23%); F16 5,120 MB: fits (14%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%).

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    7ba5e6dc-b664-4a7b-93f9-8b8d826d882e TabularSequencePoint         35.4     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.0    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.6    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.3    11.1 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.0     5.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.9     4.9       0
                                                                                       Commit          2.9     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.4     0.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.6     0.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.9  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.3     0.0       0
```

## Log

```
2026-11-10T11:13:49Z run 20261110T111306Z-v26-d200: variant=v26-bad-dax data_tag=data-1m-v1 targets=['F64'] expected_commit=10c16c38a89d0f2e8a8e67a3194e2559eb728b54
2026-11-10T11:13:57Z F64: workspace already at 10c16c38a89d0f2e8a8e67a3194e2559eb728b54
2026-11-10T11:13:59Z F64: v26-bad-dax is 7ba5e6dc-b664-4a7b-93f9-8b8d826d882e, DataTag reads back data-1m-v1
2026-11-10T11:14:06Z F64: refresh started, request 16e8200f-a45c-44f1-afbd-1b1aae29a156
2026-11-10T11:14:51Z F64: refresh refreshed (Completed) 
2026-11-10T11:17:29Z F64: ExecutionMetrics event found
```
