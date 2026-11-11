# Harness run 20261111T190051Z-v00-05d6

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 5b3e3d5f2dc632057e19798f54b0695d4e03c3df
- Notebook run: 2162dc90-9943-425a-8902-fd3a089a5bc0
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 543 MB, Power Query 270 MB, duration 1 min, CPU 55 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request c12009e6-9c79-4e06-876c-8083f63213a8, 2026-11-11T19:03:36.55 to 2026-11-11T19:04:18.003, workspace at 5b3e3d5, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v00-baseline on F64 data-1m-v1.
- Measured peak against per-model limits: F2 3,066 MB: fits (18%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (5%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%).

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         34.6     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         34.3    10.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         32.7    10.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         32.5    10.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.6     5.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.5     4.5       0
                                                                                       Commit          2.7     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.2     0.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.5     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.8  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.2     0.3       0
```

## Log

```
2026-11-11T19:03:22Z run 20261111T190051Z-v00-05d6: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=5b3e3d5f2dc632057e19798f54b0695d4e03c3df
2026-11-11T19:03:31Z F64: workspace already at 5b3e3d5f2dc632057e19798f54b0695d4e03c3df
2026-11-11T19:03:32Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-11T19:03:36Z F64: refresh started, request c12009e6-9c79-4e06-876c-8083f63213a8
2026-11-11T19:04:22Z F64: refresh refreshed (Completed) 
2026-11-11T19:04:22Z F64: monitoring database Monitoring KQL database
2026-11-11T19:07:00Z F64: ExecutionMetrics event found
```
