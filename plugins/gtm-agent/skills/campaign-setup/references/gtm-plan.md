# GTM Plan Contract

Use this reference when GTM Agent returns the first-run GTM plan or updates an approved campaign plan. The plan is the durable contract between planning, sourcing, Gmail execution, Calendar context, and Memory Store learning.

## Exact Shape

Return these keys in this order:

```text
company_profile:
campaign_mode:
context_sources:
connector_status:
briefs_used:
offer_profiles:
customer_usage_map:
sender_voice:
website_findings:
demo_cta:
funnel_system:
icp_matrix:
signal_sources:
gmail_learnings:
calendar_policy:
channel_policy:
send_ramp_policy:
autopilot_routines:
memory_distillation:
brief_delta:
approval_needed_before_start:
```

Do not rename keys. If a value is unavailable, mark it as `unknown`, `missing_connector`, or `needs_user_confirmation`.

## Field Requirements

- `company_profile`: company name, website, one-line product read, market category, confidence, and missing facts.
- `campaign_mode`: `plan_new_campaign`, `start_new_campaign`, `monitor_campaign`, `campaign_insights`, `update_prior_campaign`, `new_campaign`, `build_on_previous`, `refresh_existing`, `expand_winner`, `rescue_underperformer`, `reactivation`, or `event_or_launch`; include evidence and policy implications.
- `context_sources`: Memory Store, uploaded/pasted docs, website, Gmail, Calendar, prior campaign artifacts, Exa/Websets, and what each source is allowed to influence.
- `connector_status`: production/degraded mode for Memory Store, Exa Search, Websets, Exa Monitors, Gmail, Calendar, and host automations. Mark missing Exa as `research_blocked_for_production`, missing Websets as `sourcing_blocked_for_production`, missing Monitors as `monitoring_degraded`, missing Gmail as `sending_blocked_for_production`, and missing Calendar as `booking_context_disabled`. If Exa or Websets credentials are missing, the plan status is `plan_only` until the user configures the Exa API key. If Gmail is missing, sends, reply monitoring, followups, and mailbox learning are blocked.
- `briefs_used`: 0-3 canonical Memory Store briefs selected for this plan, their status (`active`, `stale`, `conflicted`, or `none`), and what each brief is allowed to influence. If no relevant brief exists, say `none` and use recall.
- `offer_profiles`: active offer, alternate sellable offers, core claim, do-not-pitch list, proof path, and conversion action.
- `customer_usage_map`: the seller's existing customers/users when discoverable, plus the usage patterns that should shape ICPs. Include named customers/accounts when public or approved, customer categories, user segments, case studies, testimonials, reviews, active-user cohorts, churn/loss patterns, activation gaps, observed job-to-be-done, source URLs, and private Memory Store/Gmail/CRM evidence IDs where allowed. For Memory Store-owned campaigns, this means Memory Store's own customers/users. For another seller, this means that seller's customers/users. If no customers/users can be found, mark `unknown_or_not_public` and include the Exa/Websets customer-proxy searches used.
- `sender_voice`: sender identity, tone, phrases to use, phrases to avoid, and whether it came from Memory Store, Gmail, website, or user input.
- `website_findings`: website pages checked, claims found, proof assets, screenshots/assets worth collecting, and risky or unsupported claims.
- `demo_cta`: discovered link candidates, chosen link, confirmation status, CTA style, and fallback CTA.
- `funnel_system`: funnel stages being engineered, current stage strengths/gaps, and which stages can be filled by background workers or automations.
- `icp_matrix`: ICP cells, buyer/persona, company size, trigger signals, exclusions, target count, confidence, and evidence links. Memory Store IDs, Gmail/CRM references, and source URLs that justify an ICP cell belong here as evidence; they should not replace the customer usage map.
- `signal_sources`: Memory Store, Exa/Websets, website, GitHub/docs/changelog, LinkedIn, Reddit/HN, Product Hunt/YC/events, Gmail replies, and monitor candidates.
- `gmail_learnings`: search scope, warm paths, objections, reply language, suppressions, prior touches, and confidence.
- `calendar_policy`: Google Calendar availability use, booking-link policy, meeting duration if known, timezone if known, and unavailable fallback.
- `channel_policy`: email-first or email-plus-LinkedIn, per-person touch limits, LinkedIn profile requirements, same-person dedupe, and channel-specific learning intent.
- `send_ramp_policy`: day 1 max 10 sends, days 2-3 max 20/day, then max 50/day until changed; pause conditions; same-company rule.
- `autopilot_routines`: approved or proposed routine specs for Gmail reply scans, followup checks, daily campaign digest, weekly ICP/signal/copy learning summary, Websets refreshes, high-intent monitor reviews, host automation cadence, background-worker graph, allowed actions, forbidden actions, stop conditions, and expected output.
- `memory_distillation`: what should be remembered for future runs: operating rules, user preferences, constraints, approval policies, connector expectations, persona/sourcing decisions, campaign-learning intent, and whether each item is `proposed`, `approved`, `active`, or `deprecated`.
- `brief_delta`: sparse canonical brief updates proposed by the plan. Use only for reusable operating truth, such as GTM policy, ICP/persona map, proof/claims, campaign learning summary, or important account/customer context. Use `none` when records are enough.
- `approval_needed_before_start`: demo link confirmation, sender identity, send ramp, ICP cells, claims, exclusions, Exa/Websets credential setup, connector gaps, and any unresolved high-risk ambiguity.

## Plan Decision Groups

At the top of the GTM plan, briefly separate unresolved planning work into these groups:

- `inferred`: decisions inferred from Memory Store, website, Gmail, Calendar, or public research, with source and confidence.
- `needs_confirmation`: decisions likely enough to propose but requiring user approval before send.
- `unknown_blocker`: decisions that cannot be safely inferred and block autopilot. Missing Exa/Websets production credentials belong here for any campaign that asks for real ICP discovery, sourcing, drafting, or always-on monitoring. Missing Gmail belongs here for any campaign that asks for sends, followups, reply monitoring, or outcome learning.

Keep this grouping compact. The plan fields remain the canonical output.

## Approval Rule

The GTM plan can be used for planning before approval, but not for autonomous sending or scheduled host automations. After the user approves or edits it, record the confirmed decisions and `memory_distillation` items to Memory Store and treat the plan as the active campaign operating policy. Apply `brief_delta` only after approval and only when the delta changes future agent behavior; otherwise keep the learning as a record.
