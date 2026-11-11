# Harness run 20261111T190900Z-all-2694

- Task: sizes
- Variant: all
- Data tag: 
- Targets: 
- Expected commit: 6ae11b76734b4541aafa8cfcfe692b8d1218e5cd
- Notebook run: 3d5a36c0-9f9f-447c-88a2-afca398ee397
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from 

## F64old

```
                         model   data_tag                       last_refresh  total_mb  data_mb  dictionary_mb  hierarchy_mb  relationship_mb error
                  v00-baseline data-1m-v1 Completed 2026-11-11T07:55:57.377Z      66.2     40.5           16.7           8.7              0.2      
            v18-pq-10m-summary data-1m-v1  Completed 2026-11-05T11:29:32.39Z      66.2     40.5           16.7           8.7              0.2      
              v19-pq-heavy-10m data-1m-v1    Failed 2026-11-06T10:33:54.623Z       0.1      0.0            0.0           0.0              0.0      
                   v20-pq-sort data-1m-v1 Completed 2026-11-10T09:00:43.543Z      65.3     39.7           16.7           8.7              0.2      
               v21-pq-group-by data-1m-v1   Completed 2026-11-06T08:28:36.6Z      92.1     43.5           36.1          12.3              0.2      
          v22-dax-calc-columns data-1m-v1  Completed 2026-11-10T12:59:21.66Z      97.8     64.0           23.3          10.2              0.2      
           v23-dax-calc-tables data-1m-v1  Completed 2026-11-10T13:23:07.81Z     149.9    114.3           19.4          16.0              0.2      
             v24-bidirectional data-1m-v1  Completed 2026-11-10T14:46:54.47Z      66.2     40.5           16.7           8.7              0.2      
              v24a-second-fact data-1m-v1  Completed 2026-11-10T15:10:44.22Z      82.4     49.4           19.4          13.2              0.5      
v24b-second-fact-bidirectional data-1m-v1 Completed 2026-11-10T15:32:29.367Z      82.4     49.4           19.4          13.2              0.5      
              v25-many-to-many data-1m-v1                                          0.0      0.0            0.0           0.0              0.0      
                   v26-bad-dax data-1m-v1  Completed 2026-11-10T11:14:44.77Z      66.2     40.5           16.7           8.7              0.2      
  v27-high-cardinality-visuals data-1m-v1  Completed 2026-11-10T11:21:56.22Z      66.2     40.5           16.7           8.7              0.2      
              v99-kitchen-sink data-1m-v1    Failed 2026-11-04T17:07:21.493Z       0.1      0.0            0.1           0.0              0.0      
       v99a-no-big-calc-tables data-1m-v1 Completed 2026-11-04T19:25:26.327Z     197.8     79.7           85.1          31.2              1.8      
           v99b-one-sales-copy data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
           v99c-crossjoin-only data-1m-v1                                          0.1      0.0            0.1           0.0              0.0      
              v99d-power-query data-1m-v1 Completed 2026-11-04T21:03:59.737Z     197.8     79.7           85.1          31.2              1.8      
               v99e-sales-flat data-1m-v1 Completed 2026-11-05T08:16:25.417Z     356.6    147.3          152.7          54.9              1.8      
              v99f-calc-tables data-1m-v1 Completed 2026-11-05T08:12:09.147Z     385.7    172.2          154.2          57.5              1.8      
               v99g-sales-copy data-1m-v1 Completed 2026-11-05T10:42:15.053Z     540.6    258.5          200.5          79.8              1.8      
          v99h-staging-buffers data-1m-v1    Failed 2026-11-05T10:49:14.467Z       0.1      0.0            0.1           0.0              0.0      
         v99i-buffer-stg-sales data-1m-v1     Failed 2026-11-05T11:45:19.92Z       0.1      0.0            0.1           0.0              0.0      
      v99j-buffer-stg-customer data-1m-v1 Completed 2026-11-05T11:24:55.233Z     540.6    258.5          200.5          79.8              1.8      
               v99k-no-buffers data-1m-v1  Completed 2026-11-05T12:59:15.69Z     197.8     79.7           85.1          31.2              1.8      
          v99l-no-calc-columns data-1m-v1 Completed 2026-11-05T15:03:50.053Z     167.7     57.7           78.5          29.7              1.8      
              v99m-baseline-pq data-1m-v1  Completed 2026-11-05T14:57:05.12Z     101.3     64.1           25.8          11.1              0.3      
             v99n-text-staging data-1m-v1  Completed 2026-11-05T15:31:05.11Z      90.7     55.5           24.0          10.8              0.3      
                    v99o-sorts data-1m-v1 Completed 2026-11-05T15:28:12.593Z      99.0     61.8           25.8          11.1              0.3      
         v99p-high-cardinality data-1m-v1 Completed 2026-11-05T15:26:48.263Z     174.2     79.1           65.7          27.6              1.8      
           v99q-customer-stats data-1m-v1 Completed 2026-11-05T15:26:53.157Z     127.3     67.2           45.1          14.7              0.3      
```

## F2

