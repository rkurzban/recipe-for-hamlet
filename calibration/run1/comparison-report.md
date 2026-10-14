# Calibration: Claude vs. author-verified Table 2 scores

14 works x 48 ingredients = 672 score pairs. Differences are Claude minus site (positive = Claude higher).

## Overall

- Mean score, Claude: 1.41; site: 2.18; mean difference (bias): -0.77
- Mean absolute difference: 0.99 points
- Exact agreement: 31.7%; within 1 point: 75.6%; off by 3 or more: 38 pairs
- Pearson r: 0.68; Spearman rho: 0.68; quadratic weighted kappa: 0.55

Score distribution (count of each score across all pairs):

| Score | Claude | Site |
|---|---|---|
| 0 | 166 | 123 |
| 1 | 201 | 120 |
| 2 | 182 | 124 |
| 3 | 107 | 121 |
| 4 | 16 | 184 |

Confusion matrix (rows = site score, columns = Claude score):

| site \ Claude | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 86 | 32 | 5 | 0 | 0 |
| 1 | 42 | 52 | 24 | 2 | 0 |
| 2 | 24 | 56 | 39 | 5 | 0 |
| 3 | 8 | 37 | 56 | 20 | 0 |
| 4 | 6 | 24 | 58 | 80 | 16 |

Claude's mean score for each site score (how far Claude sits below or above the authors at each level):

| Site score | n | Claude mean |
|---|---|---|
| 0 | 123 | 0.34 |
| 1 | 120 | 0.88 |
| 2 | 124 | 1.20 |
| 3 | 121 | 1.73 |
| 4 | 184 | 2.41 |

## Per work

| Work | Claude mean | Site mean | Bias | Mean abs diff | Spearman | Exact % | Within 1 % |
|---|---|---|---|---|---|---|---|
| The Iliad | 1.69 | 2.48 | -0.79 | 1.00 | 0.69 | 27 | 75 |
| The Tale of Genji | 1.69 | 2.19 | -0.50 | 0.79 | 0.69 | 38 | 85 |
| The Song of Roland | 1.19 | 2.46 | -1.27 | 1.31 | 0.75 | 17 | 69 |
| Journey to the West | 1.85 | 2.88 | -1.02 | 1.15 | 0.58 | 19 | 69 |
| Hamlet | 1.52 | 2.88 | -1.35 | 1.48 | 0.57 | 15 | 54 |
| Little Red Riding Hood | 0.75 | 1.12 | -0.38 | 0.75 | 0.51 | 48 | 81 |
| In Search of Lost Time | 1.79 | 2.42 | -0.62 | 0.79 | 0.72 | 42 | 83 |
| The Metamorphosis | 1.08 | 2.40 | -1.31 | 1.52 | 0.53 | 17 | 56 |
| Murder on the Orient Express | 0.98 | 1.56 | -0.58 | 0.71 | 0.73 | 52 | 79 |
| 2001: A Space Odyssey | 0.79 | 1.73 | -0.94 | 1.06 | 0.65 | 35 | 67 |
| The Shining | 1.19 | 1.58 | -0.40 | 0.81 | 0.68 | 42 | 79 |
| Titanic | 1.48 | 2.08 | -0.60 | 0.98 | 0.63 | 31 | 75 |
| Harry Potter and the Philosopher's Stone | 1.65 | 2.27 | -0.62 | 0.75 | 0.80 | 38 | 90 |
| One Piece | 2.15 | 2.52 | -0.38 | 0.79 | 0.82 | 25 | 96 |

## Per ingredient (across the works)

Sorted by bias, most under-rated by Claude first. Spearman is across works; it is nan when one side gives every work the same score.

