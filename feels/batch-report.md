# Feels annotations of the 14 Table 2 works: batch report

Rater: claude-fable-5-1, one session, 4 October 2026, following the `feels-annotate` skill (74 feels plus 8 extra Monera rows, scores 0-4, one-sentence reasons). Character pass first, in full, then the audience pass, in full. Works annotated: 14 character, 14 audience. Unknown: none. Ambiguous: none (the 14 were treated as unambiguous, as the calibration table asks).

Files: `character/<slug>.character.feels.json`, `audience/<slug>.audience.feels.json`, and `feels-annotations.csv` (one row per work and perspective). Slugs match `calibration/<slug>.json` of the ingredients run, so the two can be joined by file name.

Limits: the ratings rest on the rater's unverified knowledge of the works, a demonstration, not data. Scores vary from run to run; for a comparison meant for publication, rate each work more than once and report the median. The audience pass rates the designed effect on an ordinary first-time audience, not any one person's reaction.


## Character perspective

Over the 74 feels of 14 works (1036 cells): 0: 22%, 1: 12%, 2: 22%, 3: 28%, 4: 15%; mean 2.01.

Fours and threes per work:

| Work | 4s | 3s | Mean of 74 |
|---|---|---|---|
| 2001: A Space Odyssey | 4 | 15 | 1.51 |
| Hamlet | 15 | 19 | 2.15 |
| Harry Potter and the Philosopher's Stone | 9 | 33 | 2.23 |
| In Search of Lost Time | 23 | 25 | 2.62 |
| Journey to the West | 12 | 28 | 2.43 |
| Little Red Riding Hood | 4 | 7 | 1.11 |
| Murder on the Orient Express | 11 | 17 | 1.76 |
| One Piece | 25 | 28 | 2.78 |
| The Iliad | 10 | 20 | 2.08 |
| The Metamorphosis | 8 | 19 | 1.84 |
| The Shining | 7 | 16 | 1.74 |
| The Song of Roland | 9 | 12 | 1.64 |
| The Tale of Genji | 10 | 18 | 2.01 |
| Titanic | 9 | 34 | 2.28 |

### Spread table

Lowest and highest score across the batch, the number of works scored 3 or 4, and the mean, for each row.

**Kingdom I: Body Maintenance**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| 1 The Need to Breathe | 0 | 3 | 3 | 1.36 |
| 2 Hungry | 0 | 4 | 5 | 1.86 |
| 3 Full | 0 | 2 | 0 | 0.64 |
| 4 Thirsty | 0 | 3 | 1 | 0.57 |
| 5 Gassy | 0 | 0 | 0 | 0.00 |
| 6 The Need to Poop | 0 | 1 | 0 | 0.07 |
| 7 The Need to Pee | 0 | 2 | 0 | 0.29 |
| 8 Sleepy | 1 | 3 | 3 | 2.00 |
| 9 Nauseous | 0 | 2 | 0 | 0.21 |
| 10 The Urge to Sneeze | 0 | 0 | 0 | 0.00 |
| 11 The Urge to Cough | 0 | 1 | 0 | 0.07 |
| 12 Dizzy | 0 | 2 | 0 | 1.21 |
| 13 Fatigued | 0 | 4 | 5 | 1.71 |
| 14 Pain | 1 | 4 | 8 | 2.64 |

**Kingdom II: External Dangers and Opportunities**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| 15 Disgusted | 0 | 4 | 8 | 2.43 |
| 16 Itchy | 0 | 2 | 0 | 0.14 |
| 17 Tickled | 0 | 0 | 0 | 0.00 |
| 18 Over-Stimulated | 0 | 3 | 1 | 0.86 |
| 19 Too Hot and Too Cold | 0 | 4 | 4 | 1.57 |
| 20 Afraid | 2 | 4 | 13 | 3.57 |
| 21 Anxious | 2 | 4 | 13 | 3.29 |
| 22 Panic | 1 | 4 | 8 | 2.57 |
| 23 Sensory Pleasures | 1 | 4 | 6 | 2.29 |
| 24 Aesthetic Pleasures | 0 | 4 | 6 | 2.14 |
| 25 Piquancy | 0 | 0 | 0 | 0.00 |
| 26 Fun and Excitement | 0 | 4 | 4 | 2.21 |
| 27 Orgasm | 0 | 2 | 0 | 0.43 |

