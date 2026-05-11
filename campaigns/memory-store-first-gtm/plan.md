# Memory Store First GTM Campaign

Status: GTM plan created; production sourcing and sending blocked until approval and connector gates pass
Created: 2026-05-09
Updated: 2026-05-09
Memory Store thread: T-V1H5BS
Prior planning thread: T-496W7H
Campaign slug: memory-store-first-gtm

## Plan Decision Groups

inferred:

- Primary offer is Memory Store core, not GTM Agent, because the campaign is for Memory Store itself.
- Campaign mode is `plan_new_campaign` now, with `start_new_campaign` after approval.
- Public positioning is strong enough for planning: "one memory for your team's agents", shared context from meetings, Claude sessions, Slack, and work history.
- First ICP cells should start from actual Memory Store usage patterns before public-market expansion.
- Memory Store MCP is usable in this session and can back campaign context plus approved learning records.
- Exa advanced search is usable for public research and query design in this session.
- Exa key is configured locally for Codex as of 2026-05-09.
- Websets MCP is visible, but production Websets API access is blocked by the current Exa team/plan.
- Gmail should remain blocked for sends, drafts, reply scanning, and mailbox learning until the GTM plan is explicitly approved.
- The first five ICP cells are launch cells, not the full Memory Store market. The broader ICP universe also includes founder/operator context owners, product/customer insight teams, support/community teams, internal AI/platform teams, vertical AI app builders, content/devrel distribution teams, research/knowledge workers, and agencies/consultancies.

needs_confirmation:

- Sender identity: Shubham, Ishita, or a shared founder identity.
- CTA: reply-first, `Talk to founders` at `https://cal.com/ishitaj/20min`, or a different booking/demo path.
- Private proof policy: default is internal strategy only unless a customer/story is explicitly approved for outbound copy.
- First shadow-sample cells. Recommended: GTM Context Operators, Customer Delivery Memory Teams, Coding Agent Continuity Teams, plus Passive Workspace Memory as the unconventional test.
- Whether the first expanded shadow sample should include founder/operator, product/customer insight, support/community, internal AI/platform, vertical AI app, content/devrel, research/knowledge-worker, or agency/consulting cells.
- Whether LinkedIn stays profile-only or becomes a second approved touch channel.
- Whether Codex automations should be created for approved routines after launch.

unknown_blocker:

- Websets production sourcing is blocked: after configuring the provided Exa key, direct Websets API verification still returned 401 because the key's Exa team does not have Websets API access and needs a Pro/API-enabled plan.
- No approved Gmail send/reply policy exists yet.
- No approved monitor creation policy exists yet, and monitors require working Websets IDs first.
- No first shadow sample has been sourced, reviewed, or approved.

## GTM Plan

company_profile:

- company_name: Memory Store
- website: https://memory.store/
- one_line_product_read: One memory for a team's agents. Memory Store turns meetings, Claude sessions, Slack chats, and other work history into shared context that teammates and agents can recall.
- market_category: agent memory, shared context layer, MCP-native workspace memory.
- public_sources:
  - https://memory.store/
  - https://memory.store/guides
  - https://app.memory.store/
  - https://cal.com/ishitaj/20min
  - https://www.ycombinator.com/companies/memory-store
- confidence: high for public positioning; moderate for exact campaign CTA until the user confirms.
- missing_facts:
  - approved sender.
  - approved CTA.
  - approved public customer proof.
  - first-batch ICP priority.
  - approved Gmail and automation policy.

campaign_mode:

- primary: plan_new_campaign
- next_mode_after_approval: start_new_campaign
- evidence: the repo already had a proposed campaign folder, but no approved account rows, signal cards, copy, sends, events, or Memory Store campaign records.
- policy_implications:
  - `plan.md` is the operating contract.
  - no Websets creation until Websets API access works and the plan is approved.
  - no production account sourcing until Websets/API gate passes or the user explicitly approves a manual/import fallback.
  - no outbound copy until a shadow sample proves account discovery, persona discovery, channel identity, live signal, and customer-pattern fit.
  - no Gmail sends, followups, or reply scans until approved.

context_sources:

