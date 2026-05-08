# Campaign Planner

Use this reference before sourcing at scale or drafting copy. Load [campaign-engineering.md](campaign-engineering.md) first when campaign mode, context sources, funnel stage, or ICP system are unclear. The planner exists because generic outreach usually fails upstream: the agent treats a website as a signal, a founder title as a persona, and a category fit as enough reason to write.

## Planner Rule

Do not draft outbound until the campaign unit is complete:

```text
persona + live signal + offer angle + proof path + next action
```

For each account or person, the planner must answer:

- **why this person** - role, responsibility, workflow ownership, or relationship context.
- **why now** - a current public or private signal, not just company existence.
- **where signal came from** - URL, Memory Store ID, Gmail/CRM thread, or approved pasted evidence.
- **what persona they are** - precise operating persona, not only title or seniority.
- **what offer angle maps to them** - the specific product, plugin, brief, workflow, service, or thesis that fits this persona and signal.
- **proof path** - how the claim can be demonstrated without inventing metrics or private customer stories.
- **next action** - reply ask, teardown offer, demo path, intro, followup, suppress, or research more.
- **what should be remembered** - the learning that should be recorded after approval, rejection, send, reply, objection, or meeting.
- **confidence and exclusion risk** - confidence level plus why the prospect might be wrong, stale, already contacted, competitor, customer, or do-not-contact.

If any field is missing, output a planner gap and the exact research query or Memory Store recall needed. Do not produce a polished email to hide weak evidence.

## Offer Profile

The planner is product-agnostic. Memory Store is the context and learning substrate; the campaign may sell Memory Store core, GTM Agent, briefs, context engineering, customer insights, a distribution plugin, a consulting motion, or any other product.

Before sourcing, define the active offer profile:

- **campaign mode** - whether this is new, building on previous work, refresh, expansion, rescue, reactivation, or launch/event-driven.
- **context source base** - Memory Store, uploaded/pasted docs, website, Gmail, Calendar, prior campaign artifacts, Exa/Websets.
- **offer being sold** - exact product, plugin, workflow, service, or thesis.
- **sender persona** - who is speaking and why they have credibility.
- **core claim** - one sentence the campaign is testing.
- **do-not-pitch list** - labels, claims, and categories that flatten the offer.
- **buyer/persona map** - who owns the pain.
- **signal sources** - where timing or pain will be proven.
- **proof path** - demo, teardown, brief, customer example, workflow audit, benchmark, or artifact.
- **conversion action** - reply, call, install, pilot, teardown, brief review, or intro.

If the offer is ambiguous, infer from Memory Store first. If more than one offer is plausible, show the likely options and ask the user to choose before drafting.

## First-Run Setup Contract

When GTM Agent has no approved setup packet, route setup to `campaign-setup` before sourcing or drafting. Campaign Setup owns the repeatable onboarding questions and exact setup packet schema. The approved setup packet must define:

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

Default Memory Store-built ICP range is AI/devtools/startup-to-midmarket teams with roughly 10-500 employees and active product, GTM, support, or agent motion. Fortune and enterprise campaigns require an explicit user choice.

Default same-company rule: max 2 contacts per company, only when personas are meaningfully different. Keep one primary active thread per company unless a referral happens.

Default media policy: text-first outreach, no screenshot attachment by default, but discovered screenshots/assets may be collected as proof options.

## Memory Store Offer Profiles

Use these only when Memory Store or a Memory Store-built plugin is the seller. For other sellers, infer equivalent profiles from their memories and public evidence.

### Memory Store Core

**Sender persona:** Shubham as technical founder/operator, not a sales rep. Voice: sharp, memory-native, skeptical of generic AI automation, focused on agent continuity and execution context.

**Core claim:** Agents have amnesia. A wiki will not fix it. Memory Store is the shared execution context layer across Slack, email, docs, GitHub, support, GTM, and agents.

**Do not lead with:** better AI memory, knowledge base, CRM, RAG, AI sales tool, or MCP plugin. Those may appear as implementation detail only if the prospect's context makes them relevant.

**Default first wedge:** devtools and AI infra teams with public support, community, docs, GitHub, or context-loss signals. This wedge best matches Memory Store's strongest remembered positioning around agent continuity, support/community memory, coding-agent memory, and Memory Store-powered GTM learning.

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

## ICP Personas

Use these as the default persona map for Memory Store-built offers. Pick the narrowest persona that explains why the person would care.

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
persona | live signal | source | offer angle | proof path | next action | remember after touch | confidence | exclusion risk
```

For Memory Store-built offers, also include:

- active offer profile.
- strongest wedge to start with.
- personas to exclude for now.
- signal sources to prioritize.
- claims that are approved.
- claims that need proof before copy.

## Draft Eligibility

An account/person is draft-eligible only when:

- the persona is specific enough to explain ownership of the pain.
- the signal is timely, sourceable, and stronger than "they exist".
- the offer angle maps to that persona's actual workflow.
- the proof path is honest without private leakage.
- the next action is concrete and low-friction.
- confidence is at least moderate and exclusion risk is low or explicitly accepted.

Otherwise, keep the row in `research_more`, `exclude`, or `watch` state.
