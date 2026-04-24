# Voice bootstrap

Use this when `recall` for an author's voice returns nothing, or returns only weak signal (one stale memory, no approved posts, no phrase patterns). Without voice grounding, drafts will read like anyone and be dropped by editors.

## When to bootstrap

- No voice memories exist for the author.
- Voice memories exist but cover only one dimension (e.g. a banned phrase and nothing else).
- The author is new to the system or recently switched context enough that old voice is stale.

Do not bootstrap if a rich voice profile already exists. Improve it incrementally via `voice_rule_update` and `banned_phrase_added` events instead.

## Inputs needed (in priority order)

Try these before asking the user anything:

- **(A0) Infer from Memory Store.** Before any interview, synthesize a voice profile from the author's existing writing already in the store: published LinkedIn posts, Slack messages, blog drafts, internal docs, email drafts, edit diffs showing before/after preferences. Use the inferential voice cues in [recall-cues.md](recall-cues.md). Present the inferred profile to the user for a one-shot confirmation. For any author with even a small footprint in Memory Store, inference is usually enough to start.

Only if inference fails or covers fewer than four of the seven dimensions:

- **(A) Writing samples.** Ask for 3–5 pieces the author thinks sound like them. LinkedIn posts, internal Slack threads, blog drafts, product copy — any medium where the author was deliberate about voice. Paste text or pass memory IDs.
- **(B) Short interview.** If samples are not available, ask the five questions below and work from the answers.

Samples are higher fidelity than interview answers. Inference from existing memory is faster than both and should be the default on any run where Memory Store has any history of the author's writing.

## Interview questions

1. What words or phrases do you repeat on purpose?
2. What words or phrases do you refuse to use, and why?
3. Who do you write for? Role, context, and the specific frustration they are sitting in.
4. What belief do you hold about your space that most of your peers disagree with?
5. Name one post (anyone's, anywhere) you would be proud to have written. What about it lands for you?

Keep the interview tight. Five answers is enough. Do not keep asking until the user is exhausted — the skill's job is to extract a working profile, not a perfect one.

## Extraction

From the samples and/or answers, extract these seven dimensions:

- **signature_phrases** — 3–5 words or constructions that recur or feel distinctly like the author.
- **banned_phrases** — specific words or patterns the author refuses to use.
- **rhythm** — sentence-length tendency (short/clipped, medium, long), use of em-dashes vs parentheses, comfort with fragments, use of lists vs prose.
- **positioning** — one-line self-position ("the person who ships fast and owns the bugs", "the infra-reliability sceptic"). Must be falsifiable; "thoughtful and curious" does not count.
- **audience** — role + context + frustration the author writes for. Concrete enough that you can picture one person reading.
- **claim_boundaries** — topics the author will speak to with authority vs topics they defer on. This protects future drafts from overreach.
- **defensible_views** — 1–3 beliefs the author holds that peers disagree with. These are the seeds of Founder POV posts.

If a sample or answer does not support a dimension, leave it blank rather than inventing. Partial voice profiles are valid; invented voice is not.

## Confirmation

Present the extracted profile as a structured summary. Ask three questions:

- Does this feel like you?
- Anything missing or wrong?
- Anything overfit to a single sample we should drop?

Iterate until the user confirms. A confirmed profile is better than a clever one.

## Record

Once confirmed, call `record` using the `Voice DNA created` template in [record-templates.md](record-templates.md). Pass the active `thread_id`. This becomes the author's voice memory for every future run.

Then resume the operating loop at step 2 — the new memory should surface on re-recall and the draft phase proceeds normally.

## Partial bootstrap

If recall returns some dimensions but not others (e.g. you have banned phrases but no positioning, or you have audience but no signature phrases), do a targeted bootstrap for only the missing dimensions. Record each new dimension as its own narrower event rather than a full `voice_dna_created`:

- New banned word → `banned_phrase_added`
- New preference or pattern → `voice_rule_update`
- Customer approved for public naming → `customer_approved_public`

Reserve `voice_dna_created` for genuine from-scratch profiles.

## Anti-patterns

- Do not bootstrap silently. The user must confirm the profile before it is recorded.
- Do not reuse another author's voice as a fallback. Voice is per-author by default.
- Do not invent defensible views from stock founder tropes. Either extract from evidence or leave blank.
- Do not bootstrap mid-draft. If voice is missing, pause, bootstrap, then draft — not the other way around.
- Do not mark a profile as bootstrapped from samples the user did not approve for training. If a sample is private or off-limits, do not record it.
