# Campaign Planner

Use this reference before sourcing at scale or drafting copy. Load [campaign-engineering.md](campaign-engineering.md) first when campaign mode, context sources, funnel stage, or ICP system are unclear. The planner exists because generic outreach usually fails upstream: the agent treats a website as a signal, a founder title as a persona, and a category fit as enough reason to write.

## Planner Rule

Do not draft outbound until the campaign unit is complete:

```text
persona + high-intent signal + customer-story/persona pattern + offer angle + proof path + next action + learning intent
```

For each account or person, the planner must answer:

- **why this person** - role, responsibility, workflow ownership, or relationship context.
- **why now** - a current public or private signal, not just company existence.
- **where signal came from** - URL, Memory Store ID, Gmail/CRM thread, or approved pasted evidence.
- **what persona they are** - precise operating persona, not only title or seniority.
- **what customer story or remembered pattern maps to them** - which existing customer, user, objection, support theme, or persona pattern explains why this prospect should care. Use approved public proof only in outbound; keep private stories as internal strategy unless approved.
- **what offer angle maps to them** - the specific product, plugin, brief, workflow, service, or thesis that fits this persona and signal.
- **proof path** - how the claim can be demonstrated without inventing metrics or private customer stories.
- **next action** - reply ask, teardown offer, demo path, intro, followup, suppress, or research more.
- **what should be remembered** - the learning that should be recorded after approval, rejection, send, reply, objection, or meeting.
- **learning intent** - what this touch is testing: persona, signal source, customer-story resonance, subject line, proof path, CTA, email channel, LinkedIn channel, or sequence step.
- **confidence and exclusion risk** - confidence level plus why the prospect might be wrong, stale, already contacted, competitor, customer, or do-not-contact.

If any field is missing, output a planner gap and the exact research query or Memory Store recall needed. Do not produce a polished email to hide weak evidence.

## Briefs And Evidence

Use canonical briefs to understand the current operating map, then use recall to verify evidence. Do not treat a brief as enough evidence for a prospect-specific claim.

For each campaign plan or material update, state:

```text
briefs_used:
brief_authority: active | stale | conflicted | none
recall_queries_needed:
evidence_ids_or_urls:
brief_delta:
```

`brief_delta` is only for reusable operating truth: an ICP definition changed, a proof path became approved, a signal source became unreliable, a new objection pattern changed copy policy, or a campaign outcome changed future sourcing. Single-account research, one-off replies, and draft edits belong in records or campaign artifacts, not new briefs.

## Customer Usage Map And ICP Evidence

The `customer_usage_map` is not a dump of Memory Store IDs. It is the map of real customers/users for the seller being configured, when discoverable. For Memory Store-owned campaigns, those are Memory Store's own customers/users. For another seller, they are that seller's customers/users. For account-level signal cards, also build a lightweight prospect customer map when useful: the target account's customers, customer categories, testimonials, case studies, reviews, or users found publicly.

Use Memory Store IDs, Gmail threads, CRM IDs, and URLs as evidence attached to ICP cells. Do not let evidence IDs stand in for the actual customer usage map.

Before public ICP expansion, classify:

- paid customers and activation attempts.
- direct power users and internal dogfood users.
- old product power users, triers, ghost signups, and landing-page leads.
- passive-ingest workspaces where value comes from Slack/meeting/source memory rather than direct tool calls.
- customer failures, thin stores, unopened briefs, connector gaps, and support patterns.
- prior GTM plans, customer docs, sales playbooks, and account briefs.
- public customer pages, logos, case studies, testimonials, reviews, partner pages, changelogs mentioning customers, and social posts from users.

Then convert those observations into ICP cells:

```text
seller customer/user pattern -> job-to-be-done -> target account pool -> persona -> high-intent signal -> proof path -> evidence IDs/URLs -> exclusion rule
```

Examples for Memory Store itself:

