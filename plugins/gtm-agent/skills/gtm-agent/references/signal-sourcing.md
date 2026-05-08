# Signal Sourcing

Use this reference when defining ICP cells, sourcing accounts, using Exa/Websets, or scoring account priority.

## Tool Strategy

Use the lightest tool that can prove the current step:

- **Memory Store recall** for product positioning, customer language, ICP hypotheses, prior objections, approved claims, exclusions, and account history.
- **Exa Search MCP** for exploratory public-web research, market maps, account pages, news, docs, people pages, and source fetches.
- **Websets MCP** for structured list building: natural-language criteria, entity verification, enrichment columns, imports, async collection, and event/webhook-style updates.
- **Gmail connector** only after the account/copy review gate, and only for draft, send, or followup actions the user explicitly asked for.

If Exa Search MCP is missing, tell the user to connect it and continue with query design:

```bash
codex mcp add exa --url https://mcp.exa.ai/mcp
```

If Websets MCP is missing and the task requires structured lead sourcing, tell the user to connect it with their Exa key:

```text
https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY
```

## Campaign Math

Default high-scale plan:

- 20 ICP cells
- 50 recipients or accounts per ICP cell
- 1000 total recipients
- 5 candidate copy variants per recipient/account

For Websets, oversource each ICP cell by 25-60 percent to absorb duplicates, unreachable accounts, low-confidence rows, exclusions, and bad-fit discoveries. A 50-recipient cell should usually source 65-80 candidates before trimming.

## ICP Cell Shape

Each ICP cell should have:

- **Name** - specific enough to search, not a vague persona.
- **Buyer** - role/title/function and why they own the pain.
- **Pain** - phrased in customer language recalled from Memory Store when possible.
- **Trigger signals** - events that make outreach timely.
- **Hard criteria** - must-have filters.
- **Soft criteria** - ranking signals.
- **Exclusions** - competitors, current customers, low-fit segments, regulated edges, or do-not-contact categories.
- **Target count** - usually 50 for the user's 1000-recipient plan.

## Signal Catalog

Prioritize signals that create a legitimate reason to engage now:

- **Funding and expansion** - recent raise, Form D, hiring surge, new office, market launch.
- **Team movement** - new VP, founder shift, role change, first GTM/operator hire.
- **Product motion** - launch, changelog, docs update, public roadmap, integration announcement.
- **Technical context** - GitHub activity, repo stars, dependency adoption, API docs, infra migration.
- **GTM behavior** - event attendance, sponsor list, webinar, content campaign, partner page, agency/client roster.
- **Competitor context** - public comparison, migration, integration, review, job post mentioning a competitor.
- **Pain evidence** - support/community posts, hiring for a manual workflow, public complaint, lengthy process docs.
- **Memory Store context** - prior conversation, meeting note, customer language, internal hypothesis, objection pattern.

Avoid signals that only prove the company exists. A weak fit with a strong trigger is usually better than a static perfect-fit account with no timely reason to talk.

## Websets Pattern

For each ICP cell, create or preview a Webset with:

- Entity type: usually `company`, sometimes `person` for role-led campaigns.
- Query: one concrete sentence describing the ICP and trigger.
- Criteria: hard filters that every result must satisfy.
- Enrichments: fields needed to score, personalize, and route outreach.
- Imports: exclusion CSVs, existing customer lists, prior campaign rows, or known account universes.

Useful enrichment columns:

- Company name and website
- ICP fit reason in 20 words or less
- Trigger signal in 20 words or less
- Source URL for trigger
- Buyer title
- Relevant quote or phrase from public source
- Employee range or funding stage
- Competitor/tool overlap
- Exclusion risk
- Outreach angle

## Exa Search Pattern

Use Exa Search MCP for:

- ICP research before Websets.
- Query expansion and competitor/adjacency discovery.
- Fetching source pages behind a Websets row.
- Verifying stale or high-risk claims.
- Finding public language for personalization.

Run query variants for coverage. Search different phrasings for the same ICP cell and dedupe results by domain/company.

## Scoring

Score each account or recipient with compact integers:

- **ICP fit**: 1-10
- **Timing**: 1-10 based on signal freshness and urgency
- **Pain relevance**: 1-10
- **Memory advantage**: 0-5 for useful recalled context
- **Personalization confidence**: 1-10
- **Risk**: low, medium, high

Only send-ready rows should have high fit, a current signal, a clear buyer, a source URL or memory ID, and low exclusion risk.
