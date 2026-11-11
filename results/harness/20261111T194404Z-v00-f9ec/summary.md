# Harness run 20261111T194404Z-v00-f9ec

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 53cfca4864e70f1fda420adacf9ab5955bb08783
- Notebook run: b33981b4-38c2-417b-8209-67f031e0cd5a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 608 MB, Power Query 335 MB, duration 1 min, CPU 56 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 48aee5a8-1299-43c6-9c2a-ddac013b46cf, 2026-11-11T19:47:23.837 to 2026-11-11T19:48:05.157, workspace at 53cfca4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 545 MB (2026-11-11T19:43:29Z).
  - Peak change: +63 MB (+11.6%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 0 MB (after clearValues). The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         35.0     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         34.7    11.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.5    11.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.3    10.9 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.7     5.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.6     4.5       0
                                                                     Commit          2.5     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.2     0.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.8  104990
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.3     0.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.0     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          0.9     0.0       0
```

## Log

```
2026-11-11T19:46:16Z run 20261111T194404Z-v00-f9ec: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T19:46:24Z F64: workspace already at 53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T19:46:25Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-11T19:46:42Z F64: model size in memory before the refresh: 92.7 MB
2026-11-11T19:46:42Z F64: refresh started, request 9aeac045-ca94-4af4-884b-4464abd09d02
2026-11-11T19:46:52Z F64: refresh refreshed (Completed) 
2026-11-11T19:47:23Z F64: model size after clearValues: 0.0 MB
2026-11-11T19:47:23Z F64: refresh started, request 48aee5a8-1299-43c6-9c2a-ddac013b46cf
2026-11-11T19:48:09Z F64: refresh refreshed (Completed) 
2026-11-11T19:48:09Z F64: monitoring database Monitoring KQL database
2026-11-11T19:50:45Z F64: ExecutionMetrics event found
2026-11-11T19:50:48Z F64: model size in memory right after the refresh: 92.7 MB
```
