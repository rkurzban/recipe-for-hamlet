#!/usr/bin/env python3
"""Crosswalk between the 48 motivational ingredients and the 74 Feels.

Reads, for each of the 14 Table 2 works:
  calibration/<slug>.json                      the rater's ingredient scores
  calibration/site/table2.json                 the authors' verified ingredient scores
  feels/character/<slug>.character.feels.json  the rater's Feel scores (character pass)
  feels/audience/<slug>.audience.feels.json    the rater's Feel scores (audience pass)
and crosswalk/crosswalk.csv, which maps each ingredient to its nearest Feel or Feels.

Writes crosswalk/cells.csv (every Feel cell with its nearest ingredients and the
rule results), crosswalk/pairs.csv (every ingredient-Feel pair), and
crosswalk/report.md (the counts quoted in the post).

Rules
  pair:       each mapped ingredient and its nearest Feel (the first Feel listed in
              crosswalk.csv), in each work: 44 ingredients x 14 works = 616 pairs.
  agree:      a pair where the rater gave the same score to both.
  addition:   a Feel cell scores 3 or 4, and every ingredient mapped to it scores
              0 or 1 in both columns (authors' and rater's). The Feel adds something
              the ingredient list lacks.
  mirror:     an ingredient cell scores 3 or 4 in both columns, and every Feel mapped
              to it scores 0 or 1. The ingredient has something the Feels lack.
  table row:  a Feel with no counterpart ingredient (it appears in no row of
              crosswalk.csv) scores 3 or 4 in at least five works. The addition
              rule is reported beside it; a Feel can be on the table with few
              addition passes (Lonely) when Affiliation, a different unit, is high.
  carving:    a pair that differs by 2 or more points where the mapping is not
              one-to-one (one ingredient to several Feels, or several ingredients to
              one Feel). The difference is where the two lists cut, not a disagreement
              about the work.
  judgment:   a pair that differs by 2 or more points where the mapping is one-to-one.

Run from the repository root:  python3 crosswalk/crosswalk.py
"""
import csv, json, os, sys
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAL = os.path.join(ROOT, "calibration")
FEELS = os.path.join(ROOT, "feels")
OUT = os.path.join(ROOT, "crosswalk")

def slug_of(title):
    rows = list(csv.DictReader(open(os.path.join(ROOT, "references", "table2-titles.csv"), encoding="utf-8")))
    for r in rows:
        if r["title"] == title or r["site_id"] == title:
            return r["slug"]
    raise KeyError(title)

def ingredient_key(name):
    return name.lower().replace(" / ", "-").replace("/", "-").replace(" ", "-")

