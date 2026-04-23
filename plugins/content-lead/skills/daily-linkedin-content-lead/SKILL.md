---
name: daily-linkedin-content-lead
description: "Use when creating LinkedIn drafts from Memory Store context, including daily content, brand voice, customer stories, Slack or Granola, shipped work, and feedback from edits, approvals, rejections, or final posts."
---

# Daily LinkedIn content lead

## Overview

Write LinkedIn drafts from company memory. Start with `checkin`, use `recall` to find brand voice and story material, draft from sourced memories, then use `record` when the user gives feedback, approves, rejects, or posts a draft.

## Operating loop

1. Run Memory Store `checkin` first with the company, date range, and content intent.
2. Recall brand voice: approved posts, founder language, repeated phrases, banned words, positioning, audience, and claims that need evidence.
3. Recall source material: Slack threads, Granola notes, customer calls, shipped work, support issues, docs, and product usage stories.
4. Extract content candidates. Keep only candidates with a clear source, audience, and reason to publish.
5. Draft LinkedIn posts. Make them useful without needing the reader to buy the product.
6. Ask for feedback, approval, rejection, or posting status.
7. Record the editorial outcome back into Memory Store when the user gives it.

If Memory Store is unavailable, say so and ask for pasted source context. Mark those drafts as ungrounded.

## What to recall

Use narrow, concrete recall cues. Good cues:

- `<company> brand voice LinkedIn approved posts banned phrases`
- `<company> customer insight Slack Granola pain point use case`
- `<company> shipped work launch integration bug fix product lesson`
- `<company> rejected draft edit feedback final post performance`

Prefer recent memories for daily drafts, then pull older memories only when they explain voice, positioning, or a recurring customer pattern.

## Content formats

Use these formats first:

- `Customer story`: problem, old workflow, Memory Store moment, result, lesson.
- `User insight`: pattern from calls or Slack, what it says about the category, what the company learned.
- `Shipped work`: what shipped, why it exists, who asked for it, what changes for users.
- `Founder POV`: belief, observed evidence, practical implication.
- `Objection`: common concern, why it is reasonable, how the company thinks about it.

## Draft package

Return:

- `content read`: what Memory Store suggests today.
- `story candidates`: 5-10 options with source basis and risk.
- `drafts`: 2-3 polished LinkedIn posts with different angles.
- `source notes`: memory IDs, source names, or quoted internal context when available.
- `feedback prompt`: a short prompt asking what to record for next time.

## Learning loop

Record these outcomes when the user provides them:

- draft approved
- draft rejected and why
- line edits or rewritten version
- final posted text
- performance notes
- updated voice rule, banned phrase, preferred angle, or claim boundary

Use `record` with the active thread ID when available. Include the source memories, draft text or summary, user feedback, and what should change next time.

## Guardrails

- Do not invent customer names, metrics, quotes, or usage claims.
- Anonymize customers unless the memory says the name is approved for public use.
- Mark claims that need approval.
- Avoid empty thought-leadership language.
- Preserve explicit brand constraints, including banned words.
- Keep the post concrete enough that the source memory still matters.

## Minimal inputs

If recall does not identify the basics, ask for company name, target audience, and date range.
