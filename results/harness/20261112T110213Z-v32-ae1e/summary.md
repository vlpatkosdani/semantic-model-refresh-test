# Harness run 20261112T110213Z-v32-ae1e

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 7e87674b-ca0e-4b2e-b1e9-9c9bea27b660
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 631 MB, Power Query 595 MB, duration 1 min, CPU 121 s, rows 24,570,331, model 221 MB (Backup step in SemanticModelLogs)
- Refresh request 3b46aeda-3d98-4377-96c6-dcf4b53b25bd, 2026-11-12T11:03:09.473 to 2026-11-12T11:04:32.843, workspace at 5c382cc, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v32-calc-columns-aggregate on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-11T19:50:47Z): peak 631 MB vs 608 MB (+23 MB), Power Query 595 MB vs 335 MB, model 221 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (21%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  5c599620-07a4-4f5a-9f50-07e7127ad6ba TabularSequencePoint         65.3     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.2    20.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         56.2    20.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         56.0    20.0 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.9    10.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.6     7.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.9     1.9       0
                          Sales.Line Share Of Customer       TabularRefresh          3.8     2.5       0
                             Sales.Line Share Of Order       TabularRefresh          3.0     1.9       0
                                     Sales.Order Total       TabularRefresh          2.8     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.4     1.8  104990
```

## Log

```
2026-11-12T11:02:46Z run 20261112T110213Z-v32-ae1e: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:02:52Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:02:57Z F64: v32-calc-columns-aggregate is 5c599620-07a4-4f5a-9f50-07e7127ad6ba, DataTag reads back data-1m-v1
2026-11-12T11:03:09Z F64: model size in memory before the refresh: 0.1 MB
2026-11-12T11:03:09Z F64: refresh started, request 3b46aeda-3d98-4377-96c6-dcf4b53b25bd
2026-11-12T11:04:50Z F64: refresh refreshed (Completed) 
2026-11-12T11:04:50Z F64: monitoring database Monitoring KQL database
2026-11-12T11:05:40Z F64: ExecutionMetrics event found
2026-11-12T11:06:15Z F64: model size in memory right after the refresh: 367.9 MB
```
