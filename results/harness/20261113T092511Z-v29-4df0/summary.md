# Harness run 20261113T092511Z-v29-4df0

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
- Notebook run: 1793dbfc-cd37-4b18-8948-b54f42ee7e33
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 665 MB, Power Query 398 MB, duration 1 min, CPU 104 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request 39a173eb-2882-4838-b014-a728c76b1ee4, 2026-11-13T09:27:57.997 to 2026-11-13T09:28:58.987, workspace at 11b19b5, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v29-keys-as-text on F64 data-1m-v1: refreshed, peak 1,489 MB (2026-11-12T08:23:30Z).
  - Peak change: -824 MB (-55.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-13T09:24:27Z): peak 665 MB vs 703 MB (-38 MB), Power Query 398 MB vs 423 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 94 MB. The refresh may use the SKU maximum minus this: 25,506 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,972 MB: fits (22%); F16 5,026 MB: fits (13%); F32 10,146 MB: fits (7%); F64 25,506 MB: fits (3%); PPU 102,306 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8a2beb05-98b9-4e44-92de-799777abce23 TabularSequencePoint         55.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         51.6    25.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         49.1    25.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         48.2    25.0 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.9     9.8       0
                                                                                       Commit          4.6     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.2     1.8       0
                                                      Sales.Order Number       TabularRefresh          3.1     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.8  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.4     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.3     0.6       0
```

## Log

```
2026-11-13T09:27:24Z run 20261113T092511Z-v29-4df0: variant=v29-keys-as-text data_tag=data-1m-v1 targets=['F64'] expected_commit=11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:27:34Z F64: workspace already at 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:27:38Z F64: v29-keys-as-text is 8a2beb05-98b9-4e44-92de-799777abce23, DataTag reads back data-1m-v1
2026-11-13T09:27:57Z F64: model size in memory before the refresh: 93.8 MB
2026-11-13T09:27:58Z F64: refresh started, request 39a173eb-2882-4838-b014-a728c76b1ee4
2026-11-13T09:29:08Z F64: refresh refreshed (Completed) 
2026-11-13T09:29:09Z F64: monitoring database Monitoring KQL database
2026-11-13T09:31:46Z F64: ExecutionMetrics event found
2026-11-13T09:31:48Z F64: model size in memory right after the refresh: 141.9 MB
```
