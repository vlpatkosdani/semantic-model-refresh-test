"""Generate the workload report and its DAX queries for one variant from reports/spec.yaml.

Usage (from the repo root):

    python reports/generate.py v00-baseline

Writes:
  models/<variant>/<variant>-workload.Report/   PBIR report bound to ../<variant>.SemanticModel
  reports/queries/<variant>.json                one DAX query per visual and page

The report is regenerated in full each time. Its logicalId and all names are derived from the
variant name, so regenerating gives the same files and Git sees no change.

The DAX imitates what Power BI Desktop sends for each visual type (SUMMARIZECOLUMNS, totals
through ROLLUPADDISSUBTOTAL, TOPN windows). It is checked against Performance Analyzer before
it is used for measurements; see reports/README.md.
"""
import hashlib
import json
import re
import shutil
import sys
import uuid
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "reports" / "spec.yaml"
NS = uuid.UUID("6f1c2b84-6a43-4c55-9d0e-6c1f0a7d2e51")   # fixed namespace for stable IDs

SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/"
FIELD = re.compile(r"^\s*(.+?)\[(.+)\]\s*$")


# ---------------------------------------------------------------- model metadata from TMDL

def unquote(name):
    name = name.strip()
    return name[1:-1].replace("''", "'") if name.startswith("'") and name.endswith("'") else name


def read_model(variant):
    tables_dir = ROOT / "models" / variant / f"{variant}.SemanticModel" / "definition" / "tables"
    if not tables_dir.is_dir():
        sys.exit(f"{tables_dir} not found")
    model = {}
    for f in sorted(tables_dir.glob("*.tmdl")):
        table, cols, types, measures, current = None, {}, {}, set(), None
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^table\s+(.+?)\s*$", line)
            if m:
                table = unquote(m.group(1))
                continue
            m = re.match(r"^\tcolumn\s+('(?:[^']|'')+'|[^=\s]+)", line)
            if m:
                current = unquote(m.group(1))
                cols[current] = None
                continue
            m = re.match(r"^\tmeasure\s+('(?:[^']|'')+'|[^=\s]+)", line)
            if m:
                measures.add(unquote(m.group(1)))
                current = None
                continue
            m = re.match(r"^\t\tsortByColumn:\s*(.+?)\s*$", line)
            if m and current:
                cols[current] = unquote(m.group(1))
            m = re.match(r"^\t\tdataType:\s*(\w+)", line)
            if m and current:
                types[current] = m.group(1)
        if table:
            model[table] = {"columns": cols, "types": types, "measures": measures}
    return model


def resolve(model, ref):
    m = FIELD.match(ref)
    if not m:
        sys.exit(f"bad field reference {ref!r}, expected Table[Name]")
    table, name = m.group(1).strip(), m.group(2).strip()
    if table not in model:
        sys.exit(f"table {table!r} not in the model")
    if name in model[table]["measures"]:
        return {"table": table, "name": name, "kind": "measure"}
    if name in model[table]["columns"]:
        return {"table": table, "name": name, "kind": "column", "sort_by": model[table]["columns"][name],
                "type": model[table]["types"].get(name, "string")}
    sys.exit(f"{table}[{name}] not in the model")


# ---------------------------------------------------------------- DAX

def dax_table(t):
    return "'" + t.replace("'", "''") + "'"


def dax_col(f, name=None):
    return f"{dax_table(f['table'])}[{name or f['name']}]"


def alias(f):
    """Result column name as Desktop writes it: 'Margin %' -> Margin__, '# Orders' -> v__Orders."""
    a = re.sub(r"[^A-Za-z0-9_]", "_", f["name"])
    return a if a[:1].isalpha() else "v" + a


NUMERIC = {"int64", "double", "decimal", "dateTime"}


def group_cols(cols):
    """Grouping columns plus their sort-by columns, as Desktop adds them."""
    out = []
    for c in cols:
        out.append(dax_col(c))
        if c.get("sort_by"):
            out.append(dax_col(c, c["sort_by"]))
    return out


def order_cols(cols):
    """Sort keys: the sort-by column first, then the column itself (Desktop orders by both)."""
    out = []
    for c in cols:
        if c.get("sort_by"):
            out.append(dax_col(c, c["sort_by"]))
        out.append(dax_col(c))
    return out


