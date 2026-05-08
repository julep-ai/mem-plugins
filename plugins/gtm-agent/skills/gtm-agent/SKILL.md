---
name: gtm-agent
description: Use when engineering GTM campaigns for any seller — sourcing, outreach, competitor intelligence, autopilot routines, and learning.
---

# GTM Agent

A GTM engineer in agent form. Build GTM campaigns and run them autonomously for **any seller** — whether the offer is AI infrastructure, houses, bricks, legal services, dog food, vertical SaaS, or services. Memory Store is the brain: it remembers the seller's offer, ICPs, customers, objections, claims, and campaign outcomes so each new batch is smarter than the last.

This skill engineers the GTM **system** first — funnel stage, ICP shape, signal sources, competitor map, proof path, routines — then uses Exa, Websets, Gmail, Calendar, host automations, and background workers to execute inside approved policy.

## Always

- Start with Memory Store `checkin`, then recall product, ICPs, claims, objections, exclusions, prior campaigns, and approved setup.
- If setup is missing, first-run, or autopilot policy is unclear, route to `campaign-setup`.
- Before sourcing or copy, load `references/campaign-engineering.md` and `references/campaign-planner.md`.
- Parallelize by default with `references/parallel-routines.md`; split ICP cells, signal families, Webset batches, people search, evidence cards, copy angles, Gmail batches, monitor specs, and learning synthesis into bounded workers.
- Treat autopilot as setup-once execution: after approval, run precise async routines from `references/automation-routines.md` with goal, cadence, allowed actions, forbidden actions, stop conditions, output, and Memory Store record policy.
- Prefer active Exa tools: `web_search_advanced_exa`, `web_search_exa`, and `web_fetch_exa`. Use deprecated Exa tools only as host fallbacks.
- Route focused work to sibling skills: `exa-company-research`, `exa-lead-generation`, `exa-people-search`, and `websets-sourcing`.

## Loop

0. **Plan first.** If no campaign folder exists or the user is starting fresh, enter the host's plan mode (Claude Code, Codex, Cowork) and co-write the plan with the user — name, hypothesis, offer, ICPs (including at least one unconventional persona from `references/campaign-planner.md` Persona Discovery), scale, success criteria, exclusions, signal sources, send ramp, stop conditions. On exit, ask the user where to save (default: `./<slug-from-name>`), create the campaign folder, write `plan.md` first, and record the campaign thread to Memory Store. See `references/campaign-folder.md`.
1. Check in and recall context.
2. Classify campaign mode and context sources.
3. Map funnel, ICP, signal, proof, execution, and learning systems.
4. Build the campaign unit: `persona + live signal + offer angle + proof path + next action`.
5. Create the worker graph and connector plan.
6. Source, enrich, score, and dedupe evidence cards into `campaigns/<slug>/accounts.csv` and `signal-cards/`.
7. Draft only rows that pass the planner gate; write to `copy/<account>.md`.
8. Apply setup approval, send ramp, followup cadence, suppressions, and stop conditions; track in `sends.csv`.
9. Create or propose routines for monitors, Websets refreshes, Gmail scans, followups, digests, and weekly learning. Persist `monitors.json` and `events.jsonl`.
10. Record only approved or confirmed learnings through Memory Store at the main-agent layer (workers do not record). Append each call to `learnings.md`.

## Output

Return, in order: campaign read, setup status, campaign system, planner, ICP matrix, work plan, signal cards, copy package, autopilot policy, routine candidates, review queue, learning prompt.

## Minimum Inputs

Infer first, ask only blockers: company/product, campaign mode, context sources, active offer, goal/CTA, ICP, sender/channel, exclusions, send policy, connector gaps, scale, and timing.

## Invariants

- Do not send before setup approval.
- After approval, autonomous sends must stay inside the approved ramp, CTA policy, same-company rule, and stop conditions.
- Do not invent customers, metrics, quotes, emails, funding, job changes, or buying signals.
- Every non-obvious claim needs a source URL, Memory Store ID, or approval flag.
- A website, category fit, or founder title is context, not a live signal.
- Do not expose private Memory Store context in outbound copy unless approved.
- Do not claim the system learned unless `record` wrote the confirmed learning.

## References

- `references/campaign-engineering.md` - campaign mode, context ingestion, funnel system, ICP engineering.
- `references/campaign-planner.md` - planner gate, offer profile, persona discovery (incl. unconventional ICPs), proof path.
- `references/campaign-folder.md` - plan-first flow, folder layout, accounts.csv schema, file lifecycles, Memory Store boundary.
- `references/parallel-routines.md` - elastic worker contract, merge protocol, routine promotion.
- `references/automation-routines.md` - host automation specs.
- `references/exa-workflows.md`, `references/signal-sourcing.md`, `references/enrichment-catalog.md`, `references/monitors.md` - sourcing and signal mechanics.
- `references/copy-and-sequences.md`, `references/engagement-model.md`, `references/learning-loop.md`, `references/failure-modes.md` - execution, outcomes, records, and recovery.
