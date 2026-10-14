---
name: "motivational-ingredients"
description: "Annotate a story (film, series, novel, game, manga, comic, play) with the 48 motivational ingredients of Dubourg, Thouzeau et al. (2026): identify the work, score each ingredient 0-4 with a one-sentence reason, report a table and JSON. Use whenever the user mentions motivational ingredients, the Motivational-Ingredient Framework, Dubourg, Baumard, motivational-ingredients.com, or asks to score or annotate a story's motivations; also for calibration against the article's Table 2. The companion skill feels-annotate scores the 74 feels of All the Feels."
---

# Annotate a story with the Motivational-Ingredient Framework

This file tells Claude how to do, on its own, what the "Annotate a story" tool does at https://motivational-ingredients.com/annotate. The site sends a title to an OpenAI model (gpt-5-mini, prompt version 2026-09-17.1) and stores the result. Here, Claude plays the part of that model and uses its own knowledge of the work. Nothing is sent to the site.

## How to start

Give Claude a title. Say, for example:

- "Annotate *The Martian*."
- "Annotate *Frozen* (2013, Disney, film)."
- "Annotate every title in `titles.csv` and save the results in this folder."

Only the title is required. A year, a creator (author, director, or studio), and a medium help only when the title is ambiguous.

## The framework in short

The Motivational-Ingredient Framework (Dubourg, Thouzeau et al., 2026, *Psychological Review*) says that stories hold our attention because they contain *motivational ingredients*. An ingredient is a feature of the story's content that switches on a motivational mechanism we already have, by imitating the conditions that mechanism responds to. The framework lists 48 ingredients in six families: Self, Threats, Cooperation, Competition, Mating, and Kin. An annotation rates how prominent each ingredient is across the whole story.

## Step 1: Identify the work

Work from the title and any optional details.

1. If the title points to one work, or to one work that is clearly intended or by far the best known, go on to Step 2.
2. Different adaptations of the same story (a novel and its film) are one work, not an ambiguity. Rate the story as a whole unless the user names one adaptation (for example, "the 1962 film").
3. If the title could mean several distinct works with different stories (for example *Frozen*, *Crash*, *Mario*), do not choose silently. Mark the request as ambiguous. List 2 to 10 candidates with title, year, medium, and creator. Give no ratings. Ask the user to pick one or to add a year, a creator, or a medium.
4. If the title names a series, saga, or franchise whose instalments tell distinct stories (for example *Harry Potter*, *Star Wars*, *The Lord of the Rings*, *Final Fantasy*), also mark it as ambiguous. List the main instalments as candidates, oldest first, with their years (up to 9, keeping the best known). Then add the whole series as the last candidate, titled exactly "<Series title> (whole series)", with the year of the first instalment. A serialized work with no separate instalments (a manga, a television series) is one work: rate it as a whole. If the title already names one instalment, or says "whole series", do not mark it as ambiguous.
5. If you do not recognize the work with reasonable confidence, say so and give no ratings. Do not guess.

Never invent plot elements. If you are not sure an element is in the work, leave it out.

## Step 2: Rate the 48 ingredients

For each ingredient, in the order below:

1. Write one sentence of at most 35 words. Name the concrete story elements that meet, or fail to meet, the ingredient's input conditions. The sentence must justify the score, also when the score is 0.
2. Give one integer score from 0 to 4.

Scale (integers only):

| Score | Meaning |
|---|---|
| 0 | Absent |
| 1 | Present but negligible |
| 2 | Present and secondary |
| 3 | Present and central |
| 4 | Dominant; defines the story |

Rate the overall importance, across the whole story, of all concrete story elements that meet the input conditions of the mechanism. Rate what happens in the story, not what its genre label suggests.

Use the scale the way the authors use it. A 4 means an ingredient that runs through the whole work. Several ingredients in one work can be 4, and a long work often has ten or more: in the article's Table 2, 27 percent of all cells are 4s, and *The Iliad* has sixteen. Do not ration 4s. (This paragraph is a calibration note, added 3 October 2026, after a run with the sentence "a 4 should be rare" scored 0.77 points below the authors on average. The same scale rule is in the companion skill `feels-annotate`, so the two frameworks are rated alike.)

