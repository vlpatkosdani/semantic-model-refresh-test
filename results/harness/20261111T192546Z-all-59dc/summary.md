# Harness run 20261111T192546Z-all-59dc

- Task: sizes
- Variant: all
- Data tag: 
- Targets: 
- Expected commit: 06c9ed0e55c40ab85df7e8b1aeaeef248162ccd0
- Notebook run: b0f4514d-2c26-407c-a0cb-ae56f4f3cd25
- Pages p01,p05,p10,p20, modes cold,warm, concurrency seq,page, repeats 5, queries from 

## F64old

```
                         model   data_tag                       last_refresh  as_found_mb  total_mb  data_mb  dictionary_mb  hierarchy_mb  relationship_mb error
                  v00-baseline data-1m-v1 Completed 2026-11-11T07:55:57.377Z         66.2      66.2     40.5           16.7           8.7              0.2      
            v18-pq-10m-summary data-1m-v1  Completed 2026-11-05T11:29:32.39Z         66.2      66.2     40.5           16.7           8.7              0.2      
              v19-pq-heavy-10m data-1m-v1    Failed 2026-11-06T10:33:54.623Z          0.1       0.1      0.0            0.0           0.0              0.0      
                   v20-pq-sort data-1m-v1 Completed 2026-11-10T09:00:43.543Z         65.3      65.3     39.7           16.7           8.7              0.2      
               v21-pq-group-by data-1m-v1   Completed 2026-11-06T08:28:36.6Z         92.1      92.1     43.5           36.1          12.3              0.2      
          v22-dax-calc-columns data-1m-v1  Completed 2026-11-10T12:59:21.66Z         97.8      97.8     64.0           23.3          10.2              0.2      
           v23-dax-calc-tables data-1m-v1  Completed 2026-11-10T13:23:07.81Z        149.9     149.9    114.3           19.4          16.0              0.2      
             v24-bidirectional data-1m-v1  Completed 2026-11-10T14:46:54.47Z         66.2      66.2     40.5           16.7           8.7              0.2      
              v24a-second-fact data-1m-v1  Completed 2026-11-10T15:10:44.22Z         82.4      82.4     49.4           19.4          13.2              0.5      
v24b-second-fact-bidirectional data-1m-v1 Completed 2026-11-10T15:32:29.367Z         82.4      82.4     49.4           19.4          13.2              0.5      
              v25-many-to-many data-1m-v1                                             0.0       0.0      0.0            0.0           0.0              0.0      
                   v26-bad-dax data-1m-v1  Completed 2026-11-10T11:14:44.77Z         66.2      66.2     40.5           16.7           8.7              0.2      
  v27-high-cardinality-visuals data-1m-v1  Completed 2026-11-10T11:21:56.22Z         66.2      66.2     40.5           16.7           8.7              0.2      
              v99-kitchen-sink data-1m-v1    Failed 2026-11-04T17:07:21.493Z          0.1       0.1      0.0            0.1           0.0              0.0      
       v99a-no-big-calc-tables data-1m-v1 Completed 2026-11-04T19:25:26.327Z        197.8     197.8     79.7           85.1          31.2              1.8      
           v99b-one-sales-copy data-1m-v1                                             0.1       0.1      0.0            0.1           0.0              0.0      
           v99c-crossjoin-only data-1m-v1                                             0.1       0.1      0.0            0.1           0.0              0.0      
              v99d-power-query data-1m-v1 Completed 2026-11-04T21:03:59.737Z        197.8     197.8     79.7           85.1          31.2              1.8      
               v99e-sales-flat data-1m-v1 Completed 2026-11-05T08:16:25.417Z        356.6     356.6    147.3          152.7          54.9              1.8      
              v99f-calc-tables data-1m-v1 Completed 2026-11-05T08:12:09.147Z        385.7     385.7    172.2          154.2          57.5              1.8      
               v99g-sales-copy data-1m-v1 Completed 2026-11-05T10:42:15.053Z        540.6     540.6    258.5          200.5          79.8              1.8      
          v99h-staging-buffers data-1m-v1    Failed 2026-11-05T10:49:14.467Z          0.1       0.1      0.0            0.1           0.0              0.0      
         v99i-buffer-stg-sales data-1m-v1     Failed 2026-11-05T11:45:19.92Z          0.1       0.1      0.0            0.1           0.0              0.0      
      v99j-buffer-stg-customer data-1m-v1 Completed 2026-11-05T11:24:55.233Z        540.6     540.6    258.5          200.5          79.8              1.8      
               v99k-no-buffers data-1m-v1  Completed 2026-11-05T12:59:15.69Z        197.8     197.8     79.7           85.1          31.2              1.8      
          v99l-no-calc-columns data-1m-v1 Completed 2026-11-05T15:03:50.053Z        167.7     167.7     57.7           78.5          29.7              1.8      
              v99m-baseline-pq data-1m-v1  Completed 2026-11-05T14:57:05.12Z        101.3     101.3     64.1           25.8          11.1              0.3      
             v99n-text-staging data-1m-v1  Completed 2026-11-05T15:31:05.11Z         90.7      90.7     55.5           24.0          10.8              0.3      
                    v99o-sorts data-1m-v1 Completed 2026-11-05T15:28:12.593Z         99.0      99.0     61.8           25.8          11.1              0.3      
         v99p-high-cardinality data-1m-v1 Completed 2026-11-05T15:26:48.263Z        174.2     174.2     79.1           65.7          27.6              1.8      
           v99q-customer-stats data-1m-v1 Completed 2026-11-05T15:26:53.157Z        127.3     127.3     67.2           45.1          14.7              0.3      
```

