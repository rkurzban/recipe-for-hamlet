# crosswalk: the 48 ingredients against the 74 Feels

`crosswalk.py` joins the ingredient scores in `../calibration/` (the rater's and the authors') with the Feel scores in `../feels/character/`, using the map in `crosswalk.csv`, and writes three files.

- `crosswalk.csv` — one row per ingredient. `feels` lists the Feel or Feels it is nearest to, separated by semicolons; the first is its nearest Feel. Four ingredients map to nothing (Resource accumulation, Resource foraging, Mental time travel, Forgiveness). `note` says why where the choice is not obvious.
- `blockers.csv` — Feels that are not an ingredient's counterpart but could be mistaken for one, with the ingredients that block them under the addition rule. Lonely is the one entry: it is credited only where Affiliation and Coalitional affiliation are both low.
- `cells.csv` — every Feel cell (82 rows by 14 works = 1,148): the character score, the audience score, the ingredients it could be mistaken for with both of their scores (`rater/authors`), whether it passes the addition rule, and the rater's one-sentence reason.
- `pairs.csv` — every ingredient paired with its nearest Feel (44 by 14 = 616): the rater's ingredient score, the authors' ingredient score, the Feel score, the difference, and whether the mapping is one-to-one or a carving difference.
- `report.md` — the counts: agreement, differences, addition-rule passes, the table rows, the mirror-rule cells.

Run from the repository root: `python3 crosswalk/crosswalk.py`

## Rules

- **Agree:** a pair where the rater gave the same score under both names.
- **Carving difference:** a pair that differs by 2 or more where one list splits what the other lumps (three fears to one Afraid; one Sadness to four Feels). The difference is where the two lists cut, not a disagreement about the work.
- **Difference of judgment:** a pair that differs by 2 or more where the mapping is one-to-one.
- **Addition rule:** a Feel cell scores 3 or 4, and every ingredient it could be mistaken for scores 0 or 1 in both columns.
- **Mirror-image rule:** an ingredient cell scores 3 or 4 in both columns, and every Feel near it scores 0 or 1.
- **Table row:** a Feel with no counterpart ingredient that scores 3 or 4 in at least five works.

## A note on provenance

The crosswalk used for the post's first draft was built in a working session and not saved. This folder is a rebuild from the saved ratings, written on 14 October 2026. It reproduces the structural results of the post exactly: the twelve table rows and their cells, Lonely passing the addition rule in *The Shining* only, the eleven mirror-rule cells for the same four ingredients in the same works, and Fear of heights against Afraid in thirteen works. The mapping of ingredients to Feels is a judgment, and a reader who draws the map differently will get different counts; that is what `crosswalk.csv` is for.
