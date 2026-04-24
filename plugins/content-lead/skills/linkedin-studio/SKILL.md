---
name: linkedin-studio
description: "Drafts engagement-driving LinkedIn posts from company memory in Memory Store. Use when the user asks to write LinkedIn content, turn shipped work or customer insights into posts, generate post variants for a pillar piece, or capture edits, approvals, rejections, and final posted text so per-author voice improves over time. Requires the Memory Store MCP (checkin, recall, record)."
---

# LinkedIn Studio

Turn Memory Store insights into LinkedIn posts that earn Depth Score — dwell time, saves, meaningful comments — not just likes.

This file is the orchestrator. Craft rules, templates, examples, cue catalog, bootstrap flows, record templates, and failure handling live under `references/`. Consult them when the run calls for them rather than inlining their content.

## When to use

Trigger this skill when the user asks to:

- draft LinkedIn posts for today, this week, or a specific pillar piece
- turn a shipped feature, customer conversation, or internal artifact into public content
- generate post variants grounded in company memory (voice, customer stories, shipped work, prior posts)
- capture edits, approvals, rejections, or posted text so the system learns

Do not trigger for generic copywriting, non-LinkedIn channels, or drafts that do not need grounding in memory.

## Operating loop

1. **Checkin.** Call Memory Store `checkin` with the company, the author (whose voice is used), the pillar or topic intent, and the date range. Capture `thread_id` and pass it to every subsequent `record` call in the session.

2. **Recall brand; infer before asking; bootstrap only if empty.** Pull the company's brand profile — positioning, ICP, current pillars, defensible category view, approved claims, taboo topics — using the brand cues in [references/recall-cues.md](references/recall-cues.md). If direct brand recall returns thin, do not ask the user yet. Memory Store usually has the raw material even when no brand profile has been recorded. Infer missing dimensions from adjacent memory: recent LinkedIn posts and announcements, shipped features, customer conversations and support themes, founder discussions and Slack threads, homepage and manifesto copy. Use the inferential cues in [references/recall-cues.md](references/recall-cues.md). Present the inferred profile to the user for a one-shot confirmation, then record it via `brand_profile_created`. Only when both direct recall and inference fail, fall back to the interview flow in [references/brand-bootstrap.md](references/brand-bootstrap.md). Voice without brand produces posts that sound like the author but could be about any company.

3. **Recall voice; infer before asking; bootstrap only if empty.** Pull the author's voice DNA — approved posts, signature phrases, banned words, rhythm, positioning, claim boundaries — using the voice cues in [references/recall-cues.md](references/recall-cues.md). If direct voice recall returns thin, infer from adjacent memory: the author's prior LinkedIn posts, internal Slack threads, blog drafts, product copy, and any edit diffs showing before/after preferences. Present the inferred profile for confirmation and record via `voice_dna_created`. Only when both direct recall and inference fail, fall back to the interview flow in [references/voice-bootstrap.md](references/voice-bootstrap.md). Then resume the loop.

4. **Recall sources.** Pull source material relevant to today's pillar and intent: customer conversations, shipped work, support themes, docs, prior posts, performance notes. Memory Store abstracts upstreams — do not assume any specific source tool.

5. **Shortlist.** Extract 5–10 candidates. Keep only ones with (a) a concrete source memory ID, (b) a named audience on the ICP, (c) a fit with a current pillar or a defensible reason to add a new one, (d) a reason a reader would stop scrolling. Drop anything that fails brand checks (off-pillar, unsourced claim, taboo topic).

6. **Draft.** For each of 2–3 picked candidates, apply the craft in [references/linkedin-craft.md](references/linkedin-craft.md) and the structure in [references/format-templates.md](references/format-templates.md). Prefer `user_insight` when the memory carries multiple customer signals that share a shape — this format consistently earns Depth Score. Write three hook variants per draft; keep the strongest. Study [references/examples.md](references/examples.md) for shape.

