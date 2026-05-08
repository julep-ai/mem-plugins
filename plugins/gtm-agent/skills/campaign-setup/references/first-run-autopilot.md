# First-Run Autopilot

Use this reference when creating the first setup packet or turning an approved setup into autonomous GTM routines.

## Setup Approval

Setup approval is the one-time gate that replaces per-batch approval. Before approval, do not send. After approval, GTM Agent may source, draft, send, follow up, inspect replies, run host automations, and record learnings inside the approved policy.

The approval must cover:

- active offer profile.
- sender identity and brand voice.
- confirmed demo CTA or reply-first fallback.
- ICP cells and company-size range.
- claims, taboo claims, and proof path.
- send ramp and followup cadence.
- suppression and stop conditions.
- connector gaps and manual fallbacks.
- routine specs for any asynchronous automation.

## Autopilot Mode

Autopilot is the core product behavior: the user engineers the campaign once, approves the policy, and the host keeps running precise routines toward the campaign goal.

Approved routines may run daily, weekly, every few hours, or on monitor/reply events. Each routine needs:

- one explicit goal.
- cadence or trigger.
- Memory Store thread/context.
- required connectors.
- allowed actions.
- forbidden actions.
- send policy and ramp limits.
- stop conditions.
- expected output.
- what to record back to Memory Store.

If the current host cannot schedule routines, output the exact routine specs and mark them `manual_until_scheduled`. Do not weaken the autopilot claim; surface the missing host capability.

## Send Ramp

Default ramp:

- day 1: max 10 sends.
- days 2-3: max 20 sends per day.
- day 4 onward: max 50 sends per day until the user changes policy.

The ramp is a ceiling, not a quota. Send fewer when signal quality, evidence, mailbox health, or personalization confidence is weak.

## Followup Cadence

Default followups:

- followup 1: 3-4 business days after first touch.
- followup 2: 6-8 business days after first touch.
- breakup: 12-15 business days after first touch.

Stop followups on reply, booking, bounce, unsubscribe, negative reply, active referral, or do-not-contact signal.

## Same-Company Rule

Default rule:

- max 2 contacts per company.
- contacts must represent meaningfully different personas or workflows.
- one primary active thread per company.
- referral creates a related lead only if the referred person is relevant and not suppressed.

## Gmail Routines

Default Gmail routines:

- scan replies and active campaign threads every 2 hours.
- classify positive reply, objection, referral, not now, unsubscribe, bounce, out-of-office, or no action.
- summarize qualified replies and owner actions.
- record confirmed replies, objections, meetings, bounces, and suppressions to Memory Store.

If Gmail is unavailable, produce import-ready send/followup queues and mark Gmail automation disabled.

## Google Calendar Routines

Use Google Calendar for scheduling context after qualified replies:

- respect the confirmed demo link first.
- use calendar context for availability, meeting duration, timezone, and conflicts when tools are available.
- do not create or move events unless the user explicitly asks or the approved campaign policy includes calendar actions.

If Google Calendar is unavailable, keep the confirmed demo link and mark scheduling automation disabled.

## Digest And Learning Routines

Default routines:

- daily campaign digest with sends, replies, meetings, objections, bounces, suppressions, and next actions.
- weekly ICP/signal/copy learning summary.
- weekly suppression-list update.
- Websets refresh for approved account pools.
- monitor review for approved Exa monitor specs.

Learning records should explain what changed about ICP, signal quality, copy angle, objection handling, proof path, or suppression policy.

## Automation Specs

Use `../../gtm-agent/references/automation-routines.md` when converting any of these routines into a host automation. Do not schedule a vague "do GTM" job. The automation prompt should name the exact routine, goal, cadence, approved campaign context, required tools, allowed actions, forbidden actions, stop conditions, and output.

## Stop Conditions

Pause sending and report when:

- bounce rate or deliverability risk appears.
- unsubscribe, do-not-contact, or negative reply appears.
- duplicate recent outreach or active existing thread is detected.
- source evidence is missing, stale, or contradicted.
- a claim is unapproved or risks leaking private Memory Store context.
- spam/reputation warning appears.
- daily ramp cap would be exceeded.
- Gmail or Google Calendar connector behavior is ambiguous.

Paused campaigns may keep researching, scoring, and preparing drafts, but they must not send until the stop reason is resolved.