Also write one sentence (at most 30 words) that sums up the story's dominant motivational content.

## The 48 ingredients

These are the site's own lines, verbatim, as it sends them to its model (prompt version 2026-09-17.1, copied 3 October 2026 from the "What exactly runs" section of https://motivational-ingredients.com/annotate). Format: number. Name [slug] (Domain) — Ingredient: the story content. Input conditions: the cues that switch the mechanism on. Earlier versions of this file paraphrased these lines; the calibration of 3 October 2026 (below) is the reason they are now exact.

1. Hunger [hunger] (Self) — Ingredient: A story where a character enjoys, seeks, or struggles to obtain food. Input conditions: Cues indicating caloric or nutrient-dense food.
2. Thirst [thirst] (Self) — Ingredient: A story where a character enjoys, seeks, or struggles to obtain water. Input conditions: Cues indicating water or hydration sources.
3. Feeling cold / hot [feeling-cold-hot] (Self) — Ingredient: A story where a character experiences extreme temperatures. Input conditions: Cues indicating temperature extremes.
4. Sleepiness [sleepiness] (Self) — Ingredient: A story where a character feels exhausted or sleep-deprived. Input conditions: Cues indicating physical fatigue or lack of rest.
5. Curiosity [curiosity] (Self) — Ingredient: A story where a character explores new environments. Input conditions: Cues indicating novel or unexplored information.
6. Explanation-seeking [explanation-seeking] (Self) — Ingredient: A story where a character solves mysteries. Input conditions: Cues indicating a knowledge gap.
7. Skill acquisition [skill-acquisition] (Self) — Ingredient: A story where a character trains, pushes their limits, and becomes stronger. Input conditions: Cues indicating opportunities for learning or skill improvement.
8. Play [play] (Self) — Ingredient: A story where a character engages in play. Input conditions: Cues indicating safe, low-stakes opportunities for behavioral calibration.
9. Resource accumulation [resource-accumulation] (Self) — Ingredient: A story where a character gains wealth or valuable possessions. Input conditions: Cues indicating opportunities for acquiring material resources or wealth.
10. Resource foraging [resource-foraging] (Self) — Ingredient: A story where a character searches for necessary or rare resources. Input conditions: Cues indicating opportunities for searching or gathering resources.
11. Mental time travel [mental-time-travel] (Self) — Ingredient: A story where a character plans ahead and develops strategies to achieve their goals. Input conditions: Cues prompting reflection on past events or future planning.
12. Fear of predators [fear-of-predators] (Threats) — Ingredient: A story where a character is threatened by dangerous creatures or monsters. Input conditions: Cues indicating predatory threats.
13. Fear of aggressors [fear-of-aggressors] (Threats) — Ingredient: A story where a character is physically threatened by enemies or attackers. Input conditions: Cues indicating aggression or conflict.
14. Fear of heights [fear-of-heights] (Threats) — Ingredient: A story where a character deals with dizzying heights, dangerous falls, or vertigo. Input conditions: Cues indicating high or unstable physical environments.
15. Disgust [disgust] (Threats) — Ingredient: A story where a character is threatened by decay, disease, or contamination. Input conditions: Cues indicating contamination or disease.
16. Pain aversion [pain-aversion] (Threats) — Ingredient: A story where a character endures physical suffering. Input conditions: Cues indicating physical harm or injury.
17. Pride [pride] (Cooperation) — Ingredient: A story where a character accomplishes something impressive and earns recognition for it. Input conditions: Cues indicating success or competence.
18. Shame [shame] (Cooperation) — Ingredient: A story where a character confronts shame after violating social standards. Input conditions: Cues indicating failure or incompetence.
19. Moral pride [moral-pride] (Cooperation) — Ingredient: A story where a character stands by their values, even at great cost. Input conditions: Cues indicating self-adherence to moral virtue.
20. Guilt [guilt] (Cooperation) — Ingredient: A story where a character is haunted by their past actions, seeking redemption. Input conditions: Cues indicating personal moral wrongdoing.
21. Warmth [warmth] (Cooperation) — Ingredient: A story where a character shows kindness or deep empathy. Input conditions: Cues indicating kindness, care, or empathy from others.
22. Moral blame [moral-blame] (Cooperation) — Ingredient: A story where a character condemns wrongdoing or seeks justice. Input conditions: Cues indicating moral wrongdoing.
23. Moral praise [moral-praise] (Cooperation) — Ingredient: A story where a character is celebrated for their goodness or heroism. Input conditions: Cues indicating adherence to moral virtue.
24. Revenge [revenge] (Cooperation) — Ingredient: A story where a character seeks vengeance on those who have wronged them. Input conditions: Cues indicating injustice or betrayal.
25. Forgiveness [forgiveness] (Cooperation) — Ingredient: A story where a character chooses to let go of hatred, finding peace or reconciliation. Input conditions: Cues indicating opportunities for reconciliation.
26. Compassion [compassion] (Cooperation) — Ingredient: A story where a character cares for the weak or protects the vulnerable. Input conditions: Cues indicating suffering or vulnerability.
27. Affiliation [affiliation] (Cooperation) — Ingredient: A story where a character seeks out new friends or companions. Input conditions: Cues indicating warmth or competence.
28. Friendship [friendship] (Cooperation) — Ingredient: A story where a character forms close bonds with their friends. Input conditions: Cues indicating shared social bonds.
29. Sadness [sadness] (Cooperation) — Ingredient: A story where a character feels deep sorrow after loss, failure, or separation. Input conditions: Cues indicating the loss of something or someone valuable.
30. Humor [humor] (Cooperation) — Ingredient: A story where humor is created through a character making jokes, engaging in playful interactions, or undergoing absurd or benignly misfortunate circumstances. (Eitzen, 2012; Hye-Knudsen, 2022) Input conditions: Cues indicating benign violations.
31. Embarrassment [embarrassment] (Cooperation) — Ingredient: A story where a character feels embarrassed. Input conditions: Cues indicating social norm violations.
32. Reasoning [reasoning] (Cooperation) — Ingredient: A story where a character engages in intellectual battles or sharp debates. Input conditions: Cues indicating social justifications or arguments.
33. Coalitional affiliation [coalitional-affiliation] (Cooperation) — Ingredient: A story where a character forms or maintains a strong group identity. Input conditions: Cues indicating opportunities for group formation.
34. Status-seeking [status-seeking] (Competition) — Ingredient: A story where a character gains influence or earns respect through their actions. Input conditions: Cues indicating opportunities for social rank.
35. Envy [envy] (Competition) — Ingredient: A story where a character longs for what others have. Input conditions: Cues indicating others' success or resources.
36. Anger [anger] (Competition) — Ingredient: A story where a character is driven by rage, seeking justice, or acting on fury. Input conditions: Cues indicating perceived injustice, harm, or offense.
37. Hatred [hatred] (Competition) — Ingredient: A story where a character takes pleasure in a rival's downfall or a foe's suffering. Input conditions: Cues indicating the failure or misfortune of others.
38. Romantic affiliation [romantic-affiliation] (Mating) — Ingredient: A story where a character is drawn to another, forming a romantic connection. Input conditions: Cues indicating attractiveness (warmth, competence, beauty).
39. Sexual attraction [sexual-attraction] (Mating) — Ingredient: A story where a character experiences desire and irresistible chemistry. Input conditions: Cues indicating physical desirability or fertility.
40. Long-term love [long-term-love] (Mating) — Ingredient: A story where a character develops a deep, lasting romantic commitment. Input conditions: Cues indicating commitment or enduring emotional bonds.
41. Desire [desire] (Mating) — Ingredient: A story where a character pursues physical encounters without long-term commitment. Input conditions: Cues indicating opportunities for multiple sexual relations.
42. Romantic jealousy [romantic-jealousy] (Mating) — Ingredient: A story where a character feels threatened by a potential romantic rival. Input conditions: Cues indicating potential romantic rivalry or infidelity.
43. Sexual jealousy [sexual-jealousy] (Mating) — Ingredient: A story where a character feels threatened by a potential sexual rival. Input conditions: Cues indicating sexual infidelity or competition.
44. Sexual disgust [sexual-disgust] (Mating) — Ingredient: A story where a character deals with inappropriate, forced, or unsettling sexual relationships. Input conditions: Cues indicating inappropriate or taboo sexual behavior.
45. Kin sexual disgust [kin-sexual-disgust] (Kin) — Ingredient: A story where a character avoids or rejects incestuous relationships. Input conditions: Cues indicating sexual behavior within kinship.
46. Parental care [parental-care] (Kin) — Ingredient: A story where a character protects a child. Input conditions: Cues indicating vulnerability or dependency.
47. Parental investment [parental-investment] (Kin) — Ingredient: A story where a character nurtures or raises a child. Input conditions: Cues indicating a disposition to learn or improve.
48. Familial love [familial-love] (Kin) — Ingredient: A story where a character forms close bonds with their family. Input conditions: Cues indicating kinship ties, familial obligations, or loyalty.

