# Onboarding Questions

Use these questions when Campaign Setup cannot infer the answer from Memory Store, website research, Gmail, or Google Calendar. Ask only the smallest missing blocker. Do not turn setup into a long form when context is already available.

This reference is the repeatable GTM engineer onboarding script. Each question should become either an inferred setup decision, a confirmation request, or a true blocker.

## Setup Principle

The onboarding interview is how GTM Agent designs the campaign. The questions are repeatable, but the first move is always inference:

```text
Memory Store -> Exa/Websets/Gmail readiness -> campaign plan -> website -> Calendar -> ask only unresolved blockers
```

Do not treat a no-key Exa/Websets state as a normal setup gap for a real campaign. Website-only research can support positioning, but it cannot produce deep ICP personas, production lead lists, signal cards, or send-ready copy. If Exa Search or Websets is missing or unauthenticated, ask for the Exa API key setup before any production sourcing or drafting. If Gmail is missing, full execution is blocked; the campaign can still plan/source, but it cannot send, monitor replies, or learn from mailbox outcomes.

## Core Questions

Ask or infer these in order:

1. **What are we selling?**
   - active offer, alternate offers, core claim, proof path, taboo positioning.

2. **What kind of campaign is this?**
   - `plan_new_campaign`, `start_new_campaign`, `monitor_campaign`, `campaign_insights`, `update_prior_campaign`, `build_on_previous`, `refresh_existing`, `expand_winner`, `rescue_underperformer`, `reactivation`, `event_or_launch`.

3. **What context should the agent ingest?**
   - Memory Store, uploaded docs, pasted notes, positioning docs, prior campaign exports, CSV/account lists, website, Gmail, Calendar, Exa/Websets.

4. **Are Exa Search, Websets, and Gmail production-ready?**
   - Exa API key status, Exa Search MCP status, Websets MCP status, Gmail connector status, monitor availability, and exact setup step needed if blocked.

5. **What funnel system are we engineering?**
   - market definition, ICP hypotheses, signal discovery, account sourcing, buyer discovery, evidence cards, copy, review, send/followup, reply classification, meeting/next action, learning.

6. **Who is the sender?**
   - sender identity, relationship to offer, human voice, phrases to use, phrases to avoid.

7. **What should happen if the campaign works?**
   - reply, demo, teardown, install, pilot, brief review, intro, or other conversion event.

8. **What is the demo or next-action path?**
   - discovered demo/Cal link, confirmation status, fallback CTA, meeting length, timezone.

9. **Who should we target first?**
   - ICP cells, company size, stage, geography, buyer persona, pain, triggers, exclusions.

10. **Which signals count as live enough?**
   - hiring, launch, docs/changelog, support/community load, GitHub activity, public complaint, reply history, warm path, or other trigger.

11. **What should we never say or do?**
   - taboo claims, competitor exclusions, current customers, sensitive proof, screenshots, attachments, regulated segments, do-not-contact rules.

12. **How autonomous should this campaign be?**
   - default is full autopilot after setup approval with ramped limits, precise daily/weekly routine specs, background-worker graphs, and stop conditions. At high scale, the daily operating target may be around 1,000 sourced leads/emails, but sends are still gated by mailbox health, signal quality, suppression checks, and the approved ramp.

13. **How should Gmail be used?**
   - sender voice, sent-mail examples, inbox replies, objections, warm paths, suppressions, followups, and active threads.

14. **Should LinkedIn be part of the touch policy?**
   - default is email-first with LinkedIn profile discovery. If approved, use LinkedIn as a parallel visibility/touch channel for the same qualified person, but track channel intent separately and do not duplicate generic copy across both channels.

15. **How should Calendar be used?**
    - default is booking context after qualified replies; do not create or move events without explicit policy.

## Question Output

Before showing the setup packet, summarize the interview state:

```text
inferred:
needs_confirmation:
unknown_blocker:
```

Use `inferred` for decisions with source and confidence. Use `needs_confirmation` for demo links, claims, sender identity, send ramp, media policy, or ICP choices that are likely but still require approval. Use `unknown_blocker` only when autopilot would be unsafe without the answer.

Missing Exa/Websets production credentials are an `unknown_blocker` for production GTM, not a minor warning. The setup packet may continue as `setup_only`, but the next action must be Exa key configuration. Missing Gmail is an `unknown_blocker` for sending, reply monitoring, and learning from campaign outcomes.

## Memory Store-Built Defaults

Only apply this section when the seller or offer is Memory Store, a Memory Store plugin, or an explicitly adjacent Memory Store product. For any other seller, infer defaults from that seller's Memory Store, public evidence, and approved setup packet instead.

Use these defaults unless recalled context or the user overrides them:

- company-size range: AI/devtools/startup-to-midmarket teams, roughly 10-500 employees.
- target motion: active product, GTM, support, developer community, or agent workflow.
- Fortune/enterprise: disabled unless explicitly selected.
- CTA style: soft demo CTA, usually reply or teardown first.
- media policy: text-first; screenshots/assets collected as proof options, not attached by default.
- same-company rule: max 2 contacts per company, only for meaningfully different personas.
- send ramp: day 1 max 10, days 2-3 max 20/day, day 4 onward max 50/day.

## Output Discipline

Every setup answer should map to the setup packet:

- `company_profile`
- `campaign_mode`
- `context_sources`
- `connector_status`
- `offer_profiles`
- `sender_voice`
- `website_findings`
- `demo_cta`
- `funnel_system`
- `icp_matrix`
- `signal_sources`
- `gmail_learnings`
- `calendar_policy`
- `channel_policy`
- `send_ramp_policy`
- `autopilot_routines`
- `approval_needed_before_start`

If an answer is inferred, include source and confidence. If it is unknown, mark it as `unknown`, `missing_connector`, or `needs_user_confirmation`.
