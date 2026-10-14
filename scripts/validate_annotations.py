#!/usr/bin/env python3
"""Check annotation JSON files against the rules in SKILL.md.

Usage: python3 scripts/validate_annotations.py calibration/*.json

Checks, for each file:
- valid JSON
- all 48 ingredient keys present, in the order of SKILL.md
- every score is an integer from 0 to 4
- every 'why' sentence has at most 35 words
- the summary has at most 30 words
- 'model' and 'date' keys exist (for saved files)
Exit code 1 if any file fails.
"""
import json
import sys
from pathlib import Path

SLUGS = [
    "hunger", "thirst", "feeling-cold-hot", "sleepiness", "curiosity",
    "explanation-seeking", "skill-acquisition", "play", "resource-accumulation",
    "resource-foraging", "mental-time-travel",
    "fear-of-predators", "fear-of-aggressors", "fear-of-heights", "disgust",
    "pain-aversion",
    "pride", "shame", "moral-pride", "guilt", "warmth", "moral-blame",
    "moral-praise", "revenge", "forgiveness", "compassion", "affiliation",
    "friendship", "sadness", "humor", "embarrassment", "reasoning",
    "coalitional-affiliation",
    "status-seeking", "envy", "anger", "hatred",
    "romantic-affiliation", "sexual-attraction", "long-term-love", "desire",
    "romantic-jealousy", "sexual-jealousy", "sexual-disgust",
    "kin-sexual-disgust", "parental-care", "parental-investment",
    "familial-love",
]

MAX_WHY_WORDS = 35
MAX_SUMMARY_WORDS = 30


def word_count(text):
    return len(text.split())


def check(path):
    problems = []
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"invalid JSON: {e}"]

    keys = list(data.keys())
    present = [k for k in keys if k in SLUGS]
    missing = [s for s in SLUGS if s not in data]
    if missing:
        problems.append(f"missing ingredients: {missing}")
    if present != SLUGS:
        problems.append("ingredient keys are not in SKILL.md order")

    for slug in SLUGS:
        item = data.get(slug)
        if not isinstance(item, dict):
            continue
        score = item.get("score")
        if not isinstance(score, int) or isinstance(score, bool) or not 0 <= score <= 4:
            problems.append(f"{slug}: score {score!r} is not an integer 0-4")
        why = item.get("why", "")
        n = word_count(why)
        if n > MAX_WHY_WORDS:
            problems.append(f"{slug}: why has {n} words (max {MAX_WHY_WORDS})")
        if data.get("known") and not data.get("ambiguous") and not why.strip():
            problems.append(f"{slug}: empty why")

    n = word_count(data.get("summary", ""))
    if n > MAX_SUMMARY_WORDS:
        problems.append(f"summary has {n} words (max {MAX_SUMMARY_WORDS})")

    for key in ("known", "ambiguous", "candidates", "work", "summary"):
        if key not in data:
            problems.append(f"missing key: {key}")
    for key in ("model", "date"):
        if key not in data:
            problems.append(f"missing key: {key} (saved files need it)")
    work = data.get("work", {})
    for key in ("title", "year", "medium", "creator"):
        if key not in work:
            problems.append(f"work is missing {key}")
    return problems


def main(paths):
    bad = 0
    for p in paths:
        probs = check(p)
        if probs:
            bad += 1
            print(f"FAIL {p}")
            for q in probs:
                print(f"  - {q}")
        else:
            print(f"ok   {p}")
    print(f"\n{len(paths) - bad} of {len(paths)} files pass")
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
