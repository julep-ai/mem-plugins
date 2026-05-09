# Signal Sourcing

Use this reference when defining ICP cells, sourcing accounts, using Exa/Websets, or scoring account priority.

## Tool Strategy

Use the lightest tool that can prove the current step, but do not downgrade the production stack into "optional extras." The hierarchy is:

- **Memory Store recall** for product positioning, customer language, ICP hypotheses, prior objections, approved claims, exclusions, and account history.
- **Exa Search MCP** at `https://mcp.exa.ai/mcp` for exploratory web research, market maps, account pages, news, docs, people pages, advanced searches, and source fetches. Active tools: `web_search_exa`, `web_fetch_exa`, and `web_search_advanced_exa` (category, domain, date range, highlights, summaries, subpage crawling). Deprecated but callable for backwards compat: `company_research_exa`, `people_search_exa`, `crawling_exa`, `linkedin_search_exa`, `deep_search_exa`, `get_code_context_exa`.
- **Websets MCP** at `https://websetsmcp.exa.ai/mcp` for structured list building: natural-language criteria, entity verification, enrichment columns, imports, async collection, webhooks, and event polling. 22 tools across webset, items, search, enrichment, webhooks, imports.
- **Exa Monitors REST API** at `https://api.exa.ai/websets/v0/monitors` for cron-scheduled Webset refresh. Not exposed as MCP tools yet — create through approved REST/host automation when possible; dashboard setup is fallback only.
- **Gmail connector** only after the account/copy review gate, and only for draft, send, or followup actions the user explicitly asked for.

Production meaning:

- Memory Store is the required brain.
- Exa Search is the required live research and source-discovery layer.
- Websets is the required production sourcing, verification, enrichment, import, refresh, and export layer.
- Gmail is the required execution and reply-learning layer.
- Exa Monitors are the required always-on signal layer.
- Manual CSVs and pasted lists are valid fallback/import paths, not the primary production loop.

A website, generic company description, funding database row, or founder title is not a signal. It is only context. The sourcing job is to find a current reason to engage and the persona-specific workflow that reason maps to.

If Exa Search MCP or its production API key is missing, tell the user to connect it and continue with setup/query design only. Mark live public research and signal discovery `research_blocked_for_production`:

```bash
claude mcp add --transport http exa https://mcp.exa.ai/mcp --header "x-api-key: YOUR_EXA_API_KEY"
codex mcp add exa --url https://mcp.exa.ai/mcp
```

Current Codex CLI builds do not support arbitrary `x-api-key` headers through `codex mcp add`. Configure the header in host MCP settings for production limits, or use the free-plan URL above only for exploratory lookup. Do not create send-ready rows or outbound drafts from free-plan/website-only research.

If Websets MCP is missing and the task requires structured lead sourcing, tell the user to connect it with their Exa key (Bearer token preferred, query-param fallback for older hosts). Continue by producing Webset queries, criteria, enrichment schemas, and `accounts.csv` import shape, but mark production sourcing `sourcing_blocked_for_production`:

```bash
claude mcp add --transport http websets https://websetsmcp.exa.ai/mcp --header "Authorization: Bearer YOUR_EXA_API_KEY"
export EXA_API_KEY=YOUR_EXA_API_KEY
codex mcp add websets --url https://websetsmcp.exa.ai/mcp --bearer-token-env-var EXA_API_KEY
```

Get the API key at `https://dashboard.exa.ai/api-keys`. Both MCPs use the same key.

If Gmail is missing and the task requires execution, tell the user to connect Gmail. Continue with sourcing and copy hypotheses only. Mark sending, followups, reply scans, suppression checks, and mailbox outcome learning `sending_blocked_for_production`.

If Exa Monitors are not configured, the agent may still run one-off sourcing, but it must mark always-on GTM `monitoring_degraded` and output monitor specs from [monitors.md](monitors.md). Prefer an agent-created REST monitor or host automation after approval; do not tell the user to operate the dashboard unless the host cannot run the API call. Do not claim the campaign is continuously watching signals until a monitor or approved host automation exists.

