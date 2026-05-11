# Campaign Engineering System

Use this reference when deciding what kind of GTM campaign is being built and what system the agent should engineer before sourcing or sending.

## Principle

GTM Agent should not behave like a form filler. The user may upload docs, paste notes, connect Memory Store, sync workspace context, or point to a prior campaign. The agent's job is to infer the campaign system from that context, identify gaps, and ask only for the missing decisions that block execution.

AI is good at filling structured systems. The skill should provide the system; the agent fills it from evidence.

## Campaign Mode

Classify the run first:

- `plan_new_campaign` - co-design the campaign plan with the user before creating folders, sourcing, drafting, or automations.
- `start_new_campaign` - create or activate a new approved campaign; begin sourcing, signal cards, representative copy, and routines.
- `monitor_campaign` - inspect active campaign health, Websets/monitor changes, Gmail replies/followups, bounces, suppressions, and stop conditions.
- `campaign_insights` - summarize performance and extract learnings by ICP, signal, copy angle, channel, persona, and objection.
- `update_prior_campaign` - change an existing campaign based on new results, customer stories, exclusions, ICP shifts, copy learnings, or channel results.
- `new_campaign` - first campaign for this product, offer, sender, or market.
- `build_on_previous` - previous campaign exists; reuse learnings, exclusions, replies, objections, copy, and Websets.
- `refresh_existing` - same campaign, but ICP, signals, offer, proof, or copy need updates.
- `expand_winner` - scale a proven ICP/signal/copy combination.
- `rescue_underperformer` - diagnose weak replies, bad signals, poor ICP, or deliverability risk.
- `reactivation` - restart dormant prospects, old replies, prior demos, or aged opportunities.
- `event_or_launch` - time-bound campaign around launch, funding, conference, changelog, product release, or news.

If unclear, infer the top two modes and ask the user to confirm only when the mode changes policy, risk, or required evidence.

Planning mode is encouraged. If the user is creating or materially changing a campaign, first return a compact plan for approval: campaign name, active offer, sender, target scale, ICP cells, high-intent signal sources, email/LinkedIn channel policy, proof paths, success criteria, suppressions, send ramp, monitor specs, learning loop, and the exact connector gates. Do not skip this plan and jump straight into shallow website research.

## Context Ingestion

Ingest context in this order:

1. Memory Store `list-briefs`: select at most 1-3 relevant canonical briefs, such as GTM operating policy, ICP/persona map, proof/claims, campaign learning, customer/account brief, or current priorities.
2. Memory Store recall: retrieve evidence behind those briefs plus product, ICPs, customers, objections, approved claims, prior campaigns, exclusions, user preferences, and current facts.
3. Uploaded or pasted docs: decks, notes, CSVs, account lists, positioning docs, sales scripts, call notes, prior campaign exports.
4. Website and public proof: homepage, product, docs, pricing, customers, blog, changelog, demo/contact path.
5. Gmail: prior touches, warm paths, sender voice, objections, replies, suppressions, active threads.
6. Calendar: booking context after qualified replies, not the first CTA source.
7. Exa/Websets/Monitors: public-market discovery, structured sourcing, enrichment, recurring signal streams.

For each source, track:

```text
source:
what_it_tells_us:
briefs_used:
recall_needed_for_detail:
confidence:
usable_in_copy:
needs_confirmation:
should_record_to_memory_store:
should_update_brief:
```

Do not claim uploaded/pasted context has been learned until it is recorded through Memory Store after approval.

## Sparse Briefs

Briefs are canonical operating maps, not a second campaign folder. Use them to orient the run, then use recall for supporting evidence.

Create or update a brief only when the new information is reusable, approved or evidence-backed, and changes how future agents should operate. Otherwise, record it as memory and let recall retrieve it later.

For GTM, strong brief candidates are:

- **GTM operating brief** - campaign modes, approval gates, connector gates, send policy, routine policy.
- **ICP/persona brief** - current ICP cells, source customer patterns, excluded personas, unconventional bets.
- **Proof and claims brief** - approved public claims, private claims, proof paths, usable customer stories.
- **Campaign learning brief** - winning signals, dead signals, objections, copy lessons, next experiments.
- **Important account/customer brief** - only for accounts that matter beyond one row or one touch.

Avoid briefs for individual lead rows, raw search results, one-off replies, draft variants, unapproved brainstorms, and temporary campaign notes.

## Funnel System

Every campaign should map to funnel stages. Use this as the default system:

```text
market_definition
  -> ICP hypotheses
  -> customer-story/persona mining
  -> signal discovery
  -> account sourcing
  -> buyer/persona discovery
  -> evidence card
  -> channel plan (email + optional LinkedIn)
  -> copy hypothesis
  -> review / approval
  -> send / followup
  -> reply classification
  -> meeting / next action
  -> learning record
  -> next batch or routine
```

The agent should state which stage is being engineered and which stages are already strong, weak, unknown, or blocked.

## ICP Engineering

Do not start from a generic persona. Build ICP cells from:

- pain in customer language.
- buyer workflow ownership.
- company stage and operating environment.
- trigger signals.
- proof path available to the seller.
- exclusions and suppression rules.
- likelihood that the agent can find evidence automatically.

Each ICP cell needs:

```text
cell_name:
buyer/persona:
pain:
hard_criteria:
soft_criteria:
trigger_signals:
customer_story_or_pattern:
proof_path:
exclusions:
source_context:
confidence:
first_batch_size:
daily_target:
learning_intent:
```

High-intent sourcing is not a static persona list. Each ICP cell should define the signals that imply current need: hiring for agent/GTM/support roles, public launch/change, docs/changelog activity, community/support load, GitHub issue pattern, relevant LinkedIn post, new integration, competitor switch, customer-story match, warm path, or prior reply pattern. A generic title plus company category is not high intent.

For first-time campaigns, propose several ICP hypotheses and start small. For prior campaigns, reuse winners, suppress losers, and explicitly say what changed.

## Campaign System Output

Before large sourcing or copy, output this compact campaign-system read:

```text
campaign_mode:
context_sources:
brief_context:
funnel_stage_map:
ICP_system:
signal_system:
proof_system:
execution_system:
learning_system:
brief_delta:
open_decisions:
```

For `monitor_campaign`, include:

```text
campaign_health:
new_high_intent_signals:
reply/followup_status:
stop_conditions:
recommended_updates:
```

For `campaign_insights` or `update_prior_campaign`, include:

```text
winning_personas:
losing_personas:
winning_signals:
copy_hypotheses:
channel_results:
customer_stories_to_mine:
policy_changes:
next_experiments:
```

Keep it compact. The point is not a document; the point is to make the GTM machine explicit enough that background workers and automations can fill it.

## Learning Back Into Memory Store

Record only approved or confirmed learnings:

- campaign mode and approved GTM plan.
- uploaded/pasted docs that the user approves as source context.
- ICP cells kept, killed, or changed.
- signal types accepted or rejected.
- proof paths approved or unsafe.
- copy angles approved, sent, or rejected.
- replies, objections, meetings, suppressions, and performance.

This is how the next run knows whether it is a new campaign, a continuation, an expansion, or a rescue.

If a confirmed learning changes a canonical brief, return a compact `brief_delta` with target brief, changed section, evidence IDs, and whether the user must approve the update. Do not create a new brief when updating an existing canonical brief would preserve authority.
