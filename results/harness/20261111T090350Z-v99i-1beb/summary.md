# Harness run 20261111T090350Z-v99i-1beb

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: ebcf68eeb3375e67bdd3b2b0873aa3a1a20d2f9f
- Notebook run: c1a99e3b-4f96-4aa2-ac70-22632c0b92c3
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 23,893 MB, Power Query 23,700 MB, duration 20 min, CPU 3,961 s, rows 38,422,496, model 534 MB (Backup step in XMLA trace)
- Refresh request f2819fe4-caa3-4dbe-816f-7f1e05605d7a, 2026-11-11T09:07:08.937 to 2026-11-11T09:27:15.503, workspace at ?, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- No earlier harness run of v99i-buffer-stg-sales on PPU data-1m-v1.
- No v00-baseline harness run with a measured peak on PPU data-1m-v1 to compare with.
- Measured peak against per-model limits: F2 3,066 MB: OVER (779%); F16 5,120 MB: OVER (467%); F32 10,240 MB: OVER (233%); F64 25,600 MB: fits (93%); PPU 102,400 MB: fits (23%).

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            f6f7c939-d3ef-40b2-9552-fed2312af9d0 TabularSequencePoint       1193.0     0.6       0
                           Sales Flat.Sales Flat       TabularRefresh       1173.1    74.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1136.8    25.3       0
                           Sales Flat.Sales Flat           ExecuteSql        900.5     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        809.2     3.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        747.8     0.0       0
                   Customer Stats.Customer Stats           ExecuteSql        680.6     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        388.9    25.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        388.7    25.2 2349091
                           Sales Flat.Sales Flat              Process        272.5    74.4       0
                           Sales Flat.Sales Flat             ReadData        272.0    74.4 2349091
                   Customer Stats.Customer Stats              Process        128.4     2.9       0
```

## Log

```
2026-11-11T09:06:39Z run 20261111T090350Z-v99i-1beb: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 targets=['PPU'] expected_commit=ebcf68eeb3375e67bdd3b2b0873aa3a1a20d2f9f
2026-11-11T09:06:41Z PPU: not connected to Git; the model there is the one published by hand
2026-11-11T09:06:43Z PPU: v99i-buffer-stg-sales is f6f7c939-d3ef-40b2-9552-fed2312af9d0, DataTag reads back data-1m-v1
2026-11-11T09:07:08Z PPU: trace started (full)
2026-11-11T09:07:09Z PPU: refresh started, request f2819fe4-caa3-4dbe-816f-7f1e05605d7a
2026-11-11T09:27:23Z PPU: refresh refreshed (Completed) 
2026-11-11T09:27:54Z PPU: trace captured 834 events: ProgressReportEnd 799, ExecutionMetrics 24, CommandEnd 11
```