| Ingredient | Family | Claude mean | Site mean | Bias | Mean abs diff | Spearman |
|---|---|---|---|---|---|---|
| Moral praise | Cooperation | 1.14 | 3.21 | -2.07 | 2.07 | 0.78 |
| Moral blame | Cooperation | 2.00 | 3.57 | -1.57 | 1.57 | 0.43 |
| Affiliation | Cooperation | 1.21 | 2.79 | -1.57 | 1.86 | 0.25 |
| Pride | Cooperation | 1.93 | 3.36 | -1.43 | 1.43 | 0.58 |
| Moral pride | Cooperation | 1.43 | 2.79 | -1.36 | 1.36 | 0.75 |
| Reasoning | Cooperation | 1.29 | 2.64 | -1.36 | 1.50 | 0.56 |
| Skill acquisition | Self | 1.14 | 2.43 | -1.29 | 1.29 | 0.84 |
| Shame | Cooperation | 1.64 | 2.93 | -1.29 | 1.29 | 0.77 |
| Envy | Competition | 0.86 | 2.14 | -1.29 | 1.29 | 0.80 |
| Coalitional affiliation | Cooperation | 1.79 | 3.00 | -1.21 | 1.21 | 0.61 |
| Resource foraging | Self | 0.71 | 1.86 | -1.14 | 1.43 | 0.17 |
| Pain aversion | Threats | 1.71 | 2.86 | -1.14 | 1.29 | 0.66 |
| Feeling cold / hot | Self | 0.93 | 2.00 | -1.07 | 1.07 | 0.82 |
| Resource accumulation | Self | 1.29 | 2.36 | -1.07 | 1.21 | 0.53 |
| Parental investment | Kin | 1.07 | 2.14 | -1.07 | 1.36 | 0.32 |
| Sleepiness | Self | 1.00 | 2.00 | -1.00 | 1.14 | 0.63 |
| Embarrassment | Cooperation | 1.00 | 2.00 | -1.00 | 1.00 | 0.54 |
| Status-seeking | Competition | 1.86 | 2.86 | -1.00 | 1.00 | 0.88 |
| Anger | Competition | 2.07 | 3.07 | -1.00 | 1.00 | 0.80 |
| Parental care | Kin | 1.71 | 2.71 | -1.00 | 1.29 | 0.45 |
| Fear of aggressors | Threats | 2.43 | 3.36 | -0.93 | 1.07 | 0.60 |
| Mental time travel | Self | 1.86 | 2.71 | -0.86 | 1.00 | 0.45 |
| Guilt | Cooperation | 1.57 | 2.36 | -0.79 | 0.93 | 0.77 |
| Long-term love | Mating | 1.14 | 1.93 | -0.79 | 1.50 | 0.26 |
| Sadness | Cooperation | 2.29 | 3.00 | -0.71 | 0.86 | 0.77 |
| Curiosity | Self | 1.71 | 2.36 | -0.64 | 0.93 | 0.67 |
| Explanation-seeking | Self | 2.21 | 2.86 | -0.64 | 0.93 | 0.50 |
| Disgust | Threats | 1.14 | 1.79 | -0.64 | 1.21 | 0.22 |
| Revenge | Cooperation | 1.57 | 2.21 | -0.64 | 0.64 | 0.83 |
| Fear of heights | Threats | 0.64 | 1.21 | -0.57 | 0.86 | 0.57 |
| Play | Self | 1.29 | 1.79 | -0.50 | 0.79 | 0.58 |
| Warmth | Cooperation | 2.00 | 2.50 | -0.50 | 0.93 | 0.72 |
| Compassion | Cooperation | 1.93 | 2.43 | -0.50 | 0.79 | 0.38 |
| Hatred | Competition | 1.50 | 2.00 | -0.50 | 1.07 | 0.41 |
| Friendship | Cooperation | 1.93 | 2.36 | -0.43 | 0.43 | 0.95 |
| Sexual jealousy | Mating | 0.79 | 1.21 | -0.43 | 0.57 | 0.90 |
| Familial love | Kin | 2.36 | 2.79 | -0.43 | 0.71 | 0.38 |
| Forgiveness | Cooperation | 0.86 | 1.21 | -0.36 | 0.64 | 0.63 |
| Hunger | Self | 1.50 | 1.79 | -0.29 | 0.57 | 0.83 |
| Thirst | Self | 0.43 | 0.71 | -0.29 | 0.43 | 0.78 |
| Desire | Mating | 0.86 | 1.14 | -0.29 | 0.57 | 0.75 |
| Romantic jealousy | Mating | 1.00 | 1.21 | -0.21 | 0.50 | 0.79 |
| Humor | Cooperation | 1.57 | 1.71 | -0.14 | 0.57 | 0.77 |
| Fear of predators | Threats | 1.36 | 1.36 | 0.00 | 0.57 | 0.82 |
| Romantic affiliation | Mating | 1.43 | 1.43 | 0.00 | 0.43 | 0.86 |
| Sexual disgust | Mating | 1.00 | 1.00 | 0.00 | 0.57 | 0.83 |
| Kin sexual disgust | Kin | 0.29 | 0.29 | 0.00 | 0.29 | 0.68 |
| Sexual attraction | Mating | 1.43 | 1.36 | 0.07 | 0.64 | 0.85 |

## Per family

