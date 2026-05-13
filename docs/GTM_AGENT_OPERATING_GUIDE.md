# GTM Agent Operating Guide

This guide describes how to run Memory Store-backed outbound campaigns with GTM
Agent, Websets, Hermes, Attio, and one or more sending rails.

The core rule is simple: GTM Agent is the campaign brain, not an uncontrolled
email cannon. It engineers the campaign, prepares evidence-backed work queues,
and hands bounded jobs to the right execution layer.

## System Model

```text
Memory Store = durable campaign and company memory
GTM Agent    = campaign engineering, sourcing, copy, policy, learning
Exa/Websets  = public research, verified account/person pools, enrichments
Attio        = visual CRM and campaign-funnel operating surface
Hermes       = background runtime for approved recurring goals
Gmail        = current first-party sending and reply-learning rail
Agent Mail   = agent-owned mailbox rail, when exposed by Hermes
Resend       = programmatic transactional/bulk rail, when approved and wired
CSV/workspace = disposable execution ledger and import/export surface
```

Memory Store is the durable layer. Attio and CSVs are views or ledgers. If a
workspace or CRM view disappears, the campaign's reusable rules, outcomes, and
approved learning should still be recoverable from Memory Store.

## Responsibility Split

| Layer | Owns | Must Not Own |
| --- | --- | --- |
| Memory Store | product context, approved campaign rules, reusable learnings, proof boundaries, brief deltas | per-row CRM state, raw send logs, every transient draft |
| GTM Agent | ICP design, signal criteria, Websets specs, scoring, signal cards, copy hypotheses, send policy, routine specs | hidden sends, broad inbox changes, unapproved claims |
| Websets | persistent account/person pools, enrichment, source evidence, reusable sourcing batches | final copy quality, private Memory Store context, send approval |
| Attio | visual campaign panels, records, owners, stages, review queues, funnel health | canonical memory, unreviewed private context, autonomous send policy |
| Hermes | scheduled goals, background workers, digests, reply scans, followup checks, learning jobs | vague "do GTM" jobs, policy changes without approval |
| Gmail | sender voice, warm-path context, drafts, sends, replies, followups | campaign strategy, durable learning synthesis |
| Agent Mail | agent-specific mailbox execution when available | founder Gmail identity unless explicitly configured |
| Resend | programmatic high-volume or product-triggered email when approved | relationship-led founder outbound without deliverability policy |

## Campaign Lifecycle

```text
plan
  -> source
  -> enrich
  -> score
  -> build signal cards
  -> draft copy
  -> create review queue
  -> create Gmail/Agent Mail/Resend drafts or send jobs
  -> approve
  -> send approved batch
  -> scan replies
  -> follow up
  -> record learnings
  -> refine ICP, copy, and routines
```

The lifecycle may run partly in CSV and partly in Attio. The status machine
should stay the same across both:

```text
sourced
enriched
qualified
signal_card_ready
copy_ready
draft_created
approved_to_send
sent
replied
followup_due
meeting_booked
closed
excluded
```

No row jumps from `enriched` to `sent`.

## Attio As Campaign Surface

Attio should be the visual control plane for campaign operators. Use it to see
which campaigns, accounts, people, and followups are moving.

Recommended objects or lists:

```text
Campaign
Account
Person
Signal Card
Draft
Send Attempt
Reply/Event
Suppression
PLG Account
PLG User
```

Recommended campaign panels:

```text
Campaign Overview
ICP Cell Performance
Account Review Queue
People Review Queue
Signal Cards Ready
Drafts Awaiting Approval
Approved Sends
Replies And Objections
Meetings
Suppressions
PLG Activation Signals
Learning Backlog
```

Attio should store operational fields:

```text
campaign_id
campaign_name
icp_cell
account_domain
person_email
person_linkedin_url
webset_id
webset_item_id
signal_source_url
signal_summary
score_icp_fit
score_timing
score_pain
score_personalization
status
owner
next_action
next_action_at
draft_id
sender_rail
sent_at
reply_status
suppression_reason
memory_store_thread_id
memory_store_record_ids
```

Attio is also the right place for manual review and handoff. A teammate can
filter `signal_card_ready`, approve good rows, reject weak rows, assign owners,
and move approved rows into a draft or send queue.

## PLG Funnel Model

