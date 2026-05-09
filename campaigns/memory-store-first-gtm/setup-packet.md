inferred:
- Campaign should start as `plan_new_campaign` / `new_campaign`; no approved setup packet existed in this repo.
- Primary offer should be Memory Store core, not GTM Agent, because the user asked for a campaign "for memory store".
- Customer usage map must be built from Memory Store's actual customers/users and usage patterns, not a dump of Memory Store IDs.
- Strongest initial cells are GTM/account-context operators, onboarding/customer-delivery teams, coding-agent continuity users, passive workspace-memory teams, and owned reactivation.
- Memory Store MCP is authenticated and usable in this session; current thread is T-496W7H.
- Gmail is authenticated enough for search/read; sending remains disabled until explicit campaign approval.
- Codex MCP config now has Exa configured with the advanced-search tool URL and Websets configured with Exa API-key auth. Current tool surface still exposes only basic Exa search/fetch until Codex reloads the MCP tool list.

needs_confirmation:
- Sender identity: Shubham vs Ishita vs a shared founder identity.
- CTA: reply-first, "talk to founders", or a specific booking/demo link.
- Whether private customer names may be used only for internal strategy or also in reviewed copy. Default: internal only.
- Top ICP cells for the first 5-10 account shadow sample.
- Whether LinkedIn is profile-only or a second approved touch channel.
- Whether host automations should be created after approval.

unknown_blocker:
- Websets tools are configured but not visible in this already-running session. Production sourcing is blocked until Codex restarts/reloads and exposes the Websets tool namespace.
- Advanced Exa search is configured but not visible in this already-running session. Production-grade company/person/article/news research is blocked until Codex restarts/reloads and exposes `web_search_advanced_exa`.
- No confirmed demo/founder-call URL. Do not put a link in outbound copy yet.

company_profile:
  company_name: Memory Store
  website: https://memory.store/
  one_line_product_read: one memory for a team's agents; it turns meetings, Claude sessions, Slack chats, and other work history into context the team and agents can share.
  market_category: agent memory / shared context layer / MCP-native workspace memory.
  public_sources:
    - https://memory.store/
    - https://memory.store/guides
    - https://memory.store/manus
    - https://www.ycombinator.com/companies/memory-store
  confidence: high for current public positioning; moderate for exact CTA because the booking path needs confirmation.
  missing_facts:
    - confirmed outbound sender.
    - confirmed booking/demo URL.
    - approved public customer proof.
    - pricing/package to offer in the first campaign, if any.

campaign_mode:
  primary: plan_new_campaign
  secondary: new_campaign
  evidence: no existing first-campaign artifacts were found in the repo; setup has not been approved for sourcing or sending.
  policy_implications:
    - create setup packet and plan first.
    - no Websets, monitors, drafts, sends, or Memory Store campaign records until approval.
    - require a shadow sample before first production send.

context_sources:
  memory_store:
    status: ready
    used_for:
      - prior GTM setup semantics.
      - customer usage map.
      - customer-derived ICP cells.
      - sender voice preferences and taboo phrasing.
    evidence_ids:
      - T-496W7H
      - T-VH0DQ4
      - T-ZF8ZYP
      - T-MXBX6R
      - M-RHDFP8
      - M-KAWWFY
      - M-T9YCVT
      - M-C7RTCK
      - M-9S6F87
      - M-5H552D
      - M-348CMS
      - M-0P36VM
  website:
    status: ready
    allowed_to_influence:
      - product language.
      - proof path.
      - CTA candidates.
      - public positioning.
  exa_search:
    status: configured_pending_codex_reload
    allowed_to_influence:
      - website and public proof research.
    not_allowed_yet:
      - production ICP discovery.
      - production account sourcing.
      - send-ready signal cards.
      - outbound copy.
  websets:
    status: configured_pending_codex_reload
    allowed_to_influence: none yet.
  gmail:
    status: ready_for_search_read
    allowed_to_influence:
      - bounded sender voice.
      - warm-path and suppression search after approval.
    not_allowed_yet:
      - draft creation.
      - sending.
      - reply-monitoring automations.
  calendar:
    status: available_by_connector_context_but_not_exercised
    allowed_to_influence:
      - booking context after qualified replies.
    not_allowed_yet:
      - event creation or mutation.
  prior_campaign_artifacts:
    status: none_found
  uploaded_or_pasted_docs:
    status: none_provided

