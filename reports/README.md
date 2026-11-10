# Workload reports

One spec, `spec.yaml`, defines the query workload for every variant: a pool of 20 visuals and four pages that show the first 1, 5, 10 and 20 of them. `generate.py` turns it into a report and a query file per variant.

```
python reports/generate.py v00-baseline
```

| Output | What it is |
|---|---|
| `models/<variant>/<variant>-workload.Report/` | PBIR report bound to the variant's model (`byPath ../<variant>.SemanticModel`). Synced to both workspaces with the model. |
| `models/<variant>/<variant>-workload.pbip` | Opens that report in Power BI Desktop |
| `reports/queries/<variant>.json` | The DAX of each visual, and which visuals each page shows |

The variant's own report (`<variant>.Report`) is not touched. The workload report is regenerated in full each time; names and the logicalId come from the variant name, so the same spec gives the same files.

## Fields

Fields are written as `Table[Column]` or `Table[Measure]`. The generator reads the variant's TMDL, decides which is which, and stops if a field does not exist. Columns with a sort-by column get it added to the query, as Desktop does.

## The DAX

Each visual type has a template modelled on the queries Power BI Desktop sends:

| Visual | Query |
|---|---|
| card | `ROW` with the measure |
| column and bar chart | `SUMMARIZECOLUMNS`, top 1,001 by the first measure |
| line chart | `SUMMARIZECOLUMNS`, top 3,502 ordered by the axis |
| table | `SUMMARIZECOLUMNS` with `ROLLUPADDISSUBTOTAL` for the total row, top 502 |
| matrix | `ROLLUPADDISSUBTOTAL` per row and column level for subtotals, top 502 |

All 20 queries run on v00 (checked with the `executeQueries` API on F64, 2026-11-10).

## Checking against Performance Analyzer

The templates are close to what Desktop sends, not identical. Before using the queries for measurements:

1. Open `models/v00-baseline/v00-baseline-workload.pbip` in Desktop and refresh.
2. View > Performance analyzer > Start recording, then open page `20 visuals`.
3. Copy the query of each visual (Copy query) into `reports/validation/v00-baseline/<visual id>.dax`. The visual title says which visual it is.
4. Tell Claude Code; it compares them with `reports/queries/v00-baseline.json` and adjusts the templates where the shape differs (extra columns, other window sizes, different subtotal handling).

The query runner uses the captured Desktop queries where they exist and the generated ones otherwise, and records which.
