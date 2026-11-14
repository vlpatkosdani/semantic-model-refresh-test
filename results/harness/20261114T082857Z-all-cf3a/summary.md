# Harness run 20261114T082857Z-all-cf3a

- Task: sizes
- Variant: all
- Data tag: 
- Targets: 
- Expected commit: 2b9900b76c6748e558a8f56970dc67321d7fc4f0
- Notebook run: 602ed05d-e12e-4d76-9356-e4356951fa27
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from 

## F64

```
                           model    data_tag                       last_refresh  total_mb  data_mb  dictionary_mb  hierarchy_mb  relationship_mb error
                    v00-baseline  data-1m-v1 Completed 2026-11-13T20:31:32.867Z      66.2     40.5           16.7           8.7              0.2      
              v18-pq-10m-summary  data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
                v19-pq-heavy-10m  data-1m-v1                                          0.1      0.0            0.0           0.0              0.0      
                     v20-pq-sort  data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
                 v21-pq-group-by  data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
            v22-dax-calc-columns  data-1m-v1  Completed 2026-11-13T17:40:34.38Z      97.8     64.0           23.3          10.2              0.2      
             v23-dax-calc-tables  data-1m-v1  Completed 2026-11-12T12:24:14.11Z    1298.8    988.4          162.9         144.1              3.4      
               v24-bidirectional  data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
                v24a-second-fact  data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
  v24b-second-fact-bidirectional  data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
                v25-many-to-many  data-1m-v1 Completed 2026-11-11T19:52:48.603Z      70.6     44.5           16.7           9.1              0.2      
                     v26-bad-dax  data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
    v27-high-cardinality-visuals  data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
              v28-types-all-text  data-1m-v1 Completed 2026-11-11T20:44:15.017Z      95.8     37.4           45.5          12.7              0.2      
                v29-keys-as-text  data-1m-v1 Completed 2026-11-13T09:43:51.073Z      93.8     37.5           43.6          12.5              0.2      
     v30-double-instead-of-fixed  data-1m-v1 Completed 2026-11-12T08:25:55.713Z      66.4     40.5           16.9           8.7              0.2      
            v31-calc-columns-row  data-1m-v1 Completed 2026-11-12T08:32:28.683Z     233.5    115.4           84.2          33.7              0.2      
      v32-calc-columns-aggregate  data-1m-v1 Completed 2026-11-12T11:04:32.843Z     341.3     87.2          203.7          50.1              0.2      
              v33-auto-date-time  data-1m-v1   Completed 2026-11-13T20:36:09.7Z      69.7     40.6           19.2           9.6              0.3      
v34-auto-date-time-no-date-table  data-1m-v1  Completed 2026-11-13T20:42:06.76Z      70.3     40.6           19.6           9.8              0.3      
     v35-calc-tables-four-copies data-10m-v1 Completed 2026-11-13T12:46:16.283Z    2803.0   2408.7          246.8         144.1              3.4      
    v36-calc-summary-month-grain data-10m-v1 Completed 2026-11-13T13:35:09.067Z    1321.3   1014.4          162.9         140.5              3.4      
                v99-kitchen-sink  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
         v99a-no-big-calc-tables  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
             v99b-one-sales-copy  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
             v99c-crossjoin-only  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
                v99d-power-query  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
                 v99e-sales-flat  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
                v99f-calc-tables  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
                 v99g-sales-copy  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
            v99h-staging-buffers  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
           v99i-buffer-stg-sales  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
        v99j-buffer-stg-customer  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
                 v99k-no-buffers  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
            v99l-no-calc-columns  data-1m-v1                                          0.1      0.0            0.0           0.0              0.0      
                v99m-baseline-pq  data-1m-v1                                          0.1      0.0            0.0           0.0              0.0      
               v99n-text-staging  data-1m-v1                                          0.1      0.0            0.0           0.0              0.0      
                      v99o-sorts  data-1m-v1                                          0.1      0.0            0.0           0.0              0.0      
           v99p-high-cardinality  data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
             v99q-customer-stats  data-1m-v1                                          0.1      0.0            0.0           0.0              0.0      
```

