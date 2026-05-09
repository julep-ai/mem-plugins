---
name: campaign-setup
description: Use when users need a first GTM plan, lack an approved GTM plan, need connector readiness, sender voice, demo CTA, send ramp, autopilot policy, or approval gates.
---

# Campaign Plan

Plan GTM Agent campaigns so they can run continuously from Memory Store, uploaded/pasted context, public signals, Gmail, Calendar, Exa Search, Websets, Exa Monitors, and host automations. Infer first, ask only blockers, guide connector setup in-chat when a connector blocks production work, then produce the approved operating profile used by `gtm-agent`.

The GTM plan can start before every connector is active, but it must separate **planning fallback** from **production readiness**. Memory Store is required for normal GTM Agent operation. Exa Search, Websets, Gmail, and Exa Monitors are mandatory production layers: Exa for live research, Websets for structured sourcing, Gmail for sending/reply learning, and monitors for always-on signals. If Exa or Websets credentials are missing, stop before sourcing or drafting and ask the user to configure the Exa API key; do not let basic website research masquerade as GTM Agent output. If Gmail is missing, stop before sending, reply monitoring, or outcome learning.

## Use For

- first-run GTM Agent planning.
- missing, stale, or unapproved GTM plans.
- plan policy changes before production work starts.
- sender voice, demo CTA, send ramp, followup cadence, suppression rules, and routine specs.

For an already-approved campaign monitor, insights, refresh, rescue, reactivation, launch, or update request, return to `gtm-agent` and load only the relevant campaign, automation, connector, engagement, and learning references.

## Loop

1. Start with Memory Store `checkin` and recall.
2. Before public ICP brainstorming, build the `customer_usage_map`: the seller's real existing customers/users when discoverable. Use Memory Store, Gmail/CRM, website proof, Exa, and Websets to find named customers, customer categories, user segments, case studies, testimonials, reviews, active users, churn/loss patterns, and activation gaps. For a Memory Store-owned campaign, this means Memory Store's own customers/users. For another seller, it means that seller's customers/users. Memory Store IDs belong as evidence on ICP cells; they are not the whole customer usage map.
3. Load `../gtm-agent/references/campaign-engineering.md`; classify campaign mode, context sources, funnel stage, ICP system, signal system, proof system, execution system, and learning system.
4. Verify Memory Store, Exa Search, Websets, and Gmail readiness before any production sourcing, drafting, sending, or learning loop. If Exa/Websets setup is missing, guide it in-chat: provide `https://dashboard.exa.ai/api-keys`, ask for a terminal-safe API-key paste/setup, and run or output the host setup command from `docs/EXA_SETUP.md`. Do not send the user to a separate dashboard except where a provider has no tool/API path. If the Exa API key is missing or Websets returns an auth error, ask for setup immediately, output exact commands, and keep the campaign in `plan_only`. If Gmail is missing, keep sending and reply learning disabled.
5. Discover website/demo CTA and research public proof with Exa/Web fetch when available; if Exa is missing, output exact research queries and mark public research degraded.
6. Learn bounded sender voice, objections, suppressions, and warm paths from Gmail when available.
7. Use Calendar only for booking context after qualified replies unless policy says otherwise.
8. Ask unresolved blockers from `references/onboarding-questions.md`.
9. Build the planner and worker graph with `../gtm-agent/references/campaign-planner.md` and `../gtm-agent/references/parallel-routines.md`.
10. For any first production run, require a shadow sample that demonstrates account discovery, persona discovery, channel identity, and customer-pattern fit. If Exa/Websets cannot find people or emails, mark the exact blocker instead of pretending sourcing is complete.
11. Distill durable plan rules, preferences, approval policies, connector expectations, and skill-improvement candidates with `../gtm-agent/references/learning-loop.md`.
12. Configure full autopilot with `references/first-run-autopilot.md` and `../gtm-agent/references/automation-routines.md`.
13. Return the GTM plan from `references/gtm-plan.md`.
14. Record only after the user approves or edits the plan.

## GTM Plan Shape

```text
company_profile:
campaign_mode:
context_sources:
connector_status:
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
approval_needed_before_start:
```

Group unresolved items as `inferred`, `needs_confirmation`, and `unknown_blocker`.

## Rules

- Missing Exa/Websets/Gmail/Monitors/Calendar should not block GTM planning; mark the exact degraded mode and provide setup steps plus manual/import-ready fallback. Missing Exa or Websets must block production sourcing, lead generation, send-ready rows, and campaign copy. Missing Gmail must block sends, followups, reply scans, mailbox suppression checks, and outcome learning. Do not call a campaign production-ready until Exa, Websets, Gmail, and the relevant monitor specs are available.
- An ICP matrix without a customer usage map is incomplete when any existing customers/users can be found. Do not lead with generic categories like "founder-led teams" or "AI GTM teams" unless the GTM plan explains which real customer/user pattern, public customer proof, or explicit hypothesis created that cell. If no customers/users can be found, mark `customer_usage_map: unknown_or_not_public` and use Exa/Websets to derive public customer proxies before proposing ICPs.
- Do not send during planning.
- Do not use a discovered demo link until confirmed once.
- Do not claim uploaded or pasted context was learned until it is recorded through Memory Store after approval.
- Full autopilot is bounded by approved ramp limits, allowed actions, forbidden actions, and stop conditions.
