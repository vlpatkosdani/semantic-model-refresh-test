# Harness run 20261113T202951Z-v00-0956

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: cb20a2a2-45d3-4486-9c34-1d2fe633636b
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 602 MB, Power Query 527 MB, duration 1 min, CPU 94 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request ead2ac07-a83f-4425-9d40-c66d49c8809c, 2026-11-13T20:30:30.207 to 2026-11-13T20:31:32.867, workspace at 2b9900b, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 856 MB (2026-11-13T09:39:05Z).
  - Peak change: -254 MB (-29.7%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         54.2     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         53.6    18.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         50.2    18.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         49.9    17.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.6     9.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.4     8.4       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.8     1.8       0
                                                                                       Commit          4.7     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.4     0.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          3.2     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.1     1.8       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          3.0     0.0       0
```

## Log

```
2026-11-13T20:30:11Z run 20261113T202951Z-v00-0956: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:30:18Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T20:30:19Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1
2026-11-13T20:30:30Z F64: model size in memory before the refresh: 66.2 MB
2026-11-13T20:30:30Z F64: refresh started, request ead2ac07-a83f-4425-9d40-c66d49c8809c
2026-11-13T20:31:41Z F64: refresh refreshed (Completed) 
2026-11-13T20:31:41Z F64: monitoring database Monitoring KQL database
2026-11-13T20:32:31Z F64: ExecutionMetrics event found
2026-11-13T20:33:21Z F64: model size in memory right after the refresh: 92.7 MB
```
