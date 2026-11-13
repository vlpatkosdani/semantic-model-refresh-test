# Harness run 20261113T085036Z-v00-b3e0

- Task: refresh
- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: F2
- Expected commit: c3e551b10fc0214fbbde513336790cf1ca3cb685
- Notebook run: 9d102876-461c-4a2a-8726-cf32e0fda155
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 12 min, CPU n/a, rows n/a, model 700 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 35a85061-e75e-4fc1-9cc9-f36fe2198e1b, 2026-11-13T08:54:17.683 to 2026-11-13T09:05:53.853, workspace at c3e551b, DataTag read back data-10m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on F2 data-10m-v1: refreshed, peak n/a (2026-11-12T13:36:21Z).
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-13T08:53:03Z run 20261113T085036Z-v00-b3e0: variant=v00-baseline data_tag=data-10m-v1 targets=['F2'] expected_commit=c3e551b10fc0214fbbde513336790cf1ca3cb685
2026-11-13T08:53:16Z F2: update from Git b1660a09614e780473f21788f5ae8523db531ca7 -> c3e551b10fc0214fbbde513336790cf1ca3cb685
2026-11-13T08:53:56Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-10m-v1
2026-11-13T08:54:17Z F2: model size in memory before the refresh: 66.2 MB
2026-11-13T08:54:17Z F2: refresh started, request 35a85061-e75e-4fc1-9cc9-f36fe2198e1b
2026-11-13T09:06:00Z F2: refresh refreshed (Completed) 
2026-11-13T09:06:02Z F2: model size in memory right after the refresh: 700.0 MB
```
