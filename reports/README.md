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
| column, bar and line chart | `SUMMARIZECOLUMNS`, ordered by the axis (sort-by column first). A numeric axis on a column or line chart is sampled with `SAMPLE(3502)`, otherwise `TOPN(1001)` |
| table | `SUMMARIZECOLUMNS` with `ROLLUPADDISSUBTOTAL` for the total row, `TOPN(502)`. Several columns or a sort-by column are grouped with `ROLLUPGROUP` |
| matrix, rows only | like a table |
| matrix, rows and columns | a window of 102 row groups and 102 column groups, joined with `NATURALLEFTOUTERJOIN` and `SUBSTITUTEWITHINDEX`; two result sets (column headers, then body) |

No sort is set on the visuals, so every visual is ordered by its axis or rows. A matrix opens collapsed, so only its top level of rows and columns is queried.

Result names follow Desktop: other characters become `_`, and a name that does not start with a letter gets a `v` in front (`# Orders` is `v__Orders`).

Checked on 2026-11-10: 19 of the 20 queries are identical to Performance Analyzer apart from whitespace (`python reports/validate.py v00-baseline`). v13 was not captured; it uses the same table template as v05 and v18 with a sort-by column grouped as in v20.

The `executeQueries` REST API returns only the first result set, which for a matrix with columns is the column headers. The query runner therefore sends the queries over XMLA.

## Checking against Performance Analyzer

The templates are close to what Desktop sends, not identical. Before using the queries for measurements:

1. Open `models/v00-baseline/v00-baseline-workload.pbip` in Desktop and refresh.
2. View > Performance analyzer > Start recording, then open page `20 visuals`.
3. Copy the query of each visual (Copy query) into `reports/validation/v00-baseline/<visual id>.dax`. The visual title says which visual it is.
4. Run `python reports/validate.py v00-baseline`. It prints SAME or the first difference per visual. Adjust the templates in `generate.py` where the shape differs.

The query runner uses the captured Desktop queries where they exist and the generated ones otherwise, and records which.