- Memory Store:
  - status: ready
  - used_for: prior GTM plan semantics, Memory Store customer/user patterns, ICP hypotheses, sender voice preferences, taboo phrasing, connector expectations.
  - evidence: T-V1H5BS, T-496W7H, T-ZF8ZYP, M-25E7CG, M-46EB5Z, M-0P36VM, M-FTDTJC, M-F258XS, M-R1Z891.
  - allowed_in_copy: no private details unless explicitly approved.
- Website:
  - status: ready
  - used_for: public positioning, public proof path, CTA candidates, integration language.
  - public evidence: Memory Store homepage, app signup path, guides path, YC profile.
- Exa Search:
  - status: ready_for_public_research
  - used_for: public proof, competitor/category research, account-query design, ICP-source discovery.
  - not_sufficient_for: production Websets-backed sourcing or send-ready rows by itself.
- Websets:
  - status: sourcing_blocked_for_production
  - blocker: Websets API returned 401 for the configured Exa key's current plan/team.
  - used_for_now: query, criteria, enrichment, and monitor specs only.
- Gmail:
  - status: sending_blocked_until_approval
  - used_for_now: none in this plan update.
  - allowed_after_approval: bounded sender voice, warm paths, suppressions, campaign thread search, reply classification, followups only if explicitly allowed.
- Calendar:
  - status: booking_context_disabled_until_reply_or_cta_approval
  - used_for_now: CTA candidate only.
- Prior campaign artifacts:
  - status: proposed plan existed; no prior sends or outcomes.
- Uploaded or pasted docs:
  - status: none provided.

connector_status:

- plan_status: plan_only
- Memory Store: production_ready_for_context_and_learning_records_after_approval.
- Exa Search: research_ready; advanced search is visible in-session.
- Websets: sourcing_blocked_for_production; configured Exa key is valid for auth but the key's team lacks Websets API access.
- Exa Monitors: monitoring_degraded; requires parent Webset IDs and approved API/automation policy.
- Gmail: sending_blocked_for_production until explicit approval.
- Google Calendar: booking_context_disabled until CTA/booking policy is approved or a qualified reply needs scheduling context.
- Host automations: manual_until_scheduled; routine specs exist but are not scheduled.

briefs_used:

- none_selected_in_this_plan_update:
  - status: none
  - reason: this campaign artifact was updated from the planning thread and repo-local campaign state, not from a loaded canonical brief.
  - allowed_to_influence: none until a future run selects 0-3 canonical briefs through Memory Store `list-briefs`.
  - recall_needed_for_detail: Memory Store GTM plan requirements, Exa/Websets blocker history, and Memory Store customer/user patterns should be recalled before production sourcing.

offer_profiles:

- active_offer:
  - name: Memory Store core
  - core_claim: The hard part is not storing chat history. It is knowing what from the past is still binding for the next agent, teammate, or workflow.
  - product_claim: Memory Store gives teams one shared memory across agents and work surfaces, so context from meetings, Slack, Claude, Codex, docs, and customer work can be recalled where work happens.
  - conversion_action: reply-first or founder-call CTA, pending confirmation.
  - proof_path:
    - public website: "One memory for your team's agents."
    - public integrations: Claude, ChatGPT, Cursor, Slack, Raycast, Linear, Granola, Fathom, OpenCode.
    - YC profile: "Shared context for all of your team's agents."
    - public CTA: signup at https://app.memory.store/ and founder call at https://cal.com/ishitaj/20min.
    - private Memory Store usage patterns for internal targeting only.
- alternate_offers:
  - GTM Agent plugin: use only for GTM operators who specifically want memory-backed outbound execution.
  - Briefs / living playbooks: use for CS, FDE, onboarding, customer ops, and internal operating context.
  - Coding-agent continuity: use for engineering, devtools, MCP, and AI-agent teams.
- do_not_pitch:
  - generic RAG.
  - static knowledge base.
  - CRM replacement.
  - AI sales tool as the primary category.
  - generic "better AI memory" without a workflow.
  - automatic capture of everything without rules, connectors, and user control.

customer_usage_map:

