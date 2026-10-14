---
name: "feels-annotate"
description: "Annotate a story (film, series, novel, game, comic, play) with the 74 feels of All the Feels: identify the work, score each feel 0-4 with a one-sentence reason, report a table by Kingdom and JSON. Use whenever the user mentions All the Feels, the 74 feels, the Kingdoms, FeelsAnnotate, \"annotate with the feels\", or scoring a story on the feels. \"with ingredients\" adds the 48 motivational ingredients (companion skill motivational-ingredients) and a crosswalk; \"audience perspective\" rates what the story makes the reader feel."
---

# Annotate a story with the 74 feels

This file tells Claude how to annotate a story with the 74 feels of *All the Feels* (Rob Kurzban, Re:Writers, 2026). It is the companion to the `motivational-ingredients` skill, which annotates a story with the 48 motivational ingredients of Dubourg, Thouzeau et al. (2026). The two skills share one method, one scale, and one report shape, so their results can sit side by side.

By default this skill rates the feels only. On request it also rates the 48 ingredients and shows where the two frameworks agree and where each sees something the other does not.

## How to start

Give Claude a title. Say, for example:

- "FeelsAnnotate *The Martian*."
- "Annotate *Jaws* with the feels."
- "FeelsAnnotate *Frozen* (2013, Disney, film) with ingredients." (both frameworks)
- "FeelsAnnotate every title in `titles.csv` and save the results in this folder."

Only the title is required. A year, a creator (author, director, or studio), and a medium help only when the title is ambiguous.

Mode words:

- No mode word, or "feels only": rate the 74 feels. This is the default.
- "with ingredients", "both frameworks", "feels and motivations", "full annotation": rate the 74 feels and the 48 ingredients, and add the crosswalk (see "Combined mode" below).

Perspective words (see "Perspective" below):

- No perspective word, or "character perspective": rate the feels the characters have. This is the default, and it matches how the ingredients are rated.
- "audience perspective", "for the reader", "as experienced": rate the feels the story is built to produce in its audience.
- "both perspectives": rate both and report them side by side.

## The framework in short

*All the Feels* treats each feel as an evolved mechanism that measures something and motivates something. Every feel chapter opens with five lines: the **Problem** the feel solves, what it **Measures**, the **Quantity** it reads, the **Motivation** it produces, and its **Quality** (pleasant or unpleasant). The 74 feels are sorted into four Kingdoms, each split into Phyla: I Body Maintenance, II External Dangers and Opportunities, III Social World, and IV Mind. A fifth Kingdom, Monera, holds unnumbered feels the book examines only briefly (hope, nostalgia, schadenfreude, and others).

An annotation rates how prominent each feel is across the whole story. In the character perspective that means how much the characters experience it, or face the conditions it measures. In the audience perspective it means how much the story, by its content and by the way it is told, produces the feel in the reader or viewer.

## Step 1: Identify the work

Work from the title and any optional details.

1. If the title points to one work, or to one work that is clearly intended or by far the best known, go on to Step 2.
2. Different adaptations of the same story (a novel and its film) are one work, not an ambiguity. Rate the story as a whole unless the user names one adaptation (for example, "the 1962 film").
3. If the title could mean several distinct works with different stories (for example *Frozen*, *Crash*, *Mario*), do not choose silently. Mark the request as ambiguous. List 2 to 10 candidates with title, year, medium, and creator. Give no ratings. Ask the user to pick one or to add a year, a creator, or a medium.
4. If the title names a series, saga, or franchise whose instalments tell distinct stories (for example *Harry Potter*, *Star Wars*, *The Lord of the Rings*, *Final Fantasy*), also mark it as ambiguous. List the main instalments as candidates, oldest first, with their years (up to 9, keeping the best known). Then add the whole series as the last candidate, titled exactly "<Series title> (whole series)", with the year of the first instalment. A serialized work with no separate instalments (a manga, a television series) is one work: rate it as a whole. If the title already names one instalment, or says "whole series", do not mark it as ambiguous.
5. If you do not recognize the work with reasonable confidence, say so and give no ratings. Do not guess.

Never invent plot elements. If you are not sure an element is in the work, leave it out.

## Step 2: Rate the 74 feels

For each feel, in the order below:

1. Write one sentence of at most 35 words. Name the concrete story elements in which a character experiences the feel, or faces the conditions the feel measures. The sentence must justify the score, also when the score is 0.
2. Give one integer score from 0 to 4.

