# Calibration: Claude vs. author-verified Table 2 scores

14 works x 48 ingredients = 672 score pairs. Differences are Claude minus site (positive = Claude higher).

## Overall

- Mean score, Claude: 2.06; site: 2.18; mean difference (bias): -0.12
- Mean absolute difference: 0.73 points
- Exact agreement: 42.9%; within 1 point: 86.5%; off by 3 or more: 14 pairs
- Pearson r: 0.71; Spearman rho: 0.71; quadratic weighted kappa: 0.70

Score distribution (count of each score across all pairs):

| Score | Claude | Site |
|---|---|---|
| 0 | 84 | 123 |
| 1 | 145 | 120 |
| 2 | 190 | 124 |
| 3 | 150 | 121 |
| 4 | 103 | 184 |

Confusion matrix (rows = site score, columns = Claude score):

| site \ Claude | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 61 | 45 | 14 | 3 | 0 |
| 1 | 16 | 46 | 45 | 11 | 2 |
| 2 | 2 | 38 | 48 | 34 | 2 |
| 3 | 2 | 12 | 47 | 47 | 13 |
| 4 | 3 | 4 | 36 | 55 | 86 |

Claude's mean score for each site score (how far Claude sits below or above the authors at each level):

| Site score | n | Claude mean |
|---|---|---|
| 0 | 123 | 0.67 |
| 1 | 120 | 1.48 |
| 2 | 124 | 1.97 |
| 3 | 121 | 2.47 |
| 4 | 184 | 3.18 |

## Per work

| Work | Claude mean | Site mean | Bias | Mean abs diff | Spearman | Exact % | Within 1 % |
|---|---|---|---|---|---|---|---|
| The Iliad | 2.67 | 2.48 | 0.19 | 0.73 | 0.71 | 38 | 90 |
| The Tale of Genji | 2.35 | 2.19 | 0.17 | 0.62 | 0.67 | 52 | 90 |
| The Song of Roland | 1.90 | 2.46 | -0.56 | 0.69 | 0.85 | 46 | 88 |
| Journey to the West | 2.65 | 2.88 | -0.23 | 0.56 | 0.72 | 48 | 96 |
| Hamlet | 2.40 | 2.88 | -0.48 | 0.81 | 0.61 | 44 | 79 |
| Little Red Riding Hood | 1.21 | 1.12 | 0.08 | 0.71 | 0.64 | 40 | 90 |
| In Search of Lost Time | 2.58 | 2.42 | 0.17 | 0.75 | 0.67 | 40 | 90 |
| The Metamorphosis | 1.44 | 2.40 | -0.96 | 1.21 | 0.65 | 25 | 65 |
| Murder on the Orient Express | 1.67 | 1.56 | 0.10 | 0.65 | 0.74 | 46 | 92 |
| 2001: A Space Odyssey | 1.19 | 1.73 | -0.54 | 0.83 | 0.67 | 42 | 79 |
| The Shining | 1.60 | 1.58 | 0.02 | 0.81 | 0.64 | 35 | 85 |
| Titanic | 2.27 | 2.08 | 0.19 | 0.69 | 0.77 | 42 | 92 |
| Harry Potter and the Philosopher's Stone | 2.06 | 2.27 | -0.21 | 0.46 | 0.85 | 58 | 96 |
| One Piece | 2.92 | 2.52 | 0.40 | 0.73 | 0.71 | 46 | 81 |

## Per ingredient (across the works)

Sorted by bias, most under-rated by Claude first. Spearman is across works; it is nan when one side gives every work the same score.

