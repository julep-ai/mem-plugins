# Learning Loop

Use this reference when recording GTM outcomes, setup rules, user corrections, approval policies, and self-improvement candidates back to Memory Store.

Memory Store `record` is a natural-language quick jot, not a typed event API. Write specific prose that future agents can recall.

Always pass the active `thread_id` from `checkin`.

## Self-Learning Contract

GTM Agent is a long-term-memory agent and proactive intelligence layer, not a static prompt bundle. Its loop is:

```text
checkin -> recall durable rules -> surface relevant context -> execute under those rules -> observe user feedback/outcomes -> distill operational memory -> record -> improve later runs
```

During setup and execution, identify durable operating memory:

- `operating_rule` - what the agent must always or never do for this seller/campaign/plugin.
- `preference` - user taste, workflow preference, channel preference, writing preference, approval preference.
- `constraint` - excluded ICPs, taboo claims, connector limits, compliance boundaries, do-not-contact categories.
- `approval_policy` - actions allowed after plan approval, actions requiring explicit approval, stop conditions.
- `connector_rule` - how Memory Store, Exa, Websets, Gmail, Calendar, monitors, or host automations should be used.
- `persona_rule` - ICP/persona definitions, excluded personas, unconventional persona hypotheses, owner-of-pain framing.
- `sourcing_rule` - signal quality gates, required identity fields, email/LinkedIn policy, enrichment expectations.
- `campaign_learning` - what changed after replies, bounces, objections, meetings, weak rows, or strong rows.
- `skill_improvement_candidate` - repeated failure, missing eval, confusing instruction, bad default, or workflow gap.

Use this shape in prose when recording:

```text
kind:
scope: seller | campaign | plugin | channel | ICP | connector | skill
status: proposed | approved | active | deprecated
source: conversation | gtm_plan | user_feedback | execution_result | campaign_outcome
rule_or_learning:
evidence:
future_behavior:
```

Record when the user explicitly sets a rule, corrects the agent, approves a GTM plan, changes policy, confirms a result, or says future runs should behave differently. Do not record every brainstorm, unapproved draft, transient idea, or speculative inference. If the rule is important but not yet approved, include `status: proposed` and ask for confirmation before using it for sends or external actions.

## When To Record

Record confirmed events:

- Campaign or ICP plan approved.
- First-run GTM plan approved or changed.
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
- Conversation rule, preference, constraint, or approval policy stated by the user.
- First-run plan correction that should change future planning behavior.
- Connector expectation such as agent-led monitoring, Exa/Websets depth, Gmail limits, or dashboard/manual fallback policy.
- Skill-improvement candidate discovered during execution or user feedback.

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

### GTM plan approved

`content`:

> The user approved the GTM plan for `<company>` today. Active offer: `<offer>`. Sender: `<sender>`. Demo CTA: `<confirmed link or fallback>`. Autopilot: `<full autopilot | draft-first>` with ramp `<limits>`. Approved ICP cells: `<list>`. Same-company rule: `<rule>`. Followups: `<cadence>`. Stop conditions: `<summary>`.

`background`:

> GTM plan sources and gaps: website `<URL>`, Gmail scope `<scope>`, Google Calendar policy `<policy>`, exclusions `<summary>`, connector gaps `<summary>`.

### Automation routine approved

`content`:

> The user approved a GTM Agent automation routine for `<company>` today. Routine: `<routine_name>`. Goal: `<goal>`. Cadence: `<cadence>`. Host: `<Codex | Claude Code | Claude Cowork | OpenCode | manual>`. Allowed actions: `<summary>`. Forbidden actions: `<summary>`. Stop conditions: `<summary>`. Expected output: `<digest | draft queue | send summary | followup queue | monitor review | learning summary>`.

`background`:

> Campaign context: `<campaign/thread/ICP>`. Required tools: `<Memory Store, Exa, Websets, Gmail, Calendar, host automation>`. Record policy: `<what gets recorded>`. Owner review needed when: `<conditions>`.

### Conversational rule distilled

`content`:

> GTM Agent operating memory for `<company/plugin/campaign>` from today. Kind: `<operating_rule | preference | constraint | approval_policy | connector_rule | persona_rule | sourcing_rule>`. Scope: `<seller | campaign | plugin | channel | ICP | connector | skill>`. Status: `<proposed | approved | active | deprecated>`. Rule: `<specific durable instruction>`. Future GTM Agent runs should `<future behavior>`.

`background`:

> Source: user conversation/GTM plan/user feedback. Evidence: `<memory IDs, artifact path, source URL, Gmail thread, Webset ID, or direct user correction summary>`.

### Skill improvement candidate

`content`:

> GTM Agent skill-improvement candidate from today. Failure/gap: `<what went wrong or felt weak>`. Expected behavior: `<what future agents should do>`. Suggested update: `<eval/reference/SKILL.md/docs change>`. Priority: `<high | medium | low>`.

`background`:

> Source and reproduction: `<prompt, campaign mode, connector state, artifact path, or user feedback summary>`.

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