connector_status:
  packet_status: setup_only
  memory_store:
    status: production_ready_for_context
    evidence: checkin and recall succeeded; thread T-496W7H.
  exa_search:
    status: configured_pending_codex_reload
    evidence: `codex mcp list` shows Exa configured with `web_search_exa`, `web_fetch_exa`, and `web_search_advanced_exa`; current session still exposes only basic Exa tools.
    required_action: restart/reload Codex until `web_search_advanced_exa` is available for company, people, article, and news categories.
  websets:
    status: configured_pending_codex_reload
    evidence: `codex mcp list` shows Websets configured with Exa API-key auth; current session still does not expose Websets tools.
    required_action: restart/reload Codex until create/list/get/search/enrichment Websets tools appear.
  exa_monitors:
    status: monitoring_degraded
    evidence: monitors are REST/API-only per docs and require approved Webset IDs first.
    required_action: approve monitor specs after Websets exist.
  gmail:
    status: sending_blocked_until_approval
    evidence: Gmail search/read succeeded.
    required_action: approve draft/send/reply-scan policy before any Gmail mutations.
  google_calendar:
    status: booking_context_disabled_until_reply
    evidence: connector is declared by plugin context but not needed before qualified replies.
    required_action: confirm booking link or calendar use policy.
  host_automations:
    status: manual_until_scheduled
    required_action: approve routine specs before creating automations.

offer_profiles:
  active_offer:
    name: Memory Store core
    core_claim: Agents need shared execution context across sessions and tools; Memory Store turns meetings, Claude sessions, Slack, and work history into memory agents can recall.
    conversion_action: reply-first or founder-call CTA, pending confirmation.
    proof_path:
      - public website.
      - YC profile.
      - MCP setup guides.
      - private customer usage patterns for internal targeting only.
  alternate_offers:
    - name: GTM Agent plugin
      use_when: targeting GTM operators who specifically want a memory-backed outbound loop.
    - name: Briefs / living playbooks
      use_when: targeting customer delivery, onboarding, CS, or internal ops.
    - name: coding-agent continuity
      use_when: targeting technical founders, engineering leads, devtools, MCP, and coding-agent teams.
  do_not_pitch:
    - generic RAG.
    - static knowledge base.
    - CRM replacement.
    - AI sales tool as the primary category.
    - "better AI memory" without a concrete workflow.
    - automatic capture of everything without user/agent recording rules.

customer_usage_map:
  source_status: memory_store_private_evidence_plus_public_positioning
  usage_patterns:
    - pattern: GTM/account context and sales copy
      examples_or_evidence: Minicor sales/marketing copy usage; Ishita sales/GTM playbook; Diro/Siftly/Pandatron GTM context.
      job_to_be_done: preserve account context, ICP theory, objections, proof paths, and campaign learning across GTM workflows.
      expansion_pool: AI GTM teams, founder-led B2B sellers, GTM engineering teams, Clay/Apollo/Smartlead agencies.
      confidence: high from Memory Store recall; public proof still needs approval.
    - pattern: onboarding/wiki/customer delivery
      examples_or_evidence: Siftly onboarding wiki direction; Briefs onboarding value proposition; customer living docs.
      job_to_be_done: keep customer onboarding state, promises, implementation context, and living playbooks up to date.
      expansion_pool: CS/FDE/onboarding/implementation teams, knowledge-heavy agencies, customer-delivery teams.
      confidence: high internally; public proof needs approval.
    - pattern: coding-agent continuity
      examples_or_evidence: Shubham/Rishabh-style project continuity, Zyng usage, repo-agent context discipline.
      job_to_be_done: stop coding agents from rediscovering repo decisions, failed attempts, conventions, and working rules.
      expansion_pool: devtools, AI coding-agent teams, MCP/plugin builders, engineering-heavy startups.
      confidence: high.
    - pattern: passive workspace memory
      examples_or_evidence: Shashank/Ukumi and Diwo-style passive workspace memory, Slack/meeting/source memory.
      job_to_be_done: make Slack, meeting, standup, and product-operation context available without manual filing.
      expansion_pool: remote teams, product ops, support/community, CS/FDE, meeting-heavy B2B teams.
      confidence: moderate to high.
    - pattern: owned reactivation
      examples_or_evidence: archived Julep segments with 30 power users and 50 triers; existing exclusions.
      job_to_be_done: learn quickly from prior intent and product familiarity.
      expansion_pool: owned users only.
      confidence: high.
  private_context_policy: use private customer names for strategy and internal scoring only unless explicitly approved for outbound copy.

