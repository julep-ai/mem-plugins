# Engagement Model

Use this reference when designing the campaign workflow, review gates, followup logic, or engagement readout.

## Core Principle

Do not design this as "Exa finds leads, Gmail sends emails." Design it as an experiment system:

```text
setup approval -> ICP hypotheses -> evidence-backed accounts -> approved automation routines -> controlled sends -> engagement capture -> Memory Store learning -> next batch
```

## Campaign Entities

Track these concepts in the working output even if the host does not have a database yet:

- **setup packet** - company profile, offer profiles, sender voice, website findings, demo CTA, ICP matrix, signal sources, Gmail learnings, calendar policy, send ramp, autopilot routines, and approval blockers.
- **campaign** - company, goal, offer, CTA, sender, send policy, review policy, scale, status.
- **ICP cell** - name, buyer, criteria, trigger signals, pain hypothesis, target count, confidence.
- **account** - company/domain, fit score, timing score, source URLs, evidence summary, risk.
- **contact** - name/title/email if known, persona, source URLs, prior relationship, suppression state.
- **evidence** - source URL or memory ID, claim, freshness, relevance, whether it is safe to use in copy.
- **copy variant** - subject, body, CTA, angle, hypothesis, evidence IDs, risk flags, review status.
- **message** - draft/sent/thread IDs when available, sequence step, send status, reply status.
- **engagement event** - reply, meeting, objection, bounce, unsubscribe, referral, qualitative note.
- **learning** - what changed about ICP, signal, copy, channel, account, or objection handling.
- **suppression** - email/domain/reason/source for no-contact and future exclusion.
- **routine** - goal, cadence, host, tools, allowed actions, forbidden actions, stop conditions, output, and Memory Store record target.

## Review Gates

Minimum gates before autopilot starts:

- Setup packet approved.
- Demo CTA confirmed or reply-first fallback approved.
- Sender identity and brand voice approved.
- ICP list and company-size range approved.
- Representative copy approved.
- Send ramp, same-company rule, followup cadence, and stop conditions approved.
- Routine specs approved for any asynchronous host automation.
- Claims, taboo claims, private-memory policy, and suppressions approved.

After setup approval, per-batch approval is not required by default. Full autopilot may send and follow up inside the approved policy. If the user chooses draft-first mode, preserve per-batch approval.

Hard blocks:

- No source evidence.
- No valid sender identity.
- Duplicate recent outreach.
- Existing customer or competitor excluded by policy.
- Unsubscribe, bounce, do-not-contact, or negative reply.
- Hallucinated or unapproved claim.
- Sensitive private Memory Store detail in outbound copy.
- Too many sends for the mailbox policy.
- Google Calendar or Gmail connector behavior is ambiguous.

## States

Use clear states when reporting campaign progress:

```text
setup_needed -> setup_review -> approved -> routine_ready -> sourcing -> sourced -> qualified -> drafted -> sent -> replied -> next_action -> learned
```

Terminal or suppressing states:

```text
rejected, excluded, bounced, unsubscribed, negative_reply, no_contact, stale_signal, duplicate
```

## Gmail Followup Logic

Default behavior:

- First touch is never sent before setup approval.
- After setup approval, first touch may send automatically inside the approved ramp and stop conditions.
- No reply after the configured wait creates a followup draft.
- Positive reply stops automation, summarizes the thread, and suggests owner action.
- Negative reply records the objection and suppresses further outreach.
- Unsubscribe or do-not-contact suppresses future outreach.
- Bounce suppresses the email and optionally asks whether to find another contact.
- Out-of-office reschedules followup.
- Referral creates a new related lead if the user wants to pursue it.

Default followups after setup approval may send automatically inside the approved policy. If risk appears, switch to draft-only until resolved.

## Send Ramp

Default ramp:

- day 1: max 10 sends.
- days 2-3: max 20 sends per day.
- day 4 onward: max 50 sends per day until changed.

The ramp is a ceiling, not a quota. Send fewer when signal quality or mailbox health is weak.

## Google Calendar Booking Context

Use Google Calendar for scheduling context after qualified replies:

- prefer the confirmed demo or Cal link when available.
- use availability and timezone context only when the connector is available.
- do not create, update, or move calendar events unless explicitly approved.
- if Calendar is unavailable, keep the confirmed demo link and mark scheduling automation disabled.

## Engagement Readout

Do not over-optimize on opens. Use this order:

1. Qualified opportunities or booked meetings
2. Positive replies
3. Useful objections or referrals
4. Reply rate
5. Bounce/unsubscribe rate
6. Opens/clicks, only if available and reliable

Slice results by ICP cell, signal source, buyer title, company stage, copy variant, sender, channel, objection, and time from signal to outreach.

## V1 Boundary

V1 is a plugin-level autopilot, not a separate dashboard:

- one primary channel: email/Gmail
- one sender identity unless the user says otherwise
- full autopilot after setup approval
- approved routine specs for asynchronous daily/weekly work
- representative samples during setup before autopilot starts
- ramped sends with hard stop conditions
- Google Calendar context for qualified replies
- Memory Store records after each approval, send, reply, objection, meeting, or performance update
- Websets persists account pools where available

Later product work can add Outlook/Microsoft support, multi-mailbox rotation, CRM sync, LinkedIn/X expansion, adaptive bandits, deliverability dashboards, and team approval dashboards.
