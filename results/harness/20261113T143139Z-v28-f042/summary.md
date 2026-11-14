# Harness run 20261113T143139Z-v28-f042

- Task: queries
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: ffb4e45b-21a2-4f81-8834-21ad245bd5fc
- Pages p05,p20, modes cold, concurrency page, repeats 5, queries from harness/queries/20261113T143139Z-v28-f042.json

## F64

- 125 queries sent (0 warm-up), 1 failed, 124 found in SemanticModelLogs, 0 throttling retries
- Workspace at 2b9900b, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p05 cold page        5                450.0             586.8                 125.0                 188.0              282.0          14396.0       0
 p20 cold page        5               1100.0            1217.8                 547.0                1252.0             1690.0          28546.0       1
```

Failed queries (first 10):

```
page visual mode conc  rep                                                                                                                                                                                                                                                                                                                                                                 client_error
 p20    v07 cold page    1 HTTP 500 500 Internal Server Error for url: https://api.fabric.microsoft.com/v1.0/myorg/groups/d3119fe5-cd57-4366-b671-89a3ad82aed5/datasets/bc793114-53e1-4476-8e50-c4b0c5b15603/executeQueries\nError: {"Message":"An error has occurred."}\nHeaders: {'Content-Length': '36', 'Content-Type': 'application/json; charset=utf-8', 'Date': 'Fri, 13 Nov 2026 14:32:43 GMT'}
```

## Log

```
2026-11-13T14:32:07Z run 20261113T143139Z-v28-f042: variant=v28-types-all-text data_tag=data-1m-v1 targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T14:32:13Z F64: workspace already at 2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-13T14:32:16Z F64: v28-types-all-text is bc793114-53e1-4476-8e50-c4b0c5b15603, DataTag reads back data-1m-v1
2026-11-13T14:32:37Z F64: page p05 done, 25 queries so far
2026-11-13T14:33:32Z F64: page p20 done, 125 queries so far
2026-11-13T14:33:32Z F64: monitoring database Monitoring KQL database
2026-11-13T14:54:02Z F64: 124 of 125 queries found in SemanticModelLogs
```