sender_voice:
  proposed_sender: Shubham Attri
  confidence: moderate
  source_context:
    - Memory Store preferences.
    - Gmail quick read, which showed direct, specific, operational writing.
  style:
    - short.
    - plain text.
    - specific workflow observation before the ask.
    - skeptical of generic AI automation.
    - technical founder/operator, not SDR.
  use:
    - "what from the past is still binding"
    - "the context your agent needs before it starts"
    - "record in Claude, recall in Codex"
  avoid:
    - "genuinely"
    - generic praise.
    - inflated or unsupported claims.
    - one-size-fits-all AI memory language.

website_findings:
  pages_checked:
    - https://memory.store/
    - https://memory.store/guides
    - https://memory.store/manus
    - https://memory.store/blog
    - https://www.ycombinator.com/companies/memory-store
  claims_found:
    - Memory Store is "one memory for your team's agents".
    - It turns meetings, Claude sessions, Slack chats, and other work into shared context.
    - It works with Claude, ChatGPT, Cursor, Slack, Raycast, Linear, Granola, Fathom, and OpenCode.
    - It runs as an MCP inside agents already used today.
    - It supports hosted MCP setup at `https://memory.store/mcp`.
    - YC profile lists Memory Store as "Shared context for all of your team's agents."
  proof_assets:
    - homepage positioning.
    - setup guides.
    - Manus integration flow.
    - YC profile.
    - Ishita's public YC/Memory Store post from LinkedIn search result.
  risky_or_unsupported_claims:
    - do not claim automatic capture of every memory.
    - do not claim all integrations are production-ready for every customer.
    - do not claim metrics like time saved, close rates, or token savings without approved proof.

demo_cta:
  discovered_link_candidates:
    - homepage: "Sign up"
    - homepage: "Talk to founders"
    - Manus page: "Connect in Manus" and "Book a call"
  chosen_link: needs_user_confirmation
  confirmation_status: unconfirmed
  proposed_cta_style:
    - first touch: reply-first.
    - alternate: "Worth a 10-minute teardown of where your agents lose context?"
  fallback_cta: "If this is a real problem, reply with the tool where context gets lost most often."

funnel_system:
  current_stage: setup_packet
  stage_map:
    market_definition: strong enough for proposal.
    customer_usage_map: strong internally; public customer proof needs approval.
    ICP_hypotheses: proposed.
    signal_discovery: blocked for production until Codex reload exposes advanced Exa/Websets tools.
    account_sourcing: blocked for production.
    buyer_discovery: blocked for production.
    evidence_cards: blocked for production.
    copy_hypothesis: blocked until shadow sample and approval.
    review_approval: active next step.
    send_followup: blocked until approval.
    reply_classification: blocked until Gmail routine approved.
    learning_record: proposed only; record after approval and outcomes.

