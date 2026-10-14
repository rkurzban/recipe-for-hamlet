# motivational-ingredients skill: local files (notes from the calibration, 3 October 2026)

These are the working notes written when the calibration was run. The repository README is the place to start; this file is kept as the record of how the calibration folder was built.


## Layout

- `SKILL.md` — copy of the skill, updated 3 October 2026 with the figures of the second calibration (the same text was proposed as a skill update on claude.ai).
- `references/table2-titles.csv` — the 14 works of Table 2 of Dubourg, Thouzeau et al. (2026). The site's "Article" collection is this list. Columns: `site_id` (the key the site uses), `title`, `year`, `medium`, `creator`, `slug` (file name of the rating), `note`.
- `references/site-system-prompt.txt` — the exact prompt the site sends to gpt-5-mini (prompt version 2026-09-17.1), copied from the "What exactly runs" section of https://motivational-ingredients.com/annotate.
- `calibration/<slug>.json` — Claude's rating of each work, in the skill's JSON shape, with `model` and `date`. The current files are the second calibration (3 October 2026, after the scale fix).
- `calibration/run1/` — the first calibration (3 October 2026, before the scale fix): its 14 rating files, `annotations.csv`, `comparison.csv`, and `comparison-report.md`.
- `calibration/annotations.csv` — the 14 ratings as one spreadsheet (the format SKILL.md asks for).
- `calibration/site/table2.json` — the author-verified Table 2 scores, downloaded from `https://motivational-ingredients.com/data/table2.json`.
- `calibration/comparison.csv` — one row per work and ingredient: Claude's score, the site's score, the difference, and Claude's reason.
- `calibration/comparison-report.md` — the summary the comparison script prints.
- `scripts/validate_annotations.py` — checks rating files against the rules in SKILL.md.
- `scripts/compare_calibration.py` — compares `calibration/*.json` with `calibration/site/table2.json`.
- `scripts/build_annotations_csv.py` — builds `annotations.csv` from rating files.

## How to run the calibration again

From this folder, with Python 3 (no packages needed):

```
python scripts/validate_annotations.py calibration/*.json
python scripts/compare_calibration.py
python scripts/build_annotations_csv.py calibration
```

To rate the works again after changing SKILL.md: ask Claude to "annotate every title in references/table2-titles.csv and save the results in calibration/", then run the three commands. Rate before you look at `calibration/site/table2.json`, so the verified scores cannot pull the ratings.

## Result of the first calibration (3 October 2026)

Claude's ratings order the ingredients much like the authors do (Spearman rank correlation 0.68 over 672 pairs; 0.51 to 0.82 per work). But Claude uses the scale differently. The authors give a 4 to 27% of all ratings; Claude gave a 4 to 2%. Claude's scores sit 0.77 points below the authors' on average. Raising every nonzero Claude score by one point removes almost all of that bias and lifts exact agreement from 32% to 44%.

The likely cause is a sentence in SKILL.md that is not in the site's prompt: "a 4 should be rare and reserved for what the story is about." The authors do not use 4 that way. For them, 4 means an ingredient that runs through the whole work, and a long work can have fifteen of them.

Beyond scale use, Claude reads some ingredients more narrowly than the authors: Moral praise, Moral blame, Affiliation, Pride, Moral pride, Reasoning, Skill acquisition, Shame, Envy, and Coalitional affiliation are each 1.2 to 2.1 points lower on average. Mating ingredients agree well.

## Result of the second calibration (3 October 2026, after the scale fix)

Rater: claude-fable-5-1. Rank correlation 0.71 over 672 pairs (0.61 to 0.85 per work); quadratic weighted kappa 0.70. Exact agreement 42.9% (was 31.7%), within one point 86.5% (was 75.6%). Bias -0.12 (was -0.77); mean absolute difference 0.73 (was 0.99); 14 pairs three or more points apart (was 38). The authors give a 4 to 27% of ratings; Claude now gives a 4 to 15% (was 2%).

Stretching Claude's scale mechanically now makes agreement worse, so the remaining gap is in how some ingredients are read, not in scale use. Still read more narrowly than the authors (0.5 to 1.4 points lower on average): Moral praise, Resource foraging, Moral blame, Pride, Resource accumulation, Affiliation, Fear of aggressors, Shame, Envy. Read more broadly than the authors (0.4 to 0.8 points higher): Sexual attraction, Romantic affiliation, Sexual disgust, Humor, Compassion. Rank agreement across works is weakest for Resource foraging, Disgust, Hatred, Long-term love, Moral blame, Parental care, and Affiliation. *The Metamorphosis* agreed worst (bias -0.96); *Harry Potter* and *Journey to the West* best (within one point 96%).
