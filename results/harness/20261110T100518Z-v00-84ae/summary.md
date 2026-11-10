# Harness run 20261110T100518Z-v00-84ae

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 19840ea46b9d6c5070fb918196d266c1cfb546c6
- Notebook run: f9e7159b-1af5-49b7-beee-46fafcbe8dc5
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 698 MB, Power Query 419 MB, duration 1 min, CPU 71 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request a161f287-2a01-473e-bb90-1e16d5fa34a6, 2026-11-10T10:06:35.893 to 2026-11-10T10:07:30.007, workspace at 19840ea, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 623 MB (2026-11-10T08:52:36Z).
  - Peak change: +75 MB (+12.0%). **FLAG: peak changed by more than 1%**
- Measured peak against per-model limits: F2 3,066 MB: fits (23%); F16 5,120 MB: fits (14%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%).

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    e4fb48c3-0f90-4151-94d1-583276edd1bf TabularSequencePoint         46.9     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         46.4    12.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         44.9    12.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         44.6    12.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.7     7.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.6     6.5       0
                                                                                       Commit          4.3     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.9     1.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.0     1.0  104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.0     1.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.0     0.3       0
```

## Log

```
2026-11-10T10:06:14Z run 20261110T100518Z-v00-84ae: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=19840ea46b9d6c5070fb918196d266c1cfb546c6
2026-11-10T10:06:28Z F64: workspace already at 19840ea46b9d6c5070fb918196d266c1cfb546c6
2026-11-10T10:06:30Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-10T10:06:36Z F64: refresh started, request a161f287-2a01-473e-bb90-1e16d5fa34a6
2026-11-10T10:07:46Z F64: refresh refreshed (Completed) 
2026-11-10T10:09:22Z F64: ExecutionMetrics event found
```