7. **Self-check.** Validate each draft against the invariants below, the craft checklist in [references/linkedin-craft.md](references/linkedin-craft.md), and the brand checks in [references/brand-bootstrap.md](references/brand-bootstrap.md). Flag unsourced claims for approval.

8. **Present.** Return the draft package (see Output contract).

9. **Record.** When the user approves, rejects, edits, or posts, call `record` using the prose templates in [references/record-templates.md](references/record-templates.md). `record` is a quick-jot — natural-language prose, not JSON. Always pass the active `thread_id`.

## Output contract

Return in this order:

1. **content read** — one short paragraph: what Memory Store suggests today and why.
2. **story candidates** — 5–10 lines. Each line: format · angle · source (memory ID) · risk.
3. **drafts** — 2–3 polished posts. Each draft includes: the post text ready to paste, format label, hook framework used, source memory IDs, flagged claims (if any), and the post's intended primary goal (saves, meaningful comments, inbound DM, profile visits, named awareness).
4. **source notes** — memory IDs and any quoted internal context behind each draft.
5. **feedback prompt** — one short prompt asking the user which outcome to record: approve, reject (+ why), edit, post (+ URL).

## Stop condition

A run is done when all three are true:

- drafts satisfy every invariant below and the craft checklist
- the user has seen the draft package and the feedback prompt
- any feedback the user gave has been recorded with the active `thread_id`

Do not end the run silently if the user gave feedback and nothing was recorded.

## Minimum inputs

If recall does not surface the basics, ask once for:

- **the company** — whose brand the post speaks for. This is not the author; it is the business the post represents. For solo creators, author and company often map to the same person but remain distinct fields.
- **the author** — yourself if you are a solo creator, a client if you are ghostwriting, or a colleague whose account you are drafting for
- **the target audience** — role, context, and the frustration they sit in (this usually comes from the brand's ICP once brand is recalled)
- **the date range** for source material

If this is the first run and Memory Store has no brand memory for the company, proceed to the brand bootstrap flow in step 2. If no voice memory exists for the author, proceed to the voice bootstrap in step 3. Do not draft without identifying both a company and an author — brand and voice grounding fail otherwise.

## Invariants

- No invented customer names, metrics, quotes, or usage claims. Every non-obvious claim traces to a memory ID or is flagged as needing approval.
- Anonymize customers unless a memory explicitly says the name is approved for public use. Use the fallback naming convention in [references/format-templates.md](references/format-templates.md).
- Banned phrases from voice memory are hard constraints, not style nudges.
- First two lines must earn the scroll. No preamble, no "in today's world", no throat-clearing. Use a hook framework from [references/linkedin-craft.md](references/linkedin-craft.md).
- One idea per line. Line breaks between beats. LinkedIn is scanned, not read.
- Specific over abstract. If a post could be about any company, rewrite until it could only be about this one.
- If Memory Store MCP is unavailable, follow [references/failure-modes.md](references/failure-modes.md). Do not claim the system learned from an ungrounded draft.

## Reference files

- [references/linkedin-craft.md](references/linkedin-craft.md) — hook frameworks, length targets, 2026 algorithm signals, line-break rules, the draft checklist.
- [references/format-templates.md](references/format-templates.md) — filled templates for the five content formats, plus the anonymization convention.
- [references/examples.md](references/examples.md) — annotated good and bad drafts.
- [references/recall-cues.md](references/recall-cues.md) — recall cue catalog, ranking heuristic, empty-recall fallback.
- [references/brand-bootstrap.md](references/brand-bootstrap.md) — how to create a company brand profile when recall returns nothing, and the three brand checks every draft must pass.
- [references/voice-bootstrap.md](references/voice-bootstrap.md) — how to create an author voice profile when recall returns nothing.
- [references/record-templates.md](references/record-templates.md) — prose `record()` jot templates for every editorial outcome.
- [references/failure-modes.md](references/failure-modes.md) — MCP down, empty recall, contradictory voice rules, claim-flag policy, missing thread_id.
