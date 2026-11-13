# Harness run 20261113T102051Z-v19-8b99

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
- Notebook run: b41bec40-8aa6-4aa5-8473-cb42b7cea286
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (M evaluation memory limit)
- Peak 22,186 MB, Power Query 22,066 MB, duration 23 min, CPU 5,440 s, rows 2,563,048, model 0 MB (Backup step in XMLA trace)
- Refresh request eab24a0b-6548-4258-adcf-5e5bbd057938, 2026-11-13T10:23:50.05 to 2026-11-13T10:47:19.4, workspace at ?, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v19-pq-heavy-10m on PPU data-1m-v1.
- No v00-baseline harness run with a measured peak on PPU data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (724%); F16 5,120 MB: OVER (433%); F32 10,240 MB: OVER (217%); F64 25,600 MB: fits (87%); PPU 102,400 MB: fits (22%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 18484.
Used features: (none).;Container exited unexpectedly with code 0x0000DEAD. PID: 18484.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 18484.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 18484..
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
```

Slowest steps:

```
                                                Object OperationDetailName  DurationSec  CpuSec    Rows
                       PQ Basket Pairs.PQ Basket Pairs          ExecuteSql        994.0     0.0       0
                       PQ Basket Pairs.PQ Basket Pairs      TabularRefresh        994.0     0.0       0
             PQ Customer Segments.PQ Customer Segments      TabularRefresh        541.6     0.1       0
             PQ Customer Segments.PQ Customer Segments          ExecuteSql        541.4     0.0       0
       PQ Top Products by Year.PQ Top Products by Year      TabularRefresh        175.9     0.1       0
       PQ Top Products by Year.PQ Top Products by Year          ExecuteSql        175.8     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      TabularRefresh        103.3    27.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             Process        101.9    27.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba            ReadData        101.0    27.2 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba   AnalyzeEncodeData         13.5    14.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba            VertiPaq         13.1    13.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          5.4     2.3       0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v19-pq-heavy-10m-m-evaluation-memory.png**

## Log

```
2026-11-13T10:23:18Z run 20261113T102051Z-v19-8b99: variant=v19-pq-heavy-10m data_tag=data-1m-v1 targets=['PPU'] expected_commit=11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T10:23:21Z PPU: not connected to Git; the model there is the one published by hand
2026-11-13T10:23:23Z PPU: v19-pq-heavy-10m is 99a77495-b6bb-4d74-8f12-ae64302e01ab, DataTag reads back data-1m-v1
2026-11-13T10:23:46Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-13T10:23:49Z PPU: trace started (full)
2026-11-13T10:23:50Z PPU: refresh started, request eab24a0b-6548-4258-adcf-5e5bbd057938
2026-11-13T10:47:35Z PPU: refresh failed (Failed) M evaluation memory limit
2026-11-13T10:48:06Z PPU: trace captured 334 events: ProgressReportEnd 290, ExecutionMetrics 28, CommandEnd 11, Error 5
```
