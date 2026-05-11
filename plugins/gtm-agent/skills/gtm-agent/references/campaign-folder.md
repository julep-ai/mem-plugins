# Execution Workspace

Not every GTM campaign needs a repo folder. Memory Store briefs are the operating surface; records are the learning/event stream. A local folder is only an execution workspace for large batches, connector import/export, human review, or handoff.

## Brief-First Flow

A campaign starts with a brief-informed operating profile, never with sourcing. Use the host's plan mode (Claude Code, Codex, Cowork) to co-write the policy with the user before any execution workspace is created.

```
1. user: "plan a campaign for X"
   agent enters plan mode

2. agent + user co-write the plan covering:
   - campaign name
   - hypothesis (one sentence: who, what pain, what offer, why now)
   - active offer profile and sender persona
   - ICP cells, including at least one unconventional ICP from
     campaign-planner.md Persona Discovery
   - customer-story/persona hypotheses being tested
   - high-intent signal sources and monitor plan
   - scale and timing (target counts per ICP, daily sourcing target, send window)
   - success criteria (replies, qualified meetings, learnings)
   - exclusions, taboo claims, suppression rules
   - email/LinkedIn channel policy when dual-channel is in scope
   - signal sources to prioritize
   - send ramp and stop conditions

3. user reviews, exits plan mode

4. user approves policy-changing decisions

5. Memory Store record() captures the approved campaign operating profile

6. agent proposes brief deltas for reusable operating truth

7. create an execution workspace only if the user asks for files, a connector
   needs import/export, or high-volume review needs a ledger
```

The canonical state is the selected brief set plus the records that support it. If sourcing or copy drifts, compare back to the GTM Operating Brief, ICP/Persona Brief, Proof and Claims Brief, and Campaign Learning Brief. Use a folder only to run work.

## Workspace Layout

```
<campaign-slug>/
  operating-profile.md     # approved GTM policy: hypothesis, ICPs,
                           # connector readiness, policy, routines
  icps/
    <cell-slug>.md         # one ICP cell: persona, criteria, trigger,
                           # target count, exclusions, source plan
  websets.json             # webset_id, search_id, enrichment_ids,
                           # query, criteria, status per ICP cell
  accounts.csv             # master sourced list across all ICPs
  signal-cards/
    <account-slug>.md      # planner unit per draft-eligible account/contact
  copy/
    <account-slug>.md      # 5 variants + recommended + followup sequence
  sends.csv                # send queue: account, variant, status,
                           # gmail_thread_id, sent_at, followup_step
  events.jsonl             # append-only: replies, bounces, unsubscribes,
                           # meetings, manual feedback (one event per line)
  monitors.json            # monitor specs: monitor_id, parent webset_id,
                           # cron, query, behavior, last_run, next_run_at
  learnings.md             # dated log of Memory Store records: thread_id,
                           # mem_id, what changed, why
  briefs.md                # optional: canonical briefs used, proposed deltas,
                           # and links/IDs only; not copied brief contents
```

## Naming

- Slug: derive from the operating profile's campaign name. Lowercase, hyphenate, strip non-ASCII. Example: `Memory Store v0.4 — AI GTM teams` -> `memory-store-v04-ai-gtm-teams`.
- Default path, if a workspace is needed: `./<slug>` relative to the user's current working directory at approval time.
- The user may override on first save. Common overrides: `~/memory-store/gtm/<slug>`, a project workspace, or a shared team folder. Whatever they pick, record the absolute path back to Memory Store with the campaign thread_id so future runs can find it.

## `accounts.csv` Schema

Required columns. Every sourced row must carry these or be flagged `research_more`:

