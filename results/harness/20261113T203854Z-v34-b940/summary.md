# Harness run 20261113T203854Z-v34-b940

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: 1046e620-3ff2-4164-8ef5-30e52bfc2c37
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 723 MB, Power Query 600 MB, duration 1 min, CPU 56 s, rows 2,847,496, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request 96d12812-c47a-4ff1-ac52-8051bcbf9e0d, 2026-11-13T20:41:27.19 to 2026-11-13T20:42:06.76, workspace at 2b9900b, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v34-auto-date-time-no-date-table on F64 data-1m-v1: refreshed, peak 707 MB (2026-11-12T13:48:28Z).
  - Peak change: +16 MB (+2.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-13T20:33:20Z): peak 723 MB vs 602 MB (+121 MB), Power Query 600 MB vs 527 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 25,530 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (24%); F16 5,050 MB: fits (14%); F32 10,170 MB: fits (7%); F64 25,530 MB: fits (3%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  8876d3c4-cd50-45e6-b465-6758c70c6ca0 TabularSequencePoint         35.0     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         34.6    10.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.6    10.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.3    10.7 2349091
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.3     0.0       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          7.3     0.1       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.2     0.0       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          7.1     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.1     6.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.0     5.0       0
                                                                     Commit          2.9     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.3     0.9       0
```

## Log

```
2026-11-13T20:40:57Z run 20261113T203854Z-v34-b940: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:41:07Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:41:08Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1
2026-11-13T20:41:27Z F64: model size in memory before the refresh: 70.3 MB
2026-11-13T20:41:27Z F64: refresh started, request 96d12812-c47a-4ff1-ac52-8051bcbf9e0d
2026-11-13T20:42:12Z F64: refresh refreshed (Completed) 
2026-11-13T20:42:13Z F64: monitoring database Monitoring KQL database
2026-11-13T20:44:49Z F64: ExecutionMetrics event found
2026-11-13T20:44:51Z F64: model size in memory right after the refresh: 96.9 MB
```