- **Paid onboarding/wiki customer:** Siftly/Swiftly-style teams where implicit GTM/customer knowledge does not transfer to new hires. Public expansion pool: GEO/AEO/AI-search agencies, content-ops companies, and knowledge-heavy customer-delivery teams.
- **Sales/GTM context user:** Minicor/Ishita-style operators using Memory Store as grounded context for sales copy, account briefs, objections, and campaign learning. Public expansion pool: Clay/Smartlead/Apollo agencies, GTM engineering teams, and founder-led B2B sellers doing signal-based outbound.
- **Coding-agent continuity user:** Shubham/Rishabh-style users who need Codex, Claude, Cursor, or repo agents to preserve project context and exact working rules. Public expansion pool: developer-tool teams, AI coding-agent teams, MCP/server tooling, and engineering-heavy startups.
- **Passive workspace memory:** Shashank/Ukumi and Diwo-style teams where value comes from Slack, meeting, source, standup, and product-operation context. Public expansion pool: remote-first teams, CS/FDE/product ops teams, and companies using Fathom/Fireflies/Granola/Slack/Google Chat.
- **Reactivation pool:** existing Julep/Memory Store power users, triers, and enriched leads. This is not an Exa-discovered ICP; it is an owned-account campaign and should run before cold expansion when the goal is fast learning.

Do not use these examples as fixed defaults. Use the real seller's current Memory Store and public customer evidence first. The planner output must show which seller customer/user pattern created each ICP cell and which Memory Store IDs, Gmail/CRM references, or public URLs support it.

When direct customer evidence is absent, derive customer proxies with Exa/Websets before finalizing ICPs:

```text
"<seller> customers case studies testimonials users reviews logos"
"<seller category> case studies customers using <tool/workflow>"
"site:<seller-domain> customer OR customers OR case-study OR testimonial OR user"
"category:company companies whose customers are <target buyer> and who mention <workflow pain>"
```

For target accounts, a prospect customer map can sharpen personalization:

```text
target account -> their customers/users -> what they sell/deliver -> where Memory Store/GTM Agent helps them serve those customers -> public proof URL
```

Use this only when sourceable. Do not imply the prospect has customers that were merely inferred.

## Offer Profile

The planner is **seller-agnostic**. Memory Store is the context and learning substrate, but the seller can be any business — software, infrastructure, services, real estate, consumer goods, vertical SaaS, agencies, consulting. The planner shape is identical; only the contents change.

Before sourcing, define the active offer profile:

- **campaign mode** - whether this is new, building on previous work, refresh, expansion, rescue, reactivation, or launch/event-driven.
- **context source base** - Memory Store, uploaded/pasted docs, website, Gmail, Calendar, prior records or connector/workspace exports, Exa/Websets.
- **offer being sold** - exact product, service, package, listing, or thesis.
- **seller identity** - what the seller is, what motion they run (sales-led, product-led, founder-led, agency, broker, services), and what kind of credibility they bring.
- **sender persona** - who is speaking and why they have credibility.
- **core claim** - one sentence the campaign is testing.
- **do-not-pitch list** - labels, claims, and categories that flatten the offer.
- **buyer/persona map** - who owns the pain.
- **signal sources** - where timing or pain will be proven.
- **customer-story map** - which remembered customer stories, user behaviors, objections, or outcome patterns imply new personas to test.
- **proof path** - demo, teardown, brief, customer example, workflow audit, listing comp, case study, benchmark, or artifact.
- **conversion action** - reply, call, install, pilot, teardown, brief review, intro, viewing, consult, sample, quote.

If the offer is ambiguous, infer from Memory Store first. If more than one offer is plausible, show the likely options and ask the user to choose before drafting.

## Competitor Intelligence

Every campaign needs a live competitor map. Competitors are not just exclusion fodder — they are signal-rich, learnable opponents whose customer pages, case studies, hiring, launches, reviews, and complaints reveal the buyer landscape better than any firmographic database.

Before sourcing, define:

