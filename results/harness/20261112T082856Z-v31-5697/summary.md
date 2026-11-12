# Harness run 20261112T082856Z-v31-5697

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
- Notebook run: 51e93f04-f998-4543-b3b5-24d3d9cbec3f
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 913 MB, Power Query 334 MB, duration 1 min, CPU 91 s, rows 77,732,052, model 223 MB (Backup step in SemanticModelLogs)
- Refresh request de34f46c-2bdc-4701-a0f2-a4455e978c38, 2026-11-12T08:31:33.623 to 2026-11-12T08:32:28.683, workspace at 251a9b2, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v31-calc-columns-row on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-11T19:50:47Z): peak 913 MB vs 608 MB (+305 MB), Power Query 334 MB vs 335 MB, model 223 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (30%); F16 5,120 MB: fits (18%); F32 10,240 MB: fits (9%); F64 25,600 MB: fits (4%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18 TabularSequencePoint         46.8     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.2    12.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.0    12.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.7    12.6 2349091
                                  Sales.Order Line Key       TabularRefresh          7.0     2.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.3     7.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.0     4.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.4     0.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment          1.6     2.4       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.9       0
                                   Sales.Order Weekday       TabularRefresh          1.3     1.3       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.8  104990
```

## Log

```
2026-11-12T08:31:01Z run 20261112T082856Z-v31-5697: variant=v31-calc-columns-row data_tag=data-1m-v1 targets=['F64'] expected_commit=251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
2026-11-12T08:31:09Z F64: workspace already at 251a9b2c2ed66a487c46419cbcf5ee015f4c8b8a
2026-11-12T08:31:13Z F64: v31-calc-columns-row is 3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18, DataTag reads back data-1m-v1
2026-11-12T08:31:33Z F64: model size in memory before the refresh: 0.1 MB
2026-11-12T08:31:33Z F64: refresh started, request de34f46c-2bdc-4701-a0f2-a4455e978c38
2026-11-12T08:32:44Z F64: refresh refreshed (Completed) 
2026-11-12T08:32:44Z F64: monitoring database Monitoring KQL database
2026-11-12T08:34:22Z F64: ExecutionMetrics event found
2026-11-12T08:34:25Z F64: model size in memory right after the refresh: 316.8 MB
```