## F2

```
                   model    data_tag                       last_refresh  as_found_mb  total_mb  data_mb  dictionary_mb  hierarchy_mb  relationship_mb error
            v00-baseline data-10m-v1 Completed 2026-11-10T09:33:16.537Z        625.7     625.7    380.5          159.1          82.6              3.4      
      v18-pq-10m-summary  data-1m-v1  Completed 2026-11-05T12:21:04.18Z         66.2      66.2     40.5           16.7           8.7              0.2      
        v19-pq-heavy-10m  data-1m-v1    Failed 2026-11-05T12:29:41.643Z          0.1       0.1      0.0            0.0           0.0              0.0      
             v20-pq-sort  data-1m-v1    Failed 2026-11-10T08:58:42.743Z          0.0       0.0      0.0            0.0           0.0              0.0      
         v21-pq-group-by  data-1m-v1     Failed 2026-11-06T08:40:06.31Z          0.0       0.0      0.0            0.0           0.0              0.0      
    v22-dax-calc-columns  data-1m-v1 Completed 2026-11-06T10:26:08.677Z         97.8      97.8     64.0           23.3          10.2              0.2      
     v23-dax-calc-tables  data-1m-v1   Completed 2026-11-06T10:26:22.4Z        148.6     148.6    112.9           19.4          16.0              0.2      
        v99-kitchen-sink  data-1m-v1     Failed 2026-11-03T20:06:17.17Z          0.1       0.1      0.0            0.1           0.0              0.0      
 v99a-no-big-calc-tables  data-1m-v1    Failed 2026-11-05T12:32:41.833Z          0.3       0.3      0.0            0.3           0.0              0.0      
     v99b-one-sales-copy  data-1m-v1     Failed 2026-11-05T12:32:18.73Z          0.1       0.1      0.0            0.1           0.0              0.0      
     v99c-crossjoin-only  data-1m-v1      Failed 2026-11-05T12:32:20.6Z          0.1       0.1      0.0            0.1           0.0              0.0      
        v99d-power-query  data-1m-v1    Failed 2026-11-05T12:33:08.633Z          0.3       0.3      0.0            0.3           0.0              0.0      
         v99e-sales-flat  data-1m-v1                                             0.4       0.4      0.0            0.3           0.0              0.0      
        v99f-calc-tables  data-1m-v1                                             0.4       0.4      0.0            0.3           0.0              0.0      
         v99g-sales-copy  data-1m-v1                                             0.4       0.4      0.0            0.3           0.0              0.0      
    v99h-staging-buffers  data-1m-v1                                             0.4       0.4      0.0            0.3           0.0              0.0      
   v99i-buffer-stg-sales  data-1m-v1                                             0.4       0.4      0.0            0.3           0.0              0.0      
v99j-buffer-stg-customer  data-1m-v1                                             0.4       0.4      0.0            0.3           0.0              0.0      
         v99k-no-buffers  data-1m-v1     Failed 2026-11-05T12:56:05.68Z          0.3       0.3      0.0            0.3           0.0              0.0      
    v99l-no-calc-columns  data-1m-v1    Failed 2026-11-05T15:06:07.107Z          0.3       0.3      0.0            0.3           0.0              0.0      
        v99m-baseline-pq  data-1m-v1 Completed 2026-11-05T14:57:59.643Z        101.3     101.3     64.1           25.8          11.1              0.3      
       v99n-text-staging  data-1m-v1  Completed 2026-11-05T15:34:23.81Z         90.7      90.7     55.5           24.0          10.8              0.3      
              v99o-sorts  data-1m-v1    Failed 2026-11-05T15:38:00.867Z          0.3       0.3      0.0            0.2           0.0              0.0      
   v99p-high-cardinality  data-1m-v1 Completed 2026-11-05T15:26:57.707Z        174.2     174.2     79.1           65.7          27.6              1.8      
     v99q-customer-stats  data-1m-v1    Failed 2026-11-05T15:37:38.617Z          0.3       0.3      0.0            0.2           0.0              0.0      
```