| Ingredient | Family | Claude mean | Site mean | Bias | Mean abs diff | Spearman |
|---|---|---|---|---|---|---|
| Moral praise | Cooperation | 1.86 | 3.21 | -1.36 | 1.36 | 0.80 |
| Resource foraging | Self | 0.93 | 1.86 | -0.93 | 1.21 | 0.19 |
| Moral blame | Cooperation | 2.79 | 3.57 | -0.79 | 0.79 | 0.32 |
| Pride | Cooperation | 2.64 | 3.36 | -0.71 | 0.71 | 0.62 |
| Resource accumulation | Self | 1.71 | 2.36 | -0.64 | 0.79 | 0.61 |
| Affiliation | Cooperation | 2.14 | 2.79 | -0.64 | 1.36 | 0.39 |
| Fear of aggressors | Threats | 2.79 | 3.36 | -0.57 | 0.71 | 0.69 |
| Shame | Cooperation | 2.43 | 2.93 | -0.50 | 0.79 | 0.65 |
| Envy | Competition | 1.64 | 2.14 | -0.50 | 0.64 | 0.84 |
| Feeling cold / hot | Self | 1.57 | 2.00 | -0.43 | 0.43 | 0.86 |
| Moral pride | Cooperation | 2.36 | 2.79 | -0.43 | 0.71 | 0.76 |
| Anger | Competition | 2.64 | 3.07 | -0.43 | 0.71 | 0.67 |
| Sleepiness | Self | 1.64 | 2.00 | -0.36 | 0.50 | 0.76 |
| Skill acquisition | Self | 2.07 | 2.43 | -0.36 | 0.79 | 0.65 |
| Reasoning | Cooperation | 2.29 | 2.64 | -0.36 | 0.93 | 0.61 |
| Coalitional affiliation | Cooperation | 2.64 | 3.00 | -0.36 | 0.79 | 0.58 |
| Parental investment | Kin | 1.86 | 2.14 | -0.29 | 1.14 | 0.45 |
| Pain aversion | Threats | 2.64 | 2.86 | -0.21 | 0.64 | 0.70 |
| Embarrassment | Cooperation | 1.79 | 2.00 | -0.21 | 0.64 | 0.63 |
| Parental care | Kin | 2.50 | 2.71 | -0.21 | 1.07 | 0.34 |
| Fear of heights | Threats | 1.07 | 1.21 | -0.14 | 0.43 | 0.85 |
| Guilt | Cooperation | 2.21 | 2.36 | -0.14 | 0.57 | 0.64 |
| Long-term love | Mating | 1.79 | 1.93 | -0.14 | 1.43 | 0.28 |
| Explanation-seeking | Self | 2.79 | 2.86 | -0.07 | 0.79 | 0.53 |
| Mental time travel | Self | 2.64 | 2.71 | -0.07 | 0.50 | 0.55 |
| Sadness | Cooperation | 2.93 | 3.00 | -0.07 | 0.64 | 0.64 |
| Status-seeking | Competition | 2.79 | 2.86 | -0.07 | 0.50 | 0.82 |
| Curiosity | Self | 2.36 | 2.36 | 0.00 | 0.71 | 0.72 |
| Warmth | Cooperation | 2.50 | 2.50 | 0.00 | 0.57 | 0.86 |
| Sexual jealousy | Mating | 1.21 | 1.21 | 0.00 | 0.43 | 0.85 |
| Revenge | Cooperation | 2.29 | 2.21 | 0.07 | 0.50 | 0.84 |
| Thirst | Self | 0.86 | 0.71 | 0.14 | 0.57 | 0.56 |
| Fear of predators | Threats | 1.50 | 1.36 | 0.14 | 0.57 | 0.74 |
| Disgust | Threats | 1.93 | 1.79 | 0.14 | 1.14 | 0.24 |
| Romantic jealousy | Mating | 1.36 | 1.21 | 0.14 | 0.43 | 0.81 |
| Hunger | Self | 2.00 | 1.79 | 0.21 | 0.64 | 0.83 |
| Play | Self | 2.00 | 1.79 | 0.21 | 0.50 | 0.76 |
| Friendship | Cooperation | 2.57 | 2.36 | 0.21 | 0.36 | 0.96 |
| Hatred | Competition | 2.21 | 2.00 | 0.21 | 1.07 | 0.28 |
| Desire | Mating | 1.36 | 1.14 | 0.21 | 0.64 | 0.73 |
| Kin sexual disgust | Kin | 0.50 | 0.29 | 0.21 | 0.36 | 0.58 |
| Familial love | Kin | 3.07 | 2.79 | 0.29 | 0.57 | 0.55 |
| Forgiveness | Cooperation | 1.57 | 1.21 | 0.36 | 0.64 | 0.73 |
| Compassion | Cooperation | 2.86 | 2.43 | 0.43 | 0.86 | 0.44 |
| Humor | Cooperation | 2.14 | 1.71 | 0.43 | 0.86 | 0.72 |
| Sexual disgust | Mating | 1.50 | 1.00 | 0.50 | 0.64 | 0.77 |
| Romantic affiliation | Mating | 2.00 | 1.43 | 0.57 | 0.71 | 0.76 |
| Sexual attraction | Mating | 2.14 | 1.36 | 0.79 | 0.79 | 0.87 |

