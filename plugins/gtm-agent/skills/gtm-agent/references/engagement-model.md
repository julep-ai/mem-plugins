# Engagement Model

Use this reference when designing the campaign workflow, review gates, followup logic, or engagement readout.

## Core Principle

Do not design this as "Exa finds leads, Gmail sends emails." Design it as an experiment system:

```text
ICP hypotheses -> evidence-backed accounts -> reviewed personalization -> controlled sends -> engagement capture -> Memory Store learning -> next batch
```

## Campaign Entities

Track these concepts in the working output even if the host does not have a database yet:

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

## Review Gates

Minimum gates:

- Campaign brief approved.
- ICP list approved.
- First lead batch per ICP approved.
- Representative copy approved.
- Gmail drafts created before sends.
- Send batch explicitly approved.
- Followups drafted before sending unless the user has approved delegated followup behavior.

Hard blocks:

- No source evidence.
- No valid sender identity.
- Duplicate recent outreach.
- Existing customer or competitor excluded by policy.
- Unsubscribe, bounce, do-not-contact, or negative reply.
- Hallucinated or unapproved claim.
- Sensitive private Memory Store detail in outbound copy.
- Too many sends for the mailbox policy.

## States

Use clear states when reporting campaign progress:

```text
planned -> sourcing -> sourced -> qualified -> drafted -> review_needed -> approved -> sent -> replied -> next_action -> learned
```

Terminal or suppressing states:

```text
rejected, excluded, bounced, unsubscribed, negative_reply, no_contact, stale_signal, duplicate
```

## Gmail Followup Logic

Default behavior:

- First touch is drafted or sent only after approval.
- No reply after the configured wait creates a followup draft.
- Positive reply stops automation, summarizes the thread, and suggests owner action.
- Negative reply records the objection and suppresses further outreach.
- Unsubscribe or do-not-contact suppresses future outreach.
- Bounce suppresses the email and optionally asks whether to find another contact.
- Out-of-office reschedules followup.
- Referral creates a new related lead if the user wants to pursue it.

MVP should draft followups, not auto-send them.

## Engagement Readout

Do not over-optimize on opens. Use this order:

1. Qualified opportunities or booked meetings
2. Positive replies
3. Useful objections or referrals
4. Reply rate
5. Bounce/unsubscribe rate
6. Opens/clicks, only if available and reliable

Slice results by ICP cell, signal source, buyer title, company stage, copy variant, sender, channel, objection, and time from signal to outreach.

## MVP Boundary

MVP is a skill/playbook, not a full autonomous sales product:

- one primary channel: email/Gmail
- one sender identity unless the user says otherwise
- draft-first behavior
- representative samples before any send
- batch review by ICP
- Memory Store records after each approval, send, reply, objection, meeting, or performance update
- Websets persists account pools where available

Later product work can add autonomous send limits, multi-mailbox rotation, CRM sync, LinkedIn/X expansion, Websets monitors, adaptive bandits, deliverability monitoring, and team approval dashboards.
