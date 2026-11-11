# Harness run 20261111T081746Z-v99h-601b

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: ebcf68eeb3375e67bdd3b2b0873aa3a1a20d2f9f
- Notebook run: bfc2023e-bb91-48e2-bd2b-773577e1c4d1
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 25,971 MB, Power Query 25,814 MB, duration 34 min, CPU 7,148 s, rows 38,422,496, model 534 MB (Backup step in XMLA trace)
- Refresh request 66b61eb2-86c7-4911-9a13-2cff55ceea86, 2026-11-11T08:20:25.707 to 2026-11-11T08:55:05.19, workspace at ?, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99h-staging-buffers on PPU data-1m-v1.
- No v00-baseline harness run with a measured peak on PPU data-1m-v1 to compare with.
- Measured peak against per-model limits: F2 3,066 MB: OVER (847%); F16 5,120 MB: OVER (507%); F32 10,240 MB: OVER (254%); F64 25,600 MB: OVER (101%); PPU 102,400 MB: fits (25%).

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            fbca0670-b932-46b9-848d-2249ba6eb4be TabularSequencePoint       2064.4     0.5       0
                           Sales Flat.Sales Flat       TabularRefresh       2031.7   109.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1858.6    33.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1347.3    33.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1346.9    33.6 2349091
                           Sales Flat.Sales Flat              Process       1307.0   109.0       0
                           Sales Flat.Sales Flat             ReadData       1305.9   109.0 2349091
                           Sales Flat.Sales Flat           ExecuteSql        724.5     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        539.0     3.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        511.2     0.0       0
                   Customer Stats.Customer Stats           ExecuteSql        341.9     0.0       0
                   Customer Stats.Customer Stats              Process        196.9     3.1       0
```

## Log

```
2026-11-11T08:20:01Z run 20261111T081746Z-v99h-601b: variant=v99h-staging-buffers data_tag=data-1m-v1 targets=['PPU'] expected_commit=ebcf68eeb3375e67bdd3b2b0873aa3a1a20d2f9f
2026-11-11T08:20:04Z PPU: not connected to Git; the model there is the one published by hand
2026-11-11T08:20:07Z PPU: v99h-staging-buffers is fbca0670-b932-46b9-848d-2249ba6eb4be, DataTag reads back data-1m-v1
2026-11-11T08:20:25Z PPU: trace started (full)
2026-11-11T08:20:25Z PPU: refresh started, request 66b61eb2-86c7-4911-9a13-2cff55ceea86
2026-11-11T08:55:14Z PPU: refresh refreshed (Completed) 
2026-11-11T08:55:46Z PPU: trace captured 834 events: ProgressReportEnd 799, ExecutionMetrics 24, CommandEnd 11
```