PLG should feed GTM instead of sitting in a separate growth system. Product
signals should become campaign signals and account health signals.

Useful PLG events:

```text
new workspace created
team member invited
Slack connected
Gmail connected
Granola/Fathom/meeting source connected
first brief created
brief opened by teammate
agent checkin used repeatedly
recall used from Claude/Codex/ChatGPT-style workflow
connector failed during onboarding
user asked for docs, wiki, or customer brief
multiple users from same domain activated
high-intent page viewed
Discord/Slack support question raised
```

PLG routing:

```text
anonymous_or_trial_user -> PLG User
company_domain_seen -> PLG Account
activation_signal -> Account Review Queue
team_context_signal -> Signal Card
sales_assist_needed -> GTM Agent draft queue
support_or_success_needed -> human owner or Hermes digest
```

For Memory Store specifically, strong PLG intent is not just signup volume. The
stronger signs are team activation, connected context sources, brief creation,
cross-agent usage, and repeated recall/checkin behavior.

## Sending Rails

### Gmail

Gmail is the current default rail for founder-led and relationship-led outbound.
Use it for:

- sender voice learning.
- warm-path and prior-touch checks.
- Gmail drafts.
- approved first-touch sends.
- threaded followups.
- reply scans and outcome learning.

Default policy: draft first, send only after approval.

### Agent Mail

Agent Mail should be treated as an agent-owned mailbox rail once Hermes exposes
the adapter cleanly.

Use it for:

- campaigns where the sender identity is an agent or team mailbox.
- lower-risk experiments where founder Gmail should not be the execution rail.
- background followups that are explicitly approved.
- PLG nurture or product-assist flows that do not need the founder's personal
  thread history.

Before using it, the operating profile must define:

```text
mailbox identity
reply-to owner
signature
allowed campaign types
daily send cap
unsubscribe handling
reply routing
Memory Store record policy
```

### Resend

Resend should be treated as a programmatic email rail, not the default for
high-context founder outbound.

Use it for:

- product-triggered lifecycle emails.
- PLG nurture.
- approved newsletters or announcements.
- higher-volume campaigns after deliverability policy exists.
- system-generated notifications where Gmail threading is not needed.

Do not use Resend for relationship-led cold outbound until these are defined:

```text
domain and mailbox policy
unsubscribe handling
bounce handling
suppression sync
reply-to routing
daily and hourly limits
template approval
event webhook ingestion
Attio and Memory Store writeback
```

## Hermes Background Goals

Hermes should run precise goals, not broad "run GTM" jobs. Each routine needs a
goal, cadence, inputs, allowed actions, forbidden actions, stop conditions,
output, and Memory Store writeback policy.

### Daily Signal Card Builder

```yaml
routine_name: daily_signal_card_builder
host: Hermes
goal: Turn newly qualified Websets or PLG rows into signal cards for review.
cadence: daily
trigger: Websets idle, Attio view updated, or scheduled run
memory_context: active campaign thread and approved operating profile
required_tools:
  - Memory Store
  - Websets
  - Attio
inputs:
  - webset_id
  - Attio view: enriched or qualified rows
allowed_actions:
  - read rows
  - recall campaign context
  - score rows
  - create or update signal-card records
  - mark weak rows as research_more
forbidden_actions:
  - send email
  - create external drafts
  - expose private Memory Store context in Attio notes
stop_conditions:
  - missing source URL
  - missing personal email and LinkedIn URL
  - ambiguous company identity
  - connector error
output:
  - signal-card review queue
  - rejected-row summary
record_to_memory_store:
  - repeated sourcing learnings only
```

### Draft Batch Builder

```yaml
routine_name: draft_batch_builder
host: Hermes
goal: Generate Memory Store-aware drafts for approved signal cards.
cadence: manual or daily after owner approval
trigger: Attio rows move to signal_card_ready
required_tools:
  - Memory Store
  - Attio
  - selected sending rail
allowed_actions:
  - write local draft copy
  - update Attio draft fields
  - create Gmail or Agent Mail drafts only when draft policy is approved
forbidden_actions:
  - direct send
  - use private customer details unless approved
  - create drafts for excluded rows
output:
  - draft review packet
  - draft IDs when created
record_to_memory_store:
  - approved copy rules or repeated copy learnings only
```

### Reply Scan

