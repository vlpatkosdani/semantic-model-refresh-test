# Harness run 20261113T084411Z-v00-4f8b

- Task: xmla
- Variant: v00-baseline
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: c3e551b10fc0214fbbde513336790cf1ca3cb685
- Notebook run: 34d62674-ddd5-4943-8f33-02c4612fb719
- Pages p20, modes cold,warm, concurrency seq,page, repeats 3, queries from harness/queries/20261113T084411Z-v00-4f8b.json

## F64

- 9 queries through XMLA, one at a time, cold cache; 0 failed
- Workspace at c3e551b, DataTag read back data-10m-v1
- Server time, CPU and peak memory from an XMLA trace (QueryEnd and ExecutionMetrics)

```
page visual visual_type  rep  client_ms  server_ms  cpu_ms  peak_mem_kb  result_rows  metrics_events client_error
 p20    v05     tableEx    1       3471     1924.0 10891.0     423755.0          9.0             3.0             
 p20    v05     tableEx    2       2469     1923.0 10438.0     422761.0          9.0             1.0             
 p20    v05     tableEx    3       2655     1954.0 10906.0     423457.0          9.0             1.0             
 p20    v18     tableEx    1       2699     1876.0 10344.0     423064.0         65.0             1.0             
 p20    v18     tableEx    2       2321     1907.0 10719.0     423554.0         65.0             1.0             
 p20    v18     tableEx    3       2484     1876.0  9891.0     422799.0         65.0             1.0             
 p20    v20  pivotTable    1      14902    14323.0 49828.0     880310.0         36.0             1.0             
 p20    v20  pivotTable    2       9511     9020.0 46578.0     880309.0         36.0             1.0             
 p20    v20  pivotTable    3       9757     9208.0 48078.0     881045.0         36.0             1.0             
```

## Log

```
2026-11-13T08:46:52Z run 20261113T084411Z-v00-4f8b: variant=v00-baseline data_tag=data-10m-v1 targets=['F64'] expected_commit=c3e551b10fc0214fbbde513336790cf1ca3cb685
2026-11-13T08:47:07Z F64: workspace already at c3e551b10fc0214fbbde513336790cf1ca3cb685
2026-11-13T08:47:09Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-10m-v1
2026-11-13T08:47:31Z F64: trace started (full), 3 visuals, 3 repeats, cold cache
2026-11-13T08:47:40Z F64: p20 v05 rep 1: 3471 ms
2026-11-13T08:47:49Z F64: p20 v05 rep 2: 2469 ms
2026-11-13T08:47:58Z F64: p20 v05 rep 3: 2655 ms
2026-11-13T08:48:08Z F64: p20 v18 rep 1: 2699 ms
2026-11-13T08:48:16Z F64: p20 v18 rep 2: 2321 ms
2026-11-13T08:48:25Z F64: p20 v18 rep 3: 2484 ms
2026-11-13T08:48:47Z F64: p20 v20 rep 1: 14902 ms
2026-11-13T08:49:03Z F64: p20 v20 rep 2: 9511 ms
2026-11-13T08:49:19Z F64: p20 v20 rep 3: 9757 ms
2026-11-13T08:49:43Z F64: trace captured 20 events: ExecutionMetrics 11, QueryEnd 9
```
