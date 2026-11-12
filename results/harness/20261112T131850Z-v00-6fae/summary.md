# Harness run 20261112T131850Z-v00-6fae

- Task: refresh
- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: F2
- Expected commit: 6bbfb2927c8f84faaa5079ff221dbf194f7def02
- Notebook run: b3c52a9b-24c0-40ff-a817-c39ab0967baa
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 12 min, CPU n/a, rows n/a, model 700 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request c082609a-26d1-4605-b824-1e64e12cd5c7, 2026-11-12T13:24:07.243 to 2026-11-12T13:36:16.397, workspace at 6bbfb29, DataTag read back data-10m-v1
- Numbers from: refresh API
- No earlier harness run of v00-baseline on F2 data-10m-v1.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-12T13:21:04Z run 20261112T131850Z-v00-6fae: variant=v00-baseline data_tag=data-10m-v1 targets=['F2'] expected_commit=6bbfb2927c8f84faaa5079ff221dbf194f7def02
2026-11-12T13:21:15Z F2: update from Git 53cfca4864e70f1fda420adacf9ab5955bb08783 -> 6bbfb2927c8f84faaa5079ff221dbf194f7def02
2026-11-12T13:23:23Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-10m-v1
2026-11-12T13:24:06Z F2: model size in memory before the refresh: 66.2 MB
2026-11-12T13:24:07Z F2: refresh started, request c082609a-26d1-4605-b824-1e64e12cd5c7
2026-11-12T13:36:21Z F2: refresh refreshed (Completed) 
2026-11-12T13:36:24Z F2: model size in memory right after the refresh: 700.0 MB
```
