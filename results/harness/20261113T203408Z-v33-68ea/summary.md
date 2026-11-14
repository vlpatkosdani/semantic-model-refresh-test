# Harness run 20261113T203408Z-v33-68ea

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: b8a8134e-d980-49a9-8984-9164aa16ebcc
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 554 MB, Power Query 270 MB, duration 1 min, CPU 97 s, rows 2,791,244, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request e618f5ac-445b-4c9b-b4e4-a820de770e68, 2026-11-13T20:35:05.17 to 2026-11-13T20:36:09.7, workspace at 2b9900b, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v33-auto-date-time on F64 data-1m-v1: refreshed, peak 619 MB (2026-11-12T11:27:38Z).
  - Peak change: -65 MB (-10.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-13T20:33:20Z): peak 554 MB vs 602 MB (-48 MB), Power Query 270 MB vs 527 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 25,530 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (18%); F16 5,050 MB: fits (11%); F32 10,170 MB: fits (5%); F64 25,530 MB: fits (2%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  79c2f30d-ee15-45f7-92a8-73654d03e1a1 TabularSequencePoint         57.3     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         56.6    18.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         54.2    18.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         53.7    18.4 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.9    10.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.7     8.7       0
                                                                     Commit          4.8     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.4     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.4     1.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.3     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.2     1.8  104990
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.0     0.0       0
```

## Log

```
2026-11-13T20:34:45Z run 20261113T203408Z-v33-68ea: variant=v33-auto-date-time data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:34:50Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:34:51Z F64: v33-auto-date-time is 79c2f30d-ee15-45f7-92a8-73654d03e1a1, DataTag reads back data-1m-v1
2026-11-13T20:35:05Z F64: model size in memory before the refresh: 69.7 MB
2026-11-13T20:35:05Z F64: refresh started, request e618f5ac-445b-4c9b-b4e4-a820de770e68
2026-11-13T20:36:15Z F64: refresh refreshed (Completed) 
2026-11-13T20:36:15Z F64: monitoring database Monitoring KQL database
2026-11-13T20:37:51Z F64: ExecutionMetrics event found
2026-11-13T20:38:10Z F64: model size in memory right after the refresh: 96.2 MB
```