def main():
    site = json.load(open(os.path.join(CAL, "site", "table2.json"), encoding="utf-8"))
    works = site["works"]
    slugs = [slug_of(w) for w in works]
    ingredients = [ingredient_key(k) for k in site["scores"]]
    authors = {ingredient_key(k): v for k, v in site["scores"].items()}

    rater = {}
    for s in slugs:
        d = json.load(open(os.path.join(CAL, s + ".json"), encoding="utf-8"))
        rater[s] = {k: d[k]["score"] for k in ingredients}

    feels = {}
    feel_names = None
    extra_names = None
    for s in slugs:
        d = json.load(open(os.path.join(FEELS, "character", s + ".character.feels.json"), encoding="utf-8"))
        a = json.load(open(os.path.join(FEELS, "audience", s + ".audience.feels.json"), encoding="utf-8"))
        if feel_names is None:
            feel_names = list(d["feels"].keys())
            extra_names = list(d["extra"].keys())
        feels[s] = {}
        for k in feel_names:
            feels[s][k] = (d["feels"][k]["score"], d["feels"][k]["why"], a["feels"][k]["score"])
        for k in extra_names:
            feels[s][k] = (d["extra"][k]["score"], d["extra"][k]["why"], a["extra"][k]["score"])

    mapping = {}
    carving_ing = set()
    for r in csv.DictReader(open(os.path.join(OUT, "crosswalk.csv"), encoding="utf-8")):
        fl = [f for f in r["feels"].split(";") if f]
        mapping[r["ingredient"]] = fl
    feel_to_ing = defaultdict(list)
    for ing, fl in mapping.items():
        for f in fl:
            feel_to_ing[f].append(ing)
    # The first Feel listed is the ingredient's nearest Feel; the rest are also covered by it.
    nearest = {ing: fl[0] for ing, fl in mapping.items() if fl}
    nearest_count = Counter(nearest.values())
    one_to_one = {ing for ing, f in nearest.items() if len(mapping[ing]) == 1 and nearest_count[f] == 1}
    # Blockers for the addition rule: the counterpart ingredients, plus any listed in blockers.csv
    blockers = {f: list(v) for f, v in feel_to_ing.items()}
    bpath = os.path.join(OUT, "blockers.csv")
    if os.path.exists(bpath):
        for r in csv.DictReader(open(bpath, encoding="utf-8")):
            blockers.setdefault(r["feel"], [])
            blockers[r["feel"]] += [i for i in r["ingredients"].split(";") if i and i not in blockers[r["feel"]]]

    pairs = []
    for wi, s in enumerate(slugs):
        for ing, f in nearest.items():
            if True:
                ri = rater[s][ing]; ai = authors[ing][wi]; fs = feels[s][f][0]
                d = fs - ri
                kind = "one-to-one" if ing in one_to_one else "carving"
                pairs.append(dict(work=works[wi], ingredient=ing, feel=f, rater_ingredient=ri,
                                  authors_ingredient=ai, feel_character=fs, diff=d, mapping=kind))

    cells = []
    for wi, s in enumerate(slugs):
        for f in feel_names + extra_names:
            fs, why, aud = feels[s][f]
            ings = blockers.get(f, [])
            blocked = [i for i in ings if rater[s][i] > 1 or authors[i][wi] > 1]
            adds = fs >= 3 and not blocked
            cells.append(dict(work=works[wi], feel=f, character=fs, audience=aud,
                              counterpart="yes" if f in feel_to_ing else "",
                              nearest_ingredients=";".join(ings),
                              ingredient_scores=";".join(f"{i}={rater[s][i]}/{authors[i][wi]}" for i in ings),
                              adds="yes" if adds else "", reason=why))

    mirrors = []
    for wi, s in enumerate(slugs):
        for ing in ingredients:
            ri = rater[s][ing]; ai = authors[ing][wi]
            if ri >= 3 and ai >= 3:
                fl = mapping.get(ing, [])
                if all(feels[s][f][0] <= 1 for f in fl):
                    mirrors.append((ing, works[wi], ri, ai))

    agree = sum(1 for p in pairs if p["diff"] == 0)
    big = [p for p in pairs if abs(p["diff"]) >= 2]
    carving = [p for p in big if p["mapping"] == "carving"]
    judgment = [p for p in big if p["mapping"] == "one-to-one"]
    n_one = sum(1 for p in pairs if p["mapping"] == "one-to-one")
    adds = [c for c in cells if c["adds"]]
    per_feel = Counter(c["feel"] for c in adds)
    high = Counter(c["feel"] for c in cells if c["character"] >= 3 and not c["counterpart"])
    table_rows = [(f, n, per_feel[f]) for f, n in high.most_common() if n >= 5]
    unmapped = [i for i, fl in mapping.items() if not fl]

    with open(os.path.join(OUT, "pairs.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(pairs[0].keys())); w.writeheader(); w.writerows(pairs)
    with open(os.path.join(OUT, "cells.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(cells[0].keys())); w.writeheader(); w.writerows(cells)

    L = []
    L.append("# Crosswalk report\n")
    L.append(f"Works: {len(works)}. Ingredients: {len(ingredients)} ({len(unmapped)} mapped to no Feel: {', '.join(unmapped)}). "
             f"Feels: {len(feel_names)} plus {len(extra_names)} extra rows. Feel cells: {len(cells)}.\n")
    L.append("## Ingredient-Feel pairs\n")
    L.append(f"- Pairs: {len(pairs)} ({n_one} one-to-one, {len(pairs)-n_one} where one list splits what the other lumps).")
    L.append(f"- Same score under both names: {agree}.")
    L.append(f"- Differ by 2 or more: {len(big)}, of which {len(carving)} are the carving difference and {len(judgment)} are differences of judgment.")
    if judgment:
        L.append("\nDifferences of judgment:\n")
        L.append("| Work | Ingredient | Feel | Ingredient (rater) | Feel |\n|---|---|---|---|---|")
        for p in judgment:
            L.append(f"| {p['work']} | {p['ingredient']} | {p['feel']} | {p['rater_ingredient']} | {p['feel_character']} |")
    L.append("\n## Addition rule (Feel 3 or 4, every nearest ingredient 0 or 1 in both columns)\n")
    L.append(f"- Feel cells that pass: {len(adds)}.")
    L.append("\n## Table rows (Feels with no counterpart ingredient, scoring 3 or 4 in at least five works)\n")
    L.append(f"- Rows: {len(table_rows)}.\n")
    L.append("| Feel | Works at 3 or 4 | Works where it passes the addition rule |\n|---|---|---|")
    for f, n, a in table_rows:
        L.append(f"| {f} | {n} | {a} |")
    L.append("\n## Mirror-image rule (ingredient 3 or 4 in both columns, every nearest Feel 0 or 1)\n")
    L.append(f"- Ingredient cells that pass: {len(mirrors)}.\n")
    L.append("| Ingredient | Work | Rater | Authors |\n|---|---|---|---|")
    for ing, w, ri, ai in mirrors:
        L.append(f"| {ing} | {w} | {ri} | {ai} |")
    open(os.path.join(OUT, "report.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))

if __name__ == "__main__":
    main()