| Family | n | Claude mean | Site mean | Bias | Mean abs diff | Pearson r |
|---|---|---|---|---|---|---|
| Self | 154 | 1.28 | 2.08 | -0.80 | 0.98 | 0.64 |
| Threats | 70 | 1.46 | 2.11 | -0.66 | 1.00 | 0.70 |
| Cooperation | 238 | 1.60 | 2.59 | -1.00 | 1.12 | 0.63 |
| Competition | 56 | 1.57 | 2.52 | -0.95 | 1.09 | 0.71 |
| Mating | 98 | 1.09 | 1.33 | -0.23 | 0.68 | 0.76 |
| Kin | 56 | 1.36 | 1.98 | -0.62 | 0.91 | 0.67 |

## Largest disagreements (3 or more points apart)

| Work | Ingredient | Claude | Site | Claude's reason |
|---|---|---|---|---|
| Hamlet | Affiliation | 0 | 4 | No one seeks new companions. |
| In Search of Lost Time | Resource foraging | 0 | 4 | No one searches for resources. |
| The Metamorphosis | Affiliation | 0 | 4 | No one seeks companions. |
| The Metamorphosis | Coalitional affiliation | 0 | 4 | No groups form. |
| The Metamorphosis | Resource foraging | 0 | 4 | No one searches for resources. |
| The Song of Roland | Explanation-seeking | 0 | 4 | Charlemagne's dreams foreshadow treachery, but no mystery is investigated. |
| 2001: A Space Odyssey | Affiliation | 0 | 3 | No one seeks companions. |
| 2001: A Space Odyssey | Mental time travel | 1 | 4 | Bowman and Poole plan how to handle HAL, and the mission's secret purpose is planned on Earth. |
| 2001: A Space Odyssey | Moral praise | 0 | 3 | No one is celebrated for goodness. |
| 2001: A Space Odyssey | Reasoning | 1 | 4 | Bowman and Poole argue over HAL's reliability inside the pod. |
| Hamlet | Coalitional affiliation | 1 | 4 | Denmark faces Norway and Fortinbras, but group identity is background. |
| Hamlet | Long-term love | 1 | 4 | The ghost recalls his devoted marriage to Gertrude, which her remarriage betrays. |
| Hamlet | Moral pride | 1 | 4 | Horatio's loyalty and Hamlet's refusal to act without proof touch on principle, but at little cost. |
| Hamlet | Pain aversion | 1 | 4 | Stabbings and poisonings end the play, but bodily suffering is not dwelt on. |
| Hamlet | Pride | 1 | 4 | Laertes's fencing reputation is praised, but achievement and recognition are minor. |
| Hamlet | Resource accumulation | 1 | 4 | Claudius has gained the crown and queen, but wealth is not pursued. |
| Harry Potter and the Philosopher's Stone | Parental investment | 1 | 4 | Hagrid and Dumbledore guide and teach Harry as surrogate parents. |
| Journey to the West | Reasoning | 1 | 4 | Monkey talks his way past demons and argues with Heaven's officials, but debate is incidental. |
| Little Red Riding Hood | Fear of aggressors | 1 | 4 | The threat is a beast, not a human attacker; the hunter's killing of the wolf is the only human violence. |
| Little Red Riding Hood | Moral blame | 1 | 4 | The tale condemns the wolf's deceit, and Perrault's moral warns against smooth-tongued wolves. |
| Murder on the Orient Express | Moral praise | 1 | 4 | No one is celebrated for goodness. |
| The Iliad | Affiliation | 1 | 4 | Diomedes and Glaucus exchange armor as guest-friends, but seeking new companions is not a motive in the poem. |
| The Metamorphosis | Fear of heights | 0 | 3 | No heights appear. |
| The Metamorphosis | Moral blame | 1 | 4 | The chief clerk reproaches Gregor's absence, and Grete finally judges that the creature must go. |
| The Metamorphosis | Parental care | 1 | 4 | The mother tries to protect Gregor from the father, while the parents otherwise leave him to Grete. |
| The Metamorphosis | Parental investment | 1 | 4 | Gregor had planned to pay for Grete's conservatory studies. |
| The Metamorphosis | Reasoning | 0 | 3 | No argument or debate occurs. |
| The Metamorphosis | Sleepiness | 1 | 4 | Gregor is worn by sleepless nights and his new body's torpor, a minor strand. |
| The Shining | Pride | 1 | 4 | Jack's writing ambitions and his boast of the caretaker's job are hollow. |
| The Song of Roland | Affiliation | 0 | 3 | No one seeks new companions. |
| The Song of Roland | Disgust | 0 | 3 | No rot, disease, or contamination threatens a character. |
| The Song of Roland | Embarrassment | 0 | 3 | No social embarrassment occurs. |
| The Song of Roland | Envy | 1 | 4 | Ganelon resents Roland's favor and wealth, a seed of the betrayal. |
| The Song of Roland | Long-term love | 1 | 4 | Aude dies on hearing of Roland's death, a single scene of devoted commitment. |
| The Song of Roland | Parental care | 0 | 3 | No child is protected. |
| The Tale of Genji | Moral praise | 1 | 4 | Genji is praised for grace and generosity, though more for beauty and talent than for goodness. |
| Titanic | Envy | 1 | 4 | Cal cannot bear that Rose prefers a penniless artist, a note of envy. |
| Titanic | Moral praise | 1 | 4 | Old Rose honors Jack as the man who saved her in every way. |