```
                   model    data_tag                       last_refresh  total_mb  data_mb  dictionary_mb  hierarchy_mb  relationship_mb error
            v00-baseline data-10m-v1 Completed 2026-11-10T09:33:16.537Z     625.7    380.5          159.1          82.6              3.4      
      v18-pq-10m-summary  data-1m-v1  Completed 2026-11-05T12:21:04.18Z      66.2     40.5           16.7           8.7              0.2      
        v19-pq-heavy-10m  data-1m-v1    Failed 2026-11-05T12:29:41.643Z       0.1      0.0            0.0           0.0              0.0      
             v20-pq-sort  data-1m-v1    Failed 2026-11-10T08:58:42.743Z       0.0      0.0            0.0           0.0              0.0      
         v21-pq-group-by  data-1m-v1     Failed 2026-11-06T08:40:06.31Z       0.0      0.0            0.0           0.0              0.0      
    v22-dax-calc-columns  data-1m-v1 Completed 2026-11-06T10:26:08.677Z      97.8     64.0           23.3          10.2              0.2      
     v23-dax-calc-tables  data-1m-v1   Completed 2026-11-06T10:26:22.4Z     148.6    112.9           19.4          16.0              0.2      
        v99-kitchen-sink  data-1m-v1     Failed 2026-11-03T20:06:17.17Z       0.1      0.0            0.1           0.0              0.0      
 v99a-no-big-calc-tables  data-1m-v1    Failed 2026-11-05T12:32:41.833Z       0.3      0.0            0.3           0.0              0.0      
     v99b-one-sales-copy  data-1m-v1     Failed 2026-11-05T12:32:18.73Z       0.1      0.0            0.1           0.0              0.0      
     v99c-crossjoin-only  data-1m-v1      Failed 2026-11-05T12:32:20.6Z       0.1      0.0            0.1           0.0              0.0      
        v99d-power-query  data-1m-v1    Failed 2026-11-05T12:33:08.633Z       0.3      0.0            0.3           0.0              0.0      
         v99e-sales-flat  data-1m-v1                                          0.4      0.0            0.3           0.0              0.0      
        v99f-calc-tables  data-1m-v1                                          0.4      0.0            0.3           0.0              0.0      
         v99g-sales-copy  data-1m-v1                                          0.4      0.0            0.3           0.0              0.0      
    v99h-staging-buffers  data-1m-v1                                          0.4      0.0            0.3           0.0              0.0      
   v99i-buffer-stg-sales  data-1m-v1                                          0.4      0.0            0.3           0.0              0.0      
v99j-buffer-stg-customer  data-1m-v1                                          0.4      0.0            0.3           0.0              0.0      
         v99k-no-buffers  data-1m-v1     Failed 2026-11-05T12:56:05.68Z       0.3      0.0            0.3           0.0              0.0      
    v99l-no-calc-columns  data-1m-v1    Failed 2026-11-05T15:06:07.107Z       0.3      0.0            0.3           0.0              0.0      
        v99m-baseline-pq  data-1m-v1 Completed 2026-11-05T14:57:59.643Z     101.3     64.1           25.8          11.1              0.3      
       v99n-text-staging  data-1m-v1  Completed 2026-11-05T15:34:23.81Z      90.7     55.5           24.0          10.8              0.3      
              v99o-sorts  data-1m-v1    Failed 2026-11-05T15:38:00.867Z       0.3      0.0            0.2           0.0              0.0      
   v99p-high-cardinality  data-1m-v1 Completed 2026-11-05T15:26:57.707Z     174.2     79.1           65.7          27.6              1.8      
     v99q-customer-stats  data-1m-v1    Failed 2026-11-05T15:37:38.617Z       0.3      0.0            0.2           0.0              0.0      
```

## PPU

```
                model   data_tag                       last_refresh  total_mb  data_mb  dictionary_mb  hierarchy_mb  relationship_mb error
     v99-kitchen-sink data-1m-v1 Completed 2026-11-10T16:43:40.867Z     626.4    349.4          197.9          78.9              0.2      
 v99h-staging-buffers data-1m-v1  Completed 2026-11-11T08:55:05.19Z     540.6    258.5          200.5          79.8              1.8      
v99i-buffer-stg-sales data-1m-v1 Completed 2026-11-11T09:27:15.503Z     540.6    258.5          200.5          79.8              1.8      
```

## Log

