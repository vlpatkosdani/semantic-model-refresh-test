# Harness run 20261107T195951Z-v00-40ca

- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 77d3b4b575dbfad8cdc1585afc520183f74e8026
- Notebook run: 5923ce6d-0056-4a76-84a3-d53abef28588
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 551 MB, Power Query 312 MB, duration 1 min, CPU 55 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 63d2e1c1-86ad-40d8-baf8-b80dd2fbf69a, 2026-11-07T20:00:28.657 to 2026-11-07T20:01:14.307, workspace at 77d3b4b, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v00-baseline on F64 data-1m-v1.
- Measured peak against per-model limits: F2 3,066 MB: fits (18%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (5%); F64 25,600 MB: fits (2%).

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  e4fb48c3-0f90-4151-94d1-583276edd1bf TabularSequencePoint         40.8     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         40.4    10.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         32.4    10.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         32.2    10.5 2349091
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.8     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.8     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.6     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.0     5.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.0     5.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.8     0.8       0
                                                                     Commit          2.8     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          2.3     0.0       0
```

## Log

```
2026-11-07T20:00:18Z run 20261107T195951Z-v00-40ca: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=77d3b4b575dbfad8cdc1585afc520183f74e8026
2026-11-07T20:00:24Z F64: workspace already at 77d3b4b575dbfad8cdc1585afc520183f74e8026
2026-11-07T20:00:26Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-07T20:00:28Z F64: refresh started, request 63d2e1c1-86ad-40d8-baf8-b80dd2fbf69a
2026-11-07T20:01:39Z F64: refresh refreshed (Completed) 
2026-11-07T20:02:28Z F64: ExecutionMetrics event found
```