**Kingdom III: Social World**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| 28 Love (Romantic) | 0 | 4 | 5 | 2.14 |
| 29 Love (Family) | 2 | 4 | 12 | 3.50 |
| 30 Grief | 0 | 4 | 9 | 2.93 |
| 31 Missing Someone | 0 | 4 | 5 | 2.14 |
| 32 Aroused (Sexually) | 0 | 3 | 4 | 1.50 |
| 33 Liking as a Friend | 0 | 4 | 10 | 2.93 |
| 34 Empathy | 2 | 3 | 7 | 2.50 |
| 35 Compassion | 2 | 4 | 10 | 2.86 |
| 36 Grateful | 0 | 3 | 1 | 1.43 |
| 37 Pleasure From Helping | 0 | 3 | 1 | 1.43 |
| 38 Trustful and Distrustful | 2 | 4 | 13 | 3.71 |
| 39 Depressed | 0 | 4 | 6 | 2.21 |
| 40 Angry | 1 | 4 | 10 | 3.00 |
| 41 Envious | 0 | 3 | 4 | 1.57 |
| 42 Jealous (Romantic/Sexual) | 0 | 4 | 4 | 1.36 |
| 43 Jealous (Friendship) | 0 | 3 | 1 | 0.79 |
| 44 Hatred | 1 | 4 | 11 | 3.07 |
| 45 Contempt | 0 | 4 | 10 | 2.71 |
| 46 Resentment | 0 | 4 | 12 | 2.93 |
| 47 Proud | 0 | 4 | 11 | 3.00 |
| 48 Amused | 1 | 4 | 5 | 2.21 |
| 49 A Sense of Belonging | 0 | 4 | 11 | 2.93 |
| 50 Lonely | 1 | 4 | 9 | 2.64 |
| 51 Judgy (The Moral Sense) | 1 | 4 | 12 | 3.07 |
| 52 Admiration | 0 | 4 | 9 | 2.43 |
| 53 Embarrassed | 0 | 3 | 6 | 2.00 |
| 54 Shame | 0 | 4 | 8 | 2.64 |
| 55 Guilt | 1 | 4 | 7 | 2.57 |
| 56 Sad | 0 | 4 | 9 | 2.79 |
| 57 Happy | 1 | 3 | 4 | 1.86 |
| 58 Joyful and Euphoric | 1 | 4 | 7 | 2.57 |

**Kingdom IV: Mind**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| 59 Effort | 0 | 4 | 10 | 2.64 |
| 60 Focused/In Flow | 0 | 3 | 5 | 2.00 |
| 61 Bored | 0 | 3 | 4 | 1.93 |
| 62 Distracted | 0 | 3 | 4 | 1.86 |
| 63 Impatient | 0 | 3 | 4 | 1.93 |
| 64 Curious | 0 | 4 | 11 | 3.00 |
| 65 Surprised | 2 | 4 | 11 | 3.07 |
| 66 Awe | 0 | 4 | 9 | 2.43 |
| 67 Skeptical/Doubtful | 2 | 4 | 10 | 2.93 |
| 68 The Feeling of Knowing | 0 | 4 | 3 | 1.50 |
| 69 Confused | 1 | 3 | 9 | 2.57 |
| 70 Frustrated | 1 | 4 | 11 | 2.93 |
| 71 Uncertain / Certain | 2 | 4 | 10 | 2.93 |
| 72 Understanding | 2 | 4 | 10 | 2.86 |
| 73 Inspired | 1 | 4 | 9 | 2.57 |
| 74 Satisfied | 1 | 3 | 6 | 2.29 |

**Monera (extra rows)**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| Foreboding | 2 | 4 | 13 | 3.21 |
| Nostalgia | 0 | 4 | 5 | 2.21 |
| Anticipation / Suspense | 2 | 3 | 11 | 2.79 |
| Hope | 0 | 4 | 8 | 2.43 |
| Schadenfreude | 0 | 3 | 5 | 1.93 |
| Elevation | 1 | 4 | 4 | 2.00 |
| Infatuation | 0 | 4 | 3 | 1.29 |
| Rage | 0 | 4 | 7 | 2.50 |

Rows at the same score for every work (they say nothing about how the works differ): 5 Gassy (0), 10 The Urge to Sneeze (0), 17 Tickled (0), 25 Piquancy (0).


## Audience perspective

Over the 74 feels of 14 works (1036 cells): 0: 39%, 1: 16%, 2: 20%, 3: 17%, 4: 8%; mean 1.38.

Fours and threes per work:

