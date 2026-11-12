# Harness run 20261112T081715Z-v29-b0f1

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
- Notebook run: c9a845d0-433f-4c78-a552-7de8c9b3169d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,489 MB, Power Query 1,465 MB, duration 1 min, CPU 56 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request e39f2925-e67f-46d5-a608-8c83bfc1ac27, 2026-11-12T08:20:05.42 to 2026-11-12T08:20:41.817, workspace at 251a9b2, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v29-keys-as-text on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-11T19:50:47Z): peak 1,489 MB vs 608 MB (+881 MB), Power Query 1,465 MB vs 335 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (49%); F16 5,120 MB: fits (29%); F32 10,240 MB: fits (15%); F64 25,600 MB: fits (6%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8a2beb05-98b9-4e44-92de-799777abce23 TabularSequencePoint         32.1     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         30.1    13.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         28.3    13.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         28.1    13.3 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.4     5.4       0
                                                                                       Commit          2.5     0.0       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.3     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.2     0.8       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          2.1     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.8     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.8     0.3       0
                                                      Sales.Order Number       TabularRefresh          1.7     0.0       0
```

## Log

```
2026-11-12T08:19:31Z run 20261112T081715Z-v29-b0f1: variant=v29-keys-as-text data_tag=data-1m-v1 targets=['F64'] expected_commit=251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
2026-11-12T08:19:40Z F64: workspace already at 251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
2026-11-12T08:19:43Z F64: v29-keys-as-text is 8a2beb05-98b9-4e44-92de-799777abce23, DataTag reads back data-1m-v1
2026-11-12T08:20:05Z F64: model size in memory before the refresh: 0.0 MB
2026-11-12T08:20:05Z F64: refresh started, request e39f2925-e67f-46d5-a608-8c83bfc1ac27
2026-11-12T08:20:51Z F64: refresh refreshed (Completed) 
2026-11-12T08:20:51Z F64: monitoring database Monitoring KQL database
2026-11-12T08:23:29Z F64: ExecutionMetrics event found
2026-11-12T08:23:31Z F64: model size in memory right after the refresh: 141.9 MB
```
