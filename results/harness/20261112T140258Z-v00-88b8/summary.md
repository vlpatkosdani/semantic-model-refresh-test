# Harness run 20261112T140258Z-v00-88b8

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: b1660a09614e780473f21788f5ae8523db531ca7
- Notebook run: 5a276250-fa87-4956-a6ef-cae74a0bea5f
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 550 MB, Power Query 344 MB, duration 1 min, CPU 99 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 94eb2dc1-cc28-48b0-b3ff-386d4b7d6126, 2026-11-12T14:05:50.067 to 2026-11-12T14:06:55.933, workspace at b1660a0, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 608 MB (2026-11-11T19:50:47Z).
  - Peak change: -58 MB (-9.5%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 700 MB. The refresh may use the SKU maximum minus this: 24,900 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,366 MB: fits (23%); F16 4,420 MB: fits (12%); F32 9,540 MB: fits (6%); F64 24,900 MB: fits (2%); PPU 101,700 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         59.2     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.4    18.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.8    18.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         55.4    18.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.3    11.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.1    10.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.6     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.7  104990
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.5     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.1     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          1.9     0.0       0
```

## Log

```
2026-11-12T14:05:18Z run 20261112T140258Z-v00-88b8: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T14:05:29Z F64: workspace already at b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T14:05:32Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-12T14:05:49Z F64: model size in memory before the refresh: 700.0 MB
2026-11-12T14:05:50Z F64: refresh started, request 94eb2dc1-cc28-48b0-b3ff-386d4b7d6126
2026-11-12T14:07:00Z F64: refresh refreshed (Completed) 
2026-11-12T14:07:01Z F64: monitoring database Monitoring KQL database
2026-11-12T14:09:39Z F64: ExecutionMetrics event found
2026-11-12T14:09:41Z F64: model size in memory right after the refresh: 92.7 MB
```