| Work | 4s | 3s | Mean of 74 |
|---|---|---|---|
| 2001: A Space Odyssey | 4 | 11 | 1.20 |
| Hamlet | 6 | 16 | 1.42 |
| Harry Potter and the Philosopher's Stone | 7 | 17 | 1.57 |
| In Search of Lost Time | 6 | 20 | 1.65 |
| Journey to the West | 4 | 9 | 1.23 |
| Little Red Riding Hood | 2 | 10 | 0.97 |
| Murder on the Orient Express | 10 | 6 | 1.32 |
| One Piece | 14 | 17 | 1.91 |
| The Iliad | 8 | 8 | 1.38 |
| The Metamorphosis | 3 | 12 | 1.24 |
| The Shining | 3 | 11 | 1.27 |
| The Song of Roland | 2 | 18 | 1.28 |
| The Tale of Genji | 5 | 7 | 1.27 |
| Titanic | 4 | 16 | 1.55 |

### Spread table

Lowest and highest score across the batch, the number of works scored 3 or 4, and the mean, for each row.

**Kingdom I: Body Maintenance**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| 1 The Need to Breathe | 0 | 2 | 0 | 0.50 |
| 2 Hungry | 0 | 2 | 0 | 0.50 |
| 3 Full | 0 | 0 | 0 | 0.00 |
| 4 Thirsty | 0 | 1 | 0 | 0.07 |
| 5 Gassy | 0 | 0 | 0 | 0.00 |
| 6 The Need to Poop | 0 | 0 | 0 | 0.00 |
| 7 The Need to Pee | 0 | 0 | 0 | 0.00 |
| 8 Sleepy | 0 | 1 | 0 | 0.14 |
| 9 Nauseous | 0 | 1 | 0 | 0.07 |
| 10 The Urge to Sneeze | 0 | 0 | 0 | 0.00 |
| 11 The Urge to Cough | 0 | 0 | 0 | 0.00 |
| 12 Dizzy | 0 | 2 | 0 | 0.50 |
| 13 Fatigued | 0 | 0 | 0 | 0.00 |
| 14 Pain | 0 | 2 | 0 | 1.29 |

**Kingdom II: External Dangers and Opportunities**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| 15 Disgusted | 0 | 4 | 2 | 1.86 |
| 16 Itchy | 0 | 1 | 0 | 0.07 |
| 17 Tickled | 0 | 0 | 0 | 0.00 |
| 18 Over-Stimulated | 0 | 3 | 1 | 0.50 |
| 19 Too Hot and Too Cold | 0 | 3 | 1 | 0.50 |
| 20 Afraid | 1 | 4 | 5 | 2.36 |
| 21 Anxious | 1 | 4 | 10 | 2.71 |
| 22 Panic | 0 | 2 | 0 | 0.79 |
| 23 Sensory Pleasures | 0 | 3 | 1 | 1.21 |
| 24 Aesthetic Pleasures | 2 | 4 | 10 | 3.07 |
| 25 Piquancy | 0 | 0 | 0 | 0.00 |
| 26 Fun and Excitement | 0 | 4 | 7 | 2.36 |
| 27 Orgasm | 0 | 0 | 0 | 0.00 |

**Kingdom III: Social World**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| 28 Love (Romantic) | 0 | 4 | 3 | 1.21 |
| 29 Love (Family) | 1 | 4 | 6 | 2.36 |
| 30 Grief | 1 | 4 | 7 | 2.57 |
| 31 Missing Someone | 0 | 3 | 2 | 1.21 |
| 32 Aroused (Sexually) | 0 | 2 | 0 | 0.50 |
| 33 Liking as a Friend | 1 | 4 | 7 | 2.57 |
| 34 Empathy | 2 | 4 | 10 | 3.07 |
| 35 Compassion | 2 | 4 | 11 | 3.14 |
| 36 Grateful | 0 | 0 | 0 | 0.00 |
| 37 Pleasure From Helping | 0 | 0 | 0 | 0.00 |
| 38 Trustful and Distrustful | 2 | 4 | 10 | 2.86 |
| 39 Depressed | 0 | 1 | 0 | 0.50 |
| 40 Angry | 1 | 3 | 2 | 1.86 |
| 41 Envious | 0 | 0 | 0 | 0.00 |
| 42 Jealous (Romantic/Sexual) | 0 | 3 | 1 | 0.36 |
| 43 Jealous (Friendship) | 0 | 0 | 0 | 0.00 |
| 44 Hatred | 0 | 3 | 3 | 1.71 |
| 45 Contempt | 0 | 3 | 3 | 1.79 |
| 46 Resentment | 0 | 4 | 6 | 2.21 |
| 47 Proud | 0 | 3 | 1 | 0.50 |
| 48 Amused | 1 | 4 | 5 | 2.36 |
| 49 A Sense of Belonging | 0 | 4 | 3 | 1.50 |
| 50 Lonely | 0 | 3 | 5 | 1.93 |
| 51 Judgy (The Moral Sense) | 1 | 4 | 12 | 3.00 |
| 52 Admiration | 1 | 4 | 10 | 2.79 |
| 53 Embarrassed | 0 | 3 | 1 | 1.29 |
| 54 Shame | 0 | 1 | 0 | 0.43 |
| 55 Guilt | 0 | 1 | 0 | 0.36 |
| 56 Sad | 1 | 4 | 8 | 2.79 |
| 57 Happy | 0 | 3 | 2 | 1.14 |
| 58 Joyful and Euphoric | 1 | 4 | 6 | 2.00 |