Scale (integers only):

| Score | Meaning |
|---|---|
| 0 | Absent |
| 1 | Present but negligible |
| 2 | Present and secondary |
| 3 | Present and central |
| 4 | Dominant; defines the story |

Rules for scoring:

- In the character perspective (the default), rate the characters' feels: what happens in the story. Do not rate what the story makes the audience feel, and do not rate what the genre label suggests. The audience perspective is a separate pass with its own rule; see "Perspective" below.
- A feel counts when a character has it, or when the story dwells on the conditions it measures. Three days in the desert scores Thirsty even if nobody says the word. A monster on screen scores Afraid even if the characters say nothing about fear.
- Rate the feel as the book defines it, not the everyday word. Use the Problem and Measure lines. For example: the book's Hatred answers a person who imposes ongoing costs on you; pleasure at a rival's downfall is schadenfreude, a Monera feel, not Hatred. Jealousy over a friend is Feel 43, not Feel 42. Depressed (39) is about insufficient social support; ordinary sorrow is Sad (56) or Grief (30). Fatigued (13) is exertion, not illness.
- Everyday background is 0. Characters eat a meal or sleep at night in almost every story; score Hungry or Sleepy above 0 only when the story gives them weight.
- Use the scale the way the authors of the ingredients framework use it, so the two frameworks are rated alike. A 4 means a feel that runs through the whole work. Several feels in one work can be 4, and a long work often has ten or more: in the article's Table 2, 27 percent of all cells are 4s, and *The Iliad* has sixteen. Do not ration 4s. (Calibration note, 3 October 2026: the companion skill scored 0.77 points below the authors on average while it carried the sentence "a 4 should be rare"; that sentence was removed from both skills on the same day, and the same scale rule now stands in both, word for word.)

Also write:

- One sentence (at most 30 words) that sums up the story's dominant feels.
- Eight Monera rows, scored like the 74, with the same one-sentence reason each. These are feels the book examines only briefly, included here because stories use them often: Foreboding [foreboding], Nostalgia [nostalgia], Anticipation / Suspense [anticipation-suspense], Hope [hope], Schadenfreude [schadenfreude], Elevation [elevation], Infatuation [infatuation], and Rage [rage]. Fixed rows keep the columns the same across a batch.
- One Monera line: up to five further feels, not among the 74 and not in the eight rows, that are prominent in the story. The book also names déjà vu, fear of missing out, outrage, pun pain, cuteness, and yawning. Write "none" if none applies.

## Perspective

The ingredients framework rates story content: what happens to the characters. The book's Kingdom IV feels (surprise, suspense, confusion, the feeling of knowing, satisfaction, awe) are often produced in the audience by the *form* of a story, by what the teller withholds and when, rather than by anything a character feels. A character who gasps does not surprise the reader; an author who withholds does. The two perspectives catch different things, so the skill keeps them apart.

- **Character perspective** (default). Rate what the characters experience, or the conditions they face. Comparable with the ingredients, which are rated the same way.
- **Audience perspective.** Rate what the story is built to make its audience feel, through content and form together: surprise from a withheld fact, suspense from knowing what a character does not, confusion from an unreliable narrator, awe from spectacle, amusement from a joke, the feeling of knowing when a clue almost lands, satisfaction when the plot closes. Rate the designed effect on an ordinary first-time audience, not one person's reaction, and not the genre's promise. In this perspective, body feels (Kingdom I) and most Kingdom II feels score above 0 only when the story is built to produce them (disgust in body horror, fear in horror, hunger in a famine story). Kingdom IV is where the two perspectives differ most, and the Monera rows (foreboding, suspense, nostalgia) belong here.
- **Both perspectives.** Do the character pass first, in full, then the audience pass, in full. Report one table with two score columns (Character, Audience) and one reason column per perspective, and end with a list of feels whose two scores differ by two or more. Save two JSON blocks, one per perspective.

The `perspective` key in the JSON block records which pass a block is. Never mix the two in one block.

## The 74 feels

Format: number. Name [slug] — Problem. Measure. Motivation. The three lines are the book's own, condensed. If a line here ever disagrees with the book, the book wins.

### Kingdom I: Body Maintenance

#### Phylum: Inputs and Outputs

