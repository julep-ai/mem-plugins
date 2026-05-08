---
name: campaign-setup
description: Use when onboarding GTM Agent, creating setup packets, or approving autopilot policy.
---

# Campaign Setup

Set up GTM Agent so campaigns can run continuously from Memory Store, uploaded/pasted context, public signals, Gmail, Calendar, Exa Search, Websets, Exa Monitors, and host automations. Infer first, ask only blockers, then produce the approved operating profile used by `gtm-agent`.

Setup can start before every connector is active, but the setup packet must separate **planning fallback** from **production readiness**. Memory Store is required for normal GTM Agent operation. Exa Search, Websets, and Exa Monitors are first-class production layers for live research, structured sourcing, and always-on signals; if missing, mark the campaign degraded and output the exact setup steps/specs needed.

## Use For

- first-run GTM Agent setup.
- new campaigns from docs, notes, Memory Store, and public context.
- campaign continuations, refreshes, rescues, expansions, reactivations, launches, or events.
- sender voice, demo CTA, send ramp, followup cadence, suppression rules, and routine specs.

## Loop

1. Start with Memory Store `checkin` and recall.
2. Load `../gtm-agent/references/campaign-engineering.md`; classify campaign mode, context sources, funnel stage, ICP system, signal system, proof system, execution system, and learning system.
3. Discover website/demo CTA and research public proof with Exa/Web fetch when available; if Exa is missing, output exact research queries and mark public research degraded.
4. Learn bounded sender voice, objections, suppressions, and warm paths from Gmail when available.
5. Use Calendar only for booking context after qualified replies unless policy says otherwise.
6. Ask unresolved blockers from `references/onboarding-questions.md`.
7. Build the planner and worker graph with `../gtm-agent/references/campaign-planner.md` and `../gtm-agent/references/parallel-routines.md`.
8. Configure full autopilot with `references/first-run-autopilot.md` and `../gtm-agent/references/automation-routines.md`.
9. Return the setup packet from `references/setup-packet.md`.
10. Record only after the user approves or edits the packet.

## Setup Packet Shape

```text
company_profile:
campaign_mode:
context_sources:
connector_status:
offer_profiles:
sender_voice:
website_findings:
demo_cta:
funnel_system:
icp_matrix:
signal_sources:
gmail_learnings:
calendar_policy:
send_ramp_policy:
autopilot_routines:
approval_needed_before_start:
```

Group unresolved items as `inferred`, `needs_confirmation`, and `unknown_blocker`.

## Rules

- Missing Exa/Websets/Monitors/Gmail/Calendar should not block setup planning; mark the exact degraded mode and provide setup steps plus manual/import-ready fallback. Do not call a campaign production-ready until Exa, Websets, and the relevant monitor specs are available.
- Do not send during setup.
- Do not use a discovered demo link until confirmed once.
- Do not claim uploaded or pasted context was learned until it is recorded through Memory Store after approval.
- Full autopilot is bounded by approved ramp limits, allowed actions, forbidden actions, and stop conditions.
