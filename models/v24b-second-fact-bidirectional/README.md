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

F64, 1M, harness runs on 2026-11-10.

Refresh (run `20261110T152942Z-v24b-a4dc`): peak 1,102 MB, Power Query 1,003 MB, 1 min, 3,541,806 rows, model 103 MB. The service deployed and refreshed the model without an error, as Desktop did.

### Which path the filters take

Order Count with different filters, checked with DAX on 2026-11-10 against v24a-second-fact (single direction):

| Filter | v24a | v24b |
|---|---|---|
| none | 980,666 | 980,666 |
| Germany | 111,258 | 111,258 |
| Computers | 980,666 | 966,183 |
| Computers and Germany | 111,258 | 110,112 |
| Store "Contoso Store Berlin" | 7,377 | 7,377 |
| Store Berlin and Computers | 7,377 | 5,091 |
| Year 2020 | 70,229 | 70,229 |
| Year 2020 and Computers | 70,229 | 44,912 |

- A Store or Year filter alone gives the same count on both models. The engine uses the direct relationship from Store and Date to Orders, not the second path through Sales and Customer.
- A Category filter now reaches Orders, but through Customer: 966,183 is the number of orders placed by customers who bought a computer at any time. The number of orders that contain a computer is 422,638 (`DISTINCTCOUNT ( Sales[Order Number] )` with the same filter). A report author who turns on both directions to "make the Category slicer work" on Orders gets a number that answers a different question, with no error or warning.

### Query workload

Run `20261110T153459Z-v24b-f1b0`, 1,100 queries. Medians over 5 repeats, cold cache, all visuals at once:

| Page | Slowest visual v24a | Slowest visual v24b | CPU v24a | CPU v24b | Peak per query v24a | Peak per query v24b |
|---|---|---|---|---|---|---|
| p20 | 719 ms | 688 ms | 2,017 ms | 1,954 ms | 55 MB | 58 MB |
| pf | 62 ms | 47 ms | 233 ms | 266 ms | 12 MB | 12 MB |
| po | 16 ms | 78 ms | 48 ms | 281 ms | 6 MB | 7 MB |

On the Orders page every visual that counts orders got slower: Orders by year 0 to 63 ms, Stores 16 to 78 ms, Orders by city 16 to 47 ms, and the Country slicer 0 to 31 ms. With a warm cache Orders by year and Stores still took 31 ms each on v24b, against 0 ms on v24a. In absolute terms these are small numbers on 1M rows; the filter now has to cross Sales (2.3M rows) to reach Customer and then Orders.

Ten queries are counted as failed in `results/query-runs.csv`. They are not engine errors: all ten are the v01 matrix on page p10, sent all at once, which the REST API cannot return (two result sets). The harness counts that as a success only when the server's log confirms the query, and workspace monitoring stored no events for the 100 queries of p10 sent all at once in this run. The same kind of log loss happened on v26-bad-dax.