- source_status: Memory Store private evidence plus public positioning. Private customer names are strategy only by default.
- usage_patterns:
  - pattern: GTM/account context and sales copy
    evidence: Minicor sales/marketing copy usage, Ishita sales/GTM playbook context, Diro/Siftly/Pandatron GTM context surfaced in Memory Store recall.
    job_to_be_done: preserve account context, ICP theory, objections, proof paths, and reply learning across GTM workflows.
    expansion_pool: AI GTM teams, founder-led B2B sellers, GTM engineering teams, Clay/Apollo/Smartlead agencies.
    confidence: high internally; public proof still needs sourcing or approval.
  - pattern: onboarding/wiki/customer delivery
    evidence: Siftly onboarding/wiki direction, Briefs onboarding value proposition, living customer-doc work.
    job_to_be_done: keep customer onboarding state, promises, implementation context, support language, and living playbooks current.
    expansion_pool: CS, FDE, onboarding, implementation, customer ops, knowledge-heavy agencies.
    confidence: high internally; moderate externally until public proof is sourced.
  - pattern: coding-agent continuity
    evidence: Shubham/Rishabh-style project continuity, Zyng project-continuity usage, repo-agent context discipline.
    job_to_be_done: stop coding agents from rediscovering repo decisions, failed attempts, conventions, and working rules.
    expansion_pool: devtools, AI coding-agent teams, MCP/plugin builders, engineering-heavy startups.
    confidence: high.
  - pattern: passive workspace memory
    evidence: Shashank/Ukumi and Diwo-style passive workspace memory, Slack/meeting/source memory patterns.
    job_to_be_done: make Slack, meeting, standup, customer, and product-operation context available without manual filing.
    expansion_pool: remote teams, product ops, support/community, CS/FDE, meeting-heavy B2B teams.
    confidence: moderate to high.
  - pattern: owned reactivation
    evidence: archived Julep/Memory Store power-user and trier segments from prior planning.
    job_to_be_done: learn quickly from prior product intent and familiarity.
    expansion_pool: owned users only.
    confidence: high; requires suppression review before use.
  - pattern: founder/operator context ownership
    evidence: founder/operator Memory Store usage and repeated product framing around obligations, open loops, customer promises, investor context, hiring, and agent execution state.
    job_to_be_done: keep the company operating context alive across meetings, Slack, email, docs, and agents so the founder does not re-brief every worker.
    expansion_pool: YC and Seed/Series A founders, chiefs of staff, early operators, founder-led AI/B2B teams.
    confidence: high as a thesis; needs sourced signal proof.
  - pattern: product/customer insight memory
    evidence: customer-doc and Briefs work, customer language reuse, product feedback and account-context readouts.
    job_to_be_done: turn scattered feedback, objections, docs gaps, feature asks, and customer language into usable context before product or GTM decisions.
    expansion_pool: product leads, founder-PMs, customer researchers, product ops, support/product hybrids.
    confidence: high.
  - pattern: support/community memory
    evidence: repeated support/community context, docs gaps, Slack/community ingestion, and customer answer reuse.
    job_to_be_done: stop teams from repeatedly answering the same issues while agents lose user history, docs gaps, and community context.
    expansion_pool: devrel teams, community leads, support leads, Discord/Slack community operators, open-source maintainers.
    confidence: moderate to high.
  - pattern: internal AI/platform memory
    evidence: Memory Store positioning as shared context for a team's agents and recurring need for durable approvals, constraints, obligations, and policies.
    job_to_be_done: make internal agents usable across workflows by giving them access to approved rules, context, handoffs, and decision history.
    expansion_pool: internal AI leads, platform engineers, AI transformation owners, automation leads, RevOps/IT automation teams.
    confidence: moderate to high.
  - pattern: vertical AI app memory
    evidence: Memory Store as an agent memory layer rather than a notes app or generic RAG system.
    job_to_be_done: let vertical AI products give their own users or teams durable, scoped, inspectable context across sessions.
    expansion_pool: vertical AI app builders in legal, healthcare, finance, real estate, procurement, education, recruiting, and customer ops.
    confidence: moderate.
  - pattern: content/devrel/founder-led distribution memory
    evidence: LinkedIn Studio, content from customer calls, launch memory, and founder voice/work context.
    job_to_be_done: recover the best market language, customer stories, launch angles, and founder taste from calls, Slack, docs, and prior agent work.
    expansion_pool: founder-led distribution teams, devrel leads, content operators, community-led growth teams.
    confidence: moderate to high.
  - pattern: research/high-context knowledge work
    evidence: product thesis that memory should preserve what remains binding: sources, decisions, reasoning chains, taste constraints, and open questions.
    job_to_be_done: preserve long-running reasoning and source trails across sessions, documents, notebooks, meetings, and agents.
    expansion_pool: AI researchers, analysts, consultants, strategy teams, legal/finance operators, high-context independent experts.
    confidence: moderate; needs careful wedge selection.
  - pattern: agency/consulting multi-client memory
    evidence: customer-delivery and GTM-context patterns generalize to client-service teams that repeatedly switch contexts.
    job_to_be_done: preserve separate client context, promises, deliverables, objections, approvals, and next actions across projects and agents.
    expansion_pool: AI agencies, GTM agencies, implementation consultancies, product studios, RevOps consultancies.
    confidence: moderate to high.