## PPU

```
                model   data_tag                       last_refresh  as_found_mb  total_mb  data_mb  dictionary_mb  hierarchy_mb  relationship_mb error
     v99-kitchen-sink data-1m-v1 Completed 2026-11-10T16:43:40.867Z        626.4     626.4    349.4          197.9          78.9              0.2      
 v99h-staging-buffers data-1m-v1  Completed 2026-11-11T08:55:05.19Z        540.6     540.6    258.5          200.5          79.8              1.8      
v99i-buffer-stg-sales data-1m-v1 Completed 2026-11-11T09:27:15.503Z        540.6     540.6    258.5          200.5          79.8              1.8      
```

## Log

```
2026-11-11T19:26:12Z run 20261111T192546Z-all-59dc: variant=all data_tag= targets=['F64old', 'F2', 'PPU'] expected_commit=06c9ed0e55c40ab85df7e8b1aeaeef248162ccd0
2026-11-11T19:26:33Z F64old: v00-baseline: 66.2 MB 
2026-11-11T19:26:41Z F64old: v18-pq-10m-summary: 66.2 MB 
2026-11-11T19:26:51Z F64old: v19-pq-heavy-10m: 0.1 MB 
2026-11-11T19:26:58Z F64old: v20-pq-sort: 65.3 MB 
2026-11-11T19:27:06Z F64old: v21-pq-group-by: 92.1 MB 
2026-11-11T19:27:14Z F64old: v22-dax-calc-columns: 97.8 MB 
2026-11-11T19:27:26Z F64old: v23-dax-calc-tables: 149.9 MB 
2026-11-11T19:27:33Z F64old: v24-bidirectional: 66.2 MB 
2026-11-11T19:27:42Z F64old: v24a-second-fact: 82.4 MB 
2026-11-11T19:27:51Z F64old: v24b-second-fact-bidirectional: 82.4 MB 
2026-11-11T19:27:59Z F64old: v25-many-to-many: 0.0 MB 
2026-11-11T19:28:07Z F64old: v26-bad-dax: 66.2 MB 
2026-11-11T19:28:15Z F64old: v27-high-cardinality-visuals: 66.2 MB 
2026-11-11T19:28:28Z F64old: v99-kitchen-sink: 0.1 MB 
2026-11-11T19:28:36Z F64old: v99a-no-big-calc-tables: 197.8 MB 
2026-11-11T19:28:41Z F64old: warm-up of Calendar Auto failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '2d7e4f9a-9e2c-4216-85db-8d2d59f15eef'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Calendar
2026-11-11T19:28:43Z F64old: warm-up of Date failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'cb35a001-be0f-49fd-be07-f5d7588888cb'

Caused by AdomdErrorResponseException:
The expression referenced column '<oii>Date</oii>'[<
2026-11-11T19:28:44Z F64old: warm-up of Product Date Grid failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'a8aaab74-f5f4-48d7-8260-08abb7f792eb'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Product 
2026-11-11T19:28:45Z F64old: warm-up of Sales failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'e55d6108-ab24-487c-a406-c541e2ce6f66'

Caused by AdomdErrorResponseException:
The expression referenced column '<oii>Sales</oii>'[
2026-11-11T19:28:45Z F64old: warm-up of Sales Copy failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '28e0a3b2-78d3-4e0f-b664-f178b2117a63'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Sales Co
2026-11-11T19:28:46Z F64old: warm-up of Sales Summary failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '1887a0b5-268d-4083-af79-5c379a5ce3c1'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Sales Su
2026-11-11T19:28:47Z F64old: v99b-one-sales-copy: 0.1 MB 
2026-11-11T19:28:52Z F64old: warm-up of Calendar Auto failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '381097dc-600c-47f0-8793-5ed62b19b47a'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Calendar
2026-11-11T19:28:54Z F64old: warm-up of Date failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '38d67d4d-7bd7-4d6f-8de7-f5b489eec963'

Caused by AdomdErrorResponseException:
The expression referenced column '<oii>Date</oii>'[<
2026-11-11T19:28:55Z F64old: warm-up of Product Date Grid failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '49a37219-db2e-43c3-8ceb-b99b3eb64152'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Product 
2026-11-11T19:28:56Z F64old: warm-up of Sales failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'ca2b3169-0b0e-4604-99c1-fc9a9e45f6ce'

Caused by AdomdErrorResponseException:
The expression referenced column '<oii>Sales</oii>'[
2026-11-11T19:28:56Z F64old: warm-up of Sales Copy failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '2d55dcff-1b67-4a31-9427-47c9eb6e38e4'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Sales Co
2026-11-11T19:28:58Z F64old: warm-up of Sales Summary failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'ecc16f8b-c71c-47f8-bc3a-7bde10fee2e2'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Sales Su
2026-11-11T19:28:59Z F64old: v99c-crossjoin-only: 0.1 MB 
2026-11-11T19:29:07Z F64old: v99d-power-query: 197.8 MB 
2026-11-11T19:29:26Z F64old: v99e-sales-flat: 356.6 MB 
2026-11-11T19:29:36Z F64old: v99f-calc-tables: 385.7 MB 
2026-11-11T19:29:46Z F64old: v99g-sales-copy: 540.6 MB 
2026-11-11T19:29:51Z F64old: warm-up of Calendar Auto failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '0a56d6f7-5c15-43de-a817-bf4e10a47637'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Calendar
2026-11-11T19:29:53Z F64old: warm-up of Date failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '9d1b5f99-badc-4ad9-9377-b5b785da4800'

Caused by AdomdErrorResponseException:
The expression referenced column '<oii>Date</oii>'[<
2026-11-11T19:29:54Z F64old: warm-up of Product Date Grid failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '10270eae-30a9-40bc-b847-d44f89b2b124'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Product 
2026-11-11T19:29:54Z F64old: warm-up of Sales failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '2d5a7e5b-712d-4afa-b750-467ca17a861a'

Caused by AdomdErrorResponseException:
The expression referenced column '<oii>Sales</oii>'[
2026-11-11T19:29:55Z F64old: warm-up of Sales Copy failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '58d93f6e-2d0d-42e9-9d74-517e97b1ad81'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Sales Co
2026-11-11T19:29:56Z F64old: warm-up of Sales Summary failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'd13088d8-522b-487d-ae6f-4e3d9450a08e'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Sales Su
2026-11-11T19:29:57Z F64old: v99h-staging-buffers: 0.1 MB 
2026-11-11T19:30:01Z F64old: warm-up of Calendar Auto failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '53d9aa78-119e-4952-ae35-fe9e26e87c5a'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Calendar
2026-11-11T19:30:03Z F64old: warm-up of Date failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'fd20a87b-2712-47b8-b29a-0d22387f6e68'

Caused by AdomdErrorResponseException:
The expression referenced column '<oii>Date</oii>'[<
2026-11-11T19:30:04Z F64old: warm-up of Product Date Grid failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'd82084d3-a25e-425a-a12a-330f6b2b881c'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Product 
2026-11-11T19:30:04Z F64old: warm-up of Sales failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '9c7d27c6-32c1-4b06-9fb7-be0f16a36295'

Caused by AdomdErrorResponseException:
The expression referenced column '<oii>Sales</oii>'[
2026-11-11T19:30:05Z F64old: warm-up of Sales Copy failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: '5ed4c2db-e8cc-48ab-918e-c306aa48fbc4'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Sales Co
2026-11-11T19:30:24Z F64old: warm-up of Sales Summary failed: An error occurred when running AdomdCommand. AdomdCommandActivityId: 'b37cb934-1ef8-4e10-8813-0a393ea97841'

Caused by AdomdErrorResponseException:
The query referenced calculated table '<oii>Sales Su
2026-11-11T19:30:25Z F64old: v99i-buffer-stg-sales: 0.1 MB 
2026-11-11T19:30:36Z F64old: v99j-buffer-stg-customer: 540.6 MB 
2026-11-11T19:30:44Z F64old: v99k-no-buffers: 197.8 MB 
2026-11-11T19:30:52Z F64old: v99l-no-calc-columns: 167.7 MB 
2026-11-11T19:31:00Z F64old: v99m-baseline-pq: 101.3 MB 
2026-11-11T19:31:08Z F64old: v99n-text-staging: 90.7 MB 
2026-11-11T19:31:15Z F64old: v99o-sorts: 99.0 MB 
2026-11-11T19:31:29Z F64old: v99p-high-cardinality: 174.2 MB 
2026-11-11T19:31:37Z F64old: v99q-customer-stats: 127.3 MB 
2026-11-11T19:31:44Z F2: v00-baseline: 625.7 MB 
2026-11-11T19:31:52Z F2: v18-pq-10m-summary: 66.2 MB 
2026-11-11T19:32:02Z F2: v19-pq-heavy-10m: 0.1 MB 
2026-11-11T19:32:10Z F2: v20-pq-sort: 0.0 MB 
2026-11-11T19:32:27Z F2: v21-pq-group-by: 0.0 MB 
2026-11-11T19:32:34Z F2: v22-dax-calc-columns: 97.8 MB 
2026-11-11T19:32:44Z F2: v23-dax-calc-tables: 148.6 MB 
2026-11-11T19:32:54Z F2: v99-kitchen-sink: 0.1 MB 
2026-11-11T19:33:02Z F2: v99a-no-big-calc-tables: 0.3 MB 
2026-11-11T19:33:26Z F2: v99b-one-sales-copy: 0.1 MB 
2026-11-11T19:33:43Z F2: v99c-crossjoin-only: 0.1 MB 
2026-11-11T19:33:51Z F2: v99d-power-query: 0.3 MB 
2026-11-11T19:33:59Z F2: v99e-sales-flat: 0.4 MB 
2026-11-11T19:34:09Z F2: v99f-calc-tables: 0.4 MB 
2026-11-11T19:34:27Z F2: v99g-sales-copy: 0.4 MB 
2026-11-11T19:34:37Z F2: v99h-staging-buffers: 0.4 MB 
2026-11-11T19:34:48Z F2: v99i-buffer-stg-sales: 0.4 MB 
2026-11-11T19:34:58Z F2: v99j-buffer-stg-customer: 0.4 MB 
2026-11-11T19:35:06Z F2: v99k-no-buffers: 0.3 MB 
2026-11-11T19:35:28Z F2: v99l-no-calc-columns: 0.3 MB 
2026-11-11T19:35:35Z F2: v99m-baseline-pq: 101.3 MB 
2026-11-11T19:35:42Z F2: v99n-text-staging: 90.7 MB 
2026-11-11T19:35:50Z F2: v99o-sorts: 0.3 MB 
2026-11-11T19:35:57Z F2: v99p-high-cardinality: 174.2 MB 
2026-11-11T19:36:05Z F2: v99q-customer-stats: 0.3 MB 
2026-11-11T19:36:16Z PPU: v99-kitchen-sink: 626.4 MB 
2026-11-11T19:36:34Z PPU: v99h-staging-buffers: 540.6 MB 
2026-11-11T19:36:45Z PPU: v99i-buffer-stg-sales: 540.6 MB 
```
