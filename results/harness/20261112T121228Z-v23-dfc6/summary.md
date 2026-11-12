# Harness run 20261112T121228Z-v23-dfc6

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 8ecf2e76-7468-418e-bc6b-8a84c8619790
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,062 MB, Power Query 1,870 MB, duration 7 min, CPU 809 s, rows 75,922,895, model 1,387 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 1f712195-59f9-4a74-861c-6ccf84178f13, 2026-11-12T12:16:18.897 to 2026-11-12T12:24:14.11, workspace at 5c382cc, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v23-dax-calc-tables on F64 data-10m-v1: refreshed, peak 13,139 MB (2026-11-12T12:11:24Z).
  - Peak change: -77 MB (-0.6%).
- No v00-baseline harness run with a measured peak on F64 data-10m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB (after clearValues). The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (426%); F16 5,120 MB: OVER (255%); F32 10,240 MB: OVER (128%); F64 25,600 MB: fits (51%); PPU 102,400 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  247f4e17-b0ab-46b0-9657-92e852883e58 TabularSequencePoint        448.2     0.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        354.4   107.5        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        350.9   107.5        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        349.7   107.5 23719935
                                 Sales Copy.Sales Copy       TabularRefresh         85.5    68.8        0
                                 Sales Copy.Sales Copy              Process         59.2    56.2        0
                                 Sales Copy.Sales Copy             ReadData         56.3    56.2 23719935
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         55.2    64.5        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         53.9    53.9        0
                           Sales Summary.Sales Summary       TabularRefresh         50.2    33.9        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         25.3    14.2        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         24.0    14.2        0
```

## Log

```
2026-11-12T12:15:03Z run 20261112T121228Z-v23-dfc6: variant=v23-dax-calc-tables data_tag=data-10m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T12:15:13Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T12:15:14Z F64: v23-dax-calc-tables is 247f4e17-b0ab-46b0-9657-92e852883e58, DataTag reads back data-10m-v1
2026-11-12T12:15:37Z F64: model size in memory before the refresh: 1380.7 MB
2026-11-12T12:15:37Z F64: refresh started, request fb913ef3-fed8-47c4-bb41-a981d5092a4d
2026-11-12T12:15:48Z F64: refresh refreshed (Completed) 
2026-11-12T12:16:18Z F64: model size after clearValues: 0.1 MB
2026-11-12T12:16:19Z F64: refresh started, request 1f712195-59f9-4a74-861c-6ccf84178f13
2026-11-12T12:24:42Z F64: refresh refreshed (Completed) 
2026-11-12T12:24:42Z F64: monitoring database Monitoring KQL database
2026-11-12T12:25:33Z F64: ExecutionMetrics event found
2026-11-12T12:27:44Z F64: model size in memory right after the refresh: 1386.8 MB
```
