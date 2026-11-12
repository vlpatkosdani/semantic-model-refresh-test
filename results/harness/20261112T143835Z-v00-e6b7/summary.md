# Harness run 20261112T143835Z-v00-e6b7

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: b1660a09614e780473f21788f5ae8523db531ca7
- Notebook run: ccd0cab6-f392-4158-95eb-740a7a432ca1
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 4ddc42c8-d52b-493a-a1f4-6bec48e07e7b, 2026-11-12T14:39:37.533 to 2026-11-12T14:40:48.87, workspace at b1660a0, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on F2 data-1m-v1: refreshed, peak n/a (2026-11-11T20:17:33Z).
- Model size in memory when the full refresh started: 700 MB. The refresh may use the SKU maximum minus this: 2,366 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-12T14:39:09Z run 20261112T143835Z-v00-e6b7: variant=v00-baseline data_tag=data-1m-v1 targets=['F2'] expected_commit=b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T14:39:23Z F2: workspace already at b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T14:39:24Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1
2026-11-12T14:39:37Z F2: model size in memory before the refresh: 700.0 MB
2026-11-12T14:39:37Z F2: refresh started, request 4ddc42c8-d52b-493a-a1f4-6bec48e07e7b
2026-11-12T14:41:18Z F2: refresh refreshed (Completed) 
2026-11-12T14:41:19Z F2: model size in memory right after the refresh: 92.7 MB
```
