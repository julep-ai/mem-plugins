---
name: websets-sourcing
description: Use when users ask to create, preview, inspect, enrich, import, refresh, monitor, export, or reuse persistent Exa Websets for GTM sourcing.
---

# Websets Sourcing

Use Exa Websets as the persistent sourcing and enrichment layer for GTM Agent. Production Websets sourcing requires a configured Exa API key; if auth is missing, stop and output setup steps plus the Webset spec.

## Loop

1. Start with Memory Store `checkin`; use selected canonical brief context if provided by the main GTM agent, otherwise call `list-briefs` and select 0-3 relevant briefs; then recall campaign, ICP, exclusions, seed accounts, suppressions, and prior Webset IDs.
   When invoked directly (not routed by the main GTM Agent skill), also load ../gtm-agent/references/signal-sourcing.md, ../gtm-agent/references/enrichment-catalog.md, ../gtm-agent/references/failure-modes.md, and ../gtm-agent/references/monitors.md for monitor-related work.
2. Use Websets when a list should persist, refresh, enrich, export, import, or be reused across campaigns.
3. Preview before broad creation when available.
4. Separate criteria from enrichments: criteria filter inclusion; enrichments add action fields.
5. Pick entity type: `company`, `person`, `article`, `research_paper`, or `custom`.
6. Use imports for seed accounts, customers, competitors, suppressions, or CSV scope.
7. Add only enrichments that improve GTM action: buyer/persona, person name, title, work email or email status, LinkedIn/profile URL, identity confidence, high-intent signal, source URL, customer-story/persona pattern, offer angle, proof path, next action, learning intent, channel identity, confidence, and exclusion risk.
8. Track async IDs and status; return any brief-impact candidate to the main GTM agent. Record approved Webset/search/enrichment/import IDs to Memory Store only when this skill is the main agent for the task.

Websets MCP is separate from Exa Monitors. For monitors, use `../gtm-agent/references/monitors.md` and record returned monitor IDs after approval.

## Output

Return: webset read, spec, status, quality notes, Memory Store mapping, and next action.

## Rules

Do not create broad reusable Websets without approval. Do not commit secrets. Do not delete Websets unless explicitly asked. Do not mark rows draft-ready without complete planner fields or high-intent signal evidence. Do not create briefs for Webset rows, previews, enrichments, or async events; use Webset IDs, campaign artifacts, records, and a main-agent brief delta only when repeated results change future operating policy.
