# Harness run 20261111T204204Z-v28-3f3b

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 7c87ac648b9c75b83006c9aaf05fa1d3c8d7970f
- Notebook run: 10e90a8c-7a9b-4a81-a85b-a834c911ac4f
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 777 MB, Power Query 629 MB, duration 1 min, CPU 108 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request 1e0b61f3-d0cb-4b7b-8e5a-06dd0efb9a09, 2026-11-11T20:43:10.883 to 2026-11-11T20:44:15.017, workspace at 7c87ac6, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v28-types-all-text on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-11T19:50:47Z): peak 777 MB vs 608 MB (+169 MB), Power Query 629 MB vs 335 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (25%); F16 5,120 MB: fits (15%); F32 10,240 MB: fits (8%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    bc793114-53e1-4476-8e50-c4b0c5b15603 TabularSequencePoint         55.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         52.3    30.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         50.1    30.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         49.7    30.0 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.7     9.7       0
                                                                                       Commit          4.5     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.6     1.9       0
                                                      Sales.Order Number       TabularRefresh          3.0     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.5     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.4     1.8  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.3     0.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.0     0.0       0
```

## Log

```
2026-11-11T20:42:47Z run 20261111T204204Z-v28-3f3b: variant=v28-types-all-text data_tag=data-1m-v1 targets=['F64'] expected_commit=7c87ac648b9c75b83006c9aaf05fa1d3c8d7970f
2026-11-11T20:42:58Z F64: workspace already at 7c87ac648b9c75b83006c9aaf05fa1d3c8d7970f
2026-11-11T20:42:59Z F64: v28-types-all-text is bc793114-53e1-4476-8e50-c4b0c5b15603, DataTag reads back data-1m-v1
2026-11-11T20:43:10Z F64: model size in memory before the refresh: 0.1 MB
2026-11-11T20:43:11Z F64: refresh started, request 1e0b61f3-d0cb-4b7b-8e5a-06dd0efb9a09
2026-11-11T20:44:21Z F64: refresh refreshed (Completed) 
2026-11-11T20:44:21Z F64: monitoring database Monitoring KQL database
2026-11-11T20:45:57Z F64: ExecutionMetrics event found
2026-11-11T20:45:59Z F64: model size in memory right after the refresh: 171.5 MB
```
