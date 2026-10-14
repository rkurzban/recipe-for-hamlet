# feels: the 14 Table 2 works rated with the 74 feels

Companion to `../calibration/`, which holds the same 14 works rated with the 48 motivational ingredients. The slugs match (`the-iliad`, `hamlet-1600`, ...), so a feels file and an ingredients file for one work can be joined by name.

## Layout

- `character/<slug>.character.feels.json` — the character perspective: what the characters feel, or the conditions they face. This is the pass comparable with the ingredients.
- `audience/<slug>.audience.feels.json` — the audience perspective: what the story is built to make an ordinary first-time audience feel, through content and form together.
- `feels-annotations.csv` — one row per work and perspective (28 rows): title, year, medium, creator, model, date, mode, perspective, summary, monera, then the 74 feel slugs and the 8 extra rows, each holding the score.
- `batch-report.md` — the batch report the skill asks for: score distributions, the spread table (lowest, highest, works at 3 or 4, mean) for each row and perspective, the rows constant across all works, and the character-versus-audience differences.
- `scripts/validate_feels.py` — checks a rating file against the skill's template (keys, order, scores 0-4, reasons of at most 35 words, summary of at most 30 words).
- `scripts/build_feels_csv.py` — builds `feels-annotations.csv` from rating files; skips a title, year, and perspective already in the file.
- `scripts/batch_report.py` — writes `batch-report.md` from the two folders.

## How these were made

Rater: claude-fable-5-1, one session, 4 October 2026, in Cowork, following the `feels-annotate` skill as saved on claude.ai that day (a copy is in `../feels-skill/SKILL.md`) (the version with the scale rule shared with `motivational-ingredients`: a 4 means a feel that runs through the whole work; do not ration 4s). Each work was rated in full, character pass first for all 14, then audience pass for all 14, in the order of the calibration table. Each JSON file carries `model` and `date`. The verified Table 2 scores were not opened.

## To run the checks again

From this folder, with Python 3 (no packages needed):

```
python scripts/validate_feels.py character/*.json audience/*.json
python scripts/build_feels_csv.py feels-annotations.csv character/*.json audience/*.json
python scripts/batch_report.py batch-report.md character audience
```

## Limits

The ratings rest on the rater's unverified knowledge of the works: a demonstration, not data. Scores vary from run to run; for a comparison meant for publication, rate each work more than once and report the median. There is no author-verified feels table to calibrate against, so these files are a first rating, not a calibration. For a comparison between the two frameworks, use the character pass here beside `../calibration/<slug>.json` (same rater, same scale, same rules), with the authors' verified ingredient scores shown as the reference, never in place of the skill's.
