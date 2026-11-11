# Harness run 20261111T195607Z-v25-f02f

- Task: queries
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: 53cfca4864e70f1fda420adacf9ab5955bb08783
- Notebook run: 5cb0ccb0-68c6-4bbe-8ba4-f8db71d1b4fc
- Pages p01,p05,p10,p20,pf,pm, modes cold,warm, concurrency seq,page, repeats 5, queries from harness/queries/20261111T195607Z-v25-f02f.json

## F64

- 1100 queries sent (100 warm-up), 0 failed, 1100 found in SemanticModelLogs, 0 throttling retries
- Workspace at 53cfca4, DataTag read back data-1m-v1

Median and p90 over the repeats, per page:

```
page mode conc  repeats  page_wall_median_ms  page_wall_p90_ms  server_max_median_ms  server_sum_median_ms  cpu_sum_median_ms  peak_mem_max_kb  errors
 p01 cold page        5                604.0             618.0                  31.0                  31.0               31.0             4259       0
 p01 cold  seq        5                565.0             642.6                  16.0                  16.0               31.0             4259       0
 p01 warm page        5                558.0             694.2                   0.0                   0.0                0.0             1032       0
 p01 warm  seq        5                518.0             916.2                  16.0                  16.0               16.0             1032       0
 p05 cold page        5                618.0             664.0                 188.0                 254.0              375.0            14460       0
 p05 cold  seq        5               1189.0            1342.4                 156.0                 205.0              251.0            13854       0
 p05 warm page        5                499.0             563.4                  16.0                  16.0               16.0             1032       0
 p05 warm  seq        5                973.0            1003.6                  16.0                  16.0               32.0             1032       0
 p10 cold page        5                532.0             629.6                 141.0                 297.0              469.0            14435       0
 p10 cold  seq        5               1694.0            1908.0                 141.0                 268.0              376.0            14459       0
 p10 warm page        5                466.0             481.2                  16.0                  32.0               64.0             1032       0
 p10 warm  seq        5               1583.0            1653.0                  16.0                  32.0               80.0             1032       0
 p20 cold page        5               1388.0            1615.2                 877.0                1798.0             2267.0            56059       0
 p20 cold  seq        5               4238.0            4557.2                 814.0                1479.0             1894.0            55835       0
 p20 warm page        5                607.0             679.2                  16.0                  64.0              142.0             1032       0
 p20 warm  seq        5               3277.0            3374.0                  16.0                  80.0              127.0             1025       0
  pf cold page        5                534.0             690.8                  63.0                 206.0              250.0            11526       0
  pf cold  seq        5               1344.0            1436.2                  63.0                 158.0              235.0            11460       0
  pf warm page        5                473.0             493.2                  16.0                  32.0               48.0             3365       0
  pf warm  seq        5               1205.0            1630.4                  16.0                  48.0               79.0             3365       0
  pm cold page        5                926.0            1120.2                 609.0                 922.0             1094.0            63792       0
  pm cold  seq        5               1651.0            1704.4                 578.0                 887.0             1094.0            59057       0
  pm warm page        5                487.0             722.6                 172.0                 375.0              438.0            28525       0
  pm warm  seq        5               1367.0            1394.8                 156.0                 345.0              422.0            29142       0
```

## Log

```
2026-11-11T19:56:50Z run 20261111T195607Z-v25-f02f: variant=v25-many-to-many data_tag=data-1m-v1 targets=['F64'] expected_commit=53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T19:56:56Z F64: workspace already at 53cfca4864e70f1fda420adacf9ab5955bb08783
2026-11-11T19:56:57Z F64: v25-many-to-many is 93317245-89ef-4014-abe3-f82efec8ba78, DataTag reads back data-1m-v1
2026-11-11T19:57:34Z F64: page p01 done, 22 queries so far
2026-11-11T19:58:30Z F64: page p05 done, 132 queries so far
2026-11-11T20:00:42Z F64: page p10 done, 352 queries so far
2026-11-11T20:05:06Z F64: page p20 done, 792 queries so far
2026-11-11T20:06:51Z F64: page pf done, 968 queries so far
2026-11-11T20:08:11Z F64: page pm done, 1100 queries so far
2026-11-11T20:08:11Z F64: monitoring database Monitoring KQL database
2026-11-11T20:10:17Z F64: 1100 of 1100 queries found in SemanticModelLogs
```
