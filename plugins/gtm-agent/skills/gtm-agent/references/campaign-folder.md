# Campaign Folder

Every GTM campaign lives in its own folder. The folder is the campaign's working state — plan, ICPs, accounts, signal cards, copy, sends, events, monitors, learnings. Memory Store is the durable cross-campaign brain. The folder is current-campaign execution.

## Plan-First Flow

A campaign always starts with a plan, never with sourcing. Use the host's plan mode (Claude Code, Codex, Cowork) to co-write the plan with the user before any folder is created.

```
1. user: "plan a campaign for X"
   agent enters plan mode

2. agent + user co-write the plan covering:
   - campaign name
   - hypothesis (one sentence: who, what pain, what offer, why now)
   - active offer profile and sender persona
   - ICP cells, including at least one unconventional ICP from
     campaign-planner.md Persona Discovery
   - scale and timing (target counts per ICP, send window)
   - success criteria (replies, qualified meetings, learnings)
   - exclusions, taboo claims, suppression rules
   - signal sources to prioritize
   - send ramp and stop conditions

3. user reviews, exits plan mode

4. agent: "Save the campaign?
            Default path: ./<slug-from-name>
            Override:"
   user accepts default or provides path

5. folder created
   plan.md written first as the frozen artifact of the planning conversation

6. Memory Store record() with the new campaign thread_id, referencing
   plan.md and the campaign slug
```

The plan is the contract. Everything downstream reads it. If sourcing or copy drifts, compare back to the plan. To fork a campaign, copy the folder and edit `plan.md`.

## Folder Layout

```
<campaign-slug>/
  plan.md                  # frozen plan from plan mode (the contract)
  setup-packet.md          # approved campaign-setup output
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
```

## Naming

- Slug: derive from plan's campaign name. Lowercase, hyphenate, strip non-ASCII. Example: `Memory Store v0.4 — AI GTM teams` → `memory-store-v04-ai-gtm-teams`.
- Default path: `./<slug>` relative to the user's current working directory at plan-approval time.
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
risk                  # low | medium | high
status                # research_more | watch | qualified | exclude |
                      # send_ready | drafted | sent | replied | meeting |
                      # bounced | unsubscribed | negative_reply
signal_source_url     # the live signal that justified this row
signal_summary        # short, one sentence
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

- `plan.md` — written once at folder creation. Frozen. To change, fork the campaign.
- `setup-packet.md` — written once after `campaign-setup` approval. Updated only when the user re-approves a change.
- `icps/<cell>.md` — written when the ICP cell is approved. Updated as Memory Store learnings refine criteria.
- `accounts.csv` — appended/updated continuously by Webset and Exa workers. Status column is the source of truth.
- `signal-cards/<account>.md` — written when row reaches `qualified`. One file per account.
- `copy/<account>.md` — written when row reaches `send_ready`. Updated when followups are drafted.
- `sends.csv` — appended on draft creation, updated on send and on each engagement event.
- `events.jsonl` — append-only. Never edited.
- `monitors.json` — written when a monitor is created. Updated when cadence/query changes or it's deleted.
- `learnings.md` — appended every time the main agent calls Memory Store `record`. Format: `## YYYY-MM-DD HH:MM mem_id=M-XXXXXX thread=T-XXXXXX` then a one-paragraph summary.

## Memory Store Boundary

The folder is regenerable. Memory Store is durable. The split:

| Lives in folder | Lives in Memory Store |
|-----------------|-----------------------|
| Per-account rows, scores, statuses | Approved ICP rules, persona learnings |
| Specific draft copy | Winning copy angles, voice patterns |
| Today's signals | Signal source quality over time |
| Send queue, event log | Objection patterns, suppression policy |
| Webset/monitor IDs (for round-trip) | Which Websets/monitors paid off |
| Plan and setup packet | Campaign outcomes vs. plan hypothesis |

If the folder is deleted, the campaign is gone but the learnings remain. If Memory Store loses a thread, the folder still has the working state to rebuild from. Both layers are durable in different ways.

## Sharing

`accounts.csv` and `sends.csv` are shareable artifacts. Send them to a teammate, import to a CRM, or hand off to a human reviewer. Do not share `signal-cards/` or `copy/` without redacting Memory Store-private context — those files may carry recall content meant for internal use only.

## Do Not

- Do not start sourcing before `plan.md` exists.
- Do not start copy before `setup-packet.md` is approved.
- Do not mark a row `send_ready` if it lacks `personal_email`, `linkedin_profile_url`, or a live `signal_source_url`.
- Do not record per-row state to Memory Store. Record durable learnings only.
- Do not edit `events.jsonl` retroactively. Append corrections as new events.
- Do not delete a campaign folder without first recording its postmortem to Memory Store.
