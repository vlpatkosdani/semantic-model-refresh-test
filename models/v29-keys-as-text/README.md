# v29-keys-as-text

The baseline with the key columns loaded as text. The most common real-world type mistake: IDs that arrive as text from a source system and stay that way.

## What changed vs baseline

| Table | Columns now text instead of whole number |
|---|---|
| Sales | Order Number, CustomerKey, StoreKey, ProductKey |
| Customer | CustomerKey |
| Product | ProductKey |
| Store | StoreKey |

Everything else, including measures and relationships (now text to text), is the same as in the baseline.

## Why this run

Keys are the highest-cardinality columns in the model: Order Number has 980,666 values on 1M, CustomerKey 104,990. As text they need a hash dictionary instead of value encoding.

## Expected effect

- Model size: larger, mostly in the Sales key columns and their dictionaries.
- Refresh and queries: small differences, if any. No numbers until measured.

## Runs

1. Refresh on F64 with 1M, model sizes.
2. Query workload on F64 with 1M, pages p01 to p20.

## Results

F64, 1M, 2026-11-11 and 2026-11-12. Refresh run `20261112T081715Z-v29-b0f1`, query run `20261112T092209Z-v29-a76d` (all 792 queries succeeded). Query numbers are medians over 5 repeats, cold cache, all visuals of the page at once. The v00 column is the range over its six refreshes and three query runs on F64 with 1M.

| | v00-baseline | v29-keys-as-text |
|---|---|---|
| Refresh peak | 543 to 698 MB | 1,489 MB |
| Power Query peak | 270 to 599 MB | 1,465 MB |
| Duration | 0.6 to 0.8 min | 0.5 min |
| CPU | 55 to 71 s | 56 s |
| Model, backup size in the refresh log | 72.7 MB | 69.0 MB |
| Model in memory right after the refresh | 92.7 MB | 141.9 MB |
| p05 cold, slowest visual | 125 to 141 ms | 141 ms |
| p05 cold, CPU | 313 to 328 ms | 297 ms |
| p20 cold, slowest visual | 672 to 719 ms | 594 ms |
| p20 cold, CPU | 1,890 to 2,172 ms | 1,737 ms |
| p20 cold, peak per query | 58 MB | 28 MB |

- Model: 1.5 times the baseline in memory (141.9 MB against 92.7 MB). The backup size in the refresh log is slightly smaller, as in v28.
- Refresh: the first run peaked at 1,489 MB, almost all Power Query (1,465 MB). Two more runs, alternating with v00-baseline on 2026-11-13, are below. Duration is the same as the baseline.
- Queries: no slower than the baseline, if anything slightly faster on p20. The peak per query halves (28 MB against 58 MB), as in v28. One run.

### Repeat, alternating with v00-baseline, F64, 1M, 2026-11-13

| Run | Harness run | Peak | Power Query | CPU | In memory after |
|---|---|---|---|---|---|
| v00-baseline | `20261113T091752Z-v00-89cb` | 703 MB | 423 MB | 57 s | 92.7 MB |
| v29 | `20261113T092511Z-v29-4df0` | 665 MB | 398 MB | 104 s | 141.9 MB |
| v00-baseline | `20261113T093230Z-v00-9a26` | 856 MB | 847 MB | 57 s | 92.7 MB |
| v29 | `20261113T093950Z-v29-f936` | 1,735 MB | 1,720 MB | 122 s | 141.9 MB |

Two of the three v29 runs peaked at 1.5 to 1.7 GB of Power Query memory, one stayed at the baseline level. v00-baseline has not gone above 847 MB in any run. So converting the keys to text probably raises the Power Query peak, but by a varying amount. CPU was about twice the baseline in the two runs of 2026-11-13, but not in the first run (56 s). The model in memory is the same in every run: 141.9 MB against 92.7 MB.