icp_matrix:
  - cell_name: GTM Context Operators
    buyer_persona: founder-led GTM owner, GTM engineer, sales engineer, outbound agency operator, technical growth lead.
    company_size: 5-200 employees to start.
    trigger_signals:
      - hiring or posting about GTM engineering, AI SDRs, outbound automation, RevOps automation, or signal-based outbound.
      - public usage of Clay/Apollo/Smartlead/Instantly-style workflows.
      - founder posts about ICP refinement, reply learning, outbound quality, or customer/account briefs.
    customer_story_or_pattern: Minicor/Ishita/Diro/Siftly/Pandatron GTM/account-context usage.
    proof_path: campaign setup packet plus signal-card quality gate plus Memory Store learning loop.
    target_count: 20 accounts for shadow-backed first batch.
    confidence: high.
    exclusions:
      - pure lead-gen agencies with no AI/tooling sophistication signal.
      - teams asking only for bulk email volume.
      - current customers unless approved for expansion.
  - cell_name: Customer Delivery Memory Teams
    buyer_persona: CS lead, FDE lead, onboarding lead, implementation lead, customer ops founder.
    company_size: 10-500 employees.
    trigger_signals:
      - hiring solutions/FDE/onboarding/customer success.
      - public case studies or implementation-heavy workflows.
      - docs/changelog/customer rollout evidence.
    customer_story_or_pattern: Siftly onboarding wiki and Briefs/customer-living-doc usage.
    proof_path: account/customer brief or living playbook.
    target_count: 15 accounts.
    confidence: high internally, moderate externally until public proof is sourced.
  - cell_name: Coding Agent Continuity Teams
    buyer_persona: technical founder, engineering lead, AI platform lead, devtools/community lead, MCP/plugin builder.
    company_size: 2-200 employees.
    trigger_signals:
      - public agent tooling, MCP servers, AI coding products, Cursor/Claude/Codex workflows.
      - GitHub activity around AI agents or developer productivity.
      - docs/changelog velocity and repeated support/doc context.
    customer_story_or_pattern: Shubham/Rishabh/Zyng project continuity usage.
    proof_path: record in one agent, recall in another; project continuity demo.
    target_count: 20 accounts.
    confidence: high.
  - cell_name: Passive Workspace Memory
    buyer_persona: product ops lead, founder/operator, chief of staff, support/community lead.
    company_size: 10-300 employees.
    trigger_signals:
      - meeting-heavy remote teams.
      - visible use of Slack, Fathom, Fireflies, Granola, Linear, Notion, or customer communities.
      - public posts about coordination, standups, customer context, or AI agents.
    customer_story_or_pattern: Shashank/Ukumi/Diwo-style passive workspace memory.
    proof_path: living status/context readout from meetings and Slack.
    target_count: 10 accounts.
    confidence: moderate.
    unconventional: true.
  - cell_name: Owned Reactivation
    buyer_persona: prior Julep/Memory Store power users and triers.
    company_size: existing owned list.
    trigger_signals:
      - archived power user/trier segment.
      - previous revenue, usage, signup, or known interaction.
    customer_story_or_pattern: prior Julep and Memory Store usage.
    proof_path: prior usage plus new Memory Store offer.
    target_count: 10 contacts after suppression review.
    confidence: high.

signal_sources:
  memory_store:
    use: approved customer/user patterns, objections, exclusions, prior plans.
  exa_websets:
    use: production account pools, criteria verification, enrichment, persistent lists.
    status: configured pending Codex reload.
  exa_search:
    use: public website and proof research now; production company/person/news research after advanced tool appears.
  github_docs_changelog:
    use: coding-agent and devtools timing evidence.
  linkedin:
    use: profile discovery and public posts; touches require approval.
  reddit_hn:
    use: pain-language research for agent amnesia/context loss.
  product_hunt_yc_events:
    use: launch-timing and founder-led startup discovery.
  gmail:
    use: warm paths, suppressions, replies, sender voice; no sends until approval.

gmail_learnings:
  search_scope:
    - sent Memory Store/GTM/agent-related messages.
    - customer/demo/onboarding messages.
  connector_result: Gmail search/read succeeded.
  useful_voice_signal:
    - direct requests.
    - specific workflow feedback.
    - short signoff.
  gaps:
    - no sufficient approved outbound corpus found in quick search.
    - suppressions and prior touches still need a targeted campaign-specific search after ICP approval.
  policy: do not draft, send, label, archive, or monitor Gmail until approved.

