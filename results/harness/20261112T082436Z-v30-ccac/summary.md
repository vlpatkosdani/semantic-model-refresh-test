# Harness run 20261112T082436Z-v30-ccac

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
- Notebook run: eff59ec1-c547-4574-a563-abd64a73e05d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 550 MB, Power Query 270 MB, duration 0 min, CPU 51 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 860fd86e-a0d7-49a1-bac0-4d608821afe8, 2026-11-12T08:25:20.35 to 2026-11-12T08:25:55.713, workspace at 251a9b2, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v30-double-instead-of-fixed on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-11T19:50:47Z): peak 550 MB vs 608 MB (-58 MB), Power Query 270 MB vs 335 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (18%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (5%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    82a0b18f-7fcc-4d91-84c8-ad3d394d13f0 TabularSequencePoint         29.9     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         29.5    10.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         28.5    10.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         28.1    10.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.2     6.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.1     5.1       0
                                                                                       Commit          2.8     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.4     0.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.5     0.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.4     0.9  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.3     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.0     0.0       0
```

## Log

```
2026-11-12T08:25:00Z run 20261112T082436Z-v30-ccac: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 targets=['F64'] expected_commit=251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
2026-11-12T08:25:06Z F64: workspace already at 251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
2026-11-12T08:25:08Z F64: v30-double-instead-of-fixed is 82a0b18f-7fcc-4d91-84c8-ad3d394d13f0, DataTag reads back data-1m-v1
2026-11-12T08:25:20Z F64: model size in memory before the refresh: 0.0 MB
2026-11-12T08:25:20Z F64: refresh started, request 860fd86e-a0d7-49a1-bac0-4d608821afe8
2026-11-12T08:26:05Z F64: refresh refreshed (Completed) 
2026-11-12T08:26:06Z F64: monitoring database Monitoring KQL database
2026-11-12T08:27:42Z F64: ExecutionMetrics event found
2026-11-12T08:28:17Z F64: model size in memory right after the refresh: 92.9 MB
```
