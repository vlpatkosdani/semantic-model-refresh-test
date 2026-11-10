# Harness run 20261110T144309Z-v24-17f8

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
- Notebook run: e4a9310d-4a73-419e-811e-1860fb25a5ed
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 608 MB, Power Query 335 MB, duration 1 min, CPU 56 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request a4197a14-764c-4b86-b8b7-e39663a35a27, 2026-11-10T14:46:12.657 to 2026-11-10T14:46:54.47, workspace at e3910b1, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v24-bidirectional on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-10T10:09:23Z): peak 608 MB vs 698 MB (-90 MB), Power Query 335 MB vs 419 MB, model 73 MB vs 73 MB.
- Measured peak against per-model limits: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%).

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    79e079ab-ca76-4a15-a093-e21d8e5e1818 TabularSequencePoint         35.1     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         34.7    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.3    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.1    10.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.7     4.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.7     5.5       0
                                                                                       Commit          2.6     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.4     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.4     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.3     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.8  104990
```

## Log

```
2026-11-10T14:45:42Z run 20261110T144309Z-v24-17f8: variant=v24-bidirectional data_tag=data-1m-v1 targets=['F64'] expected_commit=e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T14:45:53Z F64: workspace already at e3910b190d4b97fd3aa397b43d0d8eb3b2fcd3d4
2026-11-10T14:45:58Z F64: v24-bidirectional is 79e079ab-ca76-4a15-a093-e21d8e5e1818, DataTag reads back data-1m-v1
2026-11-10T14:46:12Z F64: refresh started, request a4197a14-764c-4b86-b8b7-e39663a35a27
2026-11-10T14:46:58Z F64: refresh refreshed (Completed) 
2026-11-10T14:49:35Z F64: ExecutionMetrics event found
```