- **named competitors** - direct, indirect, and category-adjacent. Direct = same buyer, same pain. Indirect = same buyer, different pain, fights for the same budget. Adjacent = different buyer, related category.
- **competitor watchlist** - URLs to monitor: homepage, customers/case studies, pricing, changelog/release notes, hiring page, blog, public reviews (G2/Capterra/Trustpilot/Yelp/Zillow/etc), press mentions.
- **competitor customer signals** - who shows up on competitor case studies; who endorses them publicly; who left them and posted about it. These are the most leakable ICP signals you have.
- **competitor objections and complaints** - what reviewers, ex-customers, and Reddit/HN/community threads complain about. These are your strongest copy hooks if the seller honestly does it better.
- **competitor positioning gaps** - what they do not say, do not promise, do not cover. The seller's wedge usually hides in those gaps.

Operationalize competitor intelligence as a routine, not a one-shot:

- weekly Exa Monitor on each competitor's blog, pricing, and changelog (one monitor per competitor; cron-anchored to a buyer-friendly timezone).
- Webset of competitor customers refreshed on a slow cadence.
- Memory Store record of every confirmed competitor positioning shift, customer churn signal, or objection pattern.

Competitor intelligence feeds three downstream things: ICP cell design (use their customers as a target pool), signal sources (their changelog/news drives outreach timing), and copy proof paths (their gaps are your wedges). Without competitor intelligence the campaign reverts to firmographic spam.

## First-Run GTM Plan Contract

When GTM Agent has no approved GTM plan, route the first plan to `campaign-setup` before sourcing or drafting. The `campaign-setup` skill owns the repeatable onboarding questions and exact GTM plan schema for compatibility with existing hosts. The approved GTM plan must define:

- active offer profile.
- campaign mode and context source base.
- funnel system and current stage gaps.
- sender persona and brand voice.
- ICP cells and company-size range.
- demo CTA policy.
- media/screenshot policy.
- send policy and ramp limits.
- followup cadence.
- suppression policy.
- autopilot routine specs.

Default ICP range is whatever the seller's Memory Store recall produces — there is no universal default size or category. Recall against the seller's customer base before the planner picks ranges. (As an illustrative reference: a software/AI seller might default to 10-500 employee teams with active product/GTM motion. A real-estate seller might default to a metro-area + property-type filter. A legal-services seller might default to industry × growth-stage. The planner names defaults from Memory Store, not from this file.)

Default same-company rule: max 2 contacts per company, only when personas are meaningfully different. Keep one primary active thread per company unless a referral happens.

Default media policy: text-first outreach, no screenshot attachment by default, but discovered screenshots/assets may be collected as proof options.

## Example Offer Profiles (Memory Store seller)

The profiles below are illustrative — they show how the planner shape gets filled when Memory Store itself is the seller. They are not the default for every campaign. For any other seller, infer equivalent profiles from that seller's memories, customer language, and public evidence. Use these as a structural template, not a content template.

### Memory Store Core

**Sender persona:** Shubham as technical founder/operator, not a sales rep. Voice: sharp, memory-native, skeptical of generic AI automation, focused on agent continuity and execution context.

**Core claim:** Agents have amnesia. A wiki will not fix it. Memory Store is the shared execution context layer across Slack, email, docs, GitHub, support, GTM, and agents.

**Do not lead with:** better AI memory, knowledge base, CRM, RAG, AI sales tool, or MCP plugin. Those may appear as implementation detail only if the prospect's context makes them relevant.

**Default first wedge:** choose the strongest observed-customer wedge from Memory Store recall, then expand publicly with Exa/Websets. For Memory Store itself, current strong wedges include onboarding/wiki customers, GTM context users, coding-agent continuity users, passive workspace-memory teams, and owned-account reactivation. Do not default to "devtools and AI infra" unless current recall says that is the best starting wedge.

Useful offer angles:

- agents forgetting context across sessions, tools, and workers.
- context engineering as infrastructure, not prompt stuffing.
- making agents usable for ongoing work by giving them execution context.
- team collaboration where Slack, email, docs, GitHub, support, GTM, and agents share one context layer.
- customer insights and product feedback scattered across tools.
- briefs as living, decision-ready artifacts over company memory.

### GTM Agent Plugin

**Core claim:** GTM does not fail at the email sentence first; it fails when ICP, signal, proof, replies, and learnings are not remembered or turned into recurring execution. GTM Agent uses Memory Store plus Exa/Websets/Gmail/host automations to engineer a campaign once, then keep it running inside approved policy.

