"""Compare generated DAX with queries captured from Performance Analyzer.

Usage: python reports/validate.py v00-baseline

Reads reports/queries/<variant>.json and reports/validation/<variant>/<visual id>.dax.
Comments and whitespace are ignored. Prints SAME, DIFF (with the first difference) or
'not captured' per visual, and exits with 1 if anything differs.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(s):
    return re.sub(r"\s+", "", re.sub(r"//[^\n]*", "", s))


def main():
    variant = sys.argv[1]
    queries = json.loads((ROOT / "reports" / "queries" / f"{variant}.json").read_text(encoding="utf-8"))
    vdir = ROOT / "reports" / "validation" / variant
    diff = 0
    for vid, v in queries["visuals"].items():
        f = vdir / f"{vid}.dax"
        if not f.exists():
            print(f"{vid} {v['type']}: not captured")
            continue
        a, b = norm(f.read_text(encoding="utf-8")), norm(v["dax"])
        if a == b:
            print(f"{vid} {v['type']}: SAME")
            continue
        diff += 1
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        print(f"{vid} {v['type']}: DIFF\n  desktop:   ...{a[max(0, i - 60):i + 80]}\n  generated: ...{b[max(0, i - 60):i + 80]}")
    sys.exit(1 if diff else 0)


if __name__ == "__main__":
    main()
