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
        table, cols, measures, current = None, {}, set(), None
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
        if table:
            model[table] = {"columns": cols, "measures": measures}
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
        return {"table": table, "name": name, "kind": "column", "sort_by": model[table]["columns"][name]}
    sys.exit(f"{table}[{name}] not in the model")


# ---------------------------------------------------------------- DAX

def dax_table(t):
    return "'" + t.replace("'", "''") + "'"


def dax_col(f, name=None):
    return f"{dax_table(f['table'])}[{name or f['name']}]"


def alias(f):
    return re.sub(r"[^A-Za-z0-9_]", "_", f["name"])


def group_cols(cols):
    """Grouping columns plus their sort-by columns, as Desktop adds them."""
    out = []
    for c in cols:
        out.append(dax_col(c))
        if c.get("sort_by"):
            out.append(dax_col(c, c["sort_by"]))
    return out


def order_cols(cols):
    return [dax_col(c, c["sort_by"]) if c.get("sort_by") else dax_col(c) for c in cols]


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


def dax_for(v):
    t = v["type"]
    meas = [f for f in v["fields"]["values"] if f["kind"] == "measure"]
    m_args = ", ".join(f'"{alias(f)}", {dax_col(f)}' for f in meas)

    if t == "card":
        return f"EVALUATE\n\tROW({m_args})"

    if t in ("clusteredColumnChart", "clusteredBarChart", "lineChart"):
        cats = v["fields"]["category"]
        g = ", ".join(group_cols(cats))
        if t == "lineChart":   # ordered by the axis
            order = ", ".join(order_cols(cats))
            top = f"TOPN(3502, __DS0Core, {', '.join(c + ', 1' for c in order_cols(cats))})"
        else:                  # ordered by the first measure, descending
            order = f"[{alias(meas[0])}] DESC, " + ", ".join(order_cols(cats))
            top = f"TOPN(1001, __DS0Core, [{alias(meas[0])}], 0, {', '.join(c + ', 1' for c in order_cols(cats))})"
        return (f"DEFINE\n\tVAR __DS0Core =\n\t\tSUMMARIZECOLUMNS({g}, {m_args})\n"
                f"\tVAR __DS0PrimaryWindowed =\n\t\t{top}\n"
                f"EVALUATE\n\t__DS0PrimaryWindowed\nORDER BY\n\t{order}")

    if t == "tableEx":
        cols = [f for f in v["fields"]["values"] if f["kind"] == "column"]
        g = rollup(cols, "IsGrandTotalRowTotal")
        order = ", ".join(["[IsGrandTotalRowTotal] DESC"] + order_cols(cols))
        top = f"TOPN(502, __DS0Core, [IsGrandTotalRowTotal], 0, {', '.join(c + ', 1' for c in order_cols(cols))})"
        return (f"DEFINE\n\tVAR __DS0Core =\n\t\tSUMMARIZECOLUMNS({g}, {m_args})\n"
                f"\tVAR __DS0PrimaryWindowed =\n\t\t{top}\n"
                f"EVALUATE\n\t__DS0PrimaryWindowed\nORDER BY\n\t{order}")

    if t == "pivotTable":
        rows, cols = v["fields"].get("rows", []), v["fields"].get("columns", [])
        parts, keys = [], []   # keys: (expression, descending)
        for axis, total in ((rows, "IsGrandTotalRowTotal"), (cols, "IsGrandTotalColumnTotal")):
            if not axis:
                continue
            dax, names = rollup_levels(axis, total)
            parts.append(dax)
            for c, fl in zip(axis, names):
                keys += [(f"[{fl}]", True), (order_cols([c])[0], False)]
        g = ", ".join(parts)
        flags = [k + (" DESC" if d else "") for k, d in keys]
        top_keys = ", ".join(f"{k}, {0 if d else 1}" for k, d in keys)
        return (f"DEFINE\n\tVAR __DS0Core =\n\t\tSUMMARIZECOLUMNS({g}, {m_args})\n"
                f"\tVAR __DS0PrimaryWindowed =\n\t\tTOPN(502, __DS0Core, {top_keys})\n"
                f"EVALUATE\n\t__DS0PrimaryWindowed\nORDER BY\n\t{', '.join(flags)}")

    sys.exit(f"visual type {t} has no DAX template")


# ---------------------------------------------------------------- PBIR

ROLES = {
    "card": {"values": "Values"},
    "clusteredColumnChart": {"category": "Category", "values": "Y"},
    "clusteredBarChart": {"category": "Category", "values": "Y"},
    "lineChart": {"category": "Category", "values": "Y"},
    "tableEx": {"values": "Values"},
    "pivotTable": {"rows": "Rows", "columns": "Columns", "values": "Values"},
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
    title = {"title": [{"properties": {
        "show": {"expr": {"Literal": {"Value": "true"}}},
        "text": {"expr": {"Literal": {"Value": "'" + v["title"].replace("'", "''") + "'"}}}}}]}
    return {
        "$schema": SCHEMA + "item/report/definition/visualContainer/2.13.0/schema.json",
        "name": stable_id(variant, page, v["id"]),
        "position": {"x": pos[0], "y": pos[1], "z": pos[4], "height": pos[3], "width": pos[2]},
        "visual": {"visualType": v["type"], "query": {"queryState": state},
                   "visualContainerObjects": title, "drillFilterOtherVisuals": True},
    }


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
        chosen = visuals[:p["visuals"]]
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


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    variant = sys.argv[1]
    spec = yaml.safe_load(SPEC.read_text(encoding="utf-8"))
    model = read_model(variant)

    visuals = []
    for v in spec["visuals"]:
        if v["type"] not in ROLES:
            sys.exit(f"{v['id']}: unknown visual type {v['type']}")
        fields = {k: [resolve(model, r) for r in v.get(k, [])] for k in ROLES[v["type"]]}
        visuals.append({**v, "fields": fields})
    needed = max(p["visuals"] for p in spec["pages"])
    if needed > len(visuals):
        sys.exit(f"a page asks for {needed} visuals, the pool has {len(visuals)}")

    report = build_report(variant, spec, visuals)

    queries = {"variant": variant, "spec_version": spec["version"], "visuals": {}, "pages": {}}
    for v in visuals:
        queries["visuals"][v["id"]] = {"type": v["type"], "title": v["title"],
                                       "visual_name": None, "dax": dax_for(v)}
    for p in spec["pages"]:
        ids = [v["id"] for v in visuals[:p["visuals"]]]
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
