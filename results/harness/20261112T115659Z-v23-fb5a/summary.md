# Harness run 20261112T115659Z-v23-fb5a

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: 5c382cca5f61fa4954dfbf1be212c462e3f11215
- Notebook run: 64d183e2-99a7-4202-b611-6bfdc7334127
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,139 MB, Power Query 1,707 MB, duration 8 min, CPU 878 s, rows 75,922,895, model 1,381 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 465d5b72-1ab2-4ac1-b772-76af479a64d3, 2026-11-12T11:57:53.303 to 2026-11-12T12:06:33.99, workspace at 5c382cc, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v23-dax-calc-tables on F64 data-10m-v1: refreshed, peak 13,064 MB (2026-11-12T11:56:06Z).
  - Peak change: +75 MB (+0.6%).
- No v00-baseline harness run with a measured peak on F64 data-10m-v1 to compare with.
- Model size in memory when the full refresh started: 1,379 MB. The refresh may use the SKU maximum minus this: 24,221 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,687 MB: OVER (779%); F16 3,741 MB: OVER (351%); F32 8,861 MB: OVER (148%); F64 24,221 MB: fits (54%); PPU 101,021 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  247f4e17-b0ab-46b0-9657-92e852883e58 TabularSequencePoint        490.6     0.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        387.2   111.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        384.3   111.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        382.9   111.0 23719935
                                 Sales Copy.Sales Copy       TabularRefresh         94.5    75.5        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         71.5    81.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         70.2    70.1        0
                                 Sales Copy.Sales Copy              Process         65.8    61.9        0
                                 Sales Copy.Sales Copy             ReadData         62.5    61.8 23719935
                           Sales Summary.Sales Summary       TabularRefresh         58.1    39.5        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         25.5    13.1        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         24.3    13.1        0
```

## Log

```
2026-11-12T11:57:37Z run 20261112T115659Z-v23-fb5a: variant=v23-dax-calc-tables data_tag=data-10m-v1 targets=['F64'] expected_commit=5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:57:42Z F64: workspace already at 5c382cca5f61fa4954dfbf1be212c462e3f11215
2026-11-12T11:57:44Z F64: v23-dax-calc-tables is 247f4e17-b0ab-46b0-9657-92e852883e58, DataTag reads back data-10m-v1
2026-11-12T11:57:53Z F64: model size in memory before the refresh: 1378.9 MB
2026-11-12T11:57:53Z F64: refresh started, request 465d5b72-1ab2-4ac1-b772-76af479a64d3
2026-11-12T12:06:35Z F64: refresh refreshed (Completed) 
2026-11-12T12:06:35Z F64: monitoring database Monitoring KQL database
2026-11-12T12:09:14Z F64: ExecutionMetrics event found
2026-11-12T12:11:27Z F64: model size in memory right after the refresh: 1380.7 MB
```
