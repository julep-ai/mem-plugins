# Record schemas

Structured templates for `record` calls. The content-lineage model stores every piece from idea to post to performance, so future runs can learn per-author voice and judge what actually drives engagement against the post's `primary_goal`, not raw likes.

Always pass the active `thread_id` from `checkin`. Without it, the learning loop cannot group lineage correctly.

## Field glossary

- **thread_id** — from `checkin`. Groups all memories in this run.
- **author** — whose voice the draft uses.
- **piece_id** — a stable identifier for this content piece across drafts, edits, and performance records. Generate once at shortlist stage and reuse across every record call for this piece.
- **primary_goal** — what this post is optimizing for. One of: `saves`, `meaningful_comments`, `inbound_dm`, `profile_visits`, `named_awareness`. Recorded so performance is judged against intent, not raw reach.
- **context_tags** — attributes of the post that could correlate with performance without causing it. Used so the system does not learn false lessons. Examples: `format:customer_story`, `hook:unexpected_number`, `length:~1400`, `posted_day:tuesday`, `posted_hour:08`, `has_numbers:true`, `mentions_customer:anonymized`.
- **source_memory_ids** — the memory IDs the draft traces to. Required for every claim-bearing draft.

## Schemas by event

### draft_created

Record when a draft is first presented to the user. One call per draft variant.

```json
{
  "event": "draft_created",
  "thread_id": "<thread_id>",
  "author": "<author>",
  "piece_id": "<piece_id>",
  "variant_label": "A | B | C",
  "format": "customer_story | user_insight | shipped_work | founder_pov | objection",
  "hook_framework": "contrarian | unexpected_number | dramatic_moment | uncomfortable_truth | time_bound_transformation | question_everyone | mini_case_study | unpopular_opinion",
  "draft_text": "<full post text>",
  "primary_goal": "saves | meaningful_comments | inbound_dm | profile_visits | named_awareness",
  "source_memory_ids": ["M-...", "M-..."],
  "context_tags": ["format:customer_story", "hook:dramatic_moment", "length:~1400", "has_numbers:true"],
  "flagged_claims": ["<any unsourced claim the draft is carrying, with a note asking for approval>"]
}
```

### draft_approved

The user approves a draft without edits.

```json
{
  "event": "draft_approved",
  "thread_id": "<thread_id>",
  "piece_id": "<piece_id>",
  "variant_label": "A",
  "approved_text": "<exact text the user approved>",
  "note": "<optional: why the user picked this one>"
}
```

### draft_rejected

The user rejects a draft. `reason` is required — without it, the next run cannot avoid the same mistake.

```json
{
  "event": "draft_rejected",
  "thread_id": "<thread_id>",
  "piece_id": "<piece_id>",
  "variant_label": "B",
  "reason": "<short, concrete: 'voice too formal', 'claim unsupported', 'hook is engagement bait', etc>",
  "suggested_fix": "<optional: what the user said would work instead>"
}
```

### draft_edited

The user rewrites part of the draft. Store both the original and the edit so a future model can learn the voice delta.

```json
{
  "event": "draft_edited",
  "thread_id": "<thread_id>",
  "piece_id": "<piece_id>",
  "variant_label": "A",
  "original_text": "<draft the skill produced>",
  "edited_text": "<user's rewrite>",
  "edit_summary": "<one line: what changed and why>",
  "voice_signal": "<optional: if the edit reveals a voice rule — a phrase preferred, a phrase banned, a rhythm preference>"
}
```

### post_published

The user posted the approved or edited draft to LinkedIn.

```json
{
  "event": "post_published",
  "thread_id": "<thread_id>",
  "piece_id": "<piece_id>",
  "published_text": "<exact text that went live>",
  "published_url": "<LinkedIn post URL>",
  "published_at": "<ISO timestamp>",
  "primary_goal": "saves | meaningful_comments | inbound_dm | profile_visits | named_awareness",
  "context_tags": ["format:customer_story", "hook:dramatic_moment", "length:1412", "posted_day:tuesday", "posted_hour:08"]
}
```

### post_performance

Record at 24 hours and again at 7 days. Two separate calls.

```json
{
  "event": "post_performance",
  "thread_id": "<thread_id>",
  "piece_id": "<piece_id>",
  "window": "24h | 7d",
  "metrics": {
    "impressions": 0,
    "likes": 0,
    "comments": 0,
    "comment_meaningful_count": 0,
    "saves": 0,
    "shares": 0,
    "dm_inbound": 0,
    "profile_visits": 0
  },
  "goal_outcome": "hit | partial | missed",
  "notes": "<optional: which comments were high-quality, who reached out, what drove the dwell>"
}
```

### voice_rule_update

The user says something that should change how the skill writes for this author going forward.

```json
{
  "event": "voice_rule_update",
  "author": "<author>",
  "rule_type": "prefer | ban | pattern",
  "rule": "<one line: 'never start a post with a question', 'always use em-dashes not parentheses', 'avoid the word "unlock"'>",
  "evidence_memory_ids": ["<the memory or memories this rule came from>"],
  "scope": "linkedin_only | all_channels"
}
```

### banned_phrase_added

Short form for a new banned phrase. Use when the rule is just "do not use this word or phrase."

```json
{
  "event": "banned_phrase_added",
  "author": "<author>",
  "phrase": "<exact phrase>",
  "reason": "<one line: 'sounds like every other B2B post', 'founder hates this word', etc>"
}
```

### claim_boundary_update

The user sets or clarifies what kind of claim can be made without approval.

```json
{
  "event": "claim_boundary_update",
  "author": "<author>",
  "claim_type": "customer_name | metric | quote | category_claim",
  "policy": "<one line: 'never name <customer> publicly', 'metrics must cite a memory ID', 'quotes must be exact from memory'>",
  "scope": "author | company"
}
```

### customer_approved_public

A specific customer is approved to be named in public posts.

```json
{
  "event": "customer_approved_public",
  "customer_identifier": "<name or memory ID>",
  "approved_at": "<ISO timestamp>",
  "scope": "all_posts | <specific piece_id or pillar>",
  "approved_by": "<who on the team confirmed approval>"
}
```

### weekly_summary

Record at end of the week to keep a rolled-up view of what worked. One call per author per week.

```json
{
  "event": "weekly_summary",
  "author": "<author>",
  "week_of": "<ISO date of Monday>",
  "posts_published": 0,
  "top_piece_id": "<piece_id of the week's best post by primary_goal>",
  "top_format": "<format that performed>",
  "top_hook_framework": "<hook that performed>",
  "observed_voice_signals": ["<new phrase preferred>", "<new phrase banned>"],
  "open_questions": "<what we still do not know: e.g. 'is Tuesday 8am still best for this author'>"
}
```

## Always record these, even when the user did not explicitly ask

- `draft_created` for every draft variant presented, at present-time.
- `draft_approved` / `draft_rejected` / `draft_edited` when the user responds to the draft package.
- `post_published` when the user confirms the post is live.
- `voice_rule_update` or `banned_phrase_added` when the user says something that reads like a rule, even in passing. The line "I would never use the word 'unlock'" is a rule, not a comment.

## Never record these

- Invented performance numbers. If the user has not shared metrics, do not record them.
- Draft text that was never shown to the user.
- Feedback inferred from silence — if the user did not respond, do not record an outcome.
- Author-specific rules against a different author. Voice rules are per-author unless the user explicitly says `scope: company`.