calendar_policy:
  default: use only after qualified replies.
  booking_link: needs_user_confirmation.
  meeting_duration: unknown.
  timezone: user environment is Asia/Kolkata; campaign prospect timezone should follow recipient/company if known.
  allowed_actions_before_approval: none.
  allowed_actions_after_approval:
    - read availability only if explicitly approved.
    - do not create or move events unless separately approved.

channel_policy:
  primary_channel: email
  secondary_channel: linkedin_profile_discovery_only
  linkedin_touch_policy: disabled_until_approved
  per_person_touch_limit:
    - initial email.
    - followup 1 after 3-4 business days.
    - followup 2 after 6-8 business days.
    - breakup after 12-15 business days.
  same_company_rule: max 2 active contacts per company only when personas differ.
  dedupe_policy: one primary active thread per company unless referral creates a new relevant lead.

send_ramp_policy:
  status: proposed
  day_1: max 10 sends
  days_2_3: max 20 sends per day
  day_4_onward: max 50 sends per day until changed
  cap_policy: ceiling, not quota.
  pause_conditions:
    - bounce or deliverability risk.
    - unsubscribe or negative reply.
    - duplicate recent outreach.
    - active existing thread.
    - unapproved claim.
    - missing signal/source/person identity.
    - Gmail connector ambiguity.
    - Websets/advanced Exa unavailable in the active session for production sourcing.

autopilot_routines:
  - name: shadow_sample_builder
    status: proposed_blocked_until_codex_reload_and_websets_visible
    goal: create 5-10 reviewed account/person signal cards before production sends.
    cadence: one-time before launch.
    required_connectors:
      - Memory Store
      - Exa advanced search
      - Websets
      - Gmail for suppression check
    allowed_actions_after_approval:
      - source accounts.
      - enrich person identity.
      - write accounts.csv rows.
      - write signal cards.
    forbidden_actions:
      - drafts.
      - sends.
      - monitor creation.
  - name: daily_sourcing_digest
    status: proposed
    goal: summarize new qualified accounts, rejected accounts, evidence gaps, and questions.
    cadence: daily on weekdays after Websets exists.
    output: digest in chat or campaign artifact, not Gmail.
  - name: gmail_reply_scan
    status: proposed_requires_send_approval
    goal: classify replies, bounces, unsubscribe, objections, referrals, positive replies, and owner actions.
    cadence: every 2 hours after launch.
    forbidden_until_approved:
      - broad mailbox scan.
      - labels.
      - sends.
      - followups.
  - name: weekly_learning_summary
    status: proposed
    goal: summarize ICP, signal, copy, objection, proof-path, and suppression learning.
    cadence: weekly.
    memory_store_recording: only approved learnings and outcomes.
  - name: high_intent_monitor_review
    status: proposed_blocked_until_webset_ids
    goal: review monitor output for approved ICP cells.
    cadence: daily or weekly depending on monitor.

memory_distillation:
  proposed:
    - First Memory Store GTM campaign should be customer-usage-map first, not generic AI/devtools first.
    - Private customer/user patterns shape ICP cells; outbound copy should use only public or explicitly approved proof.
    - Production GTM requires visible advanced Exa and Websets tools; basic website research is not enough for send-ready sourcing.
    - Default first campaign should test GTM context, customer-delivery memory, coding-agent continuity, passive workspace memory, and owned reactivation.
    - Setup approval replaces per-batch approval only for actions explicitly named in allowed routines.
  approved: []
  active: []
  deprecated: []

approval_needed_before_start:
  - approve or edit this setup packet.
  - confirm active offer.
  - confirm sender.
  - confirm CTA/demo/founder-call link.
  - confirm first ICP cells for the shadow sample.
  - confirm private-customer-proof policy.
  - restart/reload Codex and verify advanced Exa and Websets tools are visible.
  - approve Gmail draft/send/reply-scan scope.
  - approve monitor creation policy after Websets exist.
  - approve host automation creation, if desired.