**Kingdom IV: Mind**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| 59 Effort | 0 | 4 | 6 | 2.00 |
| 60 Focused/In Flow | 2 | 4 | 12 | 3.14 |
| 61 Bored | 0 | 2 | 0 | 1.07 |
| 62 Distracted | 0 | 2 | 0 | 0.43 |
| 63 Impatient | 1 | 3 | 4 | 2.21 |
| 64 Curious | 2 | 4 | 11 | 3.14 |
| 65 Surprised | 1 | 4 | 8 | 2.64 |
| 66 Awe | 0 | 4 | 9 | 2.64 |
| 67 Skeptical/Doubtful | 0 | 4 | 7 | 2.21 |
| 68 The Feeling of Knowing | 1 | 4 | 4 | 1.93 |
| 69 Confused | 0 | 4 | 3 | 1.79 |
| 70 Frustrated | 2 | 3 | 4 | 2.29 |
| 71 Uncertain / Certain | 1 | 4 | 5 | 2.43 |
| 72 Understanding | 2 | 4 | 8 | 2.71 |
| 73 Inspired | 0 | 3 | 4 | 2.00 |
| 74 Satisfied | 1 | 4 | 10 | 2.71 |

**Monera (extra rows)**

| Feel | Low | High | Works at 3 or 4 | Mean |
|---|---|---|---|---|
| Foreboding | 2 | 4 | 12 | 3.36 |
| Nostalgia | 0 | 4 | 4 | 1.86 |
| Anticipation / Suspense | 2 | 4 | 12 | 3.43 |
| Hope | 1 | 4 | 4 | 2.21 |
| Schadenfreude | 0 | 3 | 4 | 1.86 |
| Elevation | 1 | 4 | 5 | 2.21 |
| Infatuation | 0 | 3 | 2 | 0.79 |
| Rage | 0 | 3 | 1 | 1.14 |

Rows at the same score for every work (they say nothing about how the works differ): 3 Full (0), 5 Gassy (0), 6 The Need to Poop (0), 7 The Need to Pee (0), 10 The Urge to Sneeze (0), 11 The Urge to Cough (0), 13 Fatigued (0), 17 Tickled (0), 25 Piquancy (0), 27 Orgasm (0), 36 Grateful (0), 37 Pleasure From Helping (0), 41 Envious (0), 43 Jealous (Friendship) (0).


## Character versus audience

Feels whose two scores differ by two or more, work by work (character -> audience).

