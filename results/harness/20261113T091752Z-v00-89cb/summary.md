# Harness run 20261113T091752Z-v00-89cb

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
- Notebook run: bcc1dfb9-52ed-4197-94fc-06b9d811966a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 703 MB, Power Query 423 MB, duration 1 min, CPU 57 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request bb4ebdb9-7a57-4471-af34-309ea2516b04, 2026-11-13T09:21:02.987 to 2026-11-13T09:21:46.273, workspace at 11b19b5, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 550 MB (2026-11-12T14:09:40Z).
  - Peak change: +153 MB (+27.8%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 700 MB. The refresh may use the SKU maximum minus this: 24,900 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,366 MB: fits (30%); F16 4,420 MB: fits (16%); F32 9,540 MB: fits (7%); F64 24,900 MB: fits (3%); PPU 101,700 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         36.4     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.1    10.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.6    10.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.4    10.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.2     6.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.1     5.0       0
                                                                                       Commit          2.6     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.1     0.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.8  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          0.9     0.3       0
```

## Log

```
2026-11-13T09:20:30Z run 20261113T091752Z-v00-89cb: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:20:41Z F64: workspace already at 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:20:43Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-13T09:21:02Z F64: model size in memory before the refresh: 700.0 MB
2026-11-13T09:21:03Z F64: refresh started, request bb4ebdb9-7a57-4471-af34-309ea2516b04
2026-11-13T09:21:48Z F64: refresh refreshed (Completed) 
2026-11-13T09:21:48Z F64: monitoring database Monitoring KQL database
2026-11-13T09:24:25Z F64: ExecutionMetrics event found
2026-11-13T09:24:28Z F64: model size in memory right after the refresh: 92.7 MB
```
