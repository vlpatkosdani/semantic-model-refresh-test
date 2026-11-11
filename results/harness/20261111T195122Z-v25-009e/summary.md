# Harness run 20261111T195122Z-v25-009e

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 53cfca4864e70f1fda420adacf9ab5955bb08783
- Notebook run: 63ab626a-83ba-4aec-bda1-f4f67d8a11b9
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 614 MB, Power Query 457 MB, duration 1 min, CPU 69 s, rows 3,611,040, model 79 MB (Backup step in SemanticModelLogs)
- Refresh request 66ece1e4-7bb2-4a07-a93a-dd18e68f82c3, 2026-11-11T19:52:03.677 to 2026-11-11T19:52:48.603, workspace at 53cfca4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v25-many-to-many on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-11T19:50:47Z): peak 614 MB vs 608 MB (+6 MB), Power Query 457 MB vs 335 MB, model 79 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                                  93317245-89ef-4014-abe3-f82efec8ba78 TabularSequencePoint         39.3     0.0       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         38.9    12.0       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.8    12.0       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         35.5    12.0 2349091
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637       TabularRefresh          6.2     2.7       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637              Process          4.8     2.7       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637             ReadData          4.6     2.6 1049900
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.5     5.4       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.4     4.4       0
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.3     1.2       0
                                                                                     Commit          3.2     0.0       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          3.0     0.0       0
```

## Log

```
2026-11-11T19:51:44Z run 20261111T195122Z-v25-009e: variant=v25-many-to-many data_tag=data-1m-v1 targets=['F64'] expected_commit=53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T19:51:50Z F64: workspace already at 53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T19:51:52Z F64: v25-many-to-many is 93317245-89ef-4014-abe3-f82efec8ba78, DataTag reads back data-1m-v1
2026-11-11T19:52:03Z F64: model size in memory before the refresh: 0.0 MB
2026-11-11T19:52:03Z F64: refresh started, request 66ece1e4-7bb2-4a07-a93a-dd18e68f82c3
2026-11-11T19:52:49Z F64: refresh refreshed (Completed) 
2026-11-11T19:52:49Z F64: monitoring database Monitoring KQL database
2026-11-11T19:55:25Z F64: ExecutionMetrics event found
2026-11-11T19:55:27Z F64: model size in memory right after the refresh: 98.1 MB
```
