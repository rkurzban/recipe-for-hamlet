#!/usr/bin/env python3
"""Write the batch report for a set of feels-annotate JSON files.

Usage: python3 batch_report.py <out.md> <character_dir> <audience_dir>

For each perspective: how many works, score distribution, and the spread
table (lowest and highest score across the batch, and the number of works
scored 3 or 4, for each of the 74 feels and the 8 extra rows), with the rows
that sit at one score for every work. Then, work by work, the feels whose
character and audience scores differ by two or more, and the feels whose
mean score differs most between the two perspectives.
"""
import glob
import json
import os
import sys
from collections import Counter

from validate_feels import EXTRA, FEELS

NAMES = {
    "need-to-breathe": "1 The Need to Breathe", "hungry": "2 Hungry", "full": "3 Full",
    "thirsty": "4 Thirsty", "gassy": "5 Gassy", "need-to-poop": "6 The Need to Poop",
    "need-to-pee": "7 The Need to Pee", "sleepy": "8 Sleepy", "nauseous": "9 Nauseous",
    "urge-to-sneeze": "10 The Urge to Sneeze", "urge-to-cough": "11 The Urge to Cough",
    "dizzy": "12 Dizzy", "fatigued": "13 Fatigued", "pain": "14 Pain",
    "disgusted": "15 Disgusted", "itchy": "16 Itchy", "tickled": "17 Tickled",
    "over-stimulated": "18 Over-Stimulated", "too-hot-too-cold": "19 Too Hot and Too Cold",
    "afraid": "20 Afraid", "anxious": "21 Anxious", "panic": "22 Panic",
    "sensory-pleasures": "23 Sensory Pleasures", "aesthetic-pleasures": "24 Aesthetic Pleasures",
    "piquancy": "25 Piquancy", "fun-excitement": "26 Fun and Excitement", "orgasm": "27 Orgasm",
    "love-romantic": "28 Love (Romantic)", "love-family": "29 Love (Family)", "grief": "30 Grief",
    "missing-someone": "31 Missing Someone", "aroused-sexually": "32 Aroused (Sexually)",
    "liking-as-a-friend": "33 Liking as a Friend", "empathy": "34 Empathy",
    "compassion": "35 Compassion", "grateful": "36 Grateful",
    "pleasure-from-helping": "37 Pleasure From Helping",
    "trustful-distrustful": "38 Trustful and Distrustful", "depressed": "39 Depressed",
    "angry": "40 Angry", "envious": "41 Envious",
    "jealous-romantic-sexual": "42 Jealous (Romantic/Sexual)",
    "jealous-friendship": "43 Jealous (Friendship)", "hatred": "44 Hatred",
    "contempt": "45 Contempt", "resentment": "46 Resentment", "proud": "47 Proud",
    "amused": "48 Amused", "sense-of-belonging": "49 A Sense of Belonging",
    "lonely": "50 Lonely", "judgy-moral-sense": "51 Judgy (The Moral Sense)",
    "admiration": "52 Admiration", "embarrassed": "53 Embarrassed", "shame": "54 Shame",
    "guilt": "55 Guilt", "sad": "56 Sad", "happy": "57 Happy",
    "joyful-euphoric": "58 Joyful and Euphoric", "effort": "59 Effort",
    "focused-in-flow": "60 Focused/In Flow", "bored": "61 Bored", "distracted": "62 Distracted",
    "impatient": "63 Impatient", "curious": "64 Curious", "surprised": "65 Surprised",
    "awe": "66 Awe", "skeptical-doubtful": "67 Skeptical/Doubtful",
    "feeling-of-knowing": "68 The Feeling of Knowing", "confused": "69 Confused",
    "frustrated": "70 Frustrated", "uncertain-certain": "71 Uncertain / Certain",
    "understanding": "72 Understanding", "inspired": "73 Inspired", "satisfied": "74 Satisfied",
    "foreboding": "Foreboding", "nostalgia": "Nostalgia",
    "anticipation-suspense": "Anticipation / Suspense", "hope": "Hope",
    "schadenfreude": "Schadenfreude", "elevation": "Elevation",
    "infatuation": "Infatuation", "rage": "Rage",
}
KINGDOMS = [
    ("Kingdom I: Body Maintenance", FEELS[0:14]),
    ("Kingdom II: External Dangers and Opportunities", FEELS[14:27]),
    ("Kingdom III: Social World", FEELS[27:58]),
    ("Kingdom IV: Mind", FEELS[58:74]),
    ("Monera (extra rows)", EXTRA),
]


def load(d):
    out = {}
    for p in sorted(glob.glob(os.path.join(d, "*.json"))):
        with open(p, encoding="utf-8") as f:
            j = json.load(f)
        scores = {k: j["feels"][k]["score"] for k in FEELS}
        scores.update({k: j["extra"][k]["score"] for k in EXTRA})
        out[j["work"]["title"]] = (j, scores)
    return out


def spread(works):
    lines = []
    constant = []
    for king, keys in KINGDOMS:
        lines.append(f"\n**{king}**\n")
        lines.append("| Feel | Low | High | Works at 3 or 4 | Mean |")
        lines.append("|---|---|---|---|---|")
        for k in keys:
            vals = [s[k] for _, s in works.values()]
            lo, hi = min(vals), max(vals)
            n34 = sum(1 for v in vals if v >= 3)
            mean = sum(vals) / len(vals)
            lines.append(f"| {NAMES[k]} | {lo} | {hi} | {n34} | {mean:.2f} |")
            if lo == hi:
                constant.append(f"{NAMES[k]} ({lo})")
    return lines, constant


def distribution(works):
    c = Counter()
    for _, s in works.values():
        for k in FEELS:
            c[s[k]] += 1
    n = sum(c.values())
    parts = [f"{v}: {100 * c[v] / n:.0f}%" for v in range(5)]
    mean = sum(v * c[v] for v in c) / n
    return f"Over the 74 feels of {len(works)} works ({n} cells): " + ", ".join(parts) + f"; mean {mean:.2f}."


def main(out, cdir, adir):
    C = load(cdir)
    A = load(adir)
    titles = [t for t in C if t in A]
    L = []
    L.append("# Feels annotations of the 14 Table 2 works: batch report\n")
    L.append("Rater: claude-fable-5-1, one session, 4 October 2026, following the `feels-annotate` skill "
             "(74 feels plus 8 extra Monera rows, scores 0-4, one-sentence reasons). "
             "Character pass first, in full, then the audience pass, in full. "
             f"Works annotated: {len(C)} character, {len(A)} audience. Unknown: none. Ambiguous: none "
             "(the 14 were treated as unambiguous, as the calibration table asks).\n")
    L.append("Files: `character/<slug>.character.feels.json`, `audience/<slug>.audience.feels.json`, "
             "and `feels-annotations.csv` (one row per work and perspective). "
             "Slugs match `calibration/<slug>.json` of the ingredients run, so the two can be joined by file name.\n")
    L.append("Limits: the ratings rest on the rater's unverified knowledge of the works, a demonstration, not data. "
             "Scores vary from run to run; for a comparison meant for publication, rate each work more than once "
             "and report the median. The audience pass rates the designed effect on an ordinary first-time audience, "
             "not any one person's reaction.\n")

    for label, works in (("Character perspective", C), ("Audience perspective", A)):
        L.append(f"\n## {label}\n")
        L.append(distribution(works) + "\n")
        L.append("Fours and threes per work:\n")
        L.append("| Work | 4s | 3s | Mean of 74 |")
        L.append("|---|---|---|---|")
        for t in sorted(works):
            s = works[t][1]
            vals = [s[k] for k in FEELS]
            L.append(f"| {t} | {vals.count(4)} | {vals.count(3)} | {sum(vals) / 74:.2f} |")
        L.append("\n### Spread table\n")
        L.append("Lowest and highest score across the batch, the number of works scored 3 or 4, and the mean, for each row.")
        lines, constant = spread(works)
        L.extend(lines)
        L.append("\nRows at the same score for every work (they say nothing about how the works differ): "
                 + (", ".join(constant) if constant else "none") + ".\n")

    L.append("\n## Character versus audience\n")
    L.append("Feels whose two scores differ by two or more, work by work (character -> audience).\n")
    for t in sorted(titles):
        cs, as_ = C[t][1], A[t][1]
        diffs = [(k, cs[k], as_[k]) for k in FEELS + EXTRA if abs(cs[k] - as_[k]) >= 2]
        if not diffs:
            L.append(f"- **{t}**: none.")
            continue
        parts = [f"{NAMES[k]} {c}->{a}" for k, c, a in diffs]
        L.append(f"- **{t}**: " + "; ".join(parts) + ".")

    L.append("\n### Largest mean differences between the perspectives\n")
    rows = []
    for k in FEELS + EXTRA:
        cm = sum(C[t][1][k] for t in titles) / len(titles)
        am = sum(A[t][1][k] for t in titles) / len(titles)
        rows.append((k, cm, am, am - cm))
    L.append("Higher in the audience pass:\n")
    L.append("| Feel | Character mean | Audience mean | Difference |")
    L.append("|---|---|---|---|")
    for k, cm, am, d in sorted(rows, key=lambda r: -r[3])[:10]:
        L.append(f"| {NAMES[k]} | {cm:.2f} | {am:.2f} | +{d:.2f} |")
    L.append("\nHigher in the character pass:\n")
    L.append("| Feel | Character mean | Audience mean | Difference |")
    L.append("|---|---|---|---|")
    for k, cm, am, d in sorted(rows, key=lambda r: r[3])[:10]:
        L.append(f"| {NAMES[k]} | {cm:.2f} | {am:.2f} | {d:.2f} |")

    # agreement between the two perspectives, over the 82 rows x works
    n = exact = within1 = 0
    for t in titles:
        for k in FEELS + EXTRA:
            n += 1
            d = abs(C[t][1][k] - A[t][1][k])
            exact += d == 0
            within1 += d <= 1
    L.append(f"\nAcross all {n} cells (82 rows x {len(titles)} works), the two perspectives agree exactly on "
             f"{100 * exact / n:.0f}% and within one point on {100 * within1 / n:.0f}%.\n")

    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    main(*sys.argv[1:])