## Per family

| Family | n | Claude mean | Site mean | Bias | Mean abs diff | Pearson r |
|---|---|---|---|---|---|---|
| Self | 154 | 1.87 | 2.08 | -0.21 | 0.68 | 0.68 |
| Threats | 70 | 1.99 | 2.11 | -0.13 | 0.70 | 0.78 |
| Cooperation | 238 | 2.35 | 2.59 | -0.24 | 0.77 | 0.65 |
| Competition | 56 | 2.32 | 2.52 | -0.20 | 0.73 | 0.69 |
| Mating | 98 | 1.62 | 1.33 | 0.30 | 0.72 | 0.75 |
| Kin | 56 | 1.98 | 1.98 | 0.00 | 0.79 | 0.72 |

## Largest disagreements (3 or more points apart)

| Work | Ingredient | Claude | Site | Claude's reason |
|---|---|---|---|---|
| In Search of Lost Time | Resource foraging | 0 | 4 | No one searches for scarce resources. |
| The Metamorphosis | Affiliation | 0 | 4 | No new companions are sought; the lodgers are strangers. |
| The Metamorphosis | Resource foraging | 0 | 4 | No one searches for scarce resources. |
| 2001: A Space Odyssey | Affiliation | 0 | 3 | No new companions are sought. |
| 2001: A Space Odyssey | Moral praise | 0 | 3 | No one is celebrated for goodness. |
| Hamlet | Disgust | 3 | 0 | Something is rotten in Denmark: an unweeded garden, Yorick's skull, Polonius's stinking corpse, and ulcer and incest imagery. |
| Hamlet | Resource accumulation | 1 | 4 | Claudius gained crown and queen by murder, but wealth is not pursued in the action. |
| Murder on the Orient Express | Hatred | 3 | 0 | Every conspirator loathes Cassetti and takes satisfaction in his death. |
| The Metamorphosis | Coalitional affiliation | 1 | 4 | The family closes ranks against Gregor and the three lodgers act as a bloc. |
| The Shining | Pride | 1 | 4 | Jack insists he is a writer and takes grim pride in his caretaking contract. |
| The Song of Roland | Explanation-seeking | 1 | 4 | Charlemagne's dreams of bears and leopards foreshadow events, and the trial establishes Ganelon's guilt, but no mystery is investigated. |
| The Tale of Genji | Kin sexual disgust | 3 | 0 | Fujitsubo rejects Genji after their adultery, Tamakazura resists her adoptive father's advances, and Genji dreads suspicion of Yugiri with Murasaki. |
| The Tale of Genji | Long-term love | 4 | 1 | Genji's lifelong devotion to Murasaki and his unending longing for Fujitsubo anchor the whole narrative. |
| Titanic | Long-term love | 4 | 1 | Rose keeps Jack in her heart for the rest of her life, as the ending shows. |

## What if Claude's scale were stretched?

Two mechanical re-mappings of Claude's scores, to separate scale use from content disagreement. They are diagnostics, not a fix: the fix is to change the instructions and re-rate.