- **2001: A Space Odyssey**: 2 Hungry 2->0; 4 Thirsty 2->0; 8 Sleepy 3->1; 24 Aesthetic Pleasures 1->4; 47 Proud 3->0; 58 Joyful and Euphoric 3->1; 63 Impatient 0->2; 68 The Feeling of Knowing 0->2; Rage 2->0.
- **Hamlet**: 8 Sleepy 2->0; 15 Disgusted 4->2; 22 Panic 2->0; 23 Sensory Pleasures 2->0; 32 Aroused (Sexually) 2->0; 34 Empathy 2->4; 39 Depressed 4->1; 40 Angry 4->2; 41 Envious 2->0; 42 Jealous (Romantic/Sexual) 2->0; 44 Hatred 4->2; 45 Contempt 4->2; 47 Proud 3->0; 54 Shame 4->1; 55 Guilt 4->0; 60 Focused/In Flow 1->3; 62 Distracted 3->0; Rage 3->1.
- **Harry Potter and the Philosopher's Stone**: 3 Full 2->0; 8 Sleepy 2->0; 14 Pain 3->1; 22 Panic 3->1; 36 Grateful 2->0; 37 Pleasure From Helping 2->0; 39 Depressed 2->0; 41 Envious 3->0; 47 Proud 3->1; 54 Shame 2->0; 55 Guilt 3->0; 59 Effort 3->0; 61 Bored 2->0; 69 Confused 3->1.
- **In Search of Lost Time**: 1 The Need to Breathe 2->0; 8 Sleepy 3->1; 18 Over-Stimulated 2->0; 22 Panic 3->1; 27 Orgasm 2->0; 32 Aroused (Sexually) 3->1; 36 Grateful 2->0; 37 Pleasure From Helping 2->0; 39 Depressed 3->1; 41 Envious 3->0; 43 Jealous (Friendship) 2->0; 44 Hatred 3->1; 45 Contempt 4->2; 47 Proud 4->0; 49 A Sense of Belonging 4->1; 54 Shame 3->1; 55 Guilt 3->1; 62 Distracted 3->1; 70 Frustrated 4->2; 71 Uncertain / Certain 4->2.
- **Journey to the West**: 2 Hungry 4->1; 3 Full 2->0; 7 The Need to Pee 2->0; 8 Sleepy 2->0; 9 Nauseous 2->0; 13 Fatigued 3->0; 14 Pain 4->1; 18 Over-Stimulated 2->0; 19 Too Hot and Too Cold 3->0; 20 Afraid 4->2; 21 Anxious 3->1; 22 Panic 3->0; 23 Sensory Pleasures 3->1; 28 Love (Romantic) 2->0; 32 Aroused (Sexually) 3->0; 35 Compassion 4->2; 36 Grateful 2->0; 37 Pleasure From Helping 2->0; 39 Depressed 2->0; 40 Angry 4->2; 41 Envious 3->0; 43 Jealous (Friendship) 3->0; 44 Hatred 3->1; 47 Proud 4->0; 49 A Sense of Belonging 3->1; 54 Shame 3->0; 55 Guilt 2->0; 62 Distracted 2->0; Infatuation 2->0; Rage 3->1.
- **Little Red Riding Hood**: 2 Hungry 4->0; 3 Full 2->0; 8 Sleepy 2->0; 29 Love (Family) 4->2; 60 Focused/In Flow 0->3; 62 Distracted 3->0; 69 Confused 2->0; 73 Inspired 3->0; Foreboding 2->4; Anticipation / Suspense 2->4; Hope 0->2; Schadenfreude 1->3.
- **Murder on the Orient Express**: 8 Sleepy 3->0; 20 Afraid 3->1; 24 Aesthetic Pleasures 0->2; 26 Fun and Excitement 0->3; 29 Love (Family) 4->2; 30 Grief 4->2; 31 Missing Someone 2->0; 44 Hatred 4->2; 47 Proud 3->0; 49 A Sense of Belonging 3->1; 53 Embarrassed 3->1; 54 Shame 2->0; Nostalgia 2->0.
- **One Piece**: 1 The Need to Breathe 3->1; 2 Hungry 4->2; 3 Full 2->0; 4 Thirsty 3->1; 8 Sleepy 2->0; 13 Fatigued 4->0; 14 Pain 4->2; 19 Too Hot and Too Cold 3->1; 20 Afraid 4->2; 22 Panic 3->1; 36 Grateful 3->0; 37 Pleasure From Helping 3->0; 39 Depressed 3->1; 41 Envious 2->0; 43 Jealous (Friendship) 2->0; 47 Proud 4->2; 54 Shame 3->0; 55 Guilt 3->0; 62 Distracted 3->0.
- **The Iliad**: 2 Hungry 2->0; 8 Sleepy 2->0; 13 Fatigued 3->0; 14 Pain 4->2; 20 Afraid 4->2; 22 Panic 3->1; 24 Aesthetic Pleasures 2->4; 39 Depressed 2->0; 40 Angry 4->2; 41 Envious 2->0; 42 Jealous (Romantic/Sexual) 3->0; 44 Hatred 4->1; 46 Resentment 4->2; 47 Proud 4->1; 49 A Sense of Belonging 3->1; 54 Shame 4->1; 55 Guilt 3->0; 58 Joyful and Euphoric 3->1; Elevation 2->4; Rage 4->2.
- **The Metamorphosis**: 2 Hungry 4->1; 8 Sleepy 2->0; 12 Dizzy 2->0; 13 Fatigued 3->0; 20 Afraid 4->2; 22 Panic 3->1; 23 Sensory Pleasures 2->0; 33 Liking as a Friend 0->2; 36 Grateful 2->0; 37 Pleasure From Helping 2->0; 39 Depressed 4->1; 44 Hatred 3->1; 47 Proud 2->0; 49 A Sense of Belonging 3->1; 54 Shame 3->1; 57 Happy 2->0; 59 Effort 3->1; 60 Focused/In Flow 0->3; 61 Bored 2->0.
- **The Shining**: 8 Sleepy 2->0; 13 Fatigued 2->0; 19 Too Hot and Too Cold 4->2; 22 Panic 4->2; 24 Aesthetic Pleasures 1->3; 28 Love (Romantic) 2->0; 29 Love (Family) 4->2; 40 Angry 4->2; 45 Contempt 3->1; 46 Resentment 3->1; 47 Proud 2->0; 49 A Sense of Belonging 3->0; 54 Shame 2->0; 55 Guilt 2->0; 59 Effort 3->1; 60 Focused/In Flow 2->4; Rage 4->1.
- **The Song of Roland**: 12 Dizzy 2->0; 13 Fatigued 2->0; 22 Panic 2->0; 24 Aesthetic Pleasures 1->3; 26 Fun and Excitement 1->3; 39 Depressed 2->0; 41 Envious 2->0; 54 Shame 4->1; 55 Guilt 2->0; 63 Impatient 1->3; 64 Curious 0->2; 67 Skeptical/Doubtful 3->0.
- **The Tale of Genji**: 21 Anxious 4->2; 22 Panic 2->0; 32 Aroused (Sexually) 3->1; 36 Grateful 2->0; 37 Pleasure From Helping 2->0; 39 Depressed 3->1; 41 Envious 3->0; 42 Jealous (Romantic/Sexual) 4->2; 44 Hatred 2->0; 47 Proud 3->0; 49 A Sense of Belonging 3->1; 54 Shame 4->1; 55 Guilt 4->0; 59 Effort 1->4; 62 Distracted 2->0.
- **Titanic**: 13 Fatigued 3->0; 22 Panic 4->2; 27 Orgasm 2->0; 36 Grateful 2->0; 38 Trustful and Distrustful 4->2; 39 Depressed 3->1; 42 Jealous (Romantic/Sexual) 4->0; 47 Proud 3->0; 54 Shame 2->0; 55 Guilt 3->1; 59 Effort 3->1; 62 Distracted 2->0; 69 Confused 2->0; Rage 3->1.

