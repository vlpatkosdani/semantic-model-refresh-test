# Harness run 20261113T094637Z-v00-c535

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
- Notebook run: 195567c7-6cee-4499-ae1f-73685ee55e82
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 177aac1f-3434-42a0-9813-3e8111e293c9, 2026-11-13T09:58:49.937 to 2026-11-13T10:00:04.177, workspace at 11b19b5, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on F2 data-1m-v1: refreshed, peak n/a (2026-11-12T14:41:18Z).
- Model size in memory when the full refresh started: 700 MB. The refresh may use the SKU maximum minus this: 2,366 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-13T09:49:08Z run 20261113T094637Z-v00-c535: variant=v00-baseline data_tag=data-1m-v1 targets=['F2'] expected_commit=11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:49:20Z F2: update from Git c3e551b10fc0214fbbde513336790cf1ca3cb685 -> 11b19b5ae786173223c42ae0ed7f0e2cc4488bfb
2026-11-13T09:58:23Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1
2026-11-13T09:58:49Z F2: model size in memory before the refresh: 700.0 MB
2026-11-13T09:58:50Z F2: refresh started, request 177aac1f-3434-42a0-9813-3e8111e293c9
2026-11-13T10:00:30Z F2: refresh refreshed (Completed) 
2026-11-13T10:00:32Z F2: model size in memory right after the refresh: 92.7 MB
```
