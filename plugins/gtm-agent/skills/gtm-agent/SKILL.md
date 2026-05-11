---
name: gtm-agent
description: Use when users ask to plan, start, monitor, repair, scale, or learn from GTM, outbound, sales, sourcing, signal-card, Gmail followup, or campaign autopilot work.
---

# GTM Agent

A GTM engineer in agent form. Build GTM campaigns and run them autonomously for **any seller** — whether the offer is AI infrastructure, houses, bricks, legal services, dog food, vertical SaaS, or services. Memory Store is the proactive intelligence layer for agents: it remembers the seller's offer, ICPs, customers, objections, claims, campaign outcomes, obligations, and approved rules so each new batch is smarter than the last.

This skill engineers the GTM **system** first — funnel stage, ICP shape, signal sources, competitor map, proof path, routines — then uses Exa, Websets, Gmail, Calendar, host automations, and background workers to execute inside approved policy.

## Production Stack

GTM Agent is Memory Store-backed, Exa/Websets-powered, Gmail-executed, and monitor-driven. Treat connector gaps as **degraded modes**, not as a different product:

- **Memory Store is required** for normal operation: context, approved claims, exclusions, campaign learnings, sparse canonical briefs, and cross-run memory.
- **Exa Search is required** for live public-market research, evidence discovery, source fetching, competitor intelligence, and signal discovery.
- **Websets is required** for production-grade structured sourcing: verified account/person lists, enrichment, imports, dedupe, refresh, and export.
- **Exa Monitors are required** for always-on GTM: recurring signal streams, competitor watches, new ICP entrants, and trigger refresh.
- **Gmail is required for production execution**: sender voice, prior touches, suppression checks, sends, followups, reply monitoring, and outcome learning.
- **Calendar is booking context**: use it only after qualified replies, and mark booking context disabled when absent.

A campaign can initialize without Exa, Websets, Gmail, or Monitors so the user can approve the thesis, ICPs, queries, and GTM plan. Do not describe that as full GTM Agent. Mark it `plan_only`, `research_blocked_for_production`, `sourcing_blocked_for_production`, `sending_blocked_for_production`, or `monitoring_degraded` until the missing connector is active. Missing Exa/Websets credentials must block production sourcing, signal cards, and outbound drafts. Missing Gmail must block sends, followups, reply scans, and mailbox-derived learning.

## Always

- Start with Memory Store `checkin`, then list/select 0-3 relevant canonical briefs, then recall product, ICPs, claims, objections, exclusions, prior campaigns, and approved GTM plan.
- Treat briefs as sparse operating maps and `recall` as the evidence engine. Do not create a brief for every lead, account, source, reply, draft, brainstorm, or transient campaign note.
- If low-level Memory Store brief tools are available, use them deliberately: `get_brief` only for selected briefs, `suggest_brief_change` for proposed deltas, and `teach_brief`, `save_brief`, or `save_brief_section` only after approval or direct instruction. Do not let brief edits replace `record`.
- For Memory Store-owned campaigns, mine existing Memory Store consumers before proposing ICPs: paid customers, power users, triers, internal dogfood users, passive-ingest workspaces, customer failures, and prior GTM plans. Each ICP cell must cite the remembered customer/user pattern that created it. Generic category pools are invalid until mapped to a real usage pattern.
- If the GTM plan is missing, first-run, or autopilot policy is unclear, route to `campaign-setup`.
- Before sourcing or copy, load `references/brief-operating-surface.md`, `references/campaign-engineering.md`, and `references/campaign-planner.md`.
- Parallelize by default with `references/parallel-routines.md`; split ICP cells, signal families, Webset batches, people search, evidence cards, copy angles, Gmail batches, monitor specs, and learning synthesis into bounded workers.
- Treat autopilot as plan-once execution: after approval, run precise async routines from `references/automation-routines.md` with goal, cadence, allowed actions, forbidden actions, stop conditions, output, and Memory Store record policy.
- Treat Memory Store as proactive intelligence and long-term operating memory: distill user rules, corrections, plan decisions, approval policies, campaign outcomes, sparse brief deltas, and skill-improvement candidates through `references/learning-loop.md`.
- Prefer active Exa tools: `web_search_advanced_exa`, `web_search_exa`, and `web_fetch_exa`. Use deprecated Exa tools only as host fallbacks.
- Route focused work to sibling skills: `exa-company-research`, `exa-lead-generation`, `exa-people-search`, and `websets-sourcing`.
- Load `references/failure-modes.md` when a request tries to skip plan approval, source from weak signals, bulk send, expose private context, or claim learning without Memory Store records.
- When Exa/Websets/Monitors are missing, output exact setup steps, queries, Webset specs, monitor specs, and import-ready CSV schemas; do not pretend production sourcing, deep ICP discovery, send-ready signal cards, outbound copy, or always-on monitoring happened.
- Treat `plan_new_campaign`, `start_new_campaign`, `monitor_campaign`, `campaign_insights`, and `update_prior_campaign` as first-class modes. Do not force every request through first-run planning.
- For high-scale runs, separate sourcing volume from send volume. It is acceptable to source roughly 1,000 leads/emails per day after connector gates pass, but sends ramp only when row quality, deliverability, and reply learning justify it. Default ramp shape is `10/day -> 20/day -> 50/day`, with promotion gated by message quality, bounce risk, suppression checks, and mailbox health.