def level(c):
    """One grouping level: the column, or ROLLUPGROUP of it and its sort-by column."""
    if c.get("sort_by"):
        return f"ROLLUPGROUP({dax_col(c)}, {dax_col(c, c['sort_by'])})"
    return dax_col(c)


def rollup(cols, total):
    """All columns as one level with a single total flag (table rows)."""
    grp = level(cols[0]) if len(cols) == 1 else "ROLLUPGROUP(" + ", ".join(group_cols(cols)) + ")"
    return f'ROLLUPADDISSUBTOTAL({grp}, "{total}")'


def rollup_levels(cols, total):
    """One subtotal flag per level (matrix rows or columns). Returns the DAX and the flag names."""
    flags = [total] + [f"{total[:-5]}DM{i}Total" for i in range(1, len(cols))]
    args = ", ".join(f'{level(c)}, "{fl}"' for c, fl in zip(cols, flags))
    return f"ROLLUPADDISSUBTOTAL({args})", flags


def dax_literal(x):
    if isinstance(x, bool):
        return "TRUE" if x else "FALSE"
    if isinstance(x, (int, float)):
        return str(x)
    return '"' + str(x).replace('"', '""') + '"'


def filter_vars(filters):
    """Slicer selections as Desktop passes them: one TREATAS table per slicer, defined first."""
    names, defs = [], []
    for i, (f, selected) in enumerate(filters):
        name = "__DS0FilterTable" + (str(i + 1) if i else "")
        names.append(name)
        values = ", ".join(dax_literal(x) for x in selected)
        defs.append(f"\tVAR {name} =\n\t\tTREATAS({{{values}}}, {dax_col(f)})\n")
    return names, "".join(defs)


def dax_for(v, filters=()):
    """filters: (field, selected values) of the slicers that filter this visual."""
    filters = list(filters)
    body = dax_body(v, filters)
    _, defs = filter_vars(filters)
    if not defs:
        return body
    if body.startswith("DEFINE\n"):
        return "DEFINE\n" + defs + body[len("DEFINE\n"):]
    return "DEFINE\n" + defs + body