**Best buyers:** AI GTM teams, founder-led GTM teams, growth engineers, sales engineers, agencies, and technical operators running signal-based outbound.

**Useful offer angles:** campaign planner, signal-card quality gate, Websets sourcing, Exa research, Gmail followups, reply learning, daily/weekly automation routines, and campaign compounding.

**Proof path:** show a campaign planner, a few high-quality signal cards, the exact routine specs, and how approved replies/objections would be recorded into Memory Store for the next batch.

### Briefs

**Core claim:** Teams do not need another static document; they need briefs that preserve decisions, customer context, proof, objections, and next actions as work changes.

**Best buyers:** founders, CS/FDE teams, sales engineers, support/community teams, customer-success leaders, product leaders, and internal AI platform teams.

**Useful offer angles:** customer briefs, account briefs, market briefs, implementation briefs, investor/customer promise tracking, and sales handoff context.

**Proof path:** produce a small account/customer/market brief from available context and show how it reduces re-briefing and next-action ambiguity.

### Customer Insights

**Core claim:** Customer insight is not a dashboard by itself; it is repeated language, objections, promises, confusion, and high-intent signals becoming usable context before the next action.

**Best buyers:** product leaders, founders, CS/FDE teams, support/community leads, GTM teams, and teams with many customer touchpoints across Slack, email, calls, docs, support, and CRM.

**Useful offer angles:** product feedback memory, objection memory, account context, docs-gap detection, churn risk, support pattern recall, and customer-language reuse.

**Proof path:** show a compact customer-insight readout or brief from real sources, then map it to next-best actions for product, support, sales, or founder followup.

### Future Distribution Plugins

**Core claim:** Distribution workflows get better when they are memory-backed instead of template-backed. Each plugin should remember context, feedback, outcomes, and channel-specific taste.

**Best buyers:** content/devrel teams, founder-led distribution teams, GTM teams, community teams, and teams building agent-native workflows for customers.

**Useful offer angles:** LinkedIn/content, GTM, support/community, customer insight, market research, launch monitoring, and workflow-specific agent routines.

**Proof path:** show the plugin's input context, output artifact, feedback loop, and what it records for the next run.

## Persona Discovery

ICPs are not a static template, and they are never seller-agnostic. The same planner method runs whether the seller is selling AI infrastructure, houses, legal services, or dog food — but the personas produced are entirely a function of the seller's offer and Memory Store's recall about that seller's customers, prior objections, and lived empathy.

Four rules for every campaign, every seller:

1. **Start from pain, not category.** Recall pain language from Memory Store first — the seller's customer notes, prior objections, support transcripts, founder threads, sales call notes, public complaints in the seller's space. Cluster the pain. Then ask which roles or workflows own that pain. Category/firmographic fit comes last, not first.

2. **Empathy gate.** The seller must be able to speak to this persona honestly because the seller has lived an adjacent version of the pain. If the planner cannot answer "why are *we* (this specific seller) the right person to write to *them*", drop the persona. This is what makes campaigns sound true and stops them from sounding like cold spam.

3. **Customer-story expansion.** Use existing customer stories and usage patterns to discover more personas. Ask: who else has the same pain but would describe it differently? who sits next to the current buyer? who benefits after the first user succeeds? what objection indicates a hidden buyer? Each new persona must name the source story/pattern and the hypothesis being tested.

4. **One unconventional ICP per campaign, mandatory.** At least one ICP cell must be a persona no one else is targeting for this offer. Found through Memory Store recall, not firmographic templates. The other cells can be conventional. Examples of how unconventional looks in practice:

   - Software/AI seller: AI researchers, indie builders, knowledge workers outside tech adopting AI, cognition-system power users.
   - Real-estate seller (houses, bricks, fixtures): probate attorneys with inherited-property clients, divorce mediators, regional architects working on additions, commercial-to-residential conversion specialists.
   - Legal services seller: solo founders without house counsel facing first-time contract pain, freelance creators with IP disputes, scaling DTC brands hitting interstate compliance.
   - Dog food / pet seller: rescue coordinators routing diet-sensitive dogs, breeders with line-specific feeding history, vet techs with chronic-condition caseloads.

   Pattern: under-served buyer × specific timing trigger × pain the seller actually understands.

