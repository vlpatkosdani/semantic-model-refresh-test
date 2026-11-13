# Harness run 20261113T093950Z-v29-f936

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
- Notebook run: 49548b07-2495-4be2-bb3c-69bdd3803e18
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,735 MB, Power Query 1,720 MB, duration 1 min, CPU 122 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request 706e7d10-753d-40a9-a88e-81fcbbf221b5, 2026-11-13T09:42:36.073 to 2026-11-13T09:43:51.073, workspace at 11b19b5, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v29-keys-as-text on F64 data-1m-v1: refreshed, peak 665 MB (2026-11-13T09:31:47Z).
  - Peak change: +1,070 MB (+160.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-13T09:39:05Z): peak 1,735 MB vs 856 MB (+879 MB), Power Query 1,720 MB vs 847 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 142 MB. The refresh may use the SKU maximum minus this: 25,458 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,924 MB: fits (59%); F16 4,978 MB: fits (35%); F32 10,098 MB: fits (17%); F64 25,458 MB: fits (7%); PPU 102,258 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8a2beb05-98b9-4e44-92de-799777abce23 TabularSequencePoint         67.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.0    30.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         60.5    30.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         60.1    30.0 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.0    10.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.8     2.5       0
                                                                                       Commit          4.9     0.0       0
                                                      Sales.Order Number       TabularRefresh          4.7     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.4     2.4       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.3     2.4  104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          2.2     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.5     0.8       0
```

## Log

```
2026-11-13T09:42:04Z run 20261113T093950Z-v29-f936: variant=v29-keys-as-text data_tag=data-1m-v1 targets=['F64'] expected_commit=11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:42:14Z F64: workspace already at 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:42:16Z F64: v29-keys-as-text is 8a2beb05-98b9-4e44-92de-799777abce23, DataTag reads back data-1m-v1
2026-11-13T09:42:35Z F64: model size in memory before the refresh: 141.9 MB
2026-11-13T09:42:36Z F64: refresh started, request 706e7d10-753d-40a9-a88e-81fcbbf221b5
2026-11-13T09:44:16Z F64: refresh refreshed (Completed) 
2026-11-13T09:44:17Z F64: monitoring database Monitoring KQL database
2026-11-13T09:45:52Z F64: ExecutionMetrics event found
2026-11-13T09:45:54Z F64: model size in memory right after the refresh: 141.9 MB
```