def dax_body(v, filters):
    t = v["type"]
    meas = [f for f in v["fields"].get("values", []) if f["kind"] == "measure"]
    fnames, _ = filter_vars(filters)
    ft = "".join(n + ", " for n in fnames)   # filter tables go between the groups and the measures
    m_args = ", ".join(f'"{alias(f)}", {dax_col(f)}' for f in meas)

    if t == "card":
        if filters:
            m_ign = ", ".join(f'"{alias(f)}", IGNORE({dax_col(f)})' for f in meas)
            return f"EVALUATE\n\tSUMMARIZECOLUMNS({ft}{m_ign})"
        return f"EVALUATE\n\tROW({m_args})"

    if t == "slicer":
        # The list of the column's values, filtered by the other slicers on the page.
        cats = v["fields"]["values"]
        keys = order_cols(cats)
        args = ", ".join(group_cols(cats) + fnames)
        return (f"DEFINE\n\tVAR __DS0Core =\n\t\tSUMMARIZECOLUMNS({args})\n"
                f"\tVAR __DS0PrimaryWindowed =\n\t\tTOPN(101, __DS0Core, {', '.join(k + ', 1' for k in keys)})\n"
                f"EVALUATE\n\t__DS0PrimaryWindowed\nORDER BY\n\t{', '.join(keys)}")

    if t in ("clusteredColumnChart", "clusteredBarChart", "lineChart"):
        # No sort is set on the visuals, so Desktop orders by the axis. A single numeric or date
        # axis is continuous and sampled; a text axis gets a window of 1,001 categories.
        cats = v["fields"]["category"]
        g = ", ".join(group_cols(cats))
        keys = order_cols(cats)
        order = ", ".join(keys)
        if len(cats) == 1 and cats[0]["type"] in NUMERIC and t != "clusteredBarChart":
            var, body = "__DS0BodyLimited", f"SAMPLE(3502, __DS0Core, {', '.join(k + ', 1' for k in keys)})"
        else:
            var, body = "__DS0PrimaryWindowed", f"TOPN(1001, __DS0Core, {', '.join(k + ', 1' for k in keys)})"
        return (f"DEFINE\n\tVAR __DS0Core =\n\t\tSUMMARIZECOLUMNS({g}, {ft}{m_args})\n"
                f"\tVAR {var} =\n\t\t{body}\n"
                f"EVALUATE\n\t{var}\nORDER BY\n\t{order}")

    if t == "tableEx":
        cols = [f for f in v["fields"]["values"] if f["kind"] == "column"]
        g = rollup(cols, "IsGrandTotalRowTotal")
        order = ", ".join(["[IsGrandTotalRowTotal] DESC"] + order_cols(cols))
        top = f"TOPN(502, __DS0Core, [IsGrandTotalRowTotal], 0, {', '.join(c + ', 1' for c in order_cols(cols))})"
        return (f"DEFINE\n\tVAR __DS0Core =\n\t\tSUMMARIZECOLUMNS({g}, {ft}{m_args})\n"
                f"\tVAR __DS0PrimaryWindowed =\n\t\t{top}\n"
                f"EVALUATE\n\t__DS0PrimaryWindowed\nORDER BY\n\t{order}")

    if t == "pivotTable":
        # A matrix opens collapsed: Desktop queries only the top level of rows and of columns.
        # Deeper levels are queried when a user expands them, which the workload does not do.
        rows, cols = v["fields"].get("rows", [])[:1], v["fields"].get("columns", [])[:1]
        row_dax, row_flags = rollup_levels(rows, "IsGrandTotalRowTotal")
        row_keys = []   # (expression, descending): subtotal flag first, then the level's sort keys
        for c, fl in zip(rows, row_flags):
            row_keys += [(f"[{fl}]", True)] + [(k, False) for k in order_cols([c])]
        if not cols:
            # Rows only: one window of 502, like a table.
            top_keys = ", ".join(f"{k}, {0 if d else 1}" for k, d in row_keys)
            order = ", ".join(k + (" DESC" if d else "") for k, d in row_keys)
            return (f"DEFINE\n\tVAR __DS0Core =\n\t\tSUMMARIZECOLUMNS({row_dax}, {ft}{m_args})\n"
                    f"\tVAR __DS0PrimaryWindowed =\n\t\tTOPN(502, __DS0Core, {top_keys})\n"
                    f"EVALUATE\n\t__DS0PrimaryWindowed\nORDER BY\n\t{order}")
        # Rows and columns: a window of 102 row groups and 102 column groups, joined by a column
        # index, returned as two result sets (column headers, then the body). As in Desktop.
        col_dax, col_flags = rollup_levels(cols, "IsGrandTotalColumnTotal")
        col_keys = []
        for c, fl in zip(cols, col_flags):
            col_keys += [f"[{fl}]"] + order_cols([c])
        row_summ = ", ".join(group_cols(rows) + [f"[{f}]" for f in row_flags])
        col_summ = ", ".join(group_cols(cols) + [f"[{f}]" for f in col_flags])
        top_rows = ", ".join(f"{k}, {0 if d else 1}" for k, d in row_keys)
        return (
            f"DEFINE\n\tVAR __DS0Core =\n\t\tSUMMARIZECOLUMNS({row_dax}, {col_dax}, {ft}{m_args})\n"
            f"\tVAR __DS0PrimaryWindowed =\n\t\tTOPN(102, SUMMARIZE(__DS0Core, {row_summ}), {top_rows})\n"
            f"\tVAR __DS0SecondaryBase =\n\t\tSUMMARIZE(__DS0Core, {col_summ})\n"
            f"\tVAR __DS0Secondary =\n\t\tTOPN(102, __DS0SecondaryBase, {', '.join(k + ', 1' for k in col_keys)})\n"
            f"\tVAR __DS0BodyLimited =\n\t\tNATURALLEFTOUTERJOIN(__DS0PrimaryWindowed, SUBSTITUTEWITHINDEX(__DS0Core, "
            f"\"ColumnIndex\", __DS0Secondary, {', '.join(k + ', ASC' for k in col_keys)}))\n"
            f"EVALUATE\n\t__DS0Secondary\nORDER BY\n\t{', '.join(col_keys)}\n"
            f"EVALUATE\n\t__DS0BodyLimited\nORDER BY\n\t"
            + ", ".join(k + (" DESC" if d else "") for k, d in row_keys) + ", [ColumnIndex]")

    sys.exit(f"visual type {t} has no DAX template")


# ---------------------------------------------------------------- PBIR