These are recall prompts, not fixed lists. Run Memory Store recall on the seller's pain language and customer history; let new personas surface; record approved unconventional personas back so the next campaign starts smarter.

## ICP Personas (illustrative, software/AI seller)

The list below is an illustrative persona map for one kind of seller — software/AI infrastructure. For other sellers, the families look entirely different. Recall against the seller's own Memory Store first; do not import this list as a default.

Pick the narrowest persona that explains why the person would care. Combine with at least one unconventional ICP from Persona Discovery above.

- **Devtools/community teams:** Discord, Slack, GitHub issues, docs gaps, and repeated support answers.
- **Coding-agent teams:** Cursor/Codex/Claude workflows, repo conventions, repeated bugs, failed fixes, and PR context.
- **AI GTM teams:** outbound or research teams using AI but losing ICP hypotheses, objections, reply learnings, and account context.
- **Founder/operator teams:** YC or funded AI teams where founder attention, investor/customer promises, and internal loops fragment.
- **Vertical AI app builders:** products where user or team memory is part of the actual app experience.
- **CS/FDE teams:** onboarding notes, implementation details, promises, objections, and next-best actions scattered across tools.
- **Product/customer-insight teams:** user feedback, support language, interviews, objections, docs gaps, churn risk, and feature demand scattered across tools.
- **Internal AI/platform teams:** teams trying to make agents usable across company workflows, approvals, handoffs, and execution context.

Do not use "founder" as the persona by itself. A founder can be a technical operator, GTM owner, community/support owner, product/customer-insight owner, internal AI/platform owner, or vertical app builder. Classify the job-to-be-done.

## Signal Sources

Prefer live or recently refreshed signals that show timing, pain, or workflow ownership:

- **LinkedIn:** hiring, founder posts, launch narratives, "we are building agents", support/CS/GTM pain, and team expansion.
- **Reddit/HN:** raw pain language, complaints about AI agents losing context, CRM/support/GTM/tooling frustration.
- **GitHub/docs/changelog:** active agent tooling, support load, integrations, docs churn, repeated issue patterns, and changelog velocity.
- **Product Hunt/YC/Bookface/events:** launch timing, founder intent, category narrative, and visible go-to-market push.
- **Gmail/CRM replies:** objections, warm paths, prior touch history, referrals, and suppression signals.
- **Memory Store:** approved claims, customer language, old experiments, exclusions, persona learning, and prior account context.

A homepage, generic "AI" category, funding page, or founder title is context, not a signal. It can support research but cannot open an email by itself.

## Planner Output

Before any copy package, return a campaign planner table with these columns:

```text
persona | high-intent signal | source | customer-story/persona pattern | offer angle | proof path | next action | learning intent | remember after touch | confidence | exclusion risk
```

Also return a customer-derived ICP map before the planner table:

```text
seller customer/user pattern | source evidence IDs/URLs | inferred job-to-be-done | public expansion pool | Websets/search query | first-batch target count | exclusion rule
```

For Memory Store-built offers, also include:

- active offer profile.
- strongest wedge to start with.
- customer-derived ICP map.
- personas to exclude for now.
- signal sources to prioritize.
- claims that are approved.
- claims that need proof before copy.
- persona/customer-story hypotheses being tested.
- email and LinkedIn channel policy when dual-channel is in scope.

## Draft Eligibility

An account/person is draft-eligible only when:

- the persona is specific enough to explain ownership of the pain.
- the signal is timely, sourceable, and stronger than "they exist".
- the customer-story/persona pattern explains why this message should be useful to someone like them.
- the offer angle maps to that persona's actual workflow.
- the proof path is honest without private leakage.
- the next action is concrete and low-friction.
- the learning intent is explicit enough to improve the next batch.
- confidence is at least moderate and exclusion risk is low or explicitly accepted.

Otherwise, keep the row in `research_more`, `exclude`, or `watch` state.