sender_voice:

- proposed_sender: Shubham Attri as technical founder/operator.
- alternate_sender: Ishita Jindal as founder, especially for founder-call CTA and public YC narrative.
- confidence: moderate until sender is confirmed.
- style:
  - short plain-text emails.
  - one concrete workflow observation before the ask.
  - specific language around agents, context, obligations, decisions, and open loops.
  - skeptical of shallow AI automation.
- use:
  - "what from the past is still binding"
  - "the context your agent needs before it starts"
  - "record in one tool, recall in another"
  - "your agent should not start from zero"
- avoid:
  - "genuinely"
  - generic praise.
  - fake urgency.
  - private customer names.
  - unsupported metrics.

website_findings:

- pages_checked:
  - https://memory.store/
  - https://memory.store/guides
  - https://app.memory.store/
  - https://www.ycombinator.com/companies/memory-store
- claims_found:
  - "One memory for your team's agents."
  - "Turn every meeting, Claude session, and Slack chat into context your team and agents share."
  - Works with Claude, ChatGPT, Cursor, Slack, Raycast, Linear, Granola, Fathom, and OpenCode.
  - Memory Store runs as an MCP inside agents already used today.
  - YC profile says Memory Store is shared context for all of a team's agents.
- proof_assets:
  - homepage positioning.
  - signup path.
  - founder-call CTA.
  - setup guides.
  - YC profile.
  - public founder YC announcement as optional social proof after confirmation.
- risky_or_unsupported_claims:
  - do not claim automatic capture from every tool for every customer.
  - do not claim every listed integration is fully production-ready for every account.
  - do not claim time saved, close-rate lift, token savings, or revenue impact without approved evidence.

demo_cta:

- discovered_link_candidates:
  - Sign up: https://app.memory.store/
  - Talk to founders: https://cal.com/ishitaj/20min
- chosen_link: needs_user_confirmation
- confirmation_status: unconfirmed for outbound use.
- proposed_cta_style:
  - first touch: reply-first.
  - high-intent founder/operator row: "Worth a 10-minute founder call on where your agents lose context?"
  - low-friction fallback: "If this is a real problem, reply with the tool where context gets lost most often."

funnel_system:

- current_stage: plan_new_campaign.
- stage_map:
  - market_definition: strong enough for planning.
  - customer_usage_map: strong internally; public usage proof needs approval.
  - ICP_hypotheses: proposed.
  - signal_discovery: partially ready through Exa; production lists blocked by Websets plan access.
  - account_sourcing: blocked for production.
  - buyer_discovery: blocked for production.
  - evidence_cards: blocked until shadow sample sourcing.
  - copy_hypothesis: blocked until signal cards pass planner gate.
  - review_approval: active next step.
  - send_followup: blocked.
  - reply_classification: blocked until Gmail routine approval.
  - learning_record: proposed only; record after approval or confirmed outcomes.

icp_matrix:

