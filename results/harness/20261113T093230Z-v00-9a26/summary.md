# Harness run 20261113T093230Z-v00-9a26

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
- Notebook run: de025e1a-f78b-4073-a73f-233297f152d9
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 856 MB, Power Query 847 MB, duration 1 min, CPU 57 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 1042b94c-9aa4-43f1-b013-d53082780ac2, 2026-11-13T09:36:26.613 to 2026-11-13T09:37:07.797, workspace at 11b19b5, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 703 MB (2026-11-13T09:24:27Z).
  - Peak change: +153 MB (+21.8%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 93 MB. The refresh may use the SKU maximum minus this: 25,507 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,973 MB: fits (29%); F16 5,027 MB: fits (17%); F32 10,147 MB: fits (8%); F64 25,507 MB: fits (3%); PPU 102,307 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         35.7     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.3    10.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.6    10.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.4    10.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.6     6.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.5     5.5       0
                                                                                       Commit          3.0     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.0     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.4     0.7  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          0.8     0.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment          0.7     1.4       0
```

## Log

```
2026-11-13T09:35:54Z run 20261113T093230Z-v00-9a26: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:36:04Z F64: workspace already at 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:36:05Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-13T09:36:26Z F64: model size in memory before the refresh: 92.7 MB
2026-11-13T09:36:26Z F64: refresh started, request 1042b94c-9aa4-43f1-b013-d53082780ac2
2026-11-13T09:37:12Z F64: refresh refreshed (Completed) 
2026-11-13T09:37:12Z F64: monitoring database Monitoring KQL database
2026-11-13T09:38:48Z F64: ExecutionMetrics event found
2026-11-13T09:39:06Z F64: model size in memory right after the refresh: 92.7 MB
```
