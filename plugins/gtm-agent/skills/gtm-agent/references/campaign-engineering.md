# Campaign Engineering System

Use this reference when deciding what kind of GTM campaign is being built and what system the agent should engineer before sourcing or sending.

## Principle

GTM Agent should not behave like a form filler. The user may upload docs, paste notes, connect Memory Store, sync workspace context, or point to a prior campaign. The agent's job is to infer the campaign system from that context, identify gaps, and ask only for the missing decisions that block execution.

AI is good at filling structured systems. The skill should provide the system; the agent fills it from evidence.

## Campaign Mode

Classify the run first:

- `new_campaign` - first campaign for this product, offer, sender, or market.
- `build_on_previous` - previous campaign exists; reuse learnings, exclusions, replies, objections, copy, and Websets.
- `refresh_existing` - same campaign, but ICP, signals, offer, proof, or copy need updates.
- `expand_winner` - scale a proven ICP/signal/copy combination.
- `rescue_underperformer` - diagnose weak replies, bad signals, poor ICP, or deliverability risk.
- `reactivation` - restart dormant prospects, old replies, prior demos, or aged opportunities.
- `event_or_launch` - time-bound campaign around launch, funding, conference, changelog, product release, or news.

If unclear, infer the top two modes and ask the user to confirm only when the mode changes policy, risk, or required evidence.

## Context Ingestion

Ingest context in this order:

1. Memory Store recall: product, ICPs, customers, objections, approved claims, prior campaigns, exclusions, user preferences.
2. Uploaded or pasted docs: decks, notes, CSVs, account lists, positioning docs, sales scripts, call notes, prior campaign exports.
3. Website and public proof: homepage, product, docs, pricing, customers, blog, changelog, demo/contact path.
4. Gmail: prior touches, warm paths, sender voice, objections, replies, suppressions, active threads.
5. Calendar: booking context after qualified replies, not the first CTA source.
6. Exa/Websets/Monitors: public-market discovery, structured sourcing, enrichment, recurring signal streams.

For each source, track:

```text
source:
what_it_tells_us:
confidence:
usable_in_copy:
needs_confirmation:
should_record_to_memory_store:
```

Do not claim uploaded/pasted context has been learned until it is recorded through Memory Store after approval.

## Funnel System

Every campaign should map to funnel stages. Use this as the default system:

```text
market_definition
  -> ICP hypotheses
  -> signal discovery
  -> account sourcing
  -> buyer/persona discovery
  -> evidence card
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
proof_path:
exclusions:
source_context:
confidence:
first_batch_size:
```

For first-time campaigns, propose several ICP hypotheses and start small. For prior campaigns, reuse winners, suppress losers, and explicitly say what changed.

## Campaign System Output

Before large sourcing or copy, output this compact campaign-system read:

```text
campaign_mode:
context_sources:
funnel_stage_map:
ICP_system:
signal_system:
proof_system:
execution_system:
learning_system:
open_decisions:
```

Keep it compact. The point is not a document; the point is to make the GTM machine explicit enough that background workers and automations can fill it.

## Learning Back Into Memory Store

Record only approved or confirmed learnings:

- campaign mode and approved setup packet.
- uploaded/pasted docs that the user approves as source context.
- ICP cells kept, killed, or changed.
- signal types accepted or rejected.
- proof paths approved or unsafe.
- copy angles approved, sent, or rejected.
- replies, objections, meetings, suppressions, and performance.

This is how the next run knows whether it is a new campaign, a continuation, an expansion, or a rescue.
