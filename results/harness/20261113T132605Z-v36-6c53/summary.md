# Harness run 20261113T132605Z-v36-6c53

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: c06482c5a6d6dfa4182241a8607629fcd3c8179c
- Notebook run: 0f572ddb-3333-4620-b850-51137fe2485f
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 14,759 MB, Power Query 1,194 MB, duration 7 min, CPU 826 s, rows 78,870,826, model 1,406 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 757c5372-6ad1-4517-b219-e9b8ac8d9642, 2026-11-13T13:27:18.05 to 2026-11-13T13:35:09.067, workspace at c06482c, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v36-calc-summary-month-grain on F64 data-10m-v1.
- Against v00-baseline on F64 data-10m-v1 (2026-11-13T08:43:01Z): peak 14,759 MB vs 1,650 MB (+13,109 MB), Power Query 1,194 MB vs 1,192 MB, model 1,406 MB vs 778 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (481%); F16 5,120 MB: OVER (288%); F32 10,240 MB: OVER (144%); F64 25,600 MB: fits (58%); PPU 102,400 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  9ab77bda-e29b-4924-9f6e-10b460e7f7c4 TabularSequencePoint        441.7     0.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        343.6   108.4        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        340.0   108.3        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        338.7   108.3 23719935
                                 Sales Copy.Sales Copy       TabularRefresh         89.4    67.3        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         65.1    73.7        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         64.0    63.9        0
                                 Sales Copy.Sales Copy              Process         62.8    54.8        0
                           Sales Summary.Sales Summary       TabularRefresh         61.0    41.3        0
                                 Sales Copy.Sales Copy             ReadData         54.8    54.8 23719935
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         27.1    14.4        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         25.3    14.4        0
```

## Log

```
2026-11-13T13:26:51Z run 20261113T132605Z-v36-6c53: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 targets=['F64'] expected_commit=c06482c5a6d6dfa4182241a8607629fcd3c8179c
2026-11-13T13:27:01Z F64: workspace already at c06482c5a6d6dfa4182241a8607629fcd3c8179c
2026-11-13T13:27:03Z F64: v36-calc-summary-month-grain is 9ab77bda-e29b-4924-9f6e-10b460e7f7c4, DataTag reads back data-10m-v1
2026-11-13T13:27:17Z F64: model size in memory before the refresh: 0.1 MB
2026-11-13T13:27:18Z F64: refresh started, request 757c5372-6ad1-4517-b219-e9b8ac8d9642
2026-11-13T13:35:30Z F64: refresh refreshed (Completed) 
2026-11-13T13:35:30Z F64: monitoring database Monitoring KQL database
2026-11-13T13:36:20Z F64: ExecutionMetrics event found
2026-11-13T13:38:32Z F64: model size in memory right after the refresh: 1406.2 MB
```