## Deep Sourcing Minimum

A production sourcing pass is not complete until it attempts all three layers:

1. **Account discovery** - companies or entities matching the ICP cell and live trigger.
2. **Persona discovery** - the specific operating persona/job-to-be-done that owns the pain.
3. **Channel identity** - work email or email-candidate status, LinkedIn/profile URL when available, source URLs, and confidence.

For every send-ready or draft-ready person row, include:

```text
person_name:
company:
persona:
title_or_role:
work_email:
email_status: verified | candidate | unavailable | suppressed
email_source:
linkedin_profile_url:
linkedin_source:
identity_confidence:
why_this_person:
why_now:
signal_source:
offer_angle:
proof_path:
next_action:
exclusion_risk:
```

Do not invent emails. If Exa/Websets cannot produce a public or enriched email, mark `email_status: unavailable`, keep the row out of send-ready state, and propose the next enrichment/import step. If the run only finds company pages, founder titles, or generic categories, it is research, not GTM sourcing.

## Campaign Math

Default high-scale plan:

- 20 ICP cells
- 50 recipients or accounts per ICP cell
- 1000 total recipients
- 5 candidate copy variants per recipient/account

For Websets, oversource each ICP cell by 25-60 percent to absorb duplicates, unreachable accounts, low-confidence rows, exclusions, and bad-fit discoveries. A 50-recipient cell should usually source 65-80 candidates before trimming.

For daily high-intent operation, treat `1000 leads/emails per day` as a sourcing and review target, not an unconditional send quota. The campaign should produce enough verified people and channel identities for the approved ramp, plus a watchlist for later. Promote only rows that pass the signal card gate and suppression checks.

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
- **Learning intent** - what this cell is testing: persona fit, signal quality, proof path, objection, channel, copy angle, or customer-story resonance.

Persona families are seller-specific. The planner does not import a default list — it derives families from the seller's Memory Store recall (customer base, prior campaigns, lived empathy). At least one ICP cell per campaign should be unconventional (see [campaign-planner.md](campaign-planner.md) Persona Discovery), sourced through Memory Store pain recall, not firmographic templates.

## High-Intent Signal Gate

A sourced row is high-intent only when it has at least one current, sourceable reason to engage and a persona-specific reason that person owns the pain. Strong signals include:

- hiring for agent, AI platform, growth, support, community, sales engineering, FDE, or customer operations roles.
- public LinkedIn post about building agents, GTM automation, support load, community scale, launch pressure, workflow bottlenecks, or customer context.
- recent product launch, changelog, docs churn, GitHub issue pattern, integration release, or community/support discussion.
- competitor adoption, competitor complaint, migration signal, public case study, pricing/changelog shift, or public customer story.
- warm-path or prior-reply signal from Gmail/Memory Store.
- match to a remembered customer-story pattern: same persona, same pain, same workflow, similar trigger.

Weak signals do not qualify: generic AI category, old funding, founder title alone, homepage copy, broad company size, or a list membership with no current timing.

## Channel Identity

When LinkedIn is in scope, each person row should keep email and LinkedIn identity together:

```text
person_name:
company:
persona:
work_email:
linkedin_profile_url:
email_source:
linkedin_source:
identity_confidence:
channel_policy: email_only | email_plus_linkedin | linkedin_only | suppress
channel_learning_intent:
```

Email and LinkedIn touches should reinforce the same hypothesis, not duplicate the same wording. Track both against the same person so later insights can answer whether email-only, LinkedIn-only, or combined touches worked for that persona/signal.

The lists below are **illustrative for one kind of seller** (software/AI infrastructure). For other sellers — real estate, legal services, consumer goods, agencies, services, vertical SaaS — recall produces entirely different families. Use these as a structural example only.

### Illustrative families (software/AI seller)

Conventional:

