---
name: websets-sourcing
description: Use when creating Exa Websets sourcing, previews, enrichments, imports, or refreshes.
---

# Websets Sourcing

Use Exa Websets as the persistent sourcing and enrichment layer for GTM Agent.

## Loop

1. Start with Memory Store `checkin` and recall campaign, ICP, exclusions, seed accounts, suppressions, and prior Webset IDs.
2. Use Websets when a list should persist, refresh, enrich, export, import, or be reused across campaigns.
3. Preview before broad creation when available.
4. Separate criteria from enrichments: criteria filter inclusion; enrichments add action fields.
5. Pick entity type: `company`, `person`, `article`, `research_paper`, or `custom`.
6. Use imports for seed accounts, customers, competitors, suppressions, or CSV scope.
7. Add only enrichments that improve GTM action: buyer/persona, recent signal, source URL, offer angle, proof path, next action, confidence, and exclusion risk.
8. Track async IDs and status; record approved Webset/search/enrichment/import IDs to Memory Store.

Websets MCP is separate from Exa Monitors. For monitors, use `../gtm-agent/references/monitors.md` and record returned monitor IDs after approval.

## Output

Return: webset read, spec, status, quality notes, Memory Store mapping, and next action.

## Rules

Do not create broad reusable Websets without approval. Do not commit secrets. Do not delete Websets unless explicitly asked. Do not mark rows draft-ready without complete planner fields.
