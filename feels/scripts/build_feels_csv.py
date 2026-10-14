#!/usr/bin/env python3
"""Build feels-annotations.csv from feels-annotate JSON files.

Usage: python3 build_feels_csv.py <out.csv> <file.json> [<file.json> ...]

One row per story and perspective. Columns: title, year, medium, creator,
model, date, mode, perspective, summary, monera (joined with "; "), then the
74 feel slugs in order and the 8 extra slugs in order, each holding the score.
Rows whose (title, year, perspective) is already in the file are not added.
"""
import csv
import json
import os
import sys

from validate_feels import EXTRA, FEELS

HEAD = ["title", "year", "medium", "creator", "model", "date", "mode",
        "perspective", "summary", "monera"] + FEELS + EXTRA


def row_of(d):
    w = d["work"]
    r = [w["title"], w["year"], w["medium"], w["creator"], d["model"],
         d["date"], d["mode"], d["perspective"], d["summary"],
         "; ".join(d["monera"])]
    r += [d["feels"][k]["score"] for k in FEELS]
    r += [d["extra"][k]["score"] for k in EXTRA]
    return r


def main(out, paths):
    existing = set()
    rows = []
    if os.path.exists(out):
        with open(out, newline="", encoding="utf-8") as f:
            rd = csv.reader(f)
            head = next(rd, None)
            if head != HEAD:
                sys.exit(f"{out} has a different header; refusing to append")
            for r in rd:
                rows.append(r)
                existing.add((r[0], r[1], r[7]))
    added = 0
    for p in sorted(paths):
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        key = (d["work"]["title"], d["work"]["year"], d["perspective"])
        if key in existing:
            print(f"skip (already there): {key}")
            continue
        rows.append(row_of(d))
        existing.add(key)
        added += 1
    rows.sort(key=lambda r: (r[7], r[0]))
    with open(out, "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(HEAD)
        wr.writerows(rows)
    print(f"{out}: {len(rows)} rows ({added} added)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main(sys.argv[1], sys.argv[2:])
