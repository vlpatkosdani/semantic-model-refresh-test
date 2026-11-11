# Harness run 20261111T193917Z-v00-05d4

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 53cfca4864e70f1fda420adacf9ab5955bb08783
- Notebook run: 35530117-b1c5-49c8-a0ae-b6bb76d31fb0
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 545 MB, Power Query 374 MB, duration 1 min, CPU 57 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request a969a422-5d45-4f50-9ac3-b422102951ef, 2026-11-11T19:40:06.143 to 2026-11-11T19:40:47.203, workspace at 53cfca4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 543 MB (2026-11-11T19:07:03Z).
  - Peak change: +2 MB (+0.4%).
- Model size in memory when the full refresh started: 93 MB. The refresh may use the SKU maximum minus this: 25,507 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,973 MB: fits (18%); F16 5,027 MB: fits (11%); F32 10,147 MB: fits (5%); F64 25,507 MB: fits (2%); PPU 102,307 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         36.1     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.7    11.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.4    11.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.2    11.0 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.0     5.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.8     4.8       0
                                                                     Commit          2.4     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.0     0.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.8  104990
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.2     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          0.9     0.0       0
```

## Log

```
2026-11-11T19:39:45Z run 20261111T193917Z-v00-05d4: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T19:39:52Z F64: workspace already at 53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T19:39:53Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-11T19:40:06Z F64: model size in memory before the refresh: 92.7 MB
2026-11-11T19:40:06Z F64: refresh started, request a969a422-5d45-4f50-9ac3-b422102951ef
2026-11-11T19:40:51Z F64: refresh refreshed (Completed) 
2026-11-11T19:40:51Z F64: monitoring database Monitoring KQL database
2026-11-11T19:43:28Z F64: ExecutionMetrics event found
2026-11-11T19:43:30Z F64: model size in memory right after the refresh: 92.7 MB
```
