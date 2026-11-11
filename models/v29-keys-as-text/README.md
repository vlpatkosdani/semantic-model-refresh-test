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

Not run yet.
