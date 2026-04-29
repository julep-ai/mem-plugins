# Brand bootstrap

Use this when `recall` for a company's brand returns nothing, or returns only weak signal (a product name with no positioning, a target customer with no defensible view). Author voice without brand context produces posts that sound like the author but could be about any company. Brand grounding makes the post unmistakably the company's.

## Brand versus voice

- **Voice** is per-author: how this person writes.
- **Brand** is per-company: what this company stands for, who it serves, what it refuses to be.

For a solo creator writing under their own brand, the two overlap but should still be recorded separately — voice is how they write, brand is what the business believes.

## When to bootstrap

- No brand memory exists for the company.
- Brand memory exists but covers only one dimension (e.g. a tagline and nothing else).
- The company has pivoted, repositioned, or shifted pillars recently and the stored profile is stale.

Do not bootstrap if rich brand memory already exists. Update it incrementally via `brand_pillar_update`, `approved_claim_added`, and `taboo_topic_added` events instead.

## Inputs needed (in priority order)

Try these before asking the user anything:

- **(A0) Infer from Memory Store.** Before any interview, synthesize the brand profile from what the store already has: recent posts, shipped features, customer conversations, founder Slack threads, homepage copy, support themes. Use the inferential brand cues in [recall-cues.md](recall-cues.md). Present the inferred profile to the user for a one-shot confirmation. For most teams with a few weeks of Memory Store usage this is enough — no interview needed.

Only if inference fails or covers fewer than four of the eight dimensions:

- **(A) Existing brand assets.** Ask for a positioning doc, sales deck, homepage, recent launch post, manifesto, or approved customer-story copy. Paste text or pass memory IDs.
- **(B) Short interview.** If assets are not available or are out of date, ask the six questions below.

Assets are higher fidelity than interview answers. Inference from existing memory is faster than both and should be the default on any run where Memory Store is not freshly empty.

## Interview questions

1. In one sentence, what does your company do and for whom?
2. Who buys from you? Be specific — role, company size, industry, and the pain they hire you for.
3. What three to five narrative pillars is your content focused on this quarter? What do you want to be known for right now?
4. What belief about your category is your company willing to defend publicly? Where do you disagree with how the category is usually framed?
5. What does your company refuse to be compared to, and why? What are you not?
6. Which customers, metrics, and claims are approved for public mention — and which are off-limits?

Keep the interview tight. Six answers is enough to start. Gaps can be filled by later updates.

## Extraction

From the assets and/or answers, extract these eight dimensions:

- **company_name** — the exact public-facing name.
- **one_line_positioning** — what the company does and for whom, in one falsifiable sentence. "We help teams build better software" does not count; "We give SRE teams one-screen root-cause timelines for incidents over 10 minutes" does.
- **icp** — ideal customer profile. Role + company size + industry + the specific pain they sit in.
- **pillars** — three to five narrative themes the company wants to be known for this quarter. These become the `pillar/topic` inputs on future draft runs.
- **defensible_category_view** — the company's public, defensible position on its category. What everyone else gets wrong.
- **anti_positioning** — what the company refuses to be compared to or framed as.
- **approved_claims** — specific customer names, metrics, quotes, and category claims approved for public mention. Treat as an allowlist.
- **taboo_topics** — topics the company will not address publicly: competitor names, internal-only facts, pricing specifics if private, sensitive customer information.

If a sample or answer does not support a dimension, leave it blank rather than inventing. Partial brand profiles are valid; invented brand claims are not.

## Confirmation

Present the extracted profile as a structured summary. Ask three questions:

- Does this sound like how you would introduce the company to a skeptical buyer?
- Anything missing or wrong?
- Which dimensions are you most likely to update in the next 30 days?

Iterate until the user confirms. A confirmed profile is better than an aspirational one.

## Record

Once confirmed, call `record` using the `Brand profile created` template in [record-templates.md](record-templates.md). Pass the active `thread_id`. This becomes the company's brand memory for every future run.

Then resume the operating loop — voice recall next, then source material.

## Partial bootstrap

If recall returns some dimensions but not others, fill only the missing ones and record each with a narrower event:

- New or updated pillar → `brand_pillar_update`
- New claim cleared for public use → `approved_claim_added`
- New topic off-limits → `taboo_topic_added`

Reserve `brand_profile_created` for genuinely from-scratch profiles.

## How brand grounds drafting

Once brand is known, every draft should satisfy three brand checks in addition to the craft checklist:

1. The post is about one of the company's current pillars, or the post argues why a new pillar should be added. Off-pillar drafts get flagged, not shipped.
2. Every customer, metric, or category claim in the post is on the approved_claims list or explicitly flagged as needing approval.
3. The post does not cross into taboo_topics. No competitor names, no internal-only facts, no comparisons the company refuses.

If a draft candidate cannot satisfy all three, drop it at the shortlist stage. A strong angle outside the brand is still a bad draft.

## Anti-patterns

- Do not conflate voice and brand. A founder who writes casually can still represent a company that positions precisely.
- Do not invent pillars. If the user cannot name current pillars, ask — do not guess from shipped features.
- Do not promote internal facts to approved_claims. A thing being true is not the same as a thing being cleared to say publicly.
- Do not record competitor names as taboo unless the user explicitly says so. Sometimes competitors are fair game (for example, a category reframe).
- Do not bootstrap brand silently. The user must confirm the profile before it is recorded.
