# LinkedIn craft reference

Grounded in what the 2026 LinkedIn algorithm rewards and what drives the Depth Score ranking signal. Consult this file before drafting.

## What the 2026 algorithm rewards

The ranking signal is **Depth Score**, not reach. Five things move it:

1. **Dwell time.** Posts with 61+ seconds of dwell outperform posts under 3 seconds by large margins. Long-enough-to-read-through-once is a hard floor.
2. **Saves.** The strongest single signal. A post that gets saved gets extended distribution. Reference value beats reaction value.
3. **Meaningful comments.** Comments over 15 words carry far more weight than short reactions. Comments are weighted roughly 15× a like.
4. **Knowledge and advice framing.** The algorithm downranks generic engagement-bait ("agree?", "thoughts?"). Posts that teach, analyze, or take a defensible position get distributed.
5. **Early engagement in the first 60–90 minutes.** Not a reason to spam tags; a reason to make the post good enough that real readers react fast.

Do not optimize for likes or raw reach. Optimize for the post being saved, being read to the end, and drawing a substantive comment.

## Length targets

- **First-line hook:** under 200 characters. LinkedIn truncates around 210 characters with "See more" — everything before that has to carry the post.
- **Full post:** 1,300–2,000 characters is the working range for text posts. Do not pad to hit the upper end.
- **Hard platform limit:** 3,000 characters. Almost never the right choice.
- **Line length:** 8–12 words per line maximum. One idea per line.

## Hook frameworks

Pick one framework per draft. Write three hook variants, keep the strongest.

### 1. Contrarian statement

Challenges conventional wisdom. Works when the post has evidence that reframes a belief the audience holds.

> Stop optimizing your onboarding for first-day activation. You are measuring the wrong thing.

### 2. Unexpected number

Leads with a specific, surprising stat. Works when a source memory contains a concrete measurement.

> We deleted 47% of our documentation and support tickets dropped.

### 3. Dramatic moment

Drops the reader into the middle of a scene with stakes. Works for customer stories and shipped-work retros.

> The customer's email arrived at 2:13 AM. "We need to pull the integration tomorrow."

### 4. Uncomfortable truth

States what the audience privately thinks but rarely sees written down. Works for founder POV posts.

> Most B2B content is written to be admired, not to be used. Including mine, until recently.

### 5. Time-bound transformation

Compresses before/after over a specific window. Works when memory has both a baseline and a current state.

> 90 days ago our onboarding took 4 weeks. Last customer shipped in 9 days. Here is what changed.

### 6. Question everyone is asking

Articulates what the target audience is already wondering. Works when customer memory surfaces a repeated question.

> Why do new customers churn at day 14 even when activation looks healthy?

### 7. Mini case-study preview

Teases a specific result to pull the reader into the method. Works for shipped-work and customer-story formats.

> A customer went from 9 tickets a week to 1. Same team. Same product. One configuration change.

### 8. Unpopular opinion

Signals a minority position, primes the reader to evaluate the argument. Works when the founder has a sharp, defensible view.

> Unpopular opinion: your API docs are more important than your marketing site.

## Hooks to avoid

- Generic openings ("In today's world", "As leaders, we often...").
- Rhetorical questions with no body answer ("Have you ever felt stuck?").
- Burying the most interesting line on line three.
- Promises the post does not deliver ("Here is the secret to 10× growth" when the post says "try harder").
- Hooks that could open any post on any topic.

## Body structure: the 3–2–1 rule

- Draft **3** hook variants; publish the strongest.
- Deliver **2** concrete insights or actionable takeaways — things the reader can apply today.
- End with **1** clear ask or question that invites a specific reply, not a vibe check.

## Line-break rules

- Use empty lines between beats. A wall of prose is invisible on mobile.
- 8–12 words per line.
- Short lines land harder. One-word lines are fine when earned.
- Avoid mid-sentence breaks that fragment an idea.

## CTA policy

- Prefer specific questions that invite a story ("What changed for you between week 2 and week 6?") over open prompts ("Thoughts?").
- One CTA per post. Do not stack "save this, follow me, and comment below".
- If the primary_goal of the post is saves (see [record-schemas.md](record-schemas.md)), consider closing with a line that names the save ("Save this for your next onboarding review").

## Formatting conventions

- Emoji: restrained. One or two per post, never as bullets.
- Hashtags: 0–3 at the end, specific not generic. `#B2BSaaS` yes, `#Monday` no.
- @ mentions: only when the mentioned person or company has approved or is a public figure whose public work is being credited.
- No "See more" bait ("wait for it...") — the algorithm penalizes it.

## Formats worth using first

Five formats that perform consistently. Filled templates for each are in [format-templates.md](format-templates.md).

- **Customer story** — problem → old workflow → Memory Store moment → result → lesson.
- **User insight** — pattern from calls or conversations → what it says about the category → what the company learned.
- **Shipped work** — what shipped → why it exists → who asked for it → what changes for users.
- **Founder POV** — belief → observed evidence → practical implication.
- **Objection** — common concern → why it is reasonable → how the company thinks about it.

## Draft checklist

Run this against every draft before presenting. If any check fails, fix before shipping.

- [ ] First two lines under 200 characters and use one of the eight hook frameworks.
- [ ] Body is 1,300–2,000 characters.
- [ ] One idea per line; line breaks between beats.
- [ ] Two concrete insights or takeaways, not abstractions.
- [ ] Every non-obvious claim traces to a memory ID or is flagged as needing approval.
- [ ] No banned phrases from the author's voice memory.
- [ ] Customer names anonymized unless memory marks the name as publicly approved.
- [ ] CTA is one specific question or named ask.
- [ ] Specific enough that it could only be about this company.
- [ ] No throat-clearing, no rhetorical questions without answers, no generic openers.
- [ ] Hashtags 0–3 and specific, emoji restrained.
- [ ] primary_goal named (saves, comments, inbound DM, profile visit, or named awareness target).