```text
account_slug          # stable slug from company name
company_name
company_url           # canonical homepage
linkedin_url          # company LinkedIn page
contact_name
contact_title
personal_email        # not info@ or generic; only individual
linkedin_profile_url  # contact LinkedIn page
icp_cell              # which ICP cell this account belongs to
score_icp_fit         # 1-10
score_timing          # 1-10
score_pain            # 1-10
score_personalization # 1-10
customer_story_pattern # remembered customer/persona pattern if applicable
learning_intent       # persona | signal | proof | subject | CTA | channel | sequence
risk                  # low | medium | high
status                # research_more | watch | qualified | exclude |
                      # send_ready | drafted | sent | replied | meeting |
                      # bounced | unsubscribed | negative_reply
signal_source_url     # the live signal that justified this row
signal_summary        # short, one sentence
channel_policy        # email_only | email_plus_linkedin | linkedin_only | suppress
exclusion_reason      # blank if status != exclude
last_updated          # ISO timestamp
```

Optional columns added when the campaign needs them:

```text
employee_range, funding_stage, tech_stack_overlap, competitor_overlap,
prior_thread, suppressed_by, memory_store_thread_id, memory_store_mem_ids
```

A row without `personal_email`, `linkedin_profile_url`, or `company_url` is not draft-eligible.

## File Lifecycles

- `operating-profile.md` — written once when the workspace is created from the approved GTM operating profile. Updated only when the user re-approves a policy change; fork the campaign for major pivots.
- `icps/<cell>.md` — written when the ICP cell is approved. Updated as Memory Store learnings refine criteria.
- `accounts.csv` — appended/updated continuously by Webset and Exa workers. Status column is the source of truth.
- `signal-cards/<account>.md` — written when row reaches `qualified`. One file per account.
- `copy/<account>.md` — written when row reaches `send_ready`. Updated when followups are drafted.
- `sends.csv` — appended on draft creation, updated on send and on each engagement event.
- `events.jsonl` — append-only. Never edited.
- `monitors.json` — written when a monitor is created. Updated when cadence/query changes or it's deleted.
- `learnings.md` — appended every time the main agent calls Memory Store `record`. Format: `## YYYY-MM-DD HH:MM mem_id=M-XXXXXX thread=T-XXXXXX` then a one-paragraph summary.
- `briefs.md` — optional index of canonical briefs used by the campaign and proposed brief deltas. Do not copy full brief contents into the folder unless the user explicitly wants a portable export.

## Memory Store Boundary

The execution workspace is disposable. Memory Store is durable. Briefs are sparse synthesis. The split:

| Lives in workspace | Lives as records in Memory Store | Lives in canonical briefs |
|-----------------|----------------------------------|---------------------------|
| Per-account rows, scores, statuses | Approved ICP changes, persona learnings | Current ICP/persona map |
| Specific draft copy | Winning copy angles, voice patterns | Current copy/proof policy when stable |
| Today's signals | Signal source quality over time | Trusted/blocked signal-source rules |
| Send queue, event log | Objection patterns, suppressions, outcomes | Current suppression and objection policy |
| Webset/monitor IDs (for round-trip) | Which Websets/monitors paid off | Connector/autopilot operating policy |
| GTM operating profile | Campaign outcomes vs. profile hypothesis | GTM operating brief or campaign learning brief |

If the workspace is deleted, connector IDs and records should still preserve the important state. If a canonical brief becomes stale, recall the records and update the brief rather than creating a competing brief.

## Sharing

`accounts.csv` and `sends.csv` are shareable artifacts. Send them to a teammate, import to a CRM, or hand off to a human reviewer. Do not share `signal-cards/` or `copy/` without redacting Memory Store-private context — those files may carry recall content meant for internal use only.

## Do Not

- Do not start sourcing before the campaign operating profile is approved.
- Do not start copy before the campaign operating profile is approved and required connector gates are green.
- Do not mark a row `send_ready` if it lacks `personal_email`, `linkedin_profile_url`, or a live `signal_source_url`.
- Do not record per-row state to Memory Store. Record durable learnings only.
- Do not create a brief per account, source, reply, copy variant, or ICP experiment. Use records and execution workspace files for those.
- Do not edit `events.jsonl` retroactively. Append corrections as new events.
- Do not delete an execution workspace without first recording its postmortem to Memory Store.
- Do not commit seller-specific campaign workspaces to the plugin repo unless they are deliberately curated examples.