### Largest mean differences between the perspectives

Higher in the audience pass:

| Feel | Character mean | Audience mean | Difference |
|---|---|---|---|
| 60 Focused/In Flow | 2.00 | 3.14 | +1.14 |
| 24 Aesthetic Pleasures | 2.14 | 3.07 | +0.93 |
| Anticipation / Suspense | 2.79 | 3.43 | +0.64 |
| 34 Empathy | 2.50 | 3.07 | +0.57 |
| 74 Satisfied | 2.29 | 2.71 | +0.43 |
| 68 The Feeling of Knowing | 1.50 | 1.93 | +0.43 |
| 52 Admiration | 2.43 | 2.79 | +0.36 |
| 63 Impatient | 1.93 | 2.21 | +0.29 |
| 35 Compassion | 2.86 | 3.14 | +0.29 |
| 66 Awe | 2.43 | 2.64 | +0.21 |

Higher in the character pass:

| Feel | Character mean | Audience mean | Difference |
|---|---|---|---|
| 47 Proud | 3.00 | 0.50 | -2.50 |
| 54 Shame | 2.64 | 0.43 | -2.21 |
| 55 Guilt | 2.57 | 0.36 | -2.21 |
| 8 Sleepy | 2.00 | 0.14 | -1.86 |
| 22 Panic | 2.57 | 0.79 | -1.79 |
| 39 Depressed | 2.21 | 0.50 | -1.71 |
| 13 Fatigued | 1.71 | 0.00 | -1.71 |
| 41 Envious | 1.57 | 0.00 | -1.57 |
| 36 Grateful | 1.43 | 0.00 | -1.43 |
| 37 Pleasure From Helping | 1.43 | 0.00 | -1.43 |

Across all 1148 cells (82 rows x 14 works), the two perspectives agree exactly on 41% and within one point on 80%.