| Mapping | Mean abs diff | Exact % | Within 1 % | Bias |
|---|---|---|---|---|
| As rated | 0.73 | 42.9 | 86.5 | -0.12 |
| Nonzero scores raised by 1 (1->2, 2->3, 3->4, 4->4) | 0.88 | 42.7 | 75.1 | 0.60 |
| Scores of 2 or more raised by 1 (2->3, 3->4) | 0.83 | 43.9 | 80.1 | 0.39 |
| Each Claude level -> rounded mean site score at that level: 0->0, 1->1, 2->2, 3->3, 4->4 | 0.73 | 42.9 | 86.5 | -0.12 |

## Does Claude pick out the same top ingredients?

For each work: the site's ingredients scored 4, and how Claude scored them; then Claude's ingredients scored 4 that the site put at 2 or lower.

- **The Iliad** - site 4s: Resource accumulation (Claude 3), Fear of aggressors (Claude 4), Pain aversion (Claude 4), Pride (Claude 4), Shame (Claude 4), Moral blame (Claude 3), Moral praise (Claude 3), Revenge (Claude 4), Affiliation (Claude 2), Friendship (Claude 4), Sadness (Claude 4), Coalitional affiliation (Claude 4), Status-seeking (Claude 4), Anger (Claude 4), Long-term love (Claude 3), Parental care (Claude 3). Claude 4s the site rates 2 or lower: none.
- **The Tale of Genji** - site 4s: Pride (Claude 4), Shame (Claude 3), Moral praise (Claude 2), Sadness (Claude 4), Status-seeking (Claude 4), Romantic affiliation (Claude 4), Sexual attraction (Claude 4), Parental investment (Claude 3), Familial love (Claude 3). Claude 4s the site rates 2 or lower: Long-term love (site 1).
- **The Song of Roland** - site 4s: Explanation-seeking (Claude 1), Fear of aggressors (Claude 4), Pain aversion (Claude 4), Pride (Claude 4), Shame (Claude 4), Moral pride (Claude 4), Moral blame (Claude 4), Moral praise (Claude 3), Revenge (Claude 4), Friendship (Claude 4), Sadness (Claude 4), Coalitional affiliation (Claude 4), Status-seeking (Claude 3), Envy (Claude 2), Anger (Claude 4), Long-term love (Claude 2), Familial love (Claude 3). Claude 4s the site rates 2 or lower: none.
- **Journey to the West** - site 4s: Skill acquisition (Claude 4), Play (Claude 3), Fear of predators (Claude 4), Fear of aggressors (Claude 4), Pride (Claude 4), Moral pride (Claude 3), Moral blame (Claude 3), Moral praise (Claude 3), Forgiveness (Claude 3), Compassion (Claude 4), Affiliation (Claude 3), Friendship (Claude 4), Humor (Claude 4), Reasoning (Claude 2), Coalitional affiliation (Claude 4), Status-seeking (Claude 4), Anger (Claude 3), Desire (Claude 3). Claude 4s the site rates 2 or lower: none.
- **Hamlet** - site 4s: Explanation-seeking (Claude 4), Resource accumulation (Claude 1), Mental time travel (Claude 4), Fear of aggressors (Claude 3), Pain aversion (Claude 2), Pride (Claude 2), Shame (Claude 3), Moral pride (Claude 2), Guilt (Claude 4), Moral blame (Claude 4), Revenge (Claude 4), Affiliation (Claude 2), Friendship (Claude 3), Sadness (Claude 4), Reasoning (Claude 4), Coalitional affiliation (Claude 2), Status-seeking (Claude 3), Anger (Claude 4), Long-term love (Claude 2), Sexual disgust (Claude 4), Kin sexual disgust (Claude 3), Parental care (Claude 2), Familial love (Claude 4). Claude 4s the site rates 2 or lower: none.
- **Little Red Riding Hood** - site 4s: Hunger (Claude 3), Fear of predators (Claude 4), Fear of aggressors (Claude 2), Moral blame (Claude 2), Parental care (Claude 3). Claude 4s the site rates 2 or lower: none.
- **In Search of Lost Time** - site 4s: Curiosity (Claude 3), Resource foraging (Claude 0), Mental time travel (Claude 4), Pride (Claude 3), Warmth (Claude 3), Affiliation (Claude 4), Reasoning (Claude 3), Coalitional affiliation (Claude 3), Status-seeking (Claude 4), Envy (Claude 3), Romantic affiliation (Claude 4), Long-term love (Claude 3), Romantic jealousy (Claude 4), Sexual jealousy (Claude 4), Parental investment (Claude 2). Claude 4s the site rates 2 or lower: none.
- **The Metamorphosis** - site 4s: Hunger (Claude 3), Sleepiness (Claude 2), Resource accumulation (Claude 2), Resource foraging (Claude 0), Fear of aggressors (Claude 2), Disgust (Claude 4), Pain aversion (Claude 3), Shame (Claude 3), Guilt (Claude 2), Moral blame (Claude 2), Affiliation (Claude 0), Sadness (Claude 3), Embarrassment (Claude 3), Coalitional affiliation (Claude 1), Anger (Claude 2), Parental care (Claude 2), Parental investment (Claude 2), Familial love (Claude 4). Claude 4s the site rates 2 or lower: none.
- **Murder on the Orient Express** - site 4s: Explanation-seeking (Claude 4), Fear of aggressors (Claude 2), Moral blame (Claude 4), Moral praise (Claude 2), Revenge (Claude 4), Reasoning (Claude 4). Claude 4s the site rates 2 or lower: none.
- **2001: A Space Odyssey** - site 4s: Curiosity (Claude 4), Explanation-seeking (Claude 4), Skill acquisition (Claude 2), Mental time travel (Claude 2), Fear of predators (Claude 2), Fear of aggressors (Claude 3), Reasoning (Claude 2), Coalitional affiliation (Claude 2). Claude 4s the site rates 2 or lower: none.
- **The Shining** - site 4s: Fear of aggressors (Claude 4), Pain aversion (Claude 3), Pride (Claude 1), Shame (Claude 2), Moral blame (Claude 2), Anger (Claude 4), Hatred (Claude 3), Parental care (Claude 4). Claude 4s the site rates 2 or lower: none.
- **Titanic** - site 4s: Feeling cold / hot (Claude 4), Pain aversion (Claude 3), Moral pride (Claude 3), Warmth (Claude 3), Moral praise (Claude 2), Compassion (Claude 3), Sadness (Claude 4), Envy (Claude 2), Romantic affiliation (Claude 4), Sexual attraction (Claude 4), Romantic jealousy (Claude 4), Sexual jealousy (Claude 3). Claude 4s the site rates 2 or lower: Long-term love (site 1).
- **Harry Potter and the Philosopher's Stone** - site 4s: Curiosity (Claude 4), Explanation-seeking (Claude 4), Skill acquisition (Claude 4), Fear of aggressors (Claude 3), Moral pride (Claude 3), Warmth (Claude 3), Moral praise (Claude 3), Affiliation (Claude 4), Friendship (Claude 4), Coalitional affiliation (Claude 4), Parental care (Claude 3), Parental investment (Claude 2). Claude 4s the site rates 2 or lower: none.
- **One Piece** - site 4s: Hunger (Claude 4), Curiosity (Claude 4), Explanation-seeking (Claude 3), Skill acquisition (Claude 4), Resource foraging (Claude 2), Fear of aggressors (Claude 4), Pride (Claude 4), Moral pride (Claude 4), Warmth (Claude 4), Moral blame (Claude 3), Moral praise (Claude 3), Compassion (Claude 4), Affiliation (Claude 4), Friendship (Claude 4), Coalitional affiliation (Claude 4), Status-seeking (Claude 4), Anger (Claude 3). Claude 4s the site rates 2 or lower: Sadness (site 2), Familial love (site 2).