1. The Need to Breathe [need-to-breathe] — Problem: Supplying oxygen for the reaction that produces usable energy. Measure: Current need for oxygen. Motivation: Inhale air/oxygen.
2. Hungry [hungry] — Problem: Supplying calories for metabolism. Measure: Current energy demands. Motivation: Eat.
3. Full [full] — Problem: Avoiding taking in too many calories. Measure: Current need for additional food. Motivation: Stop (or don't start) eating.
4. Thirsty [thirsty] — Problem: Maintaining enough water. Measure: Current need for water. Motivation: Drink water.
5. Gassy [gassy] — Problem: Expel gases that can cause harm. Measure: Urgency of expelling gases in the digestive tract. Motivation: Expel gases through the anus.
6. The Need to Poop [need-to-poop] — Problem: Expelling solid waste. Measure: Current room left at the end of the digestive tract. Motivation: Push out waste.
7. The Need to Pee [need-to-pee] — Problem: Maintaining proper amount of water (not too much). Measure: Urgency of the need to eliminate liquid waste. Motivation: Urinate.
8. Sleepy [sleepy] — Problem: Sleeping at the right time and the right amount to tidy up the brain. Measure: Current need to purge waste products, time since last sleep. Motivation: Sleep.

#### Phylum: Damage Control

9. Nauseous [nauseous] — Problem: Poison and pathogens in the digestive system. Measure: Possibility of having ingested pathogens or toxins. Motivation: Vomit.
10. The Urge to Sneeze [urge-to-sneeze] — Problem: Cleaning the airway of pathogens/toxins. Measure: Likely presence of foreign matter. Motivation: Sneeze, expelling air through the nose and mouth.
11. The Urge to Cough [urge-to-cough] — Problem: Keep the respiratory tract clear of irritants and blockages. Measure: Need to expel material from the lungs. Motivation: Cough, rapidly expelling air.
12. Dizzy [dizzy] — Problem: Avoiding an uncontrolled fall. Measure: Risk of imminent fall. Motivation: Sit or lie down.
13. Fatigued [fatigued] — Problem: Reduce risk of major system failure (heat stroke, hypoxia, hypoglycemia). Measure: Probability of physical system failures. Motivation: Reduce exercise effort.
14. Pain [pain] — Problem: Limiting damage to tissue. Measure: Current rate of damage. Motivation: Avoid damage.

### Kingdom II: External Dangers and Opportunities

#### Phylum: Danger

15. Disgusted [disgusted] — Problem: Keeping pathogens and toxins out of the body; avoiding bad decisions regarding sexual partners. Measure: Risk of contagion from pathogens or poison; risk of choosing an inappropriate sexual partner. Motivation: Avoid physical contact/ingestion, avoid sexual contact.
16. Itchy [itchy] — Problem: Defending surfaces from threats on the skin. Measure: Possibility of presence of insects, harmful chemicals. Motivation: Scratch surface, direct attention to the location.
17. Tickled [tickled] — Problem: Credibly signaling deference. Measure: Proximity of potentially malevolent but currently harmless other. Motivation: Giggle, laugh, convulse, evade.
18. Over-Stimulated [over-stimulated] — Problem: Protecting delicate sensors. Measure: Magnitude of stimulus. Motivation: Reduce stimulus on the sensor.
19. Too Hot and Too Cold [too-hot-too-cold] — Problem: Maintaining body temperature within a narrow range. Measure: Current temperature. Motivation: Various strategies to reduce the difference.
20. Afraid [afraid] — Problem: Identifying threats. Measure: Likelihood and size of threat (predators, heights, disadvantageous settings, learned dangers). Motivation: Gather information, prepare to freeze, fight, or flee.
21. Anxious [anxious] — Problem: Dealing with future threats. Measure: Size, imminence of future threat. Motivation: Ruminate on, prepare for threat.
22. Panic [panic] — Problem: Escaping a perceived desperate situation. Measure: Chance of survival without swift action. Motivation: Run, other motor movements.

#### Phylum: Opportunities

23. Sensory Pleasures [sensory-pleasures] — Problem: Identifying fitness opportunities. Measure: Varies by sense. Motivation: Seek fitness opportunities.
24. Aesthetic Pleasures [aesthetic-pleasures] — Problem: Learning about life and evaluating others' talents. Measure: Varies. Motivation: Attend to the art, in whatever form.
25. Piquancy (Spiciness) [piquancy] — Problem: Reducing pathogen risk. Measure: Anti-pathogen properties of food. Motivation: Eat well-spiced foods.
26. Fun and Excitement [fun-excitement] — Problem: Learn and practice safely, signal traits and loyalty. Measure: Size of the gain from learning, practice, signaling. Motivation: Play, ride, enjoy.
27. Orgasm [orgasm] — Problem: Get gamete to the proper place. Measure: A potentially successful reproductive attempt. Motivation: Do it again.

### Kingdom III: Social World

#### Phylum: Loved Ones

28. Love (Romantic) [love-romantic] — Problem: Attract and retain a long-term mate. Measure: Other person's value as a mate. Motivation: Try to attract a mate, send costly signals.
29. Love (Family) [love-family] — Problem: Aid close relatives. Measure: Cues to the genetic relatedness of another person. Motivation: Deliver benefits of various kinds to close relatives.
30. Grief [grief] — Problem: Learning from and adapting to a great loss. Measure: Need to learn from and adapt to a loss. Motivation: Withdraw, consider, solicit support.
31. Missing Someone [missing-someone] — Problem: Restoring lost benefits that close relationships normally supply. Measure: Benefits lost due to absence of a close other. Motivation: Restore proximity.
32. Aroused (Sexually) [aroused-sexually] — Problem: Identifying and preparing for sexual opportunities. Measure: Value of having sex with potential partner. Motivation: Increase proximity to potential mates, facilitate sexual behavior.

#### Phylum: Alliances and Cooperation

33. Liking as a Friend [liking-as-a-friend] — Problem: Build a network of allies who will support you. Measure: How much you value the other person. Motivation: Support when conflicts arise, deliver benefits, signal friendship.
34. Empathy [empathy] — Problem: Identifying those in need of aid. Measure: Extent and type of others' needs. Motivation: Choosing who to help.
35. Compassion [compassion] — Problem: Helping others in need to store future help from others. Measure: Degree of perceived need or suffering. Motivation: Altruistic behavior (caregiving, resource sharing).
36. Grateful [grateful] — Problem: Sustaining relationships with people who benefit oneself. Measure: Value of maintaining the relationship. Motivation: Signal knowledge of benefit, reciprocate.
37. Pleasure From Helping [pleasure-from-helping] — Problem: Providing benefits to others to maximize return benefits. Measure: How much target has been helped, expectation of reciprocal benefits. Motivation: Repeat the behavior.
38. Trustful and Distrustful [trustful-distrustful] — Problem: Determining if the potential benefits of cooperation outweigh the cost of making oneself vulnerable. Measure: Other person's true intentions to help/harm. Motivation: Cooperate or not, depending on measurement.
39. Depressed [depressed] — Problem: Insufficient social support. Measure: Increased need for support. Motivation: Recruit aid from social partners.

#### Phylum: Competition

40. Angry [angry] — Problem: Deter harm by others, increase how much others value you. Measure: How much (or little) others value you. Motivation: Persuade others, through threat, to increase how much they value you.
41. Envious [envious] — Problem: Identifying opportunities for improving outcomes. Measure: Outcomes of relevant others. Motivation: Improve one's standing/resources, diminish that of others.
42. Jealous—Romantic/Sexual [jealous-romantic-sexual] — Problem: Defend against threats to a romantic relationship. Measure: Magnitude of threat to one's relationship or paternity. Motivation: Increase vigilance, deter rivals, increase appeal to partner.
43. Jealous—Friendship [jealous-friendship] — Problem: Defend against threat to one's place in a friendship ranking. Measure: Magnitude of threat to the relationship. Motivation: Increase vigilance, deter rivals, increase appeal as a friend.
44. Hatred [hatred] — Problem: Deter or neutralize people who negatively impact you. Measure: Behavioral evidence another person imposes ongoing costs on you. Motivation: Avoid the hated individual and/or reduce harm from the hated individual.
45. Contempt [contempt] — Problem: Responding to people who add little value. Measure: The (low) value another person brings to social relationships. Motivation: Reduce/avoid/end social interactions.
46. Resentment [resentment] — Problem: Ensuring people get (only) those benefits to which they are entitled. Measure: Degree of violation of social contracts and norms. Motivation: Recruiting allies to secure benefits and deterring future violations.
47. Proud [proud] — Problem: Obtaining and signaling high status. Measure: The extent to which one has achieved valued goals or can exercise power in the group. Motivation: Signal achievements, repeat activities that build regard, elicit enhanced respect from others.
48. Amused [amused] — Problem: Identify others who share knowledge; signal intelligence to potential allies and mates. Measure: Identify hidden knowledge that resolves an apparent inconsistency; how cleverly the knowledge is hidden. Motivation: Signal possession of hidden key knowledge through creating or enjoying jokes, humor, etc.

#### Phylum: The Group

49. A Sense of Belonging [sense-of-belonging] — Problem: Benefits of being seen as a member of a group/coalition. Measure: Others' beliefs about one's status as a group member. Motivation: Additional efforts to influence others' beliefs about one's membership in a group.
50. Lonely [lonely] — Problem: Take precautions when social support is limited; increase social support. Measure: Others' beliefs about one's value as a relationship partner, group member, etc. Motivation: Increase vigilance to social threats, seek ways to increase one's value to others.
51. Judgy—The Moral Sense [judgy-moral-sense] — Problem: Choosing the same side as others when conflicts emerge, avoiding being on the smaller side. Measure: The "wrongness" of actions. Motivation: Side against the person that others are siding against and support punishment for the offending person.
52. Admiration [admiration] — Problem: Gain access to those with valuable skills to learn from them. Measure: Size of others' accomplishments. Motivation: Get close to target, learn from target, enhance target's reputation.
53. Embarrassed [embarrassed] — Problem: Repairing damage from missteps and avoiding appearing to intentionally behave in a socially undesirable way. Measure: Extent to which one has been observed violating or failing to live up to a norm/convention. Motivation: Signal that one knows norms, that violations were not intentional, and that one does not claim higher status than intended.
54. Shame [shame] — Problem: Minimizing or repairing damage to others' views of one's social value. Measure: The extent to which others reduce or might reduce their estimation of one's value. Motivation: Hiding/withdrawal, appeasement, and/or taking actions to raise status or signal conformity to group norms and standards.
55. Guilt [guilt] — Problem: Repairing damage one has done, especially to valued others. Measure: The extent to which one has harmed others, especially friends and allies. Motivation: Suppressing further harm, making apologies, and compensating those harmed.

#### Phylum: Moods and Benchmarks

56. Sad [sad] — Problem: React to losses or failed goals with fitness consequences. Measure: Size of the adaptive setback or problem. Motivation: Consider the best move given the circumstances, solicit aid.
57. Happy [happy] — Problem: Evaluate how one is doing overall solving adaptive problems. Measure: Current overall state on many different facets of life, both physical and social. Motivation: Choose strategic focus.
58. Joyful and Euphoric [joyful-euphoric] — Problem: Repeat successful fitness-good behaviors. Measure: Size of a large fitness gain. Motivation: Repeat actions that led to the success.

### Kingdom IV: Mind

#### Phylum: Attention

59. Effort [effort] — Problem: Whether to persist on the current task. Measure: The opportunity cost of continuing. Motivation: Switch tasks.
60. Focused/In Flow [focused-in-flow] — Problem: Allocate one's time and attention to the most productive use. Measure: Difficulty of current task and match between one's skills and the difficulty of current task. Motivation: Continue the activity.
61. Bored [bored] — Problem: Choosing among different possible tasks. Measure: Advantage of switching tasks. Motivation: Finding new task/goal.
62. Distracted [distracted] — Problem: Where best to direct one's limited attention. Measure: Fit between where one wants to attend and where one is actually attending. Motivation: Attend to what one wishes to.
63. Impatient [impatient] — Problem: Take advantage of opportunities before they disappear. Measure: Benefit of an opportunity in the future. Motivation: Ensure one gets the anticipated benefit.
64. Curious [curious] — Problem: Acquire new information when doing so is valuable. Measure: Benefit of getting information minus cost of getting it. Motivation: Seek new information.
65. Surprised [surprised] — Problem: Updating beliefs to reflect new information. Measure: Difference between expectations and observations. Motivation: Attend to unexpected information, update beliefs.
66. Awe [awe] — Problem: Learn information. Measure: Large deviations from expectations. Motivation: Attend to new information.

#### Phylum: Epistemic / Metacognitive States

67. Skeptical/Doubtful [skeptical-doubtful] — Problem: Distinguish truth from falsehoods. Measure: Likelihood something is false. Motivation: Find out more information, resist updating beliefs.
68. The Feeling of Knowing [feeling-of-knowing] — Problem: Making good decisions about spending time trying to remember. Measure: Likelihood that you will eventually remember. Motivation: Continue or end memory search.
69. Confused [confused] — Problem: Deciding whether to try to understand surprising or inconsistent information. Measure: One's understanding of new information. Motivation: Expend additional effort to understand or abandon attempt at understanding.
70. Frustrated [frustrated] — Problem: Detecting diminishing returns to effort and abandoning useless effort. Measure: The probability that a problem cannot be solved with the current method. Motivation: Desist from current strategy and either end the task or adopt a new, often more extreme, approach.
71. Uncertain / Certain [uncertain-certain] — Problem: When to stop considering and implement a choice. Measure: Likelihood that you have reached the "correct" decision or choice. Motivation: Continue to ruminate, gather information, or seek help when uncertain; implement a choice when certain.
72. Understanding [understanding] — Problem: Knowing when something has been understood. Measure: The consistency, familiarity, or fluency of new information. Motivation: Close the file and move on.
73. Inspired [inspired] — Problem: Solving problems, knowing when a problem is solved. Measure: The extent to which a new idea clearly solves a problem. Motivation: Repeat the insightful experience.
74. Satisfied [satisfied] — Problem: Knowing when a problem has been solved or a task has been completed. Measure: Likelihood a problem has been solved or a task completed. Motivation: Learn how to get to that end state, move to a new task or problem.

## Step 3: Report the result

Always give these four parts, in this order.

1. **The work.** Title, year, medium, creator. Medium is one of: movie, tv, novel, game, manga, comic, theatre, epic, tale, book, other.
2. **The perspective, the summary sentence, and the Monera line.**
3. **A table by Kingdom**, with a Phylum row between groups, and three columns: Feel, Score, Why; then a Monera group with the eight scored rows. Put the 4s and 3s in bold so the profile is easy to read. In "both perspectives" mode the table has two score columns and two reason columns.
4. **A JSON block** (JavaScript Object Notation) in the shape below, which matches the `motivational-ingredients` skill's block so the two can be compared. Keep all 74 keys, in this order.

Rules for the JSON block:

- `year` is 4 digits or an empty string.
- `creator` is names only, with no role label (for example "Nintendo", "Bong Joon-ho"), or an empty string.
- `mode` is "feels" or "feels+ingredients".
- `perspective` is "character" or "audience".
- `extra` holds the eight scored Monera rows, in the order below.
- `monera` is a list of short strings (the Monera line), or an empty list.
- If the work is unknown (`known` is false) or the title is ambiguous (`ambiguous` is true): leave every `why` empty, set every `score` to 0, and set the four `work` fields to empty strings. When ambiguous, fill `candidates`; otherwise leave it as an empty list. A candidate has the same four fields as `work`.

```json
{
  "known": true,
  "ambiguous": false,
  "candidates": [],
  "work": { "title": "", "year": "", "medium": "", "creator": "" },
  "mode": "feels",
  "perspective": "character",
  "summary": "",
  "monera": [],
  "feels": {
    "need-to-breathe": { "why": "", "score": 0 },
    "hungry": { "why": "", "score": 0 },
    "full": { "why": "", "score": 0 },
    "thirsty": { "why": "", "score": 0 },
    "gassy": { "why": "", "score": 0 },
    "need-to-poop": { "why": "", "score": 0 },
    "need-to-pee": { "why": "", "score": 0 },
    "sleepy": { "why": "", "score": 0 },
    "nauseous": { "why": "", "score": 0 },
    "urge-to-sneeze": { "why": "", "score": 0 },
    "urge-to-cough": { "why": "", "score": 0 },
    "dizzy": { "why": "", "score": 0 },
    "fatigued": { "why": "", "score": 0 },
    "pain": { "why": "", "score": 0 },
    "disgusted": { "why": "", "score": 0 },
    "itchy": { "why": "", "score": 0 },
    "tickled": { "why": "", "score": 0 },
    "over-stimulated": { "why": "", "score": 0 },
    "too-hot-too-cold": { "why": "", "score": 0 },
    "afraid": { "why": "", "score": 0 },
    "anxious": { "why": "", "score": 0 },
    "panic": { "why": "", "score": 0 },
    "sensory-pleasures": { "why": "", "score": 0 },
    "aesthetic-pleasures": { "why": "", "score": 0 },
    "piquancy": { "why": "", "score": 0 },
    "fun-excitement": { "why": "", "score": 0 },
    "orgasm": { "why": "", "score": 0 },
    "love-romantic": { "why": "", "score": 0 },
    "love-family": { "why": "", "score": 0 },
    "grief": { "why": "", "score": 0 },
    "missing-someone": { "why": "", "score": 0 },
    "aroused-sexually": { "why": "", "score": 0 },
    "liking-as-a-friend": { "why": "", "score": 0 },
    "empathy": { "why": "", "score": 0 },
    "compassion": { "why": "", "score": 0 },
    "grateful": { "why": "", "score": 0 },
    "pleasure-from-helping": { "why": "", "score": 0 },
    "trustful-distrustful": { "why": "", "score": 0 },
    "depressed": { "why": "", "score": 0 },
    "angry": { "why": "", "score": 0 },
    "envious": { "why": "", "score": 0 },
    "jealous-romantic-sexual": { "why": "", "score": 0 },
    "jealous-friendship": { "why": "", "score": 0 },
    "hatred": { "why": "", "score": 0 },
    "contempt": { "why": "", "score": 0 },
    "resentment": { "why": "", "score": 0 },
    "proud": { "why": "", "score": 0 },
    "amused": { "why": "", "score": 0 },
    "sense-of-belonging": { "why": "", "score": 0 },
    "lonely": { "why": "", "score": 0 },
    "judgy-moral-sense": { "why": "", "score": 0 },
    "admiration": { "why": "", "score": 0 },
    "embarrassed": { "why": "", "score": 0 },
    "shame": { "why": "", "score": 0 },
    "guilt": { "why": "", "score": 0 },
    "sad": { "why": "", "score": 0 },
    "happy": { "why": "", "score": 0 },
    "joyful-euphoric": { "why": "", "score": 0 },
    "effort": { "why": "", "score": 0 },
    "focused-in-flow": { "why": "", "score": 0 },
    "bored": { "why": "", "score": 0 },
    "distracted": { "why": "", "score": 0 },
    "impatient": { "why": "", "score": 0 },
    "curious": { "why": "", "score": 0 },
    "surprised": { "why": "", "score": 0 },
    "awe": { "why": "", "score": 0 },
    "skeptical-doubtful": { "why": "", "score": 0 },
    "feeling-of-knowing": { "why": "", "score": 0 },
    "confused": { "why": "", "score": 0 },
    "frustrated": { "why": "", "score": 0 },
    "uncertain-certain": { "why": "", "score": 0 },
    "understanding": { "why": "", "score": 0 },
    "inspired": { "why": "", "score": 0 },
    "satisfied": { "why": "", "score": 0 }
  },
  "extra": {
    "foreboding": { "why": "", "score": 0 },
    "nostalgia": { "why": "", "score": 0 },
    "anticipation-suspense": { "why": "", "score": 0 },
    "hope": { "why": "", "score": 0 },
    "schadenfreude": { "why": "", "score": 0 },
    "elevation": { "why": "", "score": 0 },
    "infatuation": { "why": "", "score": 0 },
    "rage": { "why": "", "score": 0 }
  }
}
```

## Combined mode (feels and ingredients)

When the user asks for both frameworks:

1. Do Steps 1 and 2 above, in the character perspective (the ingredients are rated that way, so only the character pass is comparable). If the user also asked for the audience perspective, do that pass too, but build the crosswalk from the character pass only.
2. Load the `motivational-ingredients` skill and do its Step 2 (rate the 48 ingredients) for the same work. If that skill is not available, say so and report the feels only.
3. Report, in this order: the work; both summary sentences and the Monera line; the feels table; the ingredients table; the crosswalk (below); one JSON block that adds an `ingredients` object (the 48 keys from that skill's template, in its order) after `feels`, with `mode` set to "feels+ingredients".

The crosswalk is a short section with four lists. "Nearest feel" means any of the feels listed for the ingredient in the table below; a feel is a "counterpart" if it appears anywhere in that table.

- **Agreement.** Ingredients scored 3 or 4 with at least one nearest feel also scored 3 or 4.
- **What the feels add.** Feels scored 3 or 4 that are no ingredient's nearest feel. The eight Monera rows count here too.
- **What the ingredients add.** Ingredients scored 3 or 4 whose nearest feel is "—" or whose nearest feels are all scored 0 or 1.
- **Disagreements.** Ingredient and nearest-feel pairs whose scores differ by two or more, in either direction, with a few words on why (a goal named on one side and the feeling of its lack on the other, as with affiliation and lonely; a definition that differs, as with hatred).

Nearest feel for each ingredient. This is a first-pass mapping; edit it as needed.

| Ingredient | Nearest feel(s) |
|---|---|
| hunger | hungry |
| thirst | thirsty |
| feeling-cold-hot | too-hot-too-cold |
| sleepiness | sleepy, fatigued |
| curiosity | curious |
| explanation-seeking | curious, confused, understanding, feeling-of-knowing |
| skill-acquisition | fun-excitement, focused-in-flow |
| play | fun-excitement |
| resource-accumulation | — |
| resource-foraging | — |
| mental-time-travel | — |
| fear-of-predators | afraid, panic |
| fear-of-aggressors | afraid, anxious, panic |
| fear-of-heights | afraid, dizzy |
| disgust | disgusted, nauseous |
| pain-aversion | pain |
| pride | proud |
| shame | shame |
| moral-pride | proud (partial) |
| guilt | guilt |
| warmth | compassion, liking-as-a-friend, grateful |
| moral-blame | judgy-moral-sense, resentment |
| moral-praise | admiration |
| revenge | angry, hatred, resentment |
| forgiveness | — |
| compassion | compassion, empathy |
| affiliation | liking-as-a-friend, sense-of-belonging, lonely (the goal on their side, the feeling of its lack on the book's) |
| friendship | liking-as-a-friend |
| sadness | sad, grief, missing-someone, depressed |
| humor | amused |
| embarrassment | embarrassed |
| reasoning | skeptical-doubtful, uncertain-certain |
| coalitional-affiliation | sense-of-belonging |
| status-seeking | proud, admiration, envious |
| envy | envious |
| anger | angry |
| hatred | hatred, contempt (the book's Hatred answers ongoing costs, not a rival's downfall) |
| romantic-affiliation | love-romantic |
| sexual-attraction | aroused-sexually |
| long-term-love | love-romantic |
| desire | aroused-sexually, orgasm |
| romantic-jealousy | jealous-romantic-sexual |
| sexual-jealousy | jealous-romantic-sexual |
| sexual-disgust | disgusted |
| kin-sexual-disgust | disgusted |
| parental-care | love-family |
| parental-investment | love-family |
| familial-love | love-family |

## Saving results (when asked, or when a folder is given)

- Save one JSON file per story and perspective, named `<title-slug>-<year>.<perspective>.feels.json` (for example `jaws-1975.character.feels.json`), with the block above plus two extra keys: `model` (the Claude model that did the rating) and `date` (today, YYYY-MM-DD).
- Keep one spreadsheet, `feels-annotations.csv` (comma-separated values), with one row per story and perspective. Columns: title, year, medium, creator, model, date, mode, perspective, summary, monera (the list joined with "; "), then the 74 slugs in order and the 8 extra slugs in order, each holding the score. Add new rows; do not add a title, year, and perspective that is already there.
- In combined mode, also save the ingredients result the way the `motivational-ingredients` skill says (its own JSON file and `annotations.csv`), so that file stays comparable with the site's.

## Batch mode

When the user gives a list of titles (in a text file, a comma-separated values file, or a spreadsheet), annotate each title in turn with the rules above. If a title is ambiguous, do not guess: note its candidates in the report and go on to the next title, unless the user said to take the best-known work. If a title is unknown, note that and go on. End with a short report: how many titles were annotated, which were unknown, and which were ambiguous. Then a spread table: for each of the 74 feels and the 8 extra rows, the lowest and highest score across the batch and the number of works scored 3 or 4. A row that sits at the same score for every work tells the reader nothing about how the works differ, and the report should say which rows those are.

## Limits to state when you report

- The ratings rest on Claude's unverified knowledge of the work: a demonstration, not data. Scores vary from run to run; for a comparison you mean to publish, rate each work more than once and report the median.
- The companion skill `motivational-ingredients` was calibrated against the article's author-verified Table 2 on 3 October 2026 (rank correlation 0.68 before the scale fix; ten social-evaluation ingredients read more narrowly than the authors read them). That rater is this rater. For a comparison between the two frameworks, use scores from the same instrument on both sides (this skill and the companion skill, same rules, same scale), and show the authors' verified scores beside them as the reference, never in place of the companion skill's scores.
- Works released after Claude's knowledge cutoff cannot be rated.
- The feel definitions here are the book's five-line chapter openers, condensed to three. The book is the authority.
- The crosswalk between the two frameworks is a first-pass mapping made for this skill, not a claim by either set of authors.

## References

- Kurzban, R. (2026). *All the Feels*. Re:Writers. https://allthefeelsbook.com
- Dubourg, E., Thouzeau, V., et al. (2026). The Motivational-Ingredient Framework. *Psychological Review*. See the `motivational-ingredients` skill and https://motivational-ingredients.com.