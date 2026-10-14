#!/usr/bin/env python3
"""Validate a feels-annotate JSON file against the skill's template.

Usage: python3 validate_feels.py <file.json> [<file.json> ...]
Exit code 0 when every file passes, 1 otherwise.
"""
import json
import re
import sys

FEELS = [
    "need-to-breathe", "hungry", "full", "thirsty", "gassy", "need-to-poop",
    "need-to-pee", "sleepy", "nauseous", "urge-to-sneeze", "urge-to-cough",
    "dizzy", "fatigued", "pain", "disgusted", "itchy", "tickled",
    "over-stimulated", "too-hot-too-cold", "afraid", "anxious", "panic",
    "sensory-pleasures", "aesthetic-pleasures", "piquancy", "fun-excitement",
    "orgasm", "love-romantic", "love-family", "grief", "missing-someone",
    "aroused-sexually", "liking-as-a-friend", "empathy", "compassion",
    "grateful", "pleasure-from-helping", "trustful-distrustful", "depressed",
    "angry", "envious", "jealous-romantic-sexual", "jealous-friendship",
    "hatred", "contempt", "resentment", "proud", "amused",
    "sense-of-belonging", "lonely", "judgy-moral-sense", "admiration",
    "embarrassed", "shame", "guilt", "sad", "happy", "joyful-euphoric",
    "effort", "focused-in-flow", "bored", "distracted", "impatient",
    "curious", "surprised", "awe", "skeptical-doubtful", "feeling-of-knowing",
    "confused", "frustrated", "uncertain-certain", "understanding",
    "inspired", "satisfied",
]
EXTRA = [
    "foreboding", "nostalgia", "anticipation-suspense", "hope",
    "schadenfreude", "elevation", "infatuation", "rage",
]
TOP = ["known", "ambiguous", "candidates", "work", "mode", "perspective",
       "summary", "monera", "feels", "extra", "model", "date"]
MEDIA = {"movie", "tv", "novel", "game", "manga", "comic", "theatre", "epic",
         "tale", "book", "other"}
assert len(FEELS) == 74 and len(EXTRA) == 8


def words(s):
    return len(s.split())


def check(path):
    errs = []
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
    except Exception as e:  # noqa: BLE001
        return [f"not valid JSON: {e}"]

    keys = list(d.keys())
    if keys != TOP:
        errs.append(f"top-level keys are {keys}, expected {TOP}")
    if d.get("known") is not True:
        errs.append("known must be true")
    if d.get("ambiguous") is not False:
        errs.append("ambiguous must be false")
    if d.get("candidates") != []:
        errs.append("candidates must be an empty list")
    w = d.get("work", {})
    if list(w.keys()) != ["title", "year", "medium", "creator"]:
        errs.append(f"work keys are {list(w.keys())}")
    if not w.get("title"):
        errs.append("work.title is empty")
    if not re.fullmatch(r"(\d{4})?", str(w.get("year", "x"))):
        errs.append(f"work.year must be 4 digits or empty, got {w.get('year')!r}")
    if w.get("medium") not in MEDIA:
        errs.append(f"work.medium {w.get('medium')!r} not in {sorted(MEDIA)}")
    if d.get("mode") != "feels":
        errs.append(f"mode must be 'feels', got {d.get('mode')!r}")
    persp = d.get("perspective")
    if persp not in ("character", "audience"):
        errs.append(f"perspective must be character or audience, got {persp!r}")
    if persp and f".{persp}." not in path:
        errs.append(f"file name does not match perspective {persp!r}")
    s = d.get("summary", "")
    if not isinstance(s, str) or not s.strip():
        errs.append("summary is empty")
    elif words(s) > 30:
        errs.append(f"summary has {words(s)} words (max 30)")
    m = d.get("monera")
    if not isinstance(m, list) or any(not isinstance(x, str) or not x.strip() for x in m):
        errs.append("monera must be a list of non-empty strings")
    elif len(m) > 5:
        errs.append(f"monera has {len(m)} entries (max 5)")
    elif any(x.strip().lower().replace(" ", "-") in FEELS + EXTRA for x in m):
        errs.append("monera must not repeat a feel from the 74 or the 8 extra rows")

    for section, expected in (("feels", FEELS), ("extra", EXTRA)):
        block = d.get(section)
        if not isinstance(block, dict):
            errs.append(f"{section} is missing or not an object")
            continue
        got = list(block.keys())
        if got != expected:
            missing = [k for k in expected if k not in got]
            extra = [k for k in got if k not in expected]
            if missing or extra:
                errs.append(f"{section}: missing {missing}, unexpected {extra}")
            else:
                errs.append(f"{section}: keys are present but out of order")
        for k in expected:
            v = block.get(k)
            if not isinstance(v, dict) or list(v.keys()) != ["why", "score"]:
                errs.append(f"{section}.{k}: must be {{'why':..., 'score':...}}")
                continue
            why, score = v["why"], v["score"]
            if not isinstance(why, str) or not why.strip():
                errs.append(f"{section}.{k}: why is empty")
            else:
                n = words(why)
                if n > 35:
                    errs.append(f"{section}.{k}: why has {n} words (max 35)")
                if "\n" in why:
                    errs.append(f"{section}.{k}: why contains a line break")
            if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 4:
                errs.append(f"{section}.{k}: score {score!r} is not an integer 0-4")
    if not isinstance(d.get("model"), str) or not d.get("model"):
        errs.append("model is missing")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(d.get("date", ""))):
        errs.append("date must be YYYY-MM-DD")
    return errs


def main(paths):
    bad = 0
    for p in paths:
        errs = check(p)
        if errs:
            bad += 1
            print(f"FAIL {p}")
            for e in errs:
                print(f"  - {e}")
        else:
            with open(p, encoding="utf-8") as f:
                d = json.load(f)
            scores = [v["score"] for v in d["feels"].values()]
            fours = sum(1 for x in scores if x == 4)
            threes = sum(1 for x in scores if x == 3)
            print(f"OK   {p}  (74 feels: {fours} fours, {threes} threes, "
                  f"mean {sum(scores)/74:.2f})")
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
