# Harness run 20261113T090703Z-v00-4b85

- Task: xmla
- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: F2
- Expected commit: c3e551b10fc0214fbbde513336790cf1ca3cb685
- Notebook run: 36448cdd-2977-4247-89a9-a6cb8f4e8d2d
- Pages p20, modes cold,warm, concurrency seq,page, repeats 3, queries from harness/queries/20261113T090703Z-v00-4b85.json

## F2

- 9 queries through XMLA, one at a time, cold cache; 0 failed
- Workspace at c3e551b, DataTag read back data-10m-v1
- Server time, CPU and peak memory from an XMLA trace (QueryEnd and ExecutionMetrics)

```
page visual visual_type  rep  client_ms  server_ms  cpu_ms  peak_mem_kb  result_rows  metrics_events client_error
 p20    v05     tableEx    1       6313     3988.0 17078.0     424099.0          9.0             3.0             
 p20    v05     tableEx    2       4840     4081.0 17859.0     424154.0          9.0             1.0             
 p20    v05     tableEx    3       4219     3691.0 17000.0     424512.0          9.0             1.0             
 p20    v18     tableEx    1       4457     3784.0 15781.0     423868.0         65.0             1.0             
 p20    v18     tableEx    2       4469     3877.0 17188.0     423091.0         65.0             1.0             
 p20    v18     tableEx    3       4216     3721.0 16688.0     423443.0         65.0             1.0             
 p20    v20  pivotTable    1      19767    19121.0 73813.0     881023.0         36.0             1.0             
 p20    v20  pivotTable    2      65350    24771.0 74844.0     875763.0         36.0             1.0             
 p20    v20  pivotTable    3      60321    19734.0 72891.0     880973.0         36.0             1.0             
```

## Log

```
2026-11-13T09:09:20Z run 20261113T090703Z-v00-4b85: variant=v00-baseline data_tag=data-10m-v1 targets=['F2'] expected_commit=c3e551b10fc0214fbbde513336790cf1ca3cb685
2026-11-13T09:09:33Z F2: workspace already at c3e551b10fc0214fbbde513336790cf1ca3cb685
2026-11-13T09:09:35Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-10m-v1
2026-11-13T09:09:54Z F2: trace started (full), 3 visuals, 3 repeats, cold cache
2026-11-13T09:10:06Z F2: p20 v05 rep 1: 6313 ms
2026-11-13T09:10:17Z F2: p20 v05 rep 2: 4840 ms
2026-11-13T09:10:29Z F2: p20 v05 rep 3: 4219 ms
2026-11-13T09:10:39Z F2: p20 v18 rep 1: 4457 ms
2026-11-13T09:10:51Z F2: p20 v18 rep 2: 4469 ms
2026-11-13T09:11:02Z F2: p20 v18 rep 3: 4216 ms
2026-11-13T09:11:29Z F2: p20 v20 rep 1: 19767 ms
2026-11-13T09:13:01Z F2: p20 v20 rep 2: 65350 ms
2026-11-13T09:14:28Z F2: p20 v20 rep 3: 60321 ms
2026-11-13T09:15:52Z F2: trace captured 20 events: ExecutionMetrics 11, QueryEnd 9
```