## Step 3: Report the result

Always give these four parts, in this order.

1. **The work.** Title, year, medium, creator. Medium is one of: movie, tv, novel, game, manga, comic, theatre, epic, tale, book, other.
2. **The summary sentence.**
3. **A table by family** with three columns: Ingredient, Score, Why. Put the 4s and 3s in bold so the profile is easy to read.
4. **A JSON block** (JavaScript Object Notation) in the same shape the site uses, so results can be compared with the site's. Fill the template below. Keep all 48 keys, in this order.

Rules for the JSON block:

- `year` is 4 digits or an empty string.
- `creator` is names only, with no role label (for example "Nintendo", "Bong Joon-ho"), or an empty string.
- If the work is unknown (`known` is false) or the title is ambiguous (`ambiguous` is true): leave every `why` empty, set every `score` to 0, and set the four `work` fields to empty strings. When ambiguous, fill `candidates`; otherwise leave it as an empty list.

```json
{
  "known": true,
  "ambiguous": false,
  "candidates": [],
  "work": { "title": "", "year": "", "medium": "", "creator": "" },
  "summary": "",
  "hunger": { "why": "", "score": 0 },
  "thirst": { "why": "", "score": 0 },
  "feeling-cold-hot": { "why": "", "score": 0 },
  "sleepiness": { "why": "", "score": 0 },
  "curiosity": { "why": "", "score": 0 },
  "explanation-seeking": { "why": "", "score": 0 },
  "skill-acquisition": { "why": "", "score": 0 },
  "play": { "why": "", "score": 0 },
  "resource-accumulation": { "why": "", "score": 0 },
  "resource-foraging": { "why": "", "score": 0 },
  "mental-time-travel": { "why": "", "score": 0 },
  "fear-of-predators": { "why": "", "score": 0 },
  "fear-of-aggressors": { "why": "", "score": 0 },
  "fear-of-heights": { "why": "", "score": 0 },
  "disgust": { "why": "", "score": 0 },
  "pain-aversion": { "why": "", "score": 0 },
  "pride": { "why": "", "score": 0 },
  "shame": { "why": "", "score": 0 },
  "moral-pride": { "why": "", "score": 0 },
  "guilt": { "why": "", "score": 0 },
  "warmth": { "why": "", "score": 0 },
  "moral-blame": { "why": "", "score": 0 },
  "moral-praise": { "why": "", "score": 0 },
  "revenge": { "why": "", "score": 0 },
  "forgiveness": { "why": "", "score": 0 },
  "compassion": { "why": "", "score": 0 },
  "affiliation": { "why": "", "score": 0 },
  "friendship": { "why": "", "score": 0 },
  "sadness": { "why": "", "score": 0 },
  "humor": { "why": "", "score": 0 },
  "embarrassment": { "why": "", "score": 0 },
  "reasoning": { "why": "", "score": 0 },
  "coalitional-affiliation": { "why": "", "score": 0 },
  "status-seeking": { "why": "", "score": 0 },
  "envy": { "why": "", "score": 0 },
  "anger": { "why": "", "score": 0 },
  "hatred": { "why": "", "score": 0 },
  "romantic-affiliation": { "why": "", "score": 0 },
  "sexual-attraction": { "why": "", "score": 0 },
  "long-term-love": { "why": "", "score": 0 },
  "desire": { "why": "", "score": 0 },
  "romantic-jealousy": { "why": "", "score": 0 },
  "sexual-jealousy": { "why": "", "score": 0 },
  "sexual-disgust": { "why": "", "score": 0 },
  "kin-sexual-disgust": { "why": "", "score": 0 },
  "parental-care": { "why": "", "score": 0 },
  "parental-investment": { "why": "", "score": 0 },
  "familial-love": { "why": "", "score": 0 }
}
```

