#!/usr/bin/env python3
"""Build or update annotations.csv from saved annotation JSON files, as SKILL.md asks.

Usage: python3 scripts/build_annotations_csv.py <folder-with-json-files> [annotations.csv]

Columns: title, year, medium, creator, model, date, summary, then the 48 slugs (scores).
Rows whose title and year are already in the CSV are left alone; new ones are added.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_annotations import SLUGS  # noqa: E402

HEAD = ["title", "year", "medium", "creator", "model", "date", "summary"]


def main(folder, out=None):
    folder = Path(folder)
    out = Path(out) if out else folder / "annotations.csv"
    existing = []
    if out.exists():
        with open(out, newline="", encoding="utf-8") as f:
            existing = list(csv.DictReader(f))
    seen = {(r["title"], r["year"]) for r in existing}
    added = 0
    for path in sorted(folder.glob("*.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        if not d.get("known") or d.get("ambiguous"):
            continue
        w = d["work"]
        key = (w["title"], str(w["year"]))
        if key in seen:
            continue
        row = {"title": w["title"], "year": w["year"], "medium": w["medium"], "creator": w["creator"],
               "model": d.get("model", ""), "date": d.get("date", ""), "summary": d["summary"]}
        for s in SLUGS:
            row[s] = d[s]["score"]
        existing.append(row)
        seen.add(key)
        added += 1
    with open(out, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=HEAD + SLUGS)
        wr.writeheader()
        wr.writerows(existing)
    print(f"{added} rows added; {len(existing)} rows in {out}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(*sys.argv[1:3])
