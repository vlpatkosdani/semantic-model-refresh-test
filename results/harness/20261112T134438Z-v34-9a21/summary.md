# Harness run 20261112T134438Z-v34-9a21

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: b1660a09614e780473f21788f5ae8523db531ca7
- Notebook run: 6ddd975b-8eed-424d-9fa3-47042a325f8a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 707 MB, Power Query 421 MB, duration 1 min, CPU 99 s, rows 2,847,496, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request 6bef8c14-71a8-4fe0-adce-5ba4e556822c, 2026-11-12T13:45:40.117 to 2026-11-12T13:46:48.777, workspace at b1660a0, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v34-auto-date-time-no-date-table on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-11T19:50:47Z): peak 707 MB vs 608 MB (+99 MB), Power Query 421 MB vs 335 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (23%); F16 5,120 MB: fits (14%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8876d3c4-cd50-45e6-b465-6758c70c6ca0 TabularSequencePoint         59.1     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.4    18.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         56.6    18.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         54.9    18.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.1    13.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.0    12.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.2     1.5       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.2     0.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.9     1.5       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     1.4  104990
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.7     0.1       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          2.4     0.0       0
```

## Log

```
2026-11-12T13:45:17Z run 20261112T134438Z-v34-9a21: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 targets=['F64'] expected_commit=b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T13:45:23Z F64: workspace already at b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T13:45:25Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1
2026-11-12T13:45:39Z F64: model size in memory before the refresh: 0.1 MB
2026-11-12T13:45:40Z F64: refresh started, request 6bef8c14-71a8-4fe0-adce-5ba4e556822c
2026-11-12T13:46:50Z F64: refresh refreshed (Completed) 
2026-11-12T13:46:50Z F64: monitoring database Monitoring KQL database
2026-11-12T13:48:26Z F64: ExecutionMetrics event found
2026-11-12T13:48:29Z F64: model size in memory right after the refresh: 96.9 MB
```