A candidate, when the title is ambiguous, has the same four fields as `work`: `title`, `year`, `medium`, `creator`.

## Saving results (when asked, or when a folder is given)

- Save one JSON file per story, named `<title-slug>-<year>.json`, with the block above plus two extra keys: `model` (the Claude model that did the rating) and `date` (today, YYYY-MM-DD).
- Keep one spreadsheet, `annotations.csv` (comma-separated values), with one row per story. Columns: title, year, medium, creator, model, date, summary, then the 48 slugs in order, each holding the score. Add new rows; do not add a title and year that is already there.

## Batch mode

When the user gives a list of titles (in a text file, a comma-separated values file, or a spreadsheet), annotate each title in turn with the rules above. If a title is ambiguous, do not guess: note its candidates in the report and go on to the next title, unless the user said to take the best-known work. If a title is unknown, note that and go on. End with a short report: how many titles were annotated, which were unknown, and which were ambiguous.

## Calibration mode (against the article's Table 2)

Table 2 of the article gives author-verified scores for 14 works. Rating those 14 with this skill and comparing the result with the verified scores measures how well this rater reproduces the authors' judgment. Run it after any change to the rules above, and before any comparison you mean to publish.

Trigger words: "calibrate", "calibration run", "rate the Table 2 works".

The supporting files live in Dropbox at `All the Feels/motivational-ingredients/` (the skill saved on claude.ai keeps only this file): `references/site-system-prompt.txt`, `references/table2-titles.csv`, `calibration/site/table2.json` (the verified scores, downloaded from the site; they match the article's PDF cell for cell), and three scripts, `scripts/validate_annotations.py`, `scripts/compare_calibration.py`, `scripts/build_annotations_csv.py`. The packaged version of this skill also carries `references/table2-verified.csv` and a standard-library fallback, `scripts/compare_table2.py`.

1. **Do not open the verified scores before rating.** A rater that has seen the answers is not calibrated. If Table 2 is already in this conversation (the article was pasted or read earlier, or `table2.json` was opened), say so and stop: the calibration must run in a fresh conversation.
2. Rate the 14 works below with Step 2, in full, with the one-sentence reasons. Treat each as unambiguous; do not list candidates. Save one JSON file per work in `calibration/`, named `<slug>.json`.

| slug | title | year | medium | creator |
|---|---|---|---|---|
| the-iliad | The Iliad | | epic | Homer |
| the-tale-of-genji | The Tale of Genji | | novel | Murasaki Shikibu |
| the-song-of-roland | The Song of Roland | | epic | Anonymous |
| journey-to-the-west | Journey to the West | | novel | Wu Cheng'en |
| hamlet-1600 | Hamlet | 1600 | theatre | William Shakespeare |
| little-red-riding-hood | Little Red Riding Hood | | tale | Charles Perrault (rate the story across the Perrault and Grimm versions) |
| in-search-of-lost-time-1913 | In Search of Lost Time | 1913 | novel | Marcel Proust (all seven volumes) |
| the-metamorphosis-1915 | The Metamorphosis | 1915 | novel | Franz Kafka |
| murder-on-the-orient-express-1934 | Murder on the Orient Express | 1934 | novel | Agatha Christie |
| 2001-a-space-odyssey-1968 | 2001: A Space Odyssey | 1968 | movie | Stanley Kubrick |
| the-shining-1980 | The Shining | 1980 | movie | Stanley Kubrick |
| titanic-1997 | Titanic | 1997 | movie | James Cameron |
| harry-potter-and-the-philosophers-stone-1997 | Harry Potter and the Philosopher's Stone | 1997 | novel | J. K. Rowling (the article's "Harry Potter 1") |
| one-piece-1999 | One Piece | 1999 | manga | Eiichiro Oda (rate the serialized work as a whole) |

