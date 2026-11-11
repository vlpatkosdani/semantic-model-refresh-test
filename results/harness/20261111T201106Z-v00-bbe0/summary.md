# Harness run 20261111T201106Z-v00-bbe0

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 53cfca4864e70f1fda420adacf9ab5955bb08783
- Notebook run: be3ab62c-9ffc-4328-9cd2-fae4202b1aac
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 09ba1e91-0379-449c-accc-3fad8dc1124a, 2026-11-11T20:16:22.733 to 2026-11-11T20:17:32.193, workspace at 53cfca4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v00-baseline on F2 data-1m-v1.
- Model size in memory when the full refresh started: 626 MB. The refresh may use the SKU maximum minus this: 2,440 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-11T20:13:45Z run 20261111T201106Z-v00-bbe0: variant=v00-baseline data_tag=data-1m-v1 targets=['F2'] expected_commit=53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T20:13:54Z F2: update from Git bd153555c8eb47f0cf31eec9dcf80ab328a24be0 -> 53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T20:15:59Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1
2026-11-11T20:16:22Z F2: model size in memory before the refresh: 625.7 MB
2026-11-11T20:16:22Z F2: refresh started, request 09ba1e91-0379-449c-accc-3fad8dc1124a
2026-11-11T20:17:33Z F2: refresh refreshed (Completed) 
2026-11-11T20:17:34Z F2: model size in memory right after the refresh: 92.7 MB
```
