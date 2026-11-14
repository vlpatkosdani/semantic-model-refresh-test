# Harness run 20261113T173653Z-v22-df42

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: e6a0e585-e0f9-48f7-b5c1-c4e791633f50
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 794 MB, Power Query 469 MB, duration 1 min, CPU 68 s, rows 21,353,868, model 101 MB (Backup step in SemanticModelLogs)
- Refresh request 3abe2f8e-e547-406a-bb92-3f1706783fd1, 2026-11-13T17:39:45.903 to 2026-11-13T17:40:34.38, workspace at 2b9900b, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v22-dax-calc-columns on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-13T09:39:05Z): peak 794 MB vs 856 MB (-62 MB), Power Query 469 MB vs 847 MB, model 101 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (26%); F16 5,120 MB: fits (16%); F32 10,240 MB: fits (8%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    683e80a5-7d57-493c-a708-3a0b8ce5350c TabularSequencePoint         41.2     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.6    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.0    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.8    11.1 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.5     5.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.4     4.4       0
                                                                                       Commit          4.1     0.0       0
                                                  Sales.Sales Line Label       TabularRefresh          3.5     3.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.5     0.9       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          1.5     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.5     0.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.4     0.3       0
```

## Log

```
2026-11-13T17:39:17Z run 20261113T173653Z-v22-df42: variant=v22-dax-calc-columns data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T17:39:26Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T17:39:28Z F64: v22-dax-calc-columns is 683e80a5-7d57-493c-a708-3a0b8ce5350c, DataTag reads back data-1m-v1
2026-11-13T17:39:45Z F64: model size in memory before the refresh: 0.0 MB
2026-11-13T17:39:46Z F64: refresh started, request 3abe2f8e-e547-406a-bb92-3f1706783fd1
2026-11-13T17:40:56Z F64: refresh refreshed (Completed) 
2026-11-13T17:40:56Z F64: monitoring database Monitoring KQL database
2026-11-13T17:41:45Z F64: ExecutionMetrics event found
2026-11-13T17:42:20Z F64: model size in memory right after the refresh: 132.6 MB
```