- **Devtools/community teams** with Discord, Slack, GitHub issues, docs gaps, or repeated support answers.
- **Coding-agent teams** using Cursor, Codex, Claude, repo conventions, PR context, and repeated fix attempts.
- **AI GTM teams** where AI-assisted outbound loses ICP hypotheses, objections, reply learnings, and account context.
- **Founder/operator teams** where founder attention, investor/customer promises, and internal loops fragment.
- **Vertical AI app builders** where user or team memory is part of the product experience.
- **CS/FDE teams** where onboarding, implementation notes, promises, objections, and next actions scatter across tools.
- **Product/customer-insight teams** where feedback, support language, interviews, objections, docs gaps, and churn risks scatter across tools.
- **Internal AI/platform teams** trying to make agents usable across company workflows, approvals, handoffs, and execution context.

Unconventional (recall prompts, not a fixed list):

- **AI researchers, scientists, mathematicians** — context loss across papers, notebooks, reasoning chains, and prior proofs.
- **Indie / solo AI builders** — running 4 side projects with no team to absorb context loss.
- **Knowledge workers outside tech adopting AI** — lawyers, doctors, journalists, traders, consultants. Higher-stakes amnesia.
- **Cognition-system power users** — Obsidian, Logseq, Tana, Roam users graduating to agent-native thinking.

### How families look for other sellers (illustrative)

- **Real estate seller**: regional architects on additions, probate attorneys with inherited-property clients, divorce mediators, commercial-to-residential conversion specialists, first-time buyers via permit-pull data, contractors with chronic supply-chain pain.
- **Legal services seller**: solo founders pre-counsel, freelance creators with IP disputes, scaling DTC brands hitting interstate compliance, nonprofits hitting governance pain.
- **Consumer-goods / pet seller**: rescue coordinators routing diet-sensitive dogs, breeders with line-specific feeding history, vet techs with chronic-condition caseloads, multi-pet households with conflicting needs.
- **Agency / services seller**: post-funding teams hiring their first GTM body, founders trying to outsource a function, in-house teams that want to learn-by-watching, agencies servicing other agencies.

Pattern in every case: under-served buyer × specific timing trigger × pain the seller actually understands and can speak to honestly.

Do not classify someone only as a founder. Classify the operating role at the seller's level of abstraction — technical operator, community/support owner, GTM owner, CS/FDE owner, product/customer-insight owner, internal AI/platform owner, vertical app builder, researcher/scientist, indie builder, knowledge worker, cognition-system user, regional architect, probate attorney, solo founder, rescue coordinator, founder-led GTM team, etc. The list is not closed.

## Competitor Intelligence as a Signal Source

Competitors are one of the highest-leverage signal sources in any GTM system. Their public surface — customer logos, case studies, changelogs, hiring, reviews, press, complaints — leaks ICPs, objections, positioning gaps, and timing triggers better than firmographic databases.

Treat competitor watching as recurring routine, not a one-off:

- **Competitor map** — direct, indirect, and adjacent. Maintain in Memory Store. Update when the seller's positioning shifts or new entrants emerge.
- **Competitor customer scrape** — Webset of named customers from each competitor's site, case studies, and public testimonials. Refresh monthly.
- **Competitor changelog/launch monitor** — Exa Monitor per competitor on blog/changelog/release-notes URLs. Cron weekly or daily depending on competitor velocity. New launches and pricing changes are direct timing triggers.
- **Competitor hiring monitor** — what they hire reveals what they think they need next. A competitor hiring "Director of Customer Marketing" tells you they are about to push case studies; a competitor hiring "Solutions Engineer for Enterprise" tells you they are climbing market.
- **Competitor review/complaint monitor** — G2, Capterra, Trustpilot, Yelp, Reddit, HN, Glassdoor depending on category. Public negative reviews are the best objection-handling and copy-hook source you have.
- **Ex-customer signal** — people who publicly switch away from a competitor are pre-qualified leads if the seller honestly does it better.

Competitor signals feed three planner outputs: ICP cell design (their customers as a target pool), signal sourcing (their changelog/news drives outreach timing), and copy proof paths (their gaps are your wedges). See [campaign-planner.md](campaign-planner.md) Competitor Intelligence section for the planner-side requirements.

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
- Person name
- Buyer title
- Persona / job-to-be-done
- Work email or email status
- LinkedIn/profile URL
- Identity confidence
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