```
2026-11-11T19:11:16Z run 20261111T190900Z-all-2694: variant=all data_tag= targets=['F64old', 'F2', 'PPU'] expected_commit=6ae11b76734b4541aafa8cfcfe692b8d1218e5cd
2026-11-11T19:11:27Z F64old: v00-baseline: 66.2 MB 
2026-11-11T19:11:31Z F64old: v18-pq-10m-summary: 66.2 MB 
2026-11-11T19:11:35Z F64old: v19-pq-heavy-10m: 0.1 MB 
2026-11-11T19:11:39Z F64old: v20-pq-sort: 65.3 MB 
2026-11-11T19:11:43Z F64old: v21-pq-group-by: 92.1 MB 
2026-11-11T19:11:47Z F64old: v22-dax-calc-columns: 97.8 MB 
2026-11-11T19:11:51Z F64old: v23-dax-calc-tables: 149.9 MB 
2026-11-11T19:11:55Z F64old: v24-bidirectional: 66.2 MB 
2026-11-11T19:12:00Z F64old: v24a-second-fact: 82.4 MB 
2026-11-11T19:12:04Z F64old: v24b-second-fact-bidirectional: 82.4 MB 
2026-11-11T19:12:08Z F64old: v25-many-to-many: 0.0 MB 
2026-11-11T19:12:12Z F64old: v26-bad-dax: 66.2 MB 
2026-11-11T19:12:16Z F64old: v27-high-cardinality-visuals: 66.2 MB 
2026-11-11T19:12:20Z F64old: v99-kitchen-sink: 0.1 MB 
2026-11-11T19:12:24Z F64old: v99a-no-big-calc-tables: 197.8 MB 
2026-11-11T19:12:28Z F64old: v99b-one-sales-copy: 0.1 MB 
2026-11-11T19:12:33Z F64old: v99c-crossjoin-only: 0.1 MB 
2026-11-11T19:12:36Z F64old: v99d-power-query: 197.8 MB 
2026-11-11T19:12:40Z F64old: v99e-sales-flat: 356.6 MB 
2026-11-11T19:12:44Z F64old: v99f-calc-tables: 385.7 MB 
2026-11-11T19:12:48Z F64old: v99g-sales-copy: 540.6 MB 
2026-11-11T19:12:51Z F64old: v99h-staging-buffers: 0.1 MB 
2026-11-11T19:12:55Z F64old: v99i-buffer-stg-sales: 0.1 MB 
2026-11-11T19:12:59Z F64old: v99j-buffer-stg-customer: 540.6 MB 
2026-11-11T19:13:02Z F64old: v99k-no-buffers: 197.8 MB 
2026-11-11T19:13:06Z F64old: v99l-no-calc-columns: 167.7 MB 
2026-11-11T19:13:09Z F64old: v99m-baseline-pq: 101.3 MB 
2026-11-11T19:13:13Z F64old: v99n-text-staging: 90.7 MB 
2026-11-11T19:13:16Z F64old: v99o-sorts: 99.0 MB 
2026-11-11T19:13:20Z F64old: v99p-high-cardinality: 174.2 MB 
2026-11-11T19:13:23Z F64old: v99q-customer-stats: 127.3 MB 
2026-11-11T19:13:26Z F2: v00-baseline: 625.7 MB 
2026-11-11T19:13:30Z F2: v18-pq-10m-summary: 66.2 MB 
2026-11-11T19:13:33Z F2: v19-pq-heavy-10m: 0.1 MB 
2026-11-11T19:13:37Z F2: v20-pq-sort: 0.0 MB 
2026-11-11T19:13:40Z F2: v21-pq-group-by: 0.0 MB 
2026-11-11T19:13:43Z F2: v22-dax-calc-columns: 97.8 MB 
2026-11-11T19:13:46Z F2: v23-dax-calc-tables: 148.6 MB 
2026-11-11T19:13:49Z F2: v99-kitchen-sink: 0.1 MB 
2026-11-11T19:13:53Z F2: v99a-no-big-calc-tables: 0.3 MB 
2026-11-11T19:13:56Z F2: v99b-one-sales-copy: 0.1 MB 
2026-11-11T19:13:59Z F2: v99c-crossjoin-only: 0.1 MB 
2026-11-11T19:14:03Z F2: v99d-power-query: 0.3 MB 
2026-11-11T19:14:06Z F2: v99e-sales-flat: 0.4 MB 
2026-11-11T19:14:09Z F2: v99f-calc-tables: 0.4 MB 
2026-11-11T19:14:12Z F2: v99g-sales-copy: 0.4 MB 
2026-11-11T19:14:15Z F2: v99h-staging-buffers: 0.4 MB 
2026-11-11T19:14:18Z F2: v99i-buffer-stg-sales: 0.4 MB 
2026-11-11T19:14:21Z F2: v99j-buffer-stg-customer: 0.4 MB 
2026-11-11T19:14:24Z F2: v99k-no-buffers: 0.3 MB 
2026-11-11T19:14:28Z F2: v99l-no-calc-columns: 0.3 MB 
2026-11-11T19:14:31Z F2: v99m-baseline-pq: 101.3 MB 
2026-11-11T19:14:34Z F2: v99n-text-staging: 90.7 MB 
2026-11-11T19:14:37Z F2: v99o-sorts: 0.3 MB 
2026-11-11T19:14:40Z F2: v99p-high-cardinality: 174.2 MB 
2026-11-11T19:14:44Z F2: v99q-customer-stats: 0.3 MB 
2026-11-11T19:14:48Z PPU: v99-kitchen-sink: 626.4 MB 
2026-11-11T19:14:51Z PPU: v99h-staging-buffers: 540.6 MB 
2026-11-11T19:14:55Z PPU: v99i-buffer-stg-sales: 540.6 MB 
```