ROLES = {
    "card": {"values": "Values"},
    "clusteredColumnChart": {"category": "Category", "values": "Y"},
    "clusteredBarChart": {"category": "Category", "values": "Y"},
    "lineChart": {"category": "Category", "values": "Y"},
    "tableEx": {"values": "Values"},
    "pivotTable": {"rows": "Rows", "columns": "Columns", "values": "Values"},
    "slicer": {"values": "Values"},
}


def stable_id(*parts, n=20):
    return hashlib.sha1("/".join(parts).encode()).hexdigest()[:n]


def projection(f):
    kind = "Measure" if f["kind"] == "measure" else "Column"
    return {
        "field": {kind: {"Expression": {"SourceRef": {"Entity": f["table"]}}, "Property": f["name"]}},
        "queryRef": f"{f['table']}.{f['name']}",
        "nativeQueryRef": f["name"],
    }


def visual_json(variant, page, v, pos):
    state = {}
    for key, role in ROLES[v["type"]].items():
        fields = v["fields"].get(key, [])
        if fields:
            state[role] = {"projections": [projection(f) for f in fields]}
    objects = {}
    if v["type"] == "slicer" and v.get("selected"):
        # The selection is stored on the slicer; Desktop applies it to the page when it opens.
        f = v["fields"]["values"][0]
        src = f["table"][:1].lower()
        objects["general"] = [{"properties": {"filter": {"filter": {
            "Version": 2,
            "From": [{"Name": src, "Entity": f["table"], "Type": 0}],
            "Where": [{"Condition": {"In": {
                "Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": src}}, "Property": f["name"]}}],
                "Values": [[{"Literal": {"Value": pbir_literal(x)}}] for x in v["selected"]]}}}],
        }}}}]
    title = {"title": [{"properties": {
        "show": {"expr": {"Literal": {"Value": "true"}}},
        "text": {"expr": {"Literal": {"Value": "'" + v["title"].replace("'", "''") + "'"}}}}}]}
    return {
        "$schema": SCHEMA + "item/report/definition/visualContainer/2.13.0/schema.json",
        "name": stable_id(variant, page, v["id"]),
        "position": {"x": pos[0], "y": pos[1], "z": pos[4], "height": pos[3], "width": pos[2]},
        "visual": {"visualType": v["type"], "query": {"queryState": state},
                   **({"objects": objects} if objects else {}),
                   "visualContainerObjects": title, "drillFilterOtherVisuals": True},
    }


def pbir_literal(x):
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, int):
        return f"{x}L"
    if isinstance(x, float):
        return f"{x}D"
    return "'" + str(x).replace("'", "''") + "'"


