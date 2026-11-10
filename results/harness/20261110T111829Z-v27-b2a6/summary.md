# Harness run 20261110T111829Z-v27-b2a6

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 10c16c38a89d0f2e8a8e67a3194e2559eb728b54
- Notebook run: f844965d-2c8c-4899-bb1d-4fb40cdb8755
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 616 MB, Power Query 336 MB, duration 1 min, CPU 63 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 7e6646c1-b7b1-4811-bf46-d49a196aa9a3, 2026-11-10T11:21:09.85 to 2026-11-10T11:21:56.22, workspace at 10c16c3, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v27-high-cardinality-visuals on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-10T10:09:23Z): peak 616 MB vs 698 MB (-82 MB), Power Query 336 MB vs 419 MB, model 73 MB vs 73 MB.
- Measured peak against per-model limits: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%).

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    ff8802e6-5a2b-475b-a6be-b56e16fe65ca TabularSequencePoint         39.7     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         39.3    11.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         37.6    11.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         37.3    11.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.0     6.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.9     5.9       0
                                                                                       Commit          3.0     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.0     1.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          1.9     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.9     0.4       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          1.8     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          1.8     0.0       0
```

## Log

```
2026-11-10T11:20:47Z run 20261110T111829Z-v27-b2a6: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 targets=['F64'] expected_commit=10c16c38a89d0f2e8a8e67a3194e2559eb728b54
2026-11-10T11:20:57Z F64: workspace already at 10c16c38a89d0f2e8a8e67a3194e2559eb728b54
2026-11-10T11:20:59Z F64: v27-high-cardinality-visuals is ff8802e6-5a2b-475b-a6be-b56e16fe65ca, DataTag reads back data-1m-v1
2026-11-10T11:21:10Z F64: refresh started, request 7e6646c1-b7b1-4811-bf46-d49a196aa9a3
2026-11-10T11:22:20Z F64: refresh refreshed (Completed) 
2026-11-10T11:23:10Z F64: ExecutionMetrics event found
```