- cell_name: GTM Context Operators
  buyer_persona: founder-led GTM owner, GTM engineer, sales engineer, outbound agency operator, technical growth lead.
  company_size: 5-200 employees to start.
  trigger_signals:
    - hiring or posting about GTM engineering, AI SDRs, outbound automation, RevOps automation, or signal-based outbound.
    - public use of Clay, Apollo, Smartlead, Instantly, or account-brief workflows.
    - founder/operator posts about ICP refinement, reply learning, outbound quality, or customer/account context.
  customer_story_or_pattern: GTM/account-context usage from Memory Store customers and internal GTM planning.
  proof_path: GTM plan, signal-card quality gate, and Memory Store learning loop.
  target_count: 20 accounts for first reviewed batch after shadow sample.
  confidence: high.
  exclusions: pure bulk-email agencies, low-signal lead-gen shops, current customers unless expansion is approved.
- cell_name: Customer Delivery Memory Teams
  buyer_persona: CS lead, FDE lead, onboarding lead, implementation lead, customer ops founder.
  company_size: 10-500 employees.
  trigger_signals:
    - hiring solutions, FDE, onboarding, implementation, or customer success.
    - public case studies or implementation-heavy workflows.
    - docs, changelog, customer rollout, or onboarding evidence.
  customer_story_or_pattern: onboarding/wiki/customer-delivery usage patterns.
  proof_path: account/customer brief or living playbook generated from real context.
  target_count: 15 accounts.
  confidence: high internally, moderate externally until sourced.
- cell_name: Coding Agent Continuity Teams
  buyer_persona: technical founder, engineering lead, AI platform lead, devtools/community lead, MCP/plugin builder.
  company_size: 2-200 employees.
  trigger_signals:
    - public agent tooling, MCP servers, AI coding products, Cursor/Claude/Codex workflows.
    - GitHub activity around AI agents or developer productivity.
    - docs/changelog velocity suggesting active agent/product work.
  customer_story_or_pattern: repeated project-continuity and repo-agent context usage.
  proof_path: record in one agent, recall in another; project continuity readout.
  target_count: 20 accounts.
  confidence: high.
- cell_name: Passive Workspace Memory
  buyer_persona: product ops lead, founder/operator, chief of staff, support/community lead.
  company_size: 10-300 employees.
  trigger_signals:
    - meeting-heavy or remote teams.
    - visible use of Slack, Fathom, Fireflies, Granola, Linear, Notion, or customer communities.
    - public posts about coordination, standups, customer context, or AI agents.
  customer_story_or_pattern: passive workspace memory from Slack, meetings, standups, and product operations.
  proof_path: living status/context readout over meetings and Slack.
  target_count: 10 accounts.
  confidence: moderate.
  unconventional: true.
- cell_name: Owned Reactivation
  buyer_persona: prior Julep/Memory Store power users and triers.
  company_size: existing owned list.
  trigger_signals:
    - archived power-user or trier segment.
    - previous signup, usage, revenue, or product interaction.
  customer_story_or_pattern: prior Julep and Memory Store usage.
  proof_path: prior usage plus the new Memory Store shared-agent-memory surface.
  target_count: 10 contacts after suppression review.
  confidence: high.
  production_note: not an Exa/Websets-discovered ICP. Requires owned-list import plus Gmail/suppression review.
- cell_name: Founder Operator Context Owners
  buyer_persona: founder, chief of staff, early operator, founder-PM, or technical operator at an AI/B2B startup.
  company_size: 2-100 employees.
  trigger_signals:
    - YC, accelerator, launch, funding, hiring, or rapid team-growth signal.
    - founder posts about agents, internal ops, customer promises, investor asks, hiring, or losing context across tools.
    - visible use of Slack, Notion, Linear, Gmail, meetings, Claude/Codex/Cursor, or multiple operating surfaces.
  customer_story_or_pattern: founder/operator Memory Store usage where obligations, decisions, customer context, and open loops need to survive across tools and workers.
  proof_path: founder operating-memory readout or "what is still binding" briefing.
  target_count: 15 accounts after first shadow sample.
  confidence: high as a broad wedge; needs live-signal proof.
