# Harness run 20261111T201823Z-v00-e337

- Task: queries
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: 53cfca4864e70f1fda420adacf9ab5955bb08783
- Notebook run: 83294805-90fb-4393-b0dc-b7d228580477
- Pages p05,p20, modes cold, concurrency page, repeats 3, queries from harness/queries/20261111T201823Z-v00-e337.json

## F2

- 75 queries sent (0 warm-up), 9 failed, 0 found in SemanticModelLogs, 0 throttling retries
- Workspace at 53cfca4, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms server_max_median_ms server_sum_median_ms cpu_sum_median_ms peak_mem_max_kb  errors
 p05 cold page        3                537.0             670.6                  NaN                  0.0               0.0             NaN       3
 p20 cold page        3               2061.0            2089.0                  NaN                  0.0               0.0             NaN       6
```

Failed queries (first 10):

```
page visual mode conc  rep                                                                                                                         client_error
 p05    v01 cold page    1 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p05    v01 cold page    2 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p05    v01 cold page    3 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p20    v01 cold page    1 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p20    v20 cold page    1 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p20    v01 cold page    2 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p20    v20 cold page    2 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p20    v01 cold page    3 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
 p20    v20 cold page    3 {"code": "DaxResultsetCountNotSupported", "message": "More than 1 result set has been encountered. Only 1 result set is supported."}
```

## Log

```
2026-11-11T20:20:52Z run 20261111T201823Z-v00-e337: variant=v00-baseline data_tag=data-1m-v1 targets=['F2'] expected_commit=53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T20:21:00Z F2: workspace already at 53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T20:21:01Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1
2026-11-11T20:21:26Z F2: page p05 done, 15 queries so far
2026-11-11T20:21:56Z F2: page p20 done, 75 queries so far
```
