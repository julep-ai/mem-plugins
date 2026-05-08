# Exa Workflows

Use this reference when deciding which Exa surface should do which GTM job.

## Mental Model

Do not collapse Exa into one "lead search" step.

- **Exa Company Research** answers: "What is this company/space/account and why might it matter?"
- **Exa Lead Generation** answers: "Which companies match this ICP and what structured fields should we extract?"
- **Exa People Search** answers: "Which likely buyers or experts match these accounts and personas?"
- **Websets** answers: "What verified set of companies/people should we persist, enrich, revisit, and export?"
- **Monitors** answer: "What should we keep watching so new high-intent triggers enter the workflow automatically?"
- **Memory Store** answers: "What have we already learned internally, and how should that change this search, copy, or next step?"

## Company Research Worker

Use company research for market and account understanding:

- company overview, product, pricing, team, funding, customers
- competitors and alternatives
- people pages and public LinkedIn-style profiles
- news, launches, partnerships, hiring, events
- source URLs and uncertainty notes

Pattern:

1. Run query variations in parallel.
2. Use `category: "company"` for company discovery.
3. Use `category: "news"` for announcements and timing.
4. Use `category: "people"` for public profile discovery.
5. Return compact account briefs, not raw search dumps.

## Lead Generation Worker

Use lead generation for large ICP pools:

1. Research the target company and infer ICP.
2. Generate micro-verticals from confirmed ICPs.
3. Design a structured output schema.
4. Run batches in parallel.
5. Deduplicate, score, and trim.

Use `web_search_advanced_exa` for current Exa MCP lead-generation work. If a host still exposes deprecated tools such as `deep_search_exa`, treat them as backward-compatible helpers, not the primary path.

For the user's default scale:

```text
20 ICP cells x 50 accepted targets = 1000 targets
source 65-80 candidates per ICP before trimming
```

The main agent should stay lean. Batch workers should write or return only compact summaries: count, failures, file/path if applicable, and top quality notes.

## Websets Worker

Use Websets for persistent and verified sets:

- natural-language entity search
- criteria verification
- enrichment columns
- imports for exclusions or seed accounts
- async results over time
- webhook/event handoff into downstream workflows

Create a Webset when the list is likely to be reused, monitored, exported, or enriched across multiple campaign runs.

## Monitor Worker

Use Exa Monitors for recurring signal streams:

- funding news
- hiring pages
- product launches
- integration announcements
- competitor/customer mentions
- GitHub/docs/changelog movement
- conference/event pages
- pain-point language in public posts, forums, or blogs

Monitors are scheduled recurring searches that re-run a query against an existing Webset and append (or override) verified results. They are not currently exposed as MCP tools — create them via the dashboard at `https://dashboard.exa.ai` or the REST API at `POST https://api.exa.ai/websets/v0/monitors` (see [monitors.md](monitors.md)). Cadence uses a 5-field Unix cron expression that triggers at most once per day, anchored to an IANA timezone. Webhook events `webset.item.created`, `webset.item.enriched`, and `webset.idle` deliver structured output downstream. Store monitor IDs, parent Webset IDs, query, cadence, behavior, webhook route, and related Memory Store thread IDs.

## Routing Rule

Use this order:

1. Memory Store recall to define the context and exclusions.
2. Exa company research to understand and expand the market.
3. Websets or Exa lead generation to build target pools.
4. Exa people search to find likely buyers after account fit is good.
5. Monitors to keep the strongest signals alive.
6. Gmail only after review.
7. Memory Store record to make outcomes compound.
