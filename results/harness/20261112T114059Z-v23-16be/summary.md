# Harness run 20261112T114059Z-v23-16be

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 2f0c71a8-9a2d-4d1a-970c-022c944a678b
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,064 MB, Power Query 1,708 MB, duration 8 min, CPU 850 s, rows 75,922,895, model 1,379 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 38e57dc2-9061-4d60-a7ed-7827910b9f03, 2026-11-12T11:43:37.847 to 2026-11-12T11:52:04.733, workspace at 5c382cc, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v23-dax-calc-tables on F64 data-10m-v1.
- No v00-baseline harness run with a measured peak on F64 data-10m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (426%); F16 5,120 MB: OVER (255%); F32 10,240 MB: OVER (128%); F64 25,600 MB: fits (51%); PPU 102,400 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  247f4e17-b0ab-46b0-9657-92e852883e58 TabularSequencePoint        474.7     0.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        366.6   109.3        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        351.9   109.3        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        350.8   109.2 23719935
                                 Sales Copy.Sales Copy       TabularRefresh         99.1    78.2        0
                           Sales Summary.Sales Summary       TabularRefresh         61.4    39.8        0
                                 Sales Copy.Sales Copy              Process         61.2    58.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         60.9    70.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         59.6    59.6        0
                                 Sales Copy.Sales Copy             ReadData         58.7    58.6 23719935
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         27.6    12.8        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         22.8    12.8        0
```

## Log

```
2026-11-12T11:43:08Z run 20261112T114059Z-v23-16be: variant=v23-dax-calc-tables data_tag=data-10m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:43:17Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:43:20Z F64: v23-dax-calc-tables is 247f4e17-b0ab-46b0-9657-92e852883e58, DataTag reads back data-10m-v1
2026-11-12T11:43:37Z F64: model size in memory before the refresh: 0.1 MB
2026-11-12T11:43:37Z F64: refresh started, request 38e57dc2-9061-4d60-a7ed-7827910b9f03
2026-11-12T11:52:19Z F64: refresh refreshed (Completed) 
2026-11-12T11:52:20Z F64: monitoring database Monitoring KQL database
2026-11-12T11:53:56Z F64: ExecutionMetrics event found
2026-11-12T11:56:09Z F64: model size in memory right after the refresh: 1378.9 MB
```