- cell_name: Product Customer Insight Teams
  buyer_persona: product lead, founder-PM, customer researcher, product ops lead, support/product hybrid.
  company_size: 10-500 employees.
  trigger_signals:
    - public feedback programs, changelog velocity, docs gaps, support themes, customer interviews, community feedback, or roadmap posts.
    - hiring for product operations, user research, customer insights, support operations, or product marketing.
    - visible customer-facing Slack/community, review, support, or interview-heavy workflow.
  customer_story_or_pattern: Memory Store customer-doc, Briefs, and customer-language reuse patterns.
  proof_path: compact customer-insight brief that maps repeated language, objections, promises, and feature asks to next actions.
  target_count: 15 accounts.
  confidence: high.
- cell_name: Support Community Memory Teams
  buyer_persona: devrel lead, community lead, support lead, developer advocate, open-source maintainer, support/community founder.
  company_size: 5-300 employees.
  trigger_signals:
    - active Discord, Slack, GitHub issues, forum, docs, or community support channel.
    - public docs churn, repeated support questions, community growth, or onboarding complaints.
    - hiring support, community, devrel, or docs roles.
  customer_story_or_pattern: Slack/community/support memory and repeated-answer patterns.
  proof_path: support/community context brief showing repeated questions, docs gaps, owner context, and reusable answers.
  target_count: 15 accounts.
  confidence: moderate to high.
- cell_name: Internal AI Platform Teams
  buyer_persona: internal AI lead, platform engineer, automation lead, AI transformation owner, RevOps/IT automation lead.
  company_size: 50-2000 employees.
  trigger_signals:
    - hiring internal AI, AI automation, platform, AI enablement, or agent workflow roles.
    - public posts about rolling out agents internally, AI governance, workflow automation, or copilots.
    - visible multi-tool operating stack where agents need approvals, constraints, and shared context.
  customer_story_or_pattern: Memory Store as shared context for agents carrying approved rules, obligations, and handoffs.
  proof_path: internal agent policy/context profile showing what an agent can recall before acting.
  target_count: 10 accounts for validation only; enterprise motion may be slower.
  confidence: moderate.
- cell_name: Vertical AI App Builders
  buyer_persona: vertical AI founder, product lead, AI app builder, applied AI engineer.
  company_size: 2-100 employees.
  trigger_signals:
    - launching AI products where user or team memory is part of the workflow.
    - public vertical workflows with repeated user context: legal, healthcare, finance, real estate, procurement, recruiting, education, customer ops.
    - posts/docs about personalization, memory, agents, user history, or long-running workflows.
  customer_story_or_pattern: Memory Store as an embeddable agent memory layer rather than a static notes or RAG system.
  proof_path: memory profile or MCP-backed context loop that shows record/recall across sessions.
  target_count: 10 accounts.
  confidence: moderate.
- cell_name: Content Devrel Distribution Teams
  buyer_persona: founder-led distribution owner, devrel lead, content operator, community-led growth lead, product marketer.
  company_size: 2-200 employees.
  trigger_signals:
    - frequent launches, founder posts, technical blogs, community content, or product storytelling.
    - public customer calls, webinars, podcasts, case studies, or devrel/community activity.
    - visible need to reuse customer language and founder taste across channels.
  customer_story_or_pattern: LinkedIn Studio and memory-to-public-thinking workflows.
  proof_path: content angle or launch brief recovered from customer calls, Slack, docs, and prior work.
  target_count: 10 accounts.
  confidence: moderate to high.
- cell_name: Research Knowledge Workers
  buyer_persona: AI researcher, analyst, consultant, strategy lead, legal/finance operator, high-context independent expert.
  company_size: individual to 200 employees.
  trigger_signals:
    - long-form research, reports, papers, notebooks, investigations, repeated client work, or source-heavy workflows.
    - public writing about AI research, analysis, complex projects, or knowledge systems.
    - visible tool use around Obsidian, Notion, research agents, coding notebooks, or source management.
  customer_story_or_pattern: memory as preserving source trails, decisions, reasoning chains, taste constraints, and open questions.
  proof_path: research/context brief showing source-backed recall and unresolved open loops.
  target_count: 10 accounts as exploratory.
  confidence: moderate; high risk of broadness unless trigger is sharp.
