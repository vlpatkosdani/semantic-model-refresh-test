# Harness run 20261113T122445Z-v35-6ea1

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: 84eec03d6783862abe025992ee8312ed583ff855
- Notebook run: 08db0141-5a4e-4df0-9fe8-01f1065130d6
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,063 MB, Power Query 1,601 MB, duration 17 min, CPU 1,827 s, rows 147,082,700, model 2,803 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 5ea210c0-0085-4a5c-9f9f-4a5b5386b2d9, 2026-11-13T12:27:34.793 to 2026-11-13T12:46:16.283, workspace at 84eec03, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v35-calc-tables-four-copies on F64 data-10m-v1.
- Against v00-baseline on F64 data-10m-v1 (2026-11-13T08:43:01Z): peak 13,063 MB vs 1,650 MB (+11,413 MB), Power Query 1,601 MB vs 1,192 MB, model 2,803 MB vs 778 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (426%); F16 5,120 MB: OVER (255%); F32 10,240 MB: OVER (128%); F64 25,600 MB: fits (51%); PPU 102,400 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec     Rows
            d4c8e929-5a3c-4171-a267-8dc68a857e76 TabularSequencePoint       1035.5     1.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        563.3   192.7        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        556.1   192.6        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        553.0   192.6 23719935
                           Sales Copy.Sales Copy       TabularRefresh        448.5   410.2        0
                           Sales Copy.Sales Copy              Process        392.8   387.1        0
                           Sales Copy.Sales Copy             ReadData        387.3   387.0 94879740
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        133.5   146.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        131.8   131.7        0
                     Sales Summary.Sales Summary       TabularRefresh         99.2    64.2        0
                           Sales Copy.Sales Copy    AnalyzeEncodeData         63.5   129.9        0
                           Sales Copy.Sales Copy      CompressSegment         62.1   114.0        0
```

## Log

```
2026-11-13T12:27:04Z run 20261113T122445Z-v35-6ea1: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 targets=['F64'] expected_commit=84eec03d6783862abe025992ee8312ed583ff855
2026-11-13T12:27:13Z F64: workspace already at 84eec03d6783862abe025992ee8312ed583ff855
2026-11-13T12:27:15Z F64: v35-calc-tables-four-copies is d4c8e929-5a3c-4171-a267-8dc68a857e76, DataTag reads back data-10m-v1
2026-11-13T12:27:34Z F64: model size in memory before the refresh: 0.1 MB
2026-11-13T12:27:35Z F64: refresh started, request 5ea210c0-0085-4a5c-9f9f-4a5b5386b2d9
2026-11-13T12:46:18Z F64: refresh refreshed (Completed) 
2026-11-13T12:46:18Z F64: monitoring database Monitoring KQL database
2026-11-13T12:47:08Z F64: ExecutionMetrics event found
2026-11-13T12:49:20Z F64: model size in memory right after the refresh: 2803.0 MB
```
