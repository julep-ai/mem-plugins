---
name: exa-lead-generation
description: Use when generating Exa/Websets lead lists, ICP batches, schemas, dedupe, or scoring.
---

# Exa Lead Generation

Generate account or recipient lists from a confirmed campaign model. Use Websets when the list should persist, refresh, enrich, export, or become a routine; use Exa Search for one-off validation or discovery. Production lead generation requires Exa Search and Websets credentials; otherwise return setup steps and query specs only.

## Loop

1. Start with Memory Store `checkin` and recall ICPs, exclusions, winning segments, objections, and prior campaign outcomes.
2. Confirm campaign mode, ICP cells, target counts, and exclusions before bulk generation.
3. Verify Exa Search and Websets are authenticated. If not, stop production generation and ask for Exa API key setup.
4. Use active Exa Search MCP tools: `web_search_advanced_exa`, `web_search_exa`, `web_fetch_exa`. Use `deep_search_exa` or `company_research_exa` only as old-host fallbacks.
5. Use `websets-sourcing` for persistent lists, criteria verification, enrichments, imports, refreshes, and monitorable pools.
6. Keep schemas compact: company, website, ICP fit, fit reasoning, high-intent signal, source URL, persona, customer-story pattern, offer angle, proof path, next action, learning intent, confidence, exclusion risk.
7. When the campaign target is around 1000 leads/emails per day, batch by ICP cell, signal family, and micro-vertical; return counts, accepted/rejected reasons, artifact paths/IDs, and top findings, not raw 1000-row dumps.
8. Dedupe by normalized domain, person identity, work email, and LinkedIn profile URL; apply Memory Store and Gmail suppressions before copy handoff.
9. Record approved ICP rules, exclusion rules, Webset IDs, and outcomes.

## Output

Return: ICP read, high-intent signal plan, micro-vertical plan, schema, daily batch plan/result, accepted/rejected summary, shortlist summary, and next action.

## Rules

Do not send from this skill. Do not hand off to copy unless rows include persona, high-intent signal, source, customer-story/persona pattern when available, offer angle, proof path, next action, learning intent, confidence, and exclusion risk.
