---
name: exa-lead-generation
description: Use when generating Exa/Websets lead lists, ICP batches, schemas, dedupe, or scoring.
---

# Exa Lead Generation

Generate account or recipient lists from a confirmed campaign model. Use Websets when the list should persist, refresh, enrich, export, or become a routine; use Exa Search for one-off validation or discovery.

## Loop

1. Start with Memory Store `checkin` and recall ICPs, exclusions, winning segments, objections, and prior campaign outcomes.
2. Confirm campaign mode, ICP cells, target counts, and exclusions before bulk generation.
3. Use active Exa Search MCP tools: `web_search_advanced_exa`, `web_search_exa`, `web_fetch_exa`. Use `deep_search_exa` or `company_research_exa` only as old-host fallbacks.
4. Use `websets-sourcing` for persistent lists, criteria verification, enrichments, imports, refreshes, and monitorable pools.
5. Keep schemas compact: company, website, ICP fit, fit reasoning, signal, source URL, persona, offer angle, proof path, next action, confidence, exclusion risk.
6. Batch work in background workers; return counts, accepted/rejected reasons, artifact paths/IDs, and top findings, not raw 1000-row dumps.
7. Dedupe by normalized domain and apply Memory Store suppressions before copy handoff.
8. Record approved ICP rules, exclusion rules, Webset IDs, and outcomes.

## Output

Return: ICP read, micro-vertical plan, schema, batch plan/result, shortlist summary, and next action.

## Rules

Do not send from this skill. Do not hand off to copy unless rows include persona, live signal, source, offer angle, proof path, next action, confidence, and exclusion risk.
