# Harness run 20261110T090544Z-v00-a587

- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: F2, F64
- Expected commit: bd153555c8eb47f0cf31eec9dcf80ab328a24be0
- Notebook run: 61bae2fa-d78d-4849-82a9-e4cf8fc50621
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 26 min, CPU n/a, rows n/a, model 700 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 2fc8c7cd-f6c6-416f-bcf3-a263c7ff1f89, 2026-11-10T09:07:13.243 to 2026-11-10T09:33:16.537, workspace at bd15355, DataTag read back data-10m-v1
- Numbers from: refresh API
- No earlier harness run of v00-baseline on F2 data-10m-v1.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## F64

- Result: **refreshed** 
- Peak 2,116 MB, Power Query 1,584 MB, duration 6 min, CPU 572 s, rows 25,506,840, model 778 MB (Backup step in SemanticModelLogs)
- Refresh request 3e87e877-d52a-4947-b3aa-3b04ce1a6f1a, 2026-11-10T09:33:49.23 to 2026-11-10T09:40:04.273, workspace at bd15355, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v00-baseline on F64 data-10m-v1.
- Measured peak against per-model limits: F2 3,066 MB: fits (69%); F16 5,120 MB: fits (41%); F32 10,240 MB: fits (21%); F64 25,600 MB: fits (8%).

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  e4fb48c3-0f90-4151-94d1-583276edd1bf TabularSequencePoint        359.4     0.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        355.5   109.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        341.9   109.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        340.9   109.6 23719935
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         57.1    66.5        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         56.0    55.9        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         27.3    13.5        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         22.8    13.5        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData         20.6    13.2  1679846
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql         13.0     0.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment          6.0    11.4        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          3.9     0.0        0
```

## Log

```
2026-11-10T09:06:28Z run 20261110T090544Z-v00-a587: variant=v00-baseline data_tag=data-10m-v1 targets=['F2', 'F64'] expected_commit=bd153555c8eb47f0cf31eec9dcf80ab328a24be0
2026-11-10T09:06:35Z F2: update from Git cff49756f0f505e68d63aeaeb620a2a56897e44b -> bd153555c8eb47f0cf31eec9dcf80ab328a24be0
2026-11-10T09:07:01Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-10m-v1
2026-11-10T09:07:05Z F64: workspace already at bd153555c8eb47f0cf31eec9dcf80ab328a24be0
2026-11-10T09:07:07Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-10m-v1
2026-11-10T09:07:13Z F2: refresh started, request 2fc8c7cd-f6c6-416f-bcf3-a263c7ff1f89
2026-11-10T09:33:28Z F2: refresh refreshed (Completed) 
2026-11-10T09:33:49Z F64: refresh started, request 3e87e877-d52a-4947-b3aa-3b04ce1a6f1a
2026-11-10T09:40:31Z F64: refresh refreshed (Completed) 
2026-11-10T09:42:07Z F64: ExecutionMetrics event found
```
