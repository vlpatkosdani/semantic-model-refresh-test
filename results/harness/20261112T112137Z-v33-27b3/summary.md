# Harness run 20261112T112137Z-v33-27b3

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 2e84b3f1-6f76-4549-ba30-e7115a985866
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 619 MB, Power Query 423 MB, duration 1 min, CPU 59 s, rows 2,791,244, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request 0ddf7c99-9c3a-4f0d-b70b-2e1699bafb37, 2026-11-12T11:24:14.41 to 2026-11-12T11:24:56.42, workspace at 5c382cc, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v33-auto-date-time on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-11T19:50:47Z): peak 619 MB vs 608 MB (+11 MB), Power Query 423 MB vs 335 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  79c2f30d-ee15-45f7-92a8-73654d03e1a1 TabularSequencePoint         36.7     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.3    11.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.7    11.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.5    11.2 2349091
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.8     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.6     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.6     5.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.5     4.5       0
                                                                     Commit          3.1     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.0     1.1       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.7     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          2.5     0.0       0
```

## Log

```
2026-11-12T11:23:42Z run 20261112T112137Z-v33-27b3: variant=v33-auto-date-time data_tag=data-1m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:23:51Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:23:55Z F64: v33-auto-date-time is 79c2f30d-ee15-45f7-92a8-73654d03e1a1, DataTag reads back data-1m-v1
2026-11-12T11:24:14Z F64: model size in memory before the refresh: 0.1 MB
2026-11-12T11:24:14Z F64: refresh started, request 0ddf7c99-9c3a-4f0d-b70b-2e1699bafb37
2026-11-12T11:25:00Z F64: refresh refreshed (Completed) 
2026-11-12T11:25:00Z F64: monitoring database Monitoring KQL database
2026-11-12T11:27:37Z F64: ExecutionMetrics event found
2026-11-12T11:27:39Z F64: model size in memory right after the refresh: 96.2 MB
```
