# Harness run 20261110T084647Z-v00-0d16

- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2, F64
- Expected commit: 8d84b60cdbe0cd2ba7d5133827155a3fbd18995e
- Notebook run: 0386f951-040d-40d5-b29d-83ee3757251d
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 588e92d2-3f8a-4bc5-a636-da7fff37c1ee, 2026-11-10T08:47:50.333 to 2026-11-10T08:48:57.517, workspace at 8d84b60, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v00-baseline on F2 data-1m-v1.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## F64

- Result: **refreshed** 
- Peak 623 MB, Power Query 599 MB, duration 1 min, CPU 57 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 57774314-6c37-4f0f-90aa-0e4a420af223, 2026-11-10T08:49:11.4 to 2026-11-10T08:49:52.54, workspace at 8d84b60, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 551 MB (2026-11-07T20:02:45Z).
  - Peak change: +72 MB (+13.1%). **FLAG: peak changed by more than 1%**
- Measured peak against per-model limits: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%).

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    e4fb48c3-0f90-4151-94d1-583276edd1bf TabularSequencePoint         36.3     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.0    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.4    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.2    10.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.0     5.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.8     4.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.1     0.9       0
                                                                                       Commit          2.5     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.3     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          2.1     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.7     0.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.7     0.8       0
```

## Log

```
2026-11-10T08:47:31Z run 20261110T084647Z-v00-0d16: variant=v00-baseline data_tag=data-1m-v1 targets=['F2', 'F64'] expected_commit=8d84b60cdbe0cd2ba7d5133827155a3fbd18995e
2026-11-10T08:47:36Z F2: workspace already at 8d84b60cdbe0cd2ba7d5133827155a3fbd18995e
2026-11-10T08:47:38Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1
2026-11-10T08:47:42Z F64: workspace already at 8d84b60cdbe0cd2ba7d5133827155a3fbd18995e
2026-11-10T08:47:46Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-10T08:47:50Z F2: refresh started, request 588e92d2-3f8a-4bc5-a636-da7fff37c1ee
2026-11-10T08:49:00Z F2: refresh refreshed (Completed) 
2026-11-10T08:49:11Z F64: refresh started, request 57774314-6c37-4f0f-90aa-0e4a420af223
2026-11-10T08:49:56Z F64: refresh refreshed (Completed) 
2026-11-10T08:52:35Z F64: ExecutionMetrics event found
```
