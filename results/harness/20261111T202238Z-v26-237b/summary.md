# Harness run 20261111T202238Z-v26-237b

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 53cfca4864e70f1fda420adacf9ab5955bb08783
- Notebook run: 27fafe74-4d7b-4818-a3e8-b0c04b70000b
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 5f315705-2749-43f4-9d60-d75048fa84f2, 2026-11-11T20:23:49.74 to 2026-11-11T20:24:54.823, workspace at 53cfca4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v26-bad-dax on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-11T20:23:28Z run 20261111T202238Z-v26-237b: variant=v26-bad-dax data_tag=data-1m-v1 targets=['F2'] expected_commit=53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T20:23:35Z F2: workspace already at 53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T20:23:37Z F2: v26-bad-dax is e56036af-5114-4745-8442-72f81810a1ee, DataTag reads back data-1m-v1
2026-11-11T20:23:49Z F2: model size in memory before the refresh: 0.0 MB
2026-11-11T20:23:49Z F2: refresh started, request 5f315705-2749-43f4-9d60-d75048fa84f2
2026-11-11T20:25:00Z F2: refresh refreshed (Completed) 
2026-11-11T20:25:01Z F2: model size in memory right after the refresh: 92.7 MB
```
