---
name: websets-sourcing
description: Use when creating, previewing, enriching, importing, refreshing, or inspecting persistent Exa Websets for companies, people, account lists, exclusions, enrichments, and async GTM sourcing.
---

# Websets Sourcing

Use Exa Websets as the persistent sourcing and enrichment layer for GTM Agent.

Sources:

- https://exa.ai/docs/reference/websets-mcp

## Requirements

- Memory Store MCP for campaign context and learning.
- Websets MCP configured with an Exa API key.
- Do not commit real Exa API keys. Use host-level MCP config or environment setup.

## Operating Loop

1. **Checkin and recall.** Start with Memory Store `checkin`, then recall the campaign, ICP, exclusions, existing customers, seed accounts, enrichment requirements, and prior Webset IDs.

2. **Choose whether Websets is warranted.** Create or update a Webset when the list should persist, be enriched, refreshed, exported, monitored, imported into downstream tools, or reused across campaigns.

3. **Preview first.** Use preview behavior when available before creating expensive or broad Websets. Tighten the natural-language search query and criteria until the result class is clear.

4. **Separate criteria from enrichments.**
   - Criteria are hard filters every result must satisfy.
   - Enrichments are columns extracted after results pass criteria.

5. **Use the right entity type.**
   - `company` for target accounts
   - `person` for people or buyer lists
   - `article` for signal sources
   - `research_paper` only for research workflows
   - `custom` only when the entity does not fit standard types

6. **Use imports for scoping and exclusions.** Import seed accounts, existing customers, competitors, suppression lists, or CSVs when they should constrain the Webset.

7. **Add enrichments that improve action quality.** Favor CEO/buyer title, employee count, funding, hiring, tech stack, recent signal, public pain language, contact URL, and exclusion risk.

8. **Track async state.** Websets searches and enrichments are async. Return IDs, status, event/webhook notes, and next polling or review action.

9. **Record durable IDs.** Record Webset IDs, search IDs, enrichment IDs, import IDs, webhook/event routes, and campaign/thread mapping in Memory Store after the user approves.

## Tool Surface

Use Websets MCP operations when available:

- webset management: create, list, get, update, delete, preview
- items: list and inspect webset items
- searches: create, inspect, cancel
- enrichments: create, inspect, cancel
- webhooks/events: subscribe, inspect, update, delete, list events
- imports: create and inspect imports

Scheduled monitors may exist in the underlying Websets/API/dashboard surface but are not currently exposed as Websets MCP tools. When a monitor is needed, output a monitor spec and route it through the Exa Monitors/API workflow.

## Output Contract

Return:

1. **webset read** - why this should be a Webset or why it should stay a one-off search.
2. **spec** - entity type, query, criteria, enrichments, imports, exclusions.
3. **status** - created/previewed/refreshed IDs and async state.
4. **quality notes** - likely false positives, missing fields, enrichment risk.
5. **memory mapping** - campaign thread, ICP thread, Webset IDs, and next record.
6. **next action** - wait, enrich, export, people search, copy, monitor, or discard.

## Do Not

- Do not create broad reusable Websets without approval.
- Do not put secrets in repo files.
- Do not delete Websets unless explicitly asked.
- Do not confuse Websets MCP with Exa Monitors API availability.
