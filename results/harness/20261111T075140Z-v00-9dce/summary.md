# Harness run 20261111T075140Z-v00-9dce

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: ebcf68eeb3375e67bdd3b2b0873aa3a1a20d2f9f
- Notebook run: 5d1e7688-d1c3-4498-b11f-4cafde2d727d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 09b84205-ccbd-4409-9172-f686ef7dfde2, 2026-11-11T07:54:48.607 to 2026-11-11T07:55:57.377, workspace at ebcf68e, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 698 MB (2026-11-10T10:09:23Z).
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-11T07:54:20Z run 20261111T075140Z-v00-9dce: variant=v00-baseline data_tag=data-1m-v1 targets=['F64'] expected_commit=ebcf68eeb3375e67bdd3b2b0873aa3a1a20d2f9f
2026-11-11T07:54:30Z F64: workspace already at ebcf68eeb3375e67bdd3b2b0873aa3a1a20d2f9f
2026-11-11T07:54:34Z F64: v00-baseline is e4fb48c3-0f90-4151-94d1-583276edd1bf, DataTag reads back data-1m-v1
2026-11-11T07:54:48Z F64: refresh started, request 09b84205-ccbd-4409-9172-f686ef7dfde2
2026-11-11T07:55:59Z F64: refresh refreshed (Completed) 
2026-11-11T07:56:00Z F64: monitoring database Test PBI semantic model refresh - F64_Monitoring_item_Test_PBI_semantic_model_refresh_-_F64_Database
2026-11-11T08:16:02Z F64: no ExecutionMetrics event after 20 min
```
