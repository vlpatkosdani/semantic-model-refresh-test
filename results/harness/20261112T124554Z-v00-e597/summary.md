# Harness run 20261112T124554Z-v00-e597

- Task: refresh
- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: 6bbfb2927c8f84faaa5079ff221dbf194f7def02
- Notebook run: a2bd92b2-30de-4c13-ad78-2405f44bb583
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,979 MB, Power Query 1,391 MB, duration 10 min, CPU 1,009 s, rows 25,506,840, model 778 MB (Backup step in SemanticModelLogs)
- Refresh request e0954f44-67d6-47fa-8371-e0e8801dbc94, 2026-11-12T12:48:33.697 to 2026-11-12T12:58:48.42, workspace at 6bbfb29, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v00-baseline on F64 data-10m-v1.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (66%); F16 5,054 MB: fits (39%); F32 10,174 MB: fits (19%); F64 25,534 MB: fits (8%); PPU 102,334 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint        593.4     0.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        585.7   182.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        577.9   182.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        575.1   182.0 23719935
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        132.3   144.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        130.5   130.0        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         47.1    26.2        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         43.8    26.2        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData         39.7    25.6  1679846
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment          9.2    17.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.7     0.0        0
                                         Customer.Name       TabularRefresh          7.5     0.0        0
```

## Log

```
2026-11-12T12:48:04Z run 20261112T124554Z-v00-e597: variant=v00-baseline data_tag=data-10m-v1 targets=['F64'] expected_commit=6bbfb2927c8f84faaa5079ff221dbf194f7def02
2026-11-12T12:48:12Z F64: workspace already at 6bbfb2927c8f84faaa5079ff221dbf194f7def02
2026-11-12T12:48:15Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-10m-v1
2026-11-12T12:48:33Z F64: model size in memory before the refresh: 66.2 MB
2026-11-12T12:48:33Z F64: refresh started, request e0954f44-67d6-47fa-8371-e0e8801dbc94
2026-11-12T12:59:16Z F64: refresh refreshed (Completed) 
2026-11-12T12:59:16Z F64: monitoring database Monitoring KQL database
2026-11-12T13:00:07Z F64: ExecutionMetrics event found
2026-11-12T13:00:43Z F64: model size in memory right after the refresh: 700.0 MB
```
