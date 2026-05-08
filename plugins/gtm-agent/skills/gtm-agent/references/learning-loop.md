# Learning Loop

Use this reference when recording GTM outcomes back to Memory Store.

Memory Store `record` is a natural-language quick jot, not a typed event API. Write specific prose that future agents can recall.

Always pass the active `thread_id` from `checkin`.

## When To Record

Record confirmed events:

- Campaign or ICP plan approved.
- ICP cell added, removed, or reframed.
- Account/source signal accepted or rejected.
- Copy variant approved, edited, rejected, sent, or scheduled.
- Reply received and classified.
- Objection heard.
- Meeting booked.
- Bounce, unsubscribe, or do-not-contact event.
- Performance update from the user or mailbox/campaign system.
- Approved claim, customer name, metric, or taboo topic update.

Do not record drafts the user never saw, outcomes inferred from silence, guessed metrics, or private claims that were not approved.

## Record Templates

### Campaign plan approved

`content`:

> The user approved a GTM campaign plan for `<company>` today. Goal: `<goal>`. Scale: `<recipient count>` recipients across `<ICP count>` ICP cells. Channels: `<email | LinkedIn | mixed>`. The strongest thesis was `<one sentence>`. Approved ICP cells: `<list>`.
>
> Source memories and public sources used: `<IDs/URLs>`.

`background`:

> Exclusions, sender policy, and approval constraints: `<one paragraph>`.

### ICP refined

`content`:

> ICP refinement for `<company>`: `<cell name>` was `<added | removed | reframed>`. Reason: `<user reason or evidence>`. New definition: buyer `<buyer>`, pain `<pain>`, signals `<signals>`, exclusions `<exclusions>`.

### Signal accepted or rejected

`content`:

> GTM signal learning for `<company>`: `<signal type>` was `<accepted | rejected>` for `<ICP/account>`. Reason: `<specific reason>`. Source: `<URL or memory ID>`. Future sourcing should `<instruction>`.

### Copy variant outcome

`content`:

> Copy outcome for `<company>` outbound to `<ICP/account/person>`. Variant `<variant label>` was `<approved | edited | rejected | sent>`. User feedback: "`<quote if available>`". Final text or summary: `<text/summary>`. Hypothesis tested: `<one line>`.

### Reply or objection

`content`:

> Outbound reply learning for `<company>` from `<account/person>` today. ICP cell: `<cell>`. Signal used: `<signal>`. Copy variant: `<variant>`. Outcome: `<positive reply | objection | referral | not now | unsubscribe | bounce>`. Reply summary: `<one paragraph>`. Next action: `<action>`.

### Meeting booked

`content`:

> Meeting booked from GTM campaign for `<company>`. Account/person: `<name>`. ICP cell: `<cell>`. Signal: `<signal>`. Copy variant: `<variant>`. What seemed to work: `<one sentence>`. Meeting time or link if known: `<details>`.

### Performance update

`content`:

> GTM performance update for `<company>` campaign `<campaign name>` as of `<date>`. Sent: `<n>`. Replies: `<n>`. Positive replies: `<n>`. Meetings: `<n>`. Bounces: `<n>`. Unsubscribes: `<n>`. Best ICP: `<cell>`. Best signal: `<signal>`. Best copy angle: `<variant>`. Main failure pattern: `<pattern>`.

## Learning Dimensions

When summarizing results, slice by:

- ICP cell
- Signal type and source
- Buyer title
- Company stage/size/vertical
- Copy variant
- Sender
- Channel
- Objection
- Outcome
- Time lag from signal to outreach

The goal is not just "reply rate went up"; it is knowing which account context, signal, and message became predictive.