```yaml
routine_name: reply_scan
host: Hermes
goal: Classify campaign replies and stop or advance followups.
cadence: daily, or every 2-4 hours during active sends
trigger: scheduled or sending-rail event
required_tools:
  - Gmail or Agent Mail or Resend event feed
  - Attio
  - Memory Store
allowed_actions:
  - inspect campaign threads/events
  - classify replies
  - update Attio status
  - stop followups on bounce, unsubscribe, negative reply, or meeting booked
  - record confirmed outcomes
forbidden_actions:
  - send new first-touch emails
  - delete or archive broad inbox
  - alter campaign policy
output:
  - reply table
  - owner action list
  - Memory Store records written or proposed
record_to_memory_store:
  - confirmed replies, objections, bounces, suppressions, meetings
```

### Daily Campaign Digest

```yaml
routine_name: daily_campaign_digest
host: Hermes
goal: Produce one operator digest for the active campaign.
cadence: daily
inputs:
  - Attio campaign views
  - Webset IDs
  - send ledger
  - reply scan
allowed_actions:
  - summarize counts and blockers
  - propose next actions
  - surface risky rows
forbidden_actions:
  - send email
  - change statuses except digest metadata
output:
  - sends, drafts, replies, meetings, bounces, suppressions, risks, next actions
```

### Weekly Learning Summary

```yaml
routine_name: weekly_campaign_learning
host: Hermes
goal: Convert confirmed campaign outcomes into better ICP, signal, copy, and channel rules.
cadence: weekly
required_tools:
  - Memory Store
  - Attio
  - sending rail events
allowed_actions:
  - summarize patterns
  - propose ICP and copy changes
  - record confirmed learnings
  - propose sparse brief deltas
forbidden_actions:
  - edit canonical briefs without approval
  - change send policy without approval
output:
  - learning summary
  - proposed operating-profile changes
  - brief delta proposals
```

## Aggressive Outbound Policy

Separate sourcing aggression from sending aggression.

Allowed early:

```text
source hundreds or thousands
score and dedupe in the background
create Attio review queues
generate draft packets
run daily digests
scan replies
```

Not allowed early:

```text
send hundreds from founder Gmail
send without signal cards
send without suppression checks
send without reply/bounce handling
send without approved claim boundaries
send from Resend without unsubscribe and bounce policy
```

Default ramp:

```text
batch_0: 5 local drafts only
batch_1: 5-10 external drafts
send_1: 5 approved sends
days_2_3: max 10/day
later: max 20/day
higher volume: only after bounce, reply, and negative-reply quality are known
```

The ramp is a ceiling, not a quota. The routine should send fewer or none when
signal quality, sender health, suppression, or policy state is weak.

## First Campaign: Portable Company Context

Campaign thesis:

```text
AI-native teams are adopting agents faster than they are building shared
context. Memory Store turns scattered company context from Slack, calls, docs,
Gmail, code, customer work, and agent sessions into living briefs and portable
memory for humans and agents.
```

Do not lead with "second brain". Do not lead with generic RAG. Do not sell the
prospect their own product back. Lead with the missing shared-context layer
under their agents and workflows.

Working CTA:

```text
Worth sending over a concrete example of what a customer, project, or company
brief could look like for your workflow?
```

Current first-batch source:

```text
campaign-exports/portable-company-context/people-batch-1.websets-enriched.csv
```

Before any send:

```text
1. Select 5-10 rows.
2. Build signal cards.
3. Rewrite Websets angles into Memory Store-aware angles.
4. Create local drafts.
5. Owner reviews.
6. Create Gmail or Agent Mail drafts.
7. Owner approves sends.
8. Send small batch.
9. Hermes scans replies and writes outcomes.
```

## Adapter Readiness

Current repo-level v1 is optimized around Gmail and Google Calendar. Attio,
Agent Mail, and Resend may be part of the broader Hermes stack, but GTM Agent
should treat them as adapters until verified in the active host.

Adapter checklist:

```text
can create/update records?
can read campaign views?
can create draft/send events?
can receive reply/bounce/unsubscribe events?
can write stable IDs back to the ledger?
can enforce suppression before send?
can expose errors clearly?
can record durable outcomes to Memory Store?
```

If an adapter is not verified, GTM Agent should output import-ready CSVs,
routine specs, and draft packets rather than claiming automation ran.

