# Recall cues

Memory Store abstracts upstreams. Treat `recall` as the sole interface to company context. Do not assume Slack, Granola, Fireflies, or any specific source — a recall result is just a memory.

## Cue patterns

Use narrow, concrete cues. Each recall call should aim at one thing, not five. Combine cues across two or three calls rather than stuffing one.

### Brand cues — direct (call first — explicit brand-profile memories)

- `<company> brand positioning one-line ICP customer profile`
- `<company> pillars narrative themes this quarter focus`
- `<company> defensible category view belief thesis argument`
- `<company> anti-positioning what we are not refuse compared`
- `<company> approved claims public metrics customer names quotes`
- `<company> taboo topics competitors off-limits claim boundaries`

### Brand cues — inferential (fall back here before asking the user)

Memory Store often has the raw material to infer a brand profile even when no profile was recorded. Try these before interview bootstrap:

- `<company> recent LinkedIn post published announcement`
- `<company> shipped feature launch customer email internal note`
- `<company> customer conversation sales call objection quote`
- `<company> founder Slack positioning argument belief debate`
- `<company> homepage about-page manifesto tagline copy`
- `<company> support theme FAQ common question pattern`

Synthesize across these: the positioning line often appears in launch posts or homepage copy; the ICP appears in sales-call quotes or support themes; the pillars appear in recent posts and roadmap discussions; the defensible view appears in founder Slack arguments; approved claims appear in published posts; taboo topics appear in "do not say this publicly" conversations.

### Voice cues — direct (call after brand — voice is how the author writes within that brand)

- `<author> LinkedIn voice approved posts signature phrases`
- `<author> LinkedIn banned words banned phrases voice rules`
- `<author> rhythm sentence length em-dash parentheses fragments`
- `<author> LinkedIn feedback editorial notes claim boundaries`

### Voice cues — inferential (fall back here before asking the user)

Even when no voice profile was recorded, the author's writing is usually somewhere in memory:

- `<author> LinkedIn post published text prior draft`
- `<author> Slack message thread long-form writing sample`
- `<author> blog draft internal doc product copy email`
- `<author> edit diff before after preference rewrite`
- `<author> rejected draft reason feedback pattern`

Synthesize: signature phrases surface as repeats across samples; banned phrases surface as edit diffs where a word is removed; rhythm appears in sentence length distribution; positioning surfaces in how the author describes the product/self in their own words; claim boundaries surface in what the author refuses to speak to.

### Source-material cues (scoped to today's intent)

Customer and user signal:

- `<company> customer story arc turning point before after`
- `<company> customer objection concern pushback repeated`
- `<company> user pattern role workflow pain anonymized`
- `<company> sales-call quote customer exact language`

Shipped work:

- `<company> shipped this week launch integration fix product change`
- `<company> roadmap commit who asked for it motivation`
- `<company> product decision tradeoff reasoning`

Founder / category:

- `<author> founder POV belief defensible view evidence`
- `<company> category argument positioning thesis`

Performance and learning:

- `<author> LinkedIn post performance saves comments dwell`
- `<author> draft rejected reason edit final-text diff`
- `<author> high-performing post format hook framework`

## Ranking heuristic

When recall returns many memories, rank by:

1. **Author match.** Voice memories for the target author always beat same-topic memories for other authors.
2. **Recency × specificity.** A concrete memory from the last 30 days beats a vague memory from six months ago. A vague recent memory loses to a concrete older one.
3. **Source density.** A memory that cites a customer by role, a number, a date, or a direct quote beats one that paraphrases.
4. **Feedback signal.** A memory tagged with `draft_approved`, `post_published`, or `post_performance` is higher signal than untagged observational notes.
5. **Non-duplication.** If two memories say the same thing, pick the one with more evidence and drop the other.

Discard memories that fail all of: recency, specificity, feedback signal. A memory with none of these is probably not shippable.

## Empty recall fallback

If a voice recall returns nothing:

1. Try a narrower cue: swap `<author> LinkedIn voice` for `<author> writing sample prior post signature phrase`.
2. Try the author's canonical profile memory if one exists: `<author> voice DNA profile`.
3. If still empty, ask the user to paste one approved post or point at a memory ID. Mark the run as low-voice and note it in the draft package.

If a source recall returns nothing:

1. Broaden the time window once.
2. Swap the format cue: if `customer story` returned nothing, try `customer quote`, `customer conversation`, or `customer Slack`.
3. If still empty for every candidate format, tell the user recall is dry and ask for a seed (a customer name, a feature, a recent conversation). Do not invent source material.

If `checkin` itself fails:

- Fall back to operating without a `thread_id`. Draft with user-pasted context only. Mark every draft as ungrounded in the draft package.
- Do not call `record` without a `thread_id` — the learning loop needs the thread to group lineage correctly.

## What not to recall

- Do not recall on the source-tool name ("slack", "granola", "fireflies"). Memory Store abstracts these. If a cue like `<company> slack thread` returns nothing, try `<company> customer conversation`.
- Do not recall competitor memories unless the post explicitly needs a competitive comparison that is safe to publish.
- Do not recall internal-only memories (team disagreements, unshipped experiments, pricing internals) into a public draft. If a memory is tagged internal-only, treat it as out of scope.

## Recall call hygiene

- Always pass the active `thread_id` from `checkin` into `recall` when the tool supports it — it improves relevance.
- Ask once, broad, then narrow. Three focused calls beat one wide one.
- When a recall returns a useful memory, note its ID. Every draft that cites it must list the ID in source notes.
