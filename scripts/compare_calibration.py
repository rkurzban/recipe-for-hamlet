#!/usr/bin/env python3
"""Compare Claude's calibration ratings with the author-verified Table 2 scores.

Usage (from the skill folder):
    python3 scripts/compare_calibration.py
Options:
    --titles references/table2-titles.csv   (default)
    --claude calibration                    (folder with <slug>.json files)
    --site   calibration/site/table2.json   (default)
    --out    calibration                    (where to write the outputs)

Outputs:
    calibration/comparison.csv        one row per work x ingredient
    calibration/comparison-report.md  the summary below, as Markdown
    (and the same summary on the console)

Only the Python standard library is used, so it runs anywhere.
"""
import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path

# Mechanism names as the site writes them -> SKILL.md slugs, in Table 2 order.
NAME_TO_SLUG = {
    "Hunger": "hunger",
    "Thirst": "thirst",
    "Feeling cold / hot": "feeling-cold-hot",
    "Sleepiness": "sleepiness",
    "Curiosity": "curiosity",
    "Explanation-seeking": "explanation-seeking",
    "Skill acquisition": "skill-acquisition",
    "Play": "play",
    "Resource accumulation": "resource-accumulation",
    "Resource foraging": "resource-foraging",
    "Mental time travel": "mental-time-travel",
    "Fear of predators": "fear-of-predators",
    "Fear of aggressors": "fear-of-aggressors",
    "Fear of heights": "fear-of-heights",
    "Disgust": "disgust",
    "Pain aversion": "pain-aversion",
    "Pride": "pride",
    "Shame": "shame",
    "Moral pride": "moral-pride",
    "Guilt": "guilt",
    "Warmth": "warmth",
    "Moral blame": "moral-blame",
    "Moral praise": "moral-praise",
    "Revenge": "revenge",
    "Forgiveness": "forgiveness",
    "Compassion": "compassion",
    "Affiliation": "affiliation",
    "Friendship": "friendship",
    "Sadness": "sadness",
    "Humor": "humor",
    "Embarrassment": "embarrassment",
    "Reasoning": "reasoning",
    "Coalitional affiliation": "coalitional-affiliation",
    "Status-seeking": "status-seeking",
    "Envy": "envy",
    "Anger": "anger",
    "Hatred": "hatred",
    "Romantic affiliation": "romantic-affiliation",
    "Sexual attraction": "sexual-attraction",
    "Long-term love": "long-term-love",
    "Desire": "desire",
    "Romantic jealousy": "romantic-jealousy",
    "Sexual jealousy": "sexual-jealousy",
    "Sexual disgust": "sexual-disgust",
    "Kin sexual disgust": "kin-sexual-disgust",
    "Parental care": "parental-care",
    "Parental investment": "parental-investment",
    "Familial love": "familial-love",
}
SLUGS = list(NAME_TO_SLUG.values())
SLUG_TO_NAME = {v: k for k, v in NAME_TO_SLUG.items()}

FAMILY = {}
for s in SLUGS[:11]:
    FAMILY[s] = "Self"
for s in SLUGS[11:16]:
    FAMILY[s] = "Threats"
for s in SLUGS[16:33]:
    FAMILY[s] = "Cooperation"
for s in SLUGS[33:37]:
    FAMILY[s] = "Competition"
for s in SLUGS[37:44]:
    FAMILY[s] = "Mating"
for s in SLUGS[44:]:
    FAMILY[s] = "Kin"


# ---------- small statistics helpers (no numpy) ----------

def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan")
    mx, my = mean(xs), mean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    if sxx == 0 or syy == 0:
        return float("nan")
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / math.sqrt(sxx * syy)


def ranks(xs):
    """Average ranks, for ties."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def spearman(xs, ys):
    return pearson(ranks(xs), ranks(ys))


def quadratic_weighted_kappa(a, b, k=5):
    """Cohen's kappa with quadratic weights for ordinal 0..k-1 scores."""
    n = len(a)
    if n == 0:
        return float("nan")
    obs = [[0] * k for _ in range(k)]
    for x, y in zip(a, b):
        obs[x][y] += 1
    ha = [sum(obs[i][j] for j in range(k)) for i in range(k)]
    hb = [sum(obs[i][j] for i in range(k)) for j in range(k)]
    num = den = 0.0
    for i in range(k):
        for j in range(k):
            w = (i - j) ** 2 / (k - 1) ** 2
            num += w * obs[i][j]
            den += w * ha[i] * hb[j] / n
    return 1 - num / den if den else float("nan")


def fmt(x, nd=2):
    return "nan" if (isinstance(x, float) and math.isnan(x)) else f"{x:.{nd}f}"


# ---------- loading ----------

def load_titles(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_site(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    works = data["works"]
    scores = data["scores"]
    by_work = {w: {} for w in works}
    for name, values in scores.items():
        slug = NAME_TO_SLUG[name]
        for w, v in zip(works, values):
            by_work[w][slug] = int(v)
    return by_work


def load_claude(folder, slug):
    path = Path(folder) / f"{slug}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--titles", default="references/table2-titles.csv")
    ap.add_argument("--claude", default="calibration")
    ap.add_argument("--site", default="calibration/site/table2.json")
    ap.add_argument("--out", default="calibration")
    args = ap.parse_args()

    titles = load_titles(args.titles)
    site = load_site(args.site)

    rows = []          # long format
    missing = []
    per_work = {}
    for t in titles:
        site_id, slug, title = t["site_id"], t["slug"], t["title"]
        cl = load_claude(args.claude, slug)
        if cl is None:
            missing.append(f"{title} (expected {args.claude}/{slug}.json)")
            continue
        if site_id not in site:
            missing.append(f"{title} (site id '{site_id}' not in {args.site})")
            continue
        c_scores, s_scores = [], []
        for ing in SLUGS:
            c = int(cl[ing]["score"])
            s = site[site_id][ing]
            rows.append({
                "work": title, "family": FAMILY[ing], "ingredient": ing,
                "claude": c, "site": s, "diff": c - s, "abs_diff": abs(c - s),
                "claude_why": cl[ing]["why"],
            })
            c_scores.append(c)
            s_scores.append(s)
        per_work[title] = (c_scores, s_scores)

    if not rows:
        print("Nothing to compare.", "\n".join(missing))
        return 1

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "comparison.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    lines = []
    P = lines.append
    all_c = [r["claude"] for r in rows]
    all_s = [r["site"] for r in rows]
    diffs = [r["diff"] for r in rows]
    n = len(rows)

    P("# Calibration: Claude vs. author-verified Table 2 scores")
    P("")
    P(f"{len(per_work)} works x 48 ingredients = {n} score pairs. "
      "Differences are Claude minus site (positive = Claude higher).")
    if missing:
        P("")
        P("Skipped: " + "; ".join(missing))
    P("")
    P("## Overall")
    P("")
    P(f"- Mean score, Claude: {fmt(mean(all_c))}; site: {fmt(mean(all_s))}; "
      f"mean difference (bias): {fmt(mean(diffs), 2)}")
    P(f"- Mean absolute difference: {fmt(mean([abs(d) for d in diffs]))} points")
    P(f"- Exact agreement: {fmt(100 * sum(d == 0 for d in diffs) / n, 1)}%; "
      f"within 1 point: {fmt(100 * sum(abs(d) <= 1 for d in diffs) / n, 1)}%; "
      f"off by 3 or more: {sum(abs(d) >= 3 for d in diffs)} pairs")
    P(f"- Pearson r: {fmt(pearson(all_c, all_s))}; Spearman rho: {fmt(spearman(all_c, all_s))}; "
      f"quadratic weighted kappa: {fmt(quadratic_weighted_kappa(all_c, all_s))}")
    cc, cs = Counter(all_c), Counter(all_s)
    P("")
    P("Score distribution (count of each score across all pairs):")
    P("")
    P("| Score | Claude | Site |")
    P("|---|---|---|")
    for k in range(5):
        P(f"| {k} | {cc.get(k, 0)} | {cs.get(k, 0)} |")
    P("")
    P("Confusion matrix (rows = site score, columns = Claude score):")
    P("")
    P("| site \\ Claude | 0 | 1 | 2 | 3 | 4 |")
    P("|---|---|---|---|---|---|")
    conf = [[0] * 5 for _ in range(5)]
    for c, s in zip(all_c, all_s):
        conf[s][c] += 1
    for s in range(5):
        P(f"| {s} | " + " | ".join(str(conf[s][c]) for c in range(5)) + " |")

    # Per-site-score bias: when the authors say 4, what does Claude say on average?
    P("")
    P("Claude's mean score for each site score (how far Claude sits below or above the authors at each level):")
    P("")
    P("| Site score | n | Claude mean |")
    P("|---|---|---|")
    for s in range(5):
        cs_ = [c for c, ss in zip(all_c, all_s) if ss == s]
        P(f"| {s} | {len(cs_)} | {fmt(mean(cs_))} |")

    # Per work
    P("")
    P("## Per work")
    P("")
    P("| Work | Claude mean | Site mean | Bias | Mean abs diff | Spearman | Exact % | Within 1 % |")
    P("|---|---|---|---|---|---|---|---|")
    for title, (c, s) in per_work.items():
        d = [x - y for x, y in zip(c, s)]
        P(f"| {title} | {fmt(mean(c))} | {fmt(mean(s))} | {fmt(mean(d))} | "
          f"{fmt(mean([abs(x) for x in d]))} | {fmt(spearman(c, s))} | "
          f"{fmt(100 * sum(x == 0 for x in d) / len(d), 0)} | "
          f"{fmt(100 * sum(abs(x) <= 1 for x in d) / len(d), 0)} |")

    # Per ingredient
    P("")
    P("## Per ingredient (across the works)")
    P("")
    P("Sorted by bias, most under-rated by Claude first. Spearman is across works; "
      "it is nan when one side gives every work the same score.")
    P("")
    P("| Ingredient | Family | Claude mean | Site mean | Bias | Mean abs diff | Spearman |")
    P("|---|---|---|---|---|---|---|")
    per_ing = []
    for ing in SLUGS:
        rr = [r for r in rows if r["ingredient"] == ing]
        c = [r["claude"] for r in rr]
        s = [r["site"] for r in rr]
        d = [r["diff"] for r in rr]
        per_ing.append((ing, mean(c), mean(s), mean(d), mean([abs(x) for x in d]), spearman(c, s)))
    for ing, mc, ms, bias, mad, rho in sorted(per_ing, key=lambda x: x[3]):
        P(f"| {SLUG_TO_NAME[ing]} | {FAMILY[ing]} | {fmt(mc)} | {fmt(ms)} | {fmt(bias)} | {fmt(mad)} | {fmt(rho)} |")

    # Per family
    P("")
    P("## Per family")
    P("")
    P("| Family | n | Claude mean | Site mean | Bias | Mean abs diff | Pearson r |")
    P("|---|---|---|---|---|---|---|")
    for fam in ["Self", "Threats", "Cooperation", "Competition", "Mating", "Kin"]:
        rr = [r for r in rows if r["family"] == fam]
        c = [r["claude"] for r in rr]
        s = [r["site"] for r in rr]
        d = [r["diff"] for r in rr]
        P(f"| {fam} | {len(rr)} | {fmt(mean(c))} | {fmt(mean(s))} | {fmt(mean(d))} | "
          f"{fmt(mean([abs(x) for x in d]))} | {fmt(pearson(c, s))} |")

    # Largest disagreements
    P("")
    P("## Largest disagreements (3 or more points apart)")
    P("")
    big = sorted([r for r in rows if r["abs_diff"] >= 3], key=lambda r: (-r["abs_diff"], r["work"], r["ingredient"]))
    if not big:
        P("None.")
    else:
        P("| Work | Ingredient | Claude | Site | Claude's reason |")
        P("|---|---|---|---|---|")
        for r in big:
            P(f"| {r['work']} | {SLUG_TO_NAME[r['ingredient']]} | {r['claude']} | {r['site']} | {r['claude_why']} |")

    # What-if: is the gap mostly scale use rather than content disagreement?
    P("")
    P("## What if Claude's scale were stretched?")
    P("")
    P("Two mechanical re-mappings of Claude's scores, to separate scale use from content disagreement. "
      "They are diagnostics, not a fix: the fix is to change the instructions and re-rate.")
    P("")
    P("| Mapping | Mean abs diff | Exact % | Within 1 % | Bias |")
    P("|---|---|---|---|---|")

    def eval_map(name, f):
        mapped = [f(c) for c in all_c]
        d = [m - s for m, s in zip(mapped, all_s)]
        P(f"| {name} | {fmt(mean([abs(x) for x in d]))} | {fmt(100 * sum(x == 0 for x in d) / n, 1)} | "
          f"{fmt(100 * sum(abs(x) <= 1 for x in d) / n, 1)} | {fmt(mean(d))} |")

    eval_map("As rated", lambda c: c)
    eval_map("Nonzero scores raised by 1 (1->2, 2->3, 3->4, 4->4)", lambda c: min(4, c + 1) if c > 0 else 0)
    eval_map("Scores of 2 or more raised by 1 (2->3, 3->4)", lambda c: min(4, c + 1) if c >= 2 else c)
    # Best monotone mapping fitted on these data (rounded mean site score at each Claude level).
    best = {}
    for c in range(5):
        ss = [s for cc_, s in zip(all_c, all_s) if cc_ == c]
        best[c] = round(mean(ss)) if ss else c
    eval_map("Each Claude level -> rounded mean site score at that level: " +
             ", ".join(f"{c}->{best[c]}" for c in range(5)), lambda c: best[c])

    # Profile agreement: do the top ingredients match?
    P("")
    P("## Does Claude pick out the same top ingredients?")
    P("")
    P("For each work: the site's ingredients scored 4, and how Claude scored them; "
      "then Claude's ingredients scored 4 that the site put at 2 or lower.")
    P("")
    for title, (c, s) in per_work.items():
        site4 = [(SLUG_TO_NAME[SLUGS[i]], c[i]) for i in range(48) if s[i] == 4]
        claude4_low = [(SLUG_TO_NAME[SLUGS[i]], s[i]) for i in range(48) if c[i] == 4 and s[i] <= 2]
        part1 = ", ".join(f"{name} (Claude {cv})" for name, cv in site4) or "none"
        part2 = ", ".join(f"{name} (site {sv})" for name, sv in claude4_low) or "none"
        P(f"- **{title}** - site 4s: {part1}. Claude 4s the site rates 2 or lower: {part2}.")

    report = "\n".join(lines) + "\n"
    (out / "comparison-report.md").write_text(report, encoding="utf-8")
    print(report)
    print(f"Wrote {out / 'comparison.csv'} and {out / 'comparison-report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