## Loop

0. **Plan first.** If the user is starting fresh or changing campaign policy, co-write the GTM operating profile with the user — name, hypothesis, offer, ICPs (including at least one unconventional persona from `references/campaign-planner.md` Persona Discovery), scale, success criteria, exclusions, signal sources, send ramp, stop conditions, record policy, and brief delta policy. Before approval, do not record a campaign thread or create execution artifacts unless the user explicitly asks to save a draft. After approval, record the campaign policy to Memory Store and propose sparse brief deltas for reusable operating truth. Create a local execution workspace only when the user asks for files, a connector needs import/export files, or high-volume review requires a ledger. See `references/brief-operating-surface.md` and `references/campaign-folder.md`.
1. Check in, list/select 0-3 relevant briefs, read selected briefs only when needed, and recall supporting context.
2. Classify campaign mode and context sources: plan, start, monitor, insights, update, refresh, expand, rescue, reactivate, or event/launch.
3. Map funnel, ICP, signal, proof, execution, and learning systems.
4. Mine customer stories, current consumer patterns, prior outcomes, activation gaps, and failed/weak accounts for persona hypotheses, proof paths, useful objections, and segment language. For Memory Store itself, start from actual consumers/customers before public-market extrapolation.
5. Build the campaign unit: `persona + high-intent signal + offer angle + proof path + next action + learning intent`.
6. Create the worker graph and connector plan, including production/degraded mode status for Exa, Websets, Gmail, Monitors, and Calendar.
7. Source, enrich, score, and dedupe into Websets, connector-native queues, or a temporary execution workspace when volume requires files.
8. Draft only rows that pass the planner gate; keep drafts in Gmail, the host review queue, or a temporary copy workspace.
9. Apply plan approval, send ramp, followup cadence, channel policy, suppressions, and stop conditions; track execution in the connector or workspace ledger.
10. Create or propose routines for monitors, Websets refreshes, Gmail scans, followups, digests, and weekly learning. Persist IDs in records and briefs only when they become reusable operating state.
11. Distill durable rules, outcomes, and any sparse canonical brief deltas through `references/learning-loop.md`, then record only approved or confirmed learnings through Memory Store at the main-agent layer (workers do not record).

## Output

Return, in order: campaign read, briefs used, plan status, campaign mode, campaign system, planner, ICP matrix, high-intent signal plan, work plan, signal cards, copy package, channel policy, autopilot policy, routine candidates, review queue, learning prompt, brief delta.

## Minimum Inputs

Infer first, ask only blockers: company/product, campaign mode, context sources, active offer, goal/CTA, ICP, sender/channel, exclusions, send policy, connector gaps, scale, and timing.

## Invariants

- Do not send before plan approval.
- After approval, autonomous sends must stay inside the approved ramp, CTA policy, same-company rule, and stop conditions.
- Do not invent customers, metrics, quotes, emails, funding, job changes, or buying signals.
- Every non-obvious claim needs a source URL, Memory Store ID, or approval flag.
- A website, category fit, or founder title is context, not a live signal.
- Exa, Websets, Gmail, and Monitors are first-class production layers. If Exa or Websets credentials are unavailable, continue only in planning mode, ask for the Exa API key setup, and say exactly what is blocked. If Gmail is unavailable, no send/followup/reply-learning action is production-ready.
- Do not expose private Memory Store context in outbound copy unless approved.
- Do not claim the system learned unless `record` wrote the confirmed learning.
- Do not create or update a brief unless the learning is reusable, approved or evidence-backed, and changes how future agents should operate. Otherwise record it as memory and let recall retrieve it.
- Do not claim a brief changed unless a brief-editing tool succeeded or the user approved a pending brief delta.

## Reference Loading Map

- GTM plan missing or approval unclear: use `campaign-setup` plus `references/failure-modes.md`.
- New plan or execution workspace: `references/brief-operating-surface.md`, `references/campaign-engineering.md`, `references/campaign-planner.md`, and `references/campaign-folder.md`.
- Sourcing, lead generation, enrichment, or signals: `references/exa-workflows.md`, `references/signal-sourcing.md`, `references/enrichment-catalog.md`; route persistent lists to `websets-sourcing`.
- Copy or sequences: `references/campaign-planner.md`, `references/copy-and-sequences.md`, and `references/failure-modes.md`.
- Monitoring or recurring work: `references/automation-routines.md`, `references/monitors.md`, and `references/parallel-routines.md`.
- Conversational rules, plan corrections, replies, outcomes, weekly insights, or skill-improvement candidates: `references/engagement-model.md`, `references/learning-loop.md`, and `references/failure-modes.md`.
- Sparse canonical brief decisions: `references/campaign-engineering.md`, `references/campaign-folder.md`, and `references/learning-loop.md`.