## Log

```
2026-11-14T08:31:24Z run 20261114T082857Z-all-cf3a: variant=all data_tag= targets=['F64'] expected_commit=2b9900b76c6748e558a8f56970dc67321d7fc4f0
2026-11-14T08:31:36Z F64: v00-baseline: 66.2 MB 
2026-11-14T08:31:42Z F64: v18-pq-10m-summary: 0.0 MB 
2026-11-14T08:31:47Z F64: v19-pq-heavy-10m: 0.1 MB 
2026-11-14T08:31:53Z F64: v20-pq-sort: 0.0 MB 
2026-11-14T08:31:58Z F64: v21-pq-group-by: 0.0 MB 
2026-11-14T08:32:05Z F64: v22-dax-calc-columns: 97.8 MB 
2026-11-14T08:32:09Z F64: v23-dax-calc-tables: 1298.8 MB 
2026-11-14T08:32:15Z F64: v24-bidirectional: 0.0 MB 
2026-11-14T08:32:19Z F64: v24a-second-fact: 0.0 MB 
2026-11-14T08:32:25Z F64: v24b-second-fact-bidirectional: 0.0 MB 
2026-11-14T08:32:31Z F64: v25-many-to-many: 70.6 MB 
2026-11-14T08:32:35Z F64: v26-bad-dax: 0.0 MB 
2026-11-14T08:32:41Z F64: v27-high-cardinality-visuals: 0.0 MB 
2026-11-14T08:32:47Z F64: v28-types-all-text: 95.8 MB 
2026-11-14T08:32:53Z F64: v29-keys-as-text: 93.8 MB 
2026-11-14T08:32:59Z F64: v30-double-instead-of-fixed: 66.4 MB 
2026-11-14T08:33:07Z F64: v31-calc-columns-row: 233.5 MB 
2026-11-14T08:33:15Z F64: v32-calc-columns-aggregate: 341.3 MB 
2026-11-14T08:33:19Z F64: v33-auto-date-time: 69.7 MB 
2026-11-14T08:33:23Z F64: v34-auto-date-time-no-date-table: 70.3 MB 
2026-11-14T08:33:28Z F64: v35-calc-tables-four-copies: 2803.0 MB 
2026-11-14T08:33:32Z F64: v36-calc-summary-month-grain: 1321.3 MB 
2026-11-14T08:33:38Z F64: v99-kitchen-sink: 0.1 MB 
2026-11-14T08:33:43Z F64: v99a-no-big-calc-tables: 0.1 MB 
2026-11-14T08:33:48Z F64: v99b-one-sales-copy: 0.1 MB 
2026-11-14T08:33:54Z F64: v99c-crossjoin-only: 0.1 MB 
2026-11-14T08:33:59Z F64: v99d-power-query: 0.1 MB 
2026-11-14T08:34:04Z F64: v99e-sales-flat: 0.1 MB 
2026-11-14T08:34:09Z F64: v99f-calc-tables: 0.1 MB 
2026-11-14T08:34:14Z F64: v99g-sales-copy: 0.1 MB 
2026-11-14T08:34:19Z F64: v99h-staging-buffers: 0.1 MB 
2026-11-14T08:34:24Z F64: v99i-buffer-stg-sales: 0.1 MB 
2026-11-14T08:34:29Z F64: v99j-buffer-stg-customer: 0.1 MB 
2026-11-14T08:34:35Z F64: v99k-no-buffers: 0.1 MB 
2026-11-14T08:34:39Z F64: v99l-no-calc-columns: 0.1 MB 
2026-11-14T08:34:44Z F64: v99m-baseline-pq: 0.1 MB 
2026-11-14T08:34:49Z F64: v99n-text-staging: 0.1 MB 
2026-11-14T08:34:54Z F64: v99o-sorts: 0.1 MB 
2026-11-14T08:34:58Z F64: v99p-high-cardinality: 0.1 MB 
2026-11-14T08:35:04Z F64: v99q-customer-stats: 0.1 MB 
```
