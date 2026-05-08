# Signal Sourcing

Use this reference when defining ICP cells, sourcing accounts, using Exa/Websets, or scoring account priority.

## Tool Strategy

Use the lightest tool that can prove the current step:

- **Memory Store recall** for product positioning, customer language, ICP hypotheses, prior objections, approved claims, exclusions, and account history.
- **Exa Search MCP** at `https://mcp.exa.ai/mcp` for exploratory web research, market maps, account pages, news, docs, people pages, advanced searches, and source fetches. Active tools: `web_search_exa`, `web_fetch_exa`, and `web_search_advanced_exa` (category, domain, date range, highlights, summaries, subpage crawling). Deprecated but callable for backwards compat: `company_research_exa`, `people_search_exa`, `crawling_exa`, `linkedin_search_exa`, `deep_search_exa`, `get_code_context_exa`.
- **Websets MCP** at `https://websetsmcp.exa.ai/mcp` for structured list building: natural-language criteria, entity verification, enrichment columns, imports, async collection, webhooks, and event polling. 22 tools across webset, items, search, enrichment, webhooks, imports.
- **Exa Monitors REST API** at `https://api.exa.ai/websets/v0/monitors` for cron-scheduled Webset refresh. Not exposed as MCP tools yet — output a monitor spec and let the user attach it via dashboard or API.
- **Gmail connector** only after the account/copy review gate, and only for draft, send, or followup actions the user explicitly asked for.

A website, generic company description, funding database row, or founder title is not a signal. It is only context. The sourcing job is to find a current reason to engage and the persona-specific workflow that reason maps to.

If Exa Search MCP is missing, tell the user to connect it and continue with query design:

```bash
claude mcp add --transport http exa https://mcp.exa.ai/mcp --header "x-api-key: YOUR_EXA_API_KEY"
codex mcp add exa --url https://mcp.exa.ai/mcp
```

Current Codex CLI builds do not support arbitrary `x-api-key` headers through `codex mcp add`. Configure the header in host MCP settings for production limits, or use the free-plan URL above.

If Websets MCP is missing and the task requires structured lead sourcing, tell the user to connect it with their Exa key (Bearer token preferred, query-param fallback for older hosts):

```bash
claude mcp add --transport http websets https://websetsmcp.exa.ai/mcp --header "Authorization: Bearer YOUR_EXA_API_KEY"
export EXA_API_KEY=YOUR_EXA_API_KEY
codex mcp add websets --url https://websetsmcp.exa.ai/mcp --bearer-token-env-var EXA_API_KEY
```

Get the API key at `https://dashboard.exa.ai/api-keys`. Both MCPs use the same key.

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

For Memory Store-built offers, start from these persona families unless recalled context says otherwise:

- **Devtools/community teams** with Discord, Slack, GitHub issues, docs gaps, or repeated support answers.
- **Coding-agent teams** using Cursor, Codex, Claude, repo conventions, PR context, and repeated fix attempts.
- **AI GTM teams** where AI-assisted outbound loses ICP hypotheses, objections, reply learnings, and account context.
- **Founder/operator teams** where founder attention, investor/customer promises, and internal loops fragment.
- **Vertical AI app builders** where user or team memory is part of the product experience.
- **CS/FDE teams** where onboarding, implementation notes, promises, objections, and next actions scatter across tools.
- **Product/customer-insight teams** where feedback, support language, interviews, objections, docs gaps, and churn risks scatter across tools.
- **Internal AI/platform teams** trying to make agents usable across company workflows, approvals, handoffs, and execution context.

Do not classify someone only as a founder. Classify the operating role: technical operator, community/support owner, coding-agent owner, GTM owner, CS/FDE owner, product/customer-insight owner, internal AI/platform owner, or vertical app builder.

## Signal Catalog

Prioritize signals that create a legitimate reason to engage now:

- **LinkedIn** - hiring, founder posts, launch narratives, "we are building agents", support/CS/GTM pain, and team expansion.
- **Reddit/HN** - raw pain language, complaints about AI agents losing context, CRM/support/GTM/tooling frustration.
- **GitHub/docs/changelog** - active agent tooling, support load, integrations, docs churn, repeated issue patterns, and changelog velocity.
- **Product Hunt/YC/Bookface/events** - launch timing, founder intent, category narrative, and visible go-to-market push.
- **Gmail/CRM replies** - objections, warm paths, prior touch history, referrals, and suppression signals.
- **Memory Store context** - approved claims, customer language, old experiments, exclusions, persona learning, and prior account context.
- **Funding and expansion** - recent raise, Form D, hiring surge, new office, market launch.
- **Team movement** - new VP, founder shift, role change, first GTM/operator hire.
- **Product motion** - launch, changelog, docs update, public roadmap, integration announcement.
- **Technical context** - GitHub activity, repo stars, dependency adoption, API docs, infra migration.
- **GTM behavior** - event attendance, sponsor list, webinar, content campaign, partner page, agency/client roster.
- **Competitor context** - public comparison, migration, integration, review, job post mentioning a competitor.
- **Pain evidence** - support/community posts, hiring for a manual workflow, public complaint, lengthy process docs.
- **Memory Store context** - prior conversation, meeting note, customer language, internal hypothesis, objection pattern.

Avoid signals that only prove the company exists. A weak fit with a strong trigger is usually better than a static perfect-fit account with no timely reason to talk.

## Signal Card

Each shortlisted account/person must carry a signal card before copy:

```text
why_this_person:
why_now:
signal_source:
persona:
offer_angle:
proof_path:
next_action:
remember_after_touch:
confidence:
exclusion_risk:
```

If a row cannot support this card, keep it out of draft-ready output. The next step is more research, exclusion, or a watchlist monitor.

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
- Offer angle

## Exa Search Pattern

Use Exa Search MCP for:

- ICP research before Websets.
- Query expansion and competitor/adjacency discovery.
- Fetching source pages behind a Websets row.
- Verifying stale or high-risk claims.
- Finding public language for personalization.

Run query variants for coverage. Search different phrasings for the same ICP cell and dedupe results by domain/company. Prefer `web_search_advanced_exa` for category, people, date, domain, highlights, summaries, and structured lead-generation searches.

## Scoring

Score each account or recipient with compact integers:

- **ICP fit**: 1-10
- **Timing**: 1-10 based on signal freshness and urgency
- **Pain relevance**: 1-10
- **Memory advantage**: 0-5 for useful recalled context
- **Personalization confidence**: 1-10
- **Risk**: low, medium, high

Only send-ready rows should have high fit, a current signal, a clear buyer, a source URL or memory ID, and low exclusion risk.