def grid(n, width, height, gap=8):
    cols = {1: 1, 5: 3, 10: 5, 20: 5}.get(n) or max(1, round((n * width / height) ** 0.5))
    rows = -(-n // cols)
    w = (width - gap * (cols + 1)) // cols
    h = (height - gap * (rows + 1)) // rows
    return [(gap + (i % cols) * (w + gap), gap + (i // cols) * (h + gap), w, h, i) for i in range(n)]


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def build_report(variant, spec, visuals):
    src = ROOT / "models" / variant / f"{variant}.Report"
    out = ROOT / "models" / variant / f"{variant}-workload.Report"
    if out.exists():
        shutil.rmtree(out)
    d = out / "definition"
    name = f"{variant}-workload"

    write_json(out / ".platform", {
        "$schema": SCHEMA + "gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {"type": "Report", "displayName": name},
        "config": {"version": "2.0", "logicalId": str(uuid.uuid5(NS, name))},
    })
    write_json(out / "definition.pbir", {
        "$schema": SCHEMA + "item/report/definitionProperties/2.0.0/schema.json",
        "version": "4.0",
        "datasetReference": {"byPath": {"path": f"../{variant}.SemanticModel"}},
    })
    # Report settings and theme as in the variant's own report (or v00's).
    base = src if (src / "definition" / "report.json").exists() else \
        ROOT / "models" / "v00-baseline" / "v00-baseline.Report"
    d.mkdir(parents=True, exist_ok=True)
    shutil.copy(base / "definition" / "report.json", d / "report.json")
    shutil.copytree(base / "StaticResources", out / "StaticResources")
    write_json(d / "version.json", {
        "$schema": SCHEMA + "item/report/definition/versionMetadata/1.0.0/schema.json", "version": "2.0.0"})

    pw, ph = spec["page"]["width"], spec["page"]["height"]
    order = []
    for p in spec["pages"]:
        pname = p["name"]
        order.append(pname)
        write_json(d / "pages" / pname / "page.json", {
            "$schema": SCHEMA + "item/report/definition/page/2.1.0/schema.json",
            "name": pname, "displayName": p["title"], "displayOption": "FitToPage",
            "height": ph, "width": pw,
        })
        chosen = page_visuals(p, visuals)
        for v, pos in zip(chosen, grid(len(chosen), pw, ph)):
            vj = visual_json(variant, pname, v, pos)
            write_json(d / "pages" / pname / "visuals" / vj["name"] / "visual.json", vj)
    write_json(out.parent / f"{name}.pbip", {
        "$schema": SCHEMA + "pbip/pbipProperties/1.0.0/schema.json",
        "version": "1.0",
        "artifacts": [{"report": {"path": f"{name}.Report"}}],
        "settings": {"enableAutoRecovery": True},
    })
    write_json(d / "pages" / "pages.json", {
        "$schema": SCHEMA + "item/report/definition/pagesMetadata/1.1.0/schema.json",
        "pageOrder": order, "activePageName": order[0],
    })
    return out


def page_visuals(p, visuals):
    """A page shows the first N visuals of the pool, or the visuals it lists by id."""
    if isinstance(p["visuals"], int):
        if p["visuals"] > len(visuals):
            sys.exit(f"page {p['name']} asks for {p['visuals']} visuals, the pool has {len(visuals)}")
        return visuals[:p["visuals"]]
    by_id = {v["id"]: v for v in visuals}
    missing = [i for i in p["visuals"] if i not in by_id]
    if missing:
        sys.exit(f"page {p['name']}: visuals {missing} not in the pool")
    return [by_id[i] for i in p["visuals"]]


def page_filters(spec, visuals):
    """Slicers filter every other visual on their page (Desktop's default interactions).

    The DAX is stored per visual, so a visual on a page with slicers may not be on any other page.
    """
    out, pages_of = {}, {}
    for p in spec["pages"]:
        for v in page_visuals(p, visuals):
            pages_of.setdefault(v["id"], []).append(p["name"])
    for p in spec["pages"]:
        chosen = page_visuals(p, visuals)
        slicers = [v for v in chosen if v["type"] == "slicer" and v.get("selected")]
        if not slicers:
            continue
        for v in chosen:
            if len(pages_of[v["id"]]) > 1:
                sys.exit(f"{v['id']} is on a page with slicers ({p['name']}) and on {pages_of[v['id']]}")
            out[v["id"]] = [(s["fields"]["values"][0], s["selected"]) for s in slicers if s is not v]
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    variant = sys.argv[1]
    spec = yaml.safe_load(SPEC.read_text(encoding="utf-8"))
    extra = (spec.get("variants") or {}).get(variant, {})
    spec["visuals"] = spec["visuals"] + extra.get("visuals", [])
    spec["pages"] = spec["pages"] + extra.get("pages", [])
    model = read_model(variant)

    visuals = []
    for v in spec["visuals"]:
        if v["type"] not in ROLES:
            sys.exit(f"{v['id']}: unknown visual type {v['type']}")
        fields = {k: [resolve(model, r) for r in v.get(k, [])] for k in ROLES[v["type"]]}
        visuals.append({**v, "fields": fields})
    for p in spec["pages"]:
        page_visuals(p, visuals)   # stops on a page that asks for visuals the pool does not have

    report = build_report(variant, spec, visuals)

    filters = page_filters(spec, visuals)
    queries = {"variant": variant, "spec_version": spec["version"], "visuals": {}, "pages": {}}
    for v in visuals:
        queries["visuals"][v["id"]] = {"type": v["type"], "title": v["title"],
                                       "visual_name": None, "dax": dax_for(v, filters.get(v["id"], ()))}
    for p in spec["pages"]:
        ids = [v["id"] for v in page_visuals(p, visuals)]
        queries["pages"][p["name"]] = {
            "title": p["title"], "visuals": ids,
            "visual_names": {i: stable_id(variant, p["name"], i) for i in ids},
        }
    for v in queries["visuals"].values():
        v.pop("visual_name")
    write_json(ROOT / "reports" / "queries" / f"{variant}.json", queries)
    print(f"{report.relative_to(ROOT)}: {len(spec['pages'])} pages")
    print(f"reports/queries/{variant}.json: {len(visuals)} visual queries")


if __name__ == "__main__":
    main()