## What if Claude's scale were stretched?

Two mechanical re-mappings of Claude's scores, to separate scale use from content disagreement. They are diagnostics, not a fix: the fix is to change the instructions and re-rate.

| Mapping | Mean abs diff | Exact % | Within 1 % | Bias |
|---|---|---|---|---|
| As rated | 0.99 | 31.7 | 75.6 | -0.77 |
| Nonzero scores raised by 1 (1->2, 2->3, 3->4, 4->4) | 0.80 | 43.8 | 80.7 | -0.04 |
| Scores of 2 or more raised by 1 (2->3, 3->4) | 0.85 | 43.2 | 79.9 | -0.34 |
| Each Claude level -> rounded mean site score at that level: 0->1, 1->2, 2->3, 3->4, 4->4 | 0.81 | 37.2 | 84.2 | 0.21 |

## Does Claude pick out the same top ingredients?

For each work: the site's ingredients scored 4, and how Claude scored them; then Claude's ingredients scored 4 that the site put at 2 or lower.

- **The Iliad** - site 4s: Resource accumulation (Claude 2), Fear of aggressors (Claude 3), Pain aversion (Claude 3), Pride (Claude 3), Shame (Claude 2), Moral blame (Claude 2), Moral praise (Claude 2), Revenge (Claude 3), Affiliation (Claude 1), Friendship (Claude 3), Sadness (Claude 3), Coalitional affiliation (Claude 3), Status-seeking (Claude 3), Anger (Claude 4), Long-term love (Claude 2), Parental care (Claude 2). Claude 4s the site rates 2 or lower: none.
- **The Tale of Genji** - site 4s: Pride (Claude 3), Shame (Claude 3), Moral praise (Claude 1), Sadness (Claude 4), Status-seeking (Claude 3), Romantic affiliation (Claude 4), Sexual attraction (Claude 3), Parental investment (Claude 2), Familial love (Claude 2). Claude 4s the site rates 2 or lower: none.
- **The Song of Roland** - site 4s: Explanation-seeking (Claude 0), Fear of aggressors (Claude 4), Pain aversion (Claude 3), Pride (Claude 3), Shame (Claude 3), Moral pride (Claude 3), Moral blame (Claude 3), Moral praise (Claude 2), Revenge (Claude 3), Friendship (Claude 3), Sadness (Claude 3), Coalitional affiliation (Claude 3), Status-seeking (Claude 2), Envy (Claude 1), Anger (Claude 3), Long-term love (Claude 1), Familial love (Claude 2). Claude 4s the site rates 2 or lower: none.
- **Journey to the West** - site 4s: Skill acquisition (Claude 2), Play (Claude 2), Fear of predators (Claude 4), Fear of aggressors (Claude 3), Pride (Claude 3), Moral pride (Claude 2), Moral blame (Claude 2), Moral praise (Claude 2), Forgiveness (Claude 2), Compassion (Claude 2), Affiliation (Claude 2), Friendship (Claude 3), Humor (Claude 3), Reasoning (Claude 1), Coalitional affiliation (Claude 2), Status-seeking (Claude 3), Anger (Claude 3), Desire (Claude 2). Claude 4s the site rates 2 or lower: none.
- **Hamlet** - site 4s: Explanation-seeking (Claude 3), Resource accumulation (Claude 1), Mental time travel (Claude 3), Fear of aggressors (Claude 2), Pain aversion (Claude 1), Pride (Claude 1), Shame (Claude 2), Moral pride (Claude 1), Guilt (Claude 3), Moral blame (Claude 3), Revenge (Claude 4), Affiliation (Claude 0), Friendship (Claude 2), Sadness (Claude 3), Reasoning (Claude 2), Coalitional affiliation (Claude 1), Status-seeking (Claude 2), Anger (Claude 3), Long-term love (Claude 1), Sexual disgust (Claude 3), Kin sexual disgust (Claude 2), Parental care (Claude 2), Familial love (Claude 3). Claude 4s the site rates 2 or lower: none.
- **Little Red Riding Hood** - site 4s: Hunger (Claude 2), Fear of predators (Claude 4), Fear of aggressors (Claude 1), Moral blame (Claude 1), Parental care (Claude 2). Claude 4s the site rates 2 or lower: none.
- **In Search of Lost Time** - site 4s: Curiosity (Claude 2), Resource foraging (Claude 0), Mental time travel (Claude 4), Pride (Claude 2), Warmth (Claude 3), Affiliation (Claude 3), Reasoning (Claude 2), Coalitional affiliation (Claude 3), Status-seeking (Claude 3), Envy (Claude 2), Romantic affiliation (Claude 3), Long-term love (Claude 2), Romantic jealousy (Claude 3), Sexual jealousy (Claude 3), Parental investment (Claude 2). Claude 4s the site rates 2 or lower: none.
- **The Metamorphosis** - site 4s: Hunger (Claude 3), Sleepiness (Claude 1), Resource accumulation (Claude 2), Resource foraging (Claude 0), Fear of aggressors (Claude 2), Disgust (Claude 4), Pain aversion (Claude 2), Shame (Claude 3), Guilt (Claude 2), Moral blame (Claude 1), Affiliation (Claude 0), Sadness (Claude 3), Embarrassment (Claude 2), Coalitional affiliation (Claude 0), Anger (Claude 2), Parental care (Claude 1), Parental investment (Claude 1), Familial love (Claude 3). Claude 4s the site rates 2 or lower: none.
- **Murder on the Orient Express** - site 4s: Explanation-seeking (Claude 4), Fear of aggressors (Claude 2), Moral blame (Claude 3), Moral praise (Claude 1), Revenge (Claude 3), Reasoning (Claude 3). Claude 4s the site rates 2 or lower: none.
- **2001: A Space Odyssey** - site 4s: Curiosity (Claude 4), Explanation-seeking (Claude 3), Skill acquisition (Claude 2), Mental time travel (Claude 1), Fear of predators (Claude 2), Fear of aggressors (Claude 3), Reasoning (Claude 1), Coalitional affiliation (Claude 2). Claude 4s the site rates 2 or lower: none.
- **The Shining** - site 4s: Fear of aggressors (Claude 4), Pain aversion (Claude 2), Pride (Claude 1), Shame (Claude 2), Moral blame (Claude 2), Anger (Claude 3), Hatred (Claude 2), Parental care (Claude 3). Claude 4s the site rates 2 or lower: none.
- **Titanic** - site 4s: Feeling cold / hot (Claude 3), Pain aversion (Claude 2), Moral pride (Claude 2), Warmth (Claude 2), Moral praise (Claude 1), Compassion (Claude 2), Sadness (Claude 3), Envy (Claude 1), Romantic affiliation (Claude 4), Sexual attraction (Claude 3), Romantic jealousy (Claude 3), Sexual jealousy (Claude 2). Claude 4s the site rates 2 or lower: none.
- **Harry Potter and the Philosopher's Stone** - site 4s: Curiosity (Claude 3), Explanation-seeking (Claude 3), Skill acquisition (Claude 3), Fear of aggressors (Claude 3), Moral pride (Claude 2), Warmth (Claude 3), Moral praise (Claude 2), Affiliation (Claude 3), Friendship (Claude 4), Coalitional affiliation (Claude 3), Parental care (Claude 3), Parental investment (Claude 1). Claude 4s the site rates 2 or lower: none.
- **One Piece** - site 4s: Hunger (Claude 3), Curiosity (Claude 4), Explanation-seeking (Claude 3), Skill acquisition (Claude 3), Resource foraging (Claude 3), Fear of aggressors (Claude 3), Pride (Claude 3), Moral pride (Claude 3), Warmth (Claude 3), Moral blame (Claude 3), Moral praise (Claude 2), Compassion (Claude 3), Affiliation (Claude 3), Friendship (Claude 4), Coalitional affiliation (Claude 3), Status-seeking (Claude 3), Anger (Claude 3). Claude 4s the site rates 2 or lower: none.
