# Harness run 20261110T085434Z-v20-6a89

- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: F2, F64
- Expected commit: cff49756f0f505e68d63aeaeb620a2a56897e44b
- Notebook run: 6e6e626e-4c4c-45c2-91b3-5ff300d0098d
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 8ea24a06-b500-4365-9418-64e98cf558e1, 2026-11-10T08:57:33.7 to 2026-11-10T08:58:42.743, workspace at cff4975, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v20-pq-sort on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Engine cancelled at 3,179 MB against a limit of 3,067 MB (database size before the command 4 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3179 MB, memory limit 3067 MB, database size before command execution 4 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v20-pq-sort on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v20-pq-sort-resource-governance.png**

## F64

- Result: **refreshed** 
- Peak 5,269 MB, Power Query 5,043 MB, duration 2 min, CPU 128 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request 4ebd9bcb-ecf0-43a9-a87f-55263b99cf74, 2026-11-10T08:58:50.297 to 2026-11-10T09:00:43.543, workspace at cff4975, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v20-pq-sort on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-10T08:52:36Z): peak 5,269 MB vs 623 MB (+4,646 MB), Power Query 5,043 MB vs 599 MB, model 72 MB vs 73 MB.
- Measured peak against per-model limits: F2 3,066 MB: OVER (172%); F16 5,120 MB: OVER (103%); F32 10,240 MB: fits (51%); F64 25,600 MB: fits (21%).

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    fada6b25-c3b0-4073-896a-f43875bd0a8b TabularSequencePoint        106.3     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        104.9    11.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.7    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         55.5    11.1 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql         49.1     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.5     5.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.4     4.4       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.4     1.2       0
                                                                                       Commit          2.7     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.4     1.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.4     1.1  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.9     0.5       0
```

## Log

```
2026-11-10T08:56:57Z run 20261110T085434Z-v20-6a89: variant=v20-pq-sort data_tag=data-1m-v1 targets=['F2', 'F64'] expected_commit=cff49756f0f505e68d63aeaeb620a2a56897e44b
2026-11-10T08:57:06Z F2: update from Git 8d84b60cdbe0cd2ba7d5133827155a3fbd18995e -> cff49756f0f505e68d63aeaeb620a2a56897e44b
2026-11-10T08:57:14Z F2: v20-pq-sort is e70f98a2-f0fa-4535-9cdb-7f162422b8cc, DataTag reads back data-1m-v1
2026-11-10T08:57:20Z F64: workspace already at cff49756f0f505e68d63aeaeb620a2a56897e44b
2026-11-10T08:57:23Z F64: v20-pq-sort is fada6b25-c3b0-4073-896a-f43875bd0a8b, DataTag reads back data-1m-v1
2026-11-10T08:57:33Z F2: refresh started, request 8ea24a06-b500-4365-9418-64e98cf558e1
2026-11-10T08:58:44Z F2: refresh failed (Failed) resource governance
2026-11-10T08:58:50Z F64: refresh started, request 4ebd9bcb-ecf0-43a9-a87f-55263b99cf74
2026-11-10T09:01:01Z F64: refresh refreshed (Completed) 
2026-11-10T09:02:38Z F64: ExecutionMetrics event found
```
