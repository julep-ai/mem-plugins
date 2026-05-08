---
name: gtm-agent
description: Use when running Sales/GTM campaign autopilot, sourcing, outreach, routines, or learning.
---

# GTM Agent

Orchestrate Memory Store-backed GTM campaigns. The job is to engineer the campaign system first, then use Exa, Websets, Gmail, Calendar, host automations, and background workers to run it inside approved policy.

## Always

- Start with Memory Store `checkin`, then recall product, ICPs, claims, objections, exclusions, prior campaigns, and approved setup.
- If setup is missing, first-run, or autopilot policy is unclear, route to `campaign-setup`.
- Before sourcing or copy, load `references/campaign-engineering.md` and `references/campaign-planner.md`.
- Parallelize by default with `references/parallel-routines.md`; split ICP cells, signal families, Webset batches, people search, evidence cards, copy angles, Gmail batches, monitor specs, and learning synthesis into bounded workers.
- Treat autopilot as setup-once execution: after approval, run precise async routines from `references/automation-routines.md` with goal, cadence, allowed actions, forbidden actions, stop conditions, output, and Memory Store record policy.
- Prefer active Exa tools: `web_search_advanced_exa`, `web_search_exa`, and `web_fetch_exa`. Use deprecated Exa tools only as host fallbacks.
- Route focused work to sibling skills: `exa-company-research`, `exa-lead-generation`, `exa-people-search`, and `websets-sourcing`.

## Loop

1. Check in and recall context.
2. Classify campaign mode and context sources.
3. Map funnel, ICP, signal, proof, execution, and learning systems.
4. Build the campaign unit: `persona + live signal + offer angle + proof path + next action`.
5. Create the worker graph and connector plan.
6. Source, enrich, score, and dedupe evidence cards.
7. Draft only rows that pass the planner gate.
8. Apply setup approval, send ramp, followup cadence, suppressions, and stop conditions.
9. Create or propose routines for monitors, Websets refreshes, Gmail scans, followups, digests, and weekly learning.
10. Record only approved or confirmed learnings through Memory Store.

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
- `references/campaign-planner.md` - planner gate, offer profile, persona, proof path.
- `references/parallel-routines.md` - worker graph, merge protocol, routine promotion.
- `references/automation-routines.md` - host automation specs.
- `references/exa-workflows.md`, `references/signal-sourcing.md`, `references/enrichment-catalog.md`, `references/monitors.md` - sourcing and signal mechanics.
- `references/copy-and-sequences.md`, `references/engagement-model.md`, `references/learning-loop.md`, `references/failure-modes.md` - execution, outcomes, records, and recovery.
