# Automation Routines

Use this reference when turning an approved GTM plan into daily, weekly, or event-driven host automations.

## Autopilot Definition

Autopilot means the user engineers the GTM campaign once, approves the operating policy, and then the host runs precise asynchronous routines against that policy.

It is not uncontrolled bulk sending. Each routine has one goal, one cadence, known tools, allowed actions, forbidden actions, stop conditions, and an expected output. Start small, record outcomes, and widen only when Memory Store evidence supports it.

## Routine Spec

Every routine should be written in this shape before it is scheduled:

```text
routine_name:
host:
goal:
cadence:
trigger:
memory_context:
brief_context:
required_tools:
inputs:
allowed_actions:
forbidden_actions:
send_policy:
stop_conditions:
output:
record_to_memory_store:
brief_delta_policy:
owner_review_needed_when:
```

Field rules:

- `routine_name` - stable name, e.g. `daily_websets_refresh_review`.
- `host` - `Codex`, `Claude Code`, `Claude Cowork`, `OpenCode`, or `manual`.
- `goal` - one measurable outcome, not a bundle of vague tasks.
- `cadence` - daily, weekly, every N hours, or manual until the host supports scheduling.
- `trigger` - time-based, monitor event, Gmail reply, Websets idle, or user request.
- `memory_context` - Memory Store thread ID, campaign name, ICP cell, or approved GTM plan reference.
- `brief_context` - the 0-3 canonical briefs the routine should use as operating maps, such as GTM operating policy, ICP/persona map, proof/claims, campaign learning, or important account brief.
- `required_tools` - Memory Store, Exa, Websets, Gmail, Google Calendar, or host automation support.
- `inputs` - Webset IDs, monitor IDs, Gmail labels/searches, ICP cells, campaign rows, or suppression lists.
- `allowed_actions` - actions the routine may take without more approval.
- `forbidden_actions` - actions that always require explicit user approval.
- `send_policy` - max sends, followup rules, same-company rule, and draft-only fallback.
- `stop_conditions` - bounce, unsubscribe, duplicate thread, stale evidence, connector ambiguity, or policy mismatch.
- `output` - digest, draft queue, send summary, followup queue, monitor review, learning proposal, or escalation.
- `record_to_memory_store` - what confirmed event or learning should be recorded.
- `brief_delta_policy` - when the routine may propose a canonical brief update. Most routine outputs should be records only.
- `owner_review_needed_when` - exact situations where the routine must pause and ask.

## Core Routines

Start with these routines after plan approval:

- **Daily Websets refresh review** - inspect approved Websets, summarize new candidates, score against ICP cells, and keep weak rows out of send-ready state.
- **Daily high-intent monitor review** - inspect approved monitor results, dedupe against existing accounts, identify high-intent signals, and propose new signal cards.
- **Gmail reply scan** - classify campaign replies, stop followups when needed, summarize owner actions, and record confirmed outcomes.
- **Followup check** - find sent threads eligible for the next followup, enforce stop conditions, and send or draft according to the approved policy.
- **Daily campaign digest** - report sends, drafts, replies, meetings, bounces, suppressions, risks, and next actions.
- **Weekly campaign insights** - update ICP, signal, copy, objection, channel, customer-story/persona, and suppression learnings from confirmed events; propose sparse brief deltas only when repeated evidence changes future behavior.
- **Prior campaign update** - apply approved insights to a prior campaign's ICP cells, signal rules, copy hypotheses, channel policy, and suppressions.

## Host Mapping

Use the strongest scheduling primitive the host exposes:

- **Codex** - create recurring automations for approved routines.
- **Claude Code** - use the host's recurring task or external scheduler if available; otherwise output the routine prompt and exact cadence.
- **Claude Cowork** - use Cowork scheduled/recurring agent capability when available; otherwise keep the routine as an approved manual runbook.
- **OpenCode** - use configured MCP plus external scheduler or manual runbook until plugin scheduling is verified.

If scheduling is unavailable, do not weaken the autopilot model. Return the exact routine specs and say which host capability is missing.

## Small And Slow Ramp

The first autopilot run should usually be:

```text
day_1: research + max 10 sends
days_2_3: review learnings + max 20 sends/day
day_4_plus: max 50 sends/day only if bounce, unsubscribe, and negative-reply risk stay low
```

The ramp is a ceiling, not a quota. A routine should send fewer or none when signal quality, evidence, sender health, or connector state is weak.

Daily sourcing targets can be much higher than daily sends. For example, a campaign may source and score around 1000 leads/emails per day across Websets and Exa, while sending only the approved ramp subset that passes signal-card, suppression, and Gmail health gates.

## Example Routine

```text
routine_name: daily_gmail_reply_scan
host: Codex
goal: classify new campaign replies and stop or advance followups
cadence: daily at 09:00 local time
trigger: scheduled
memory_context: approved GTM plan and active campaign thread
brief_context: GTM operating policy and campaign learning brief, if present
required_tools: Memory Store, Gmail
inputs: campaign Gmail label, sent thread IDs, suppression list
allowed_actions: inspect campaign threads, classify replies, draft owner summary, record confirmed outcomes
forbidden_actions: delete, archive, label broad inbox, send non-followup email, change calendar events
send_policy: no new first touches; followups only if already approved and no stop condition exists
stop_conditions: unsubscribe, bounce, negative reply, duplicate active thread, ambiguous Gmail result
output: reply classification table, owner actions, records written or proposed
record_to_memory_store: confirmed replies, objections, bounces, suppressions, meetings
brief_delta_policy: propose a campaign learning or suppression-policy brief delta only after repeated confirmed patterns, not for one reply
owner_review_needed_when: high-value reply, ambiguous intent, connector error, or policy conflict
```
