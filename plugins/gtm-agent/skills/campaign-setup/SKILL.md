---
name: campaign-setup
description: Use when users first configure GTM Agent, lack an approved setup packet, need connector readiness, sender voice, demo CTA, send ramp, autopilot policy, or approval gates.
---

# Campaign Setup

Set up GTM Agent so campaigns can run continuously from Memory Store, uploaded/pasted context, public signals, Gmail, Calendar, Exa Search, Websets, Exa Monitors, and host automations. Infer first, ask only blockers, guide connector setup in-chat, then produce the approved operating profile used by `gtm-agent`.

Setup can start before every connector is active, but the setup packet must separate **planning fallback** from **production readiness**. Memory Store is required for normal GTM Agent operation. Exa Search, Websets, Gmail, and Exa Monitors are mandatory production layers: Exa for live research, Websets for structured sourcing, Gmail for sending/reply learning, and monitors for always-on signals. If Exa or Websets credentials are missing, stop before sourcing or drafting and ask the user to configure the Exa API key; do not let basic website research masquerade as GTM Agent output. If Gmail is missing, stop before sending, reply monitoring, or outcome learning.

## Use For

- first-run GTM Agent setup.
- missing, stale, or unapproved setup packets.
- setup policy changes before production work starts.
- sender voice, demo CTA, send ramp, followup cadence, suppression rules, and routine specs.

For an already-approved campaign monitor, insights, refresh, rescue, reactivation, launch, or update request, return to `gtm-agent` and load only the relevant campaign, automation, connector, engagement, and learning references.

## Loop

1. Start with Memory Store `checkin` and recall.
2. Load `../gtm-agent/references/campaign-engineering.md`; classify campaign mode, context sources, funnel stage, ICP system, signal system, proof system, execution system, and learning system.
3. Verify Memory Store, Exa Search, Websets, and Gmail readiness before any production sourcing, drafting, sending, or learning loop. If setup is missing, guide it in-chat with exact host-specific steps; do not send the user to a separate dashboard except where a provider has no tool/API path. If the Exa API key is missing or Websets returns an auth error, ask for setup immediately, output exact commands, and keep the campaign in `setup_only`. If Gmail is missing, keep sending and reply learning disabled.
4. Discover website/demo CTA and research public proof with Exa/Web fetch when available; if Exa is missing, output exact research queries and mark public research degraded.
5. Learn bounded sender voice, objections, suppressions, and warm paths from Gmail when available.
6. Use Calendar only for booking context after qualified replies unless policy says otherwise.
7. Ask unresolved blockers from `references/onboarding-questions.md`.
8. Build the planner and worker graph with `../gtm-agent/references/campaign-planner.md` and `../gtm-agent/references/parallel-routines.md`.
9. For any first production run, require a shadow sample that demonstrates account discovery, persona discovery, and channel identity. If Exa/Websets cannot find people or emails, mark the exact blocker instead of pretending sourcing is complete.
10. Distill durable setup rules, preferences, approval policies, connector expectations, and skill-improvement candidates with `../gtm-agent/references/learning-loop.md`.
11. Configure full autopilot with `references/first-run-autopilot.md` and `../gtm-agent/references/automation-routines.md`.
12. Return the setup packet from `references/setup-packet.md`.
13. Record only after the user approves or edits the packet.

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
channel_policy:
send_ramp_policy:
autopilot_routines:
memory_distillation:
approval_needed_before_start:
```

Group unresolved items as `inferred`, `needs_confirmation`, and `unknown_blocker`.

## Rules

- Missing Exa/Websets/Gmail/Monitors/Calendar should not block setup planning; mark the exact degraded mode and provide setup steps plus manual/import-ready fallback. Missing Exa or Websets must block production sourcing, lead generation, send-ready rows, and campaign copy. Missing Gmail must block sends, followups, reply scans, mailbox suppression checks, and outcome learning. Do not call a campaign production-ready until Exa, Websets, Gmail, and the relevant monitor specs are available.
- Do not send during setup.
- Do not use a discovered demo link until confirmed once.
- Do not claim uploaded or pasted context was learned until it is recorded through Memory Store after approval.
- Full autopilot is bounded by approved ramp limits, allowed actions, forbidden actions, and stop conditions.
