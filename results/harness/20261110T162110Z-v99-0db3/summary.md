# Harness run 20261110T162110Z-v99-0db3

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: e2a41356967dccf8b472e4112e6b35cf2b95207b
- Notebook run: dbdff93c-fc15-4035-bb29-79505429f078
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 26,115 MB, Power Query 25,958 MB, duration 20 min, CPU 4,036 s, rows 40,515,912, model 622 MB (Backup step in XMLA trace; the notebook labelled it SemanticModelLogs, corrected by hand)
- Refresh request 73846a99-0417-43b6-af31-5d31eff48877, 2026-11-10T16:23:50.62 to 2026-11-10T16:43:40.867, workspace at ?, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99-kitchen-sink on PPU data-1m-v1.
- No v00-baseline harness run with a measured peak on PPU data-1m-v1 to compare with.
- Measured peak against per-model limits: F2 3,066 MB: OVER (852%); F16 5,120 MB: OVER (510%); F32 10,240 MB: OVER (255%); F64 25,600 MB: OVER (102%); PPU 102,400 MB: fits (26%).

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            c30a54fc-597b-4dda-b406-9efe7e320643 TabularSequencePoint       1173.9     0.3       0
                           Sales Flat.Sales Flat       TabularRefresh       1134.9    68.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1111.5    22.4       0
                           Sales Flat.Sales Flat           ExecuteSql        720.2     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        616.9    22.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        616.7    22.3 2349091
                   Customer Stats.Customer Stats       TabularRefresh        559.6     2.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        494.6     0.0       0
                           Sales Flat.Sales Flat              Process        414.5    68.3       0
                           Sales Flat.Sales Flat             ReadData        414.1    68.2 2349091
                   Customer Stats.Customer Stats           ExecuteSql        311.8     0.0       0
                   Customer Stats.Customer Stats              Process        247.7     2.5       0
```

## Log

```
2026-11-10T16:23:27Z run 20261110T162110Z-v99-0db3: variant=v99-kitchen-sink data_tag=data-1m-v1 targets=['PPU'] expected_commit=e2a41356967dccf8b472e4112e6b35cf2b95207b
2026-11-10T16:23:29Z PPU: not connected to Git; the model there is the one published by hand
2026-11-10T16:23:30Z PPU: v99-kitchen-sink is c30a54fc-597b-4dda-b406-9efe7e320643, DataTag reads back data-1m-v1
2026-11-10T16:23:50Z PPU: trace started (full)
2026-11-10T16:23:50Z PPU: refresh started, request 73846a99-0417-43b6-af31-5d31eff48877
2026-11-10T16:44:04Z PPU: refresh refreshed (Completed) 
2026-11-10T16:44:35Z PPU: trace captured 759 events: ProgressReportEnd 726, ExecutionMetrics 22, CommandEnd 11
```
