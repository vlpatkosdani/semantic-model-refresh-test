# Harness run 20261110T131904Z-v23-8705

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: ee5050bd97225153e7d3e555e414d49995893af6
- Notebook run: 36fc0e79-7872-4911-a086-314786088d78
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,406 MB, Power Query 721 MB, duration 1 min, CPU 84 s, rows 16,549,502, model 184 MB (Backup step in SemanticModelLogs)
- Refresh request e692db98-2193-4a58-bbdb-871111b5d6e1, 2026-11-10T13:22:13.107 to 2026-11-10T13:23:07.81, workspace at ee5050b, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v23-dax-calc-tables on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-10T10:09:23Z): peak 1,406 MB vs 698 MB (+708 MB), Power Query 721 MB vs 419 MB, model 184 MB vs 73 MB.
- Measured peak against per-model limits: F2 3,066 MB: fits (46%); F16 5,120 MB: fits (27%); F32 10,240 MB: fits (14%); F64 25,600 MB: fits (5%).

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            c0fbb6a6-e33c-4f6b-809e-9fc48ad57573 TabularSequencePoint         44.6     0.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.5    11.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.6    11.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.4    11.0 2349091
                           Sales Copy.Sales Copy       TabularRefresh          8.3     6.9       0
                           Sales Copy.Sales Copy              Process          6.1     5.8       0
                           Sales Copy.Sales Copy             ReadData          5.9     5.8 2349091
             Product Date Grid.Product Date Grid             VertiPaq          5.4     5.4       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.4     6.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.3     5.3       0
             Product Date Grid.Product Date Grid              Process          4.8     4.4       0
             Product Date Grid.Product Date Grid       TabularRefresh          4.8     4.4       0
```

## Log

```
2026-11-10T13:21:34Z run 20261110T131904Z-v23-8705: variant=v23-dax-calc-tables data_tag=data-1m-v1 targets=['F64'] expected_commit=ee5050bd97225153e7d3e555e414d49995893af6
2026-11-10T13:21:44Z F64: workspace already at ee5050bd97225153e7d3e555e414d49995893af6
2026-11-10T13:22:00Z F64: v23-dax-calc-tables is c0fbb6a6-e33c-4f6b-809e-9fc48ad57573, DataTag reads back data-1m-v1
2026-11-10T13:22:13Z F64: refresh started, request e692db98-2193-4a58-bbdb-871111b5d6e1
2026-11-10T13:23:23Z F64: refresh refreshed (Completed) 
2026-11-10T13:24:59Z F64: ExecutionMetrics event found
```