- cell_name: Agencies Consultancies Multi Client Memory
  buyer_persona: AI agency founder, GTM agency operator, implementation consultant, product studio lead, RevOps consultant.
  company_size: 2-100 employees.
  trigger_signals:
    - serving multiple clients, publishing case studies, hiring delivery/GTM roles, or selling AI automation/services.
    - public client roster, workflow templates, implementation offers, or agency playbooks.
    - posts about client context, handoff, onboarding, delivery quality, or AI agents.
  customer_story_or_pattern: agency and customer-delivery memory where each client has separate promises, workflows, context, artifacts, and next actions.
  proof_path: client-memory workspace or account brief that keeps each client context separate and retrievable.
  target_count: 15 accounts.
  confidence: moderate to high.

signal_sources:

- Memory Store: approved customer/user patterns, objections, exclusions, prior plans.
- Exa Search: public proof, account discovery research, competitor/category maps, public source URLs.
- Websets: structured production sourcing, enrichment, dedupe, persistent lists. Currently blocked by Exa plan access.
- GitHub/docs/changelog: coding-agent and devtools timing evidence.
- LinkedIn: profile discovery and public posts. LinkedIn touches disabled until approved.
- Reddit/HN: pain language around AI agents losing context, memory systems, MCP, and workflow fragmentation.
- Product Hunt/YC/events: launch timing, founder intent, visible GTM push.
- Gmail: warm paths, suppressions, prior touches, replies, and sender voice after approval.
- Competitor/category watch:
  - Mem0/OpenMemory.
  - Zep/Graphiti.
  - Letta/MemGPT.
  - LangMem/LangGraph memory.
  - Cognee.
  - Supermemory and other MCP memory tools.
  - Knowledge Plane and shared/team memory framing.
- Segment-specific sources:
  - YC/company directories for founder/operator, vertical AI, and internal AI teams.
  - job posts for GTM, CS/FDE, support/community, internal AI, product ops, and devrel roles.
  - GitHub, docs, changelogs, and MCP directories for coding-agent and vertical AI builders.
  - Discord, Slack community pages, GitHub issues, docs pages, and forums for support/community teams.
  - podcasts, webinars, founder posts, newsletters, and launch pages for content/devrel teams.
  - agency case studies, partner pages, service pages, and client rosters for agency/consulting cells.

gmail_learnings:

- status: not used in this update; sending and mailbox learning blocked until approval.
- planned_search_scope_after_approval:
  - prior Memory Store founder-led messages.
  - demo/onboarding/customer threads.
  - prior touches to known owned accounts.
  - unsubscribes, negative replies, bounces, and active threads for suppression.
- policy: no draft, send, label, archive, broad scan, or reply-monitoring action until approved.

calendar_policy:

- default: use only after qualified replies unless user explicitly confirms a booking-link CTA.
- booking_link_candidate: https://cal.com/ishitaj/20min
- chosen_booking_link: needs_user_confirmation.
- meeting_duration: 20 minutes if Ishita link is approved.
- timezone: use recipient/company timezone when known; current local environment is Asia/Kolkata.
- allowed_before_approval: none.
- allowed_after_approval:
  - include approved booking link.
  - read availability only if explicitly approved.
  - do not create or move events unless separately approved.

channel_policy:

- primary_channel: email.
- secondary_channel: LinkedIn profile discovery only.
- linkedin_touch_policy: disabled_until_approved.
- per_person_touch_limit:
  - initial email.
  - followup 1 after 3-4 business days.
  - followup 2 after 6-8 business days.
  - breakup after 12-15 business days.
- same_company_rule: max 2 active contacts per company only when personas differ meaningfully.
- dedupe_policy: one primary active thread per company unless a referral creates a relevant second lead.

send_ramp_policy:

- status: proposed.
- day_1: max 10 sends.
- days_2_3: max 20 sends per day.
- day_4_onward: max 50 sends per day until changed.
- cap_policy: ceiling, not quota.
- first_touch_requires:
  - approved plan.
  - approved sender.
  - approved CTA.
  - passed shadow sample.
  - Gmail approval.
  - suppression check.
  - signal card with live source URL, person identity, channel identity, customer-pattern fit, proof path, and low/accepted risk.