3. From the Dropbox folder, run `python scripts/validate_annotations.py calibration/*.json`, then `python scripts/compare_calibration.py`, then `python scripts/build_annotations_csv.py calibration`. The comparison prints the score distributions, exact and within-one agreement, mean absolute difference, rank correlation and weighted kappa, the same per work, per ingredient and per family, and every cell three or more points apart.
4. Report the figures and the per-ingredient table. Ingredients this rater reads differently from the authors are the rows to treat with care in any later comparison.

**First calibration, 3 October 2026, before the scale fix above:** rank correlation 0.68 over 672 cells (0.51 to 0.82 per work); exact agreement 31.7 percent, within one point 75.6 percent; bias −0.77 (the rater scored low); the authors gave a 4 to 27 percent of cells, the rater to 2 percent. Beyond scale use, ten ingredients were read 1.2 to 2.1 points more narrowly than the authors read them: moral praise, moral blame, affiliation, pride, moral pride, reasoning, skill acquisition, shame, envy, coalitional affiliation. Mating ingredients agreed best. Record the figures of each later run here, under this one.

**Second calibration, 3 October 2026, after the scale fix above** (rater claude-fable-5-1; its files are in `calibration/`, the first run's in `calibration/run1/`): rank correlation 0.71 over 672 cells (0.61 to 0.85 per work); weighted kappa 0.70; exact agreement 42.9 percent, within one point 86.5 percent; bias −0.12; mean absolute difference 0.73; 14 cells three or more points apart. The authors gave a 4 to 27 percent of cells, the rater to 15 percent. Stretching the rater's scale mechanically now makes agreement worse, so what remains is a difference in how ingredients are read, not in scale use. Still read more narrowly than the authors (0.5 to 1.4 points lower): moral praise, resource foraging, moral blame, pride, resource accumulation, affiliation, fear of aggressors, shame, envy. Read more broadly than the authors (0.4 to 0.8 points higher): sexual attraction, romantic affiliation, sexual disgust, humor, compassion. Rank agreement across works was weakest (below 0.4) for resource foraging, disgust, hatred, long-term love, moral blame, parental care, and affiliation. *The Metamorphosis* agreed worst (bias −0.96; within one point 65 percent); *Harry Potter* and *Journey to the West* best (within one point 96 percent).

For a published comparison that includes any of the 14 works, use the authors' verified scores for those works, not the skill's. The skill's scores are for works the article did not rate, and for the rater-against-rater comparison with `feels-annotate`, where both sides must come from the same instrument.

## Limits to state when you report

- The site says its annotations rest on "the model's unverified knowledge of the work: a demonstration, not data." The same is true here.
- The site uses gpt-5-mini (or gpt-5.4 for recent works). Claude's scores will differ from the site's. Do not present them as the site's output.
- Works released after Claude's knowledge cutoff cannot be rated.
- Nothing is stored on the site. To add a story to the site, use the form at https://motivational-ingredients.com/annotate.
- The verified Table 2 scores (`calibration/site/table2.json` in Dropbox; `references/table2-verified.csv` in the package) are for the comparison scripts, not for rating.

## A note on wording

The ingredient lines above are the site's exact text. If the site publishes a new prompt version, copy the new lines over these and record the version and date in the sentence that introduces the list.

## References

- Dubourg, E., Thouzeau, V., et al. (2026). The Motivational-Ingredient Framework. *Psychological Review*.
- Dubourg, E., Thouzeau, V., & Baumard, N. (2024). A step-by-step method for cultural annotation by LLMs.
- Dubourg, E., & Thouzeau, V. (2026). The double edge of AI annotation in cultural sciences (preprint).
- Syme, Motos, & Placek (2026). Generating units of cultural analysis with LLMs.
- The site: https://motivational-ingredients.com (prompt version 2026-09-17.1, read on 3 October 2026).