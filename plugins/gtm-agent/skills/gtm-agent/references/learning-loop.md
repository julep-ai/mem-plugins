# Learning Loop

Use this reference when recording GTM outcomes back to Memory Store.

Memory Store `record` is a natural-language quick jot, not a typed event API. Write specific prose that future agents can recall.

Always pass the active `thread_id` from `checkin`.

## When To Record

Record confirmed events:

- Campaign or ICP plan approved.
- First-run setup packet approved or changed.
- Campaign mode or context-source base approved or changed.
- Uploaded/pasted docs approved as campaign source context.
- ICP cell added, removed, or reframed.
- Account/source signal accepted or rejected.
- Copy variant approved, edited, rejected, sent, or scheduled.
- Email/LinkedIn channel policy approved, changed, or measured.
- Reply received and classified.
- Objection heard.
- Meeting booked.
- Bounce, unsubscribe, or do-not-contact event.
- Performance update from the user or mailbox/campaign system.
- Approved claim, customer name, metric, or taboo topic update.
- Automation routine approved, paused, changed, or retired.

Do not record drafts the user never saw, outcomes inferred from silence, guessed metrics, or private claims that were not approved.

## Record Templates

### Campaign plan approved

`content`:

> The user approved a GTM campaign plan for `<company>` today. Goal: `<goal>`. Scale: `<recipient count>` recipients across `<ICP count>` ICP cells. Daily sourcing target if any: `<count>`. Channels: `<email | LinkedIn | mixed>`. The strongest thesis was `<one sentence>`. Approved ICP cells: `<list>`.
>
> Source memories and public sources used: `<IDs/URLs>`.

`background`:

> Exclusions, sender policy, and approval constraints: `<one paragraph>`.

### Campaign system approved

`content`:

> The user approved the GTM campaign system for `<company>` today. Campaign mode: `<plan_new_campaign | start_new_campaign | monitor_campaign | campaign_insights | update_prior_campaign | new_campaign | build_on_previous | refresh_existing | expand_winner | rescue_underperformer | reactivation | event_or_launch>`. Context sources approved: `<Memory Store, uploaded docs, pasted notes, website, Gmail, Calendar, prior campaign artifacts, Exa/Websets>`. Funnel stages being engineered: `<summary>`. ICP system: `<summary>`. Signal system: `<summary>`. Channel system: `<email/LinkedIn policy>`. Learning system: `<summary>`.

`background`:

> Source context and constraints: `<doc names, memory IDs, URLs, Gmail scope, calendar policy, exclusions, open decisions>`.

### Setup packet approved

`content`:

> The user approved GTM Agent setup for `<company>` today. Active offer: `<offer>`. Sender: `<sender>`. Demo CTA: `<confirmed link or fallback>`. Autopilot: `<full autopilot | draft-first>` with ramp `<limits>`. Approved ICP cells: `<list>`. Same-company rule: `<rule>`. Followups: `<cadence>`. Stop conditions: `<summary>`.

`background`:

> Setup packet sources and gaps: website `<URL>`, Gmail scope `<scope>`, Google Calendar policy `<policy>`, exclusions `<summary>`, connector gaps `<summary>`.

### Automation routine approved

`content`:

> The user approved a GTM Agent automation routine for `<company>` today. Routine: `<routine_name>`. Goal: `<goal>`. Cadence: `<cadence>`. Host: `<Codex | Claude Code | Claude Cowork | OpenCode | manual>`. Allowed actions: `<summary>`. Forbidden actions: `<summary>`. Stop conditions: `<summary>`. Expected output: `<digest | draft queue | send summary | followup queue | monitor review | learning summary>`.

`background`:

> Campaign context: `<campaign/thread/ICP>`. Required tools: `<Memory Store, Exa, Websets, Gmail, Calendar, host automation>`. Record policy: `<what gets recorded>`. Owner review needed when: `<conditions>`.

### ICP refined

`content`:

> ICP refinement for `<company>`: `<cell name>` was `<added | removed | reframed>`. Reason: `<user reason or evidence>`. New definition: buyer `<buyer>`, pain `<pain>`, customer-story/persona pattern `<pattern>`, signals `<signals>`, exclusions `<exclusions>`, learning intent `<intent>`.

### Signal accepted or rejected

`content`:

> GTM signal learning for `<company>`: `<signal type>` was `<accepted | rejected>` for `<ICP/account>`. Reason: `<specific reason>`. Source: `<URL or memory ID>`. Future sourcing should `<instruction>`.

### Channel outcome

`content`:

> Channel outcome for `<company>` outbound to `<ICP/account/person>` today. Channel policy: `<email_only | linkedin_only | email_plus_linkedin>`. Persona: `<persona>`. Signal: `<signal>`. Copy hypothesis: `<hypothesis>`. Outcome: `<reply | connection | objection | meeting | no response | bounce | unsubscribe | no-contact>`. Learning: `<what changed for future channel selection>`.

### Copy variant outcome

`content`:

> Copy outcome for `<company>` outbound to `<ICP/account/person>`. Variant `<variant label>` was `<approved | edited | rejected | sent>`. User feedback: "`<quote if available>`". Final text or summary: `<text/summary>`. Hypothesis tested: `<one line>`. Customer-story/persona pattern used: `<pattern>`.

### Reply or objection

`content`:

> Outbound reply learning for `<company>` from `<account/person>` today. ICP cell: `<cell>`. Signal used: `<signal>`. Copy variant: `<variant>`. Outcome: `<positive reply | objection | referral | not now | unsubscribe | bounce>`. Reply summary: `<one paragraph>`. Next action: `<action>`.

### Meeting booked

`content`:

> Meeting booked from GTM campaign for `<company>`. Account/person: `<name>`. ICP cell: `<cell>`. Signal: `<signal>`. Copy variant: `<variant>`. What seemed to work: `<one sentence>`. Meeting time or link if known: `<details>`.

### Performance update

`content`:

> GTM performance update for `<company>` campaign `<campaign name>` as of `<date>`. Sent: `<n>`. Replies: `<n>`. Positive replies: `<n>`. Meetings: `<n>`. Bounces: `<n>`. Unsubscribes: `<n>`. Best ICP: `<cell>`. Best signal: `<signal>`. Best copy angle: `<variant>`. Main failure pattern: `<pattern>`.

### Campaign update from insights

`content`:

> Campaign update for `<company>` based on recent GTM insights. Changed ICPs: `<summary>`. Changed signal rules: `<summary>`. Changed copy hypotheses: `<summary>`. Changed channel policy: `<summary>`. Customer stories/personas to mine next: `<summary>`. Killed experiments: `<summary>`. Next batch should `<instruction>`.

## Learning Dimensions

When summarizing results, slice by:

- ICP cell
- Signal type and source
- Buyer title
- Company stage/size/vertical
- Copy variant
- Sender
- Channel
- Customer-story/persona pattern
- Email plus LinkedIn identity confidence
- Objection
- Outcome
- Time lag from signal to outreach

The goal is not just "reply rate went up"; it is knowing which account context, signal, and message became predictive.
