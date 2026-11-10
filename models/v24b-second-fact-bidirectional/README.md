# v24b-second-fact-bidirectional

v24a-second-fact with one relationship changed: Sales to Customer filters in both directions. This is the model where a bidirectional relationship makes the filter paths ambiguous.

## What changed vs v24a

| Relationship | v24a | v24b |
|---|---|---|
| `Sales[CustomerKey]` to `Customer[CustomerKey]` | single direction | both directions |

## Why this run

With two fact tables on the same dimensions, one bidirectional relationship opens a second path between tables that were already related:

- Store to Orders directly, and Store to Sales to Customer to Orders.
- Date to Orders directly, and Date to Sales to Customer to Orders.

Power BI does not allow two active filter paths between the same tables. The question is what it does with this model: refuse the relationship in Desktop, fail the deployment or refresh in the service, or accept it and pick a path. The report author's intent is the usual one, "filter orders by the product category the customer bought".

Against v24-bidirectional (the same change on a single fact), it shows whether a second fact changes what the bidirectional relationship costs.

## Expected effect

Not known until tried. The first step was to open the model in Power BI Desktop, before deploying it, because an item the service cannot load blocks the update from Git for the whole workspace.

Opened in Power BI Desktop on 2026-11-10: the model loaded and refreshed without an error or warning, and Desktop did not make any relationship inactive (`relationships.tmdl` unchanged after the refresh). Desktop accepts the two paths. Which path a filter from Store or Date takes to Orders is the next question.

## Runs

1. Open in Power BI Desktop and record what happens. Done, accepted.
2. Refresh on F64 with 1M, then the query workload with pages p01 to p20, pf and po. Compare with v24a-second-fact.

## Results

Not run yet.