- pause_conditions:
  - bounce or deliverability risk.
  - unsubscribe, do-not-contact, or negative reply.
  - duplicate recent outreach.
  - active existing thread.
  - unapproved or private claim.
  - missing signal/source/person identity.
  - Gmail connector ambiguity.
  - Websets/production sourcing unavailable.

autopilot_routines:

- routine_name: shadow_sample_builder
  status: proposed_blocked_by_approval_and_websets_access
  goal: create 5-10 reviewed account/person signal cards before production sends.
  cadence: one-time before launch.
  required_tools: Memory Store, Exa Search, Websets or approved manual import, Gmail suppression check.
  allowed_actions_after_approval: source accounts, enrich person identity, update accounts.csv, write signal cards.
  forbidden_actions: draft, send, create monitors, mutate Gmail, mutate Calendar.
  output: reviewed shadow-sample table plus planner gaps.
- routine_name: daily_sourcing_digest
  status: proposed
  goal: summarize new qualified accounts, rejected accounts, evidence gaps, and questions.
  cadence: weekdays after Websets exists or manual import is approved.
  output: digest and accounts.csv updates.
- routine_name: gmail_reply_scan
  status: proposed_requires_send_and_gmail_approval
  goal: classify replies, bounces, unsubscribes, objections, referrals, positive replies, and owner actions.
  cadence: every 2 hours after launch.
  forbidden_until_approved: broad mailbox scan, labels, sends, followups.
- routine_name: followup_check
  status: proposed_requires_send_approval
  goal: identify threads eligible for followup under stop conditions.
  cadence: daily after launch.
  allowed_actions_after_approval: draft or send only inside approved policy.
- routine_name: weekly_learning_summary
  status: proposed
  goal: summarize ICP, signal, copy, objection, proof-path, and suppression learning.
  cadence: weekly.
  record_to_memory_store: approved learnings and confirmed outcomes only.
- routine_name: high_intent_monitor_review
  status: proposed_blocked_until_websets_ids
  goal: review monitor output for approved ICP cells.
  cadence: weekly after monitor creation.

memory_distillation:

- proposed:
  - The first Memory Store campaign should be customer-usage-map first, not generic AI/devtools first.
  - Private customer/user patterns shape targeting and scoring, but outbound copy uses only public or explicitly approved proof.
  - GTM Agent for Memory Store must keep planning separate from production readiness.
  - Websets production sourcing is currently blocked by Exa plan access, not by missing local tool discovery.
  - The first launch should use a shadow sample before any draft or send.
  - The first five ICP cells are the launch set, not the full ICP universe. Expanded cells should be explored through shadow samples and kept out of send-ready state until signal quality is proven.
  - Approval of the GTM plan permits only the explicit actions listed in routine specs.
- approved: []
- active: []
- deprecated: []

brief_delta:

- target_brief: GTM Operating Brief
  section: connector gates and plan-first campaign policy
  change: GTM Agent should keep this campaign in `plan_only` while Websets production access is blocked, require a shadow sample before drafting or sending, and treat approved routines as the only autonomous action scope.
  evidence: this plan.md, Websets 401 blocker, and user-approved GTM Agent planning rules.
  status: proposed
  supersedes: none
  needs_user_approval: yes
- target_brief: ICP/Persona Brief
  section: Memory Store launch cells
  change: the first five ICP cells are the launch set; expanded cells remain shadow-sample hypotheses until evidence proves signal quality.
  evidence: this plan.md customer_usage_map and ICP matrix.
  status: proposed
  supersedes: none
  needs_user_approval: yes

approval_needed_before_start:

- approve or edit this GTM plan.
- confirm sender.
- confirm CTA.
- confirm private proof policy.
- confirm first ICP cells for the shadow sample.
- confirm which expanded ICP cells should enter the next shadow sample.
- enable Exa Websets API access or approve a manual/import fallback for the first sample.
- approve Gmail draft/send/reply-scan scope.
- approve followup cadence and same-company policy.
- approve monitor creation policy after Websets exist.
- approve host automation creation, if desired.
