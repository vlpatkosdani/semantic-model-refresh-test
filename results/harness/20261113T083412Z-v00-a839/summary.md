# Harness run 20261113T083412Z-v00-a839

- Task: refresh
- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: c3e551b10fc0214fbbde513336790cf1ca3cb685
- Notebook run: 0c79a359-527c-438f-af36-5abc6a45bd65
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,650 MB, Power Query 1,192 MB, duration 6 min, CPU 583 s, rows 25,506,840, model 778 MB (Backup step in SemanticModelLogs)
- Refresh request ea5335a0-bb8e-4e04-9042-c0f1e61ac403, 2026-11-13T08:35:11.513 to 2026-11-13T08:41:30.857, workspace at c3e551b, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-10m-v1: refreshed, peak 1,979 MB (2026-11-12T13:00:41Z).
  - Peak change: -329 MB (-16.6%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (55%); F16 5,054 MB: fits (33%); F32 10,174 MB: fits (16%); F64 25,534 MB: fits (6%); PPU 102,334 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint        363.7     0.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        359.3   108.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        351.1   108.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        349.8   108.7 23719935
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         62.2    70.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         60.9    60.4        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         27.1    12.9        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         23.5    12.9        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData         21.6    12.6  1679846
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          8.2     0.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment          5.8    10.8        0
                                         Customer.Name       TabularRefresh          4.3     0.0        0
```

## Log

```
2026-11-13T08:34:47Z run 20261113T083412Z-v00-a839: variant=v00-baseline data_tag=data-10m-v1 targets=['F64'] expected_commit=c3e551b10fc0214fbbde513336790cf1ca3cb685
2026-11-13T08:34:54Z F64: workspace already at c3e551b10fc0214fbbde513336790cf1ca3cb685
2026-11-13T08:34:57Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-10m-v1
2026-11-13T08:35:11Z F64: model size in memory before the refresh: 66.2 MB
2026-11-13T08:35:11Z F64: refresh started, request ea5335a0-bb8e-4e04-9042-c0f1e61ac403
2026-11-13T08:41:53Z F64: refresh refreshed (Completed) 
2026-11-13T08:41:53Z F64: monitoring database Monitoring KQL database
2026-11-13T08:42:43Z F64: ExecutionMetrics event found
2026-11-13T08:43:02Z F64: model size in memory right after the refresh: 700.0 MB
```
