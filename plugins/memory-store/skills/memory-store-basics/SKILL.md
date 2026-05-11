---
name: memory-store-basics
description: Use when starting Memory Store-backed work, orienting an agent to company memory, using briefs or living docs, deciding whether to record a learning, or deciding whether a new brief is warranted. Requires Memory Store MCP.
---

# Memory Store Basics

Use Memory Store as the context substrate for agent-native work. The core loop is:

```text
checkin -> list/select briefs -> recall evidence -> act -> record confirmed learning -> update/propose brief changes only when operating truth changed
```

## Required MCP Operations

Memory Store MCP provides:

- `checkin` - start or resume the focused thread.
- `recall` - retrieve evidence, decisions, prior context, and source memories.
- `list-briefs` - see maintained synthesis documents available to the agent.
- `record` - store confirmed learnings, rules, decisions, corrections, and outcomes.
- `report-issue` - report broken Memory Store behavior when the user asks or the tool behaves unexpectedly.

Tool names may be namespaced by the host. Use the operation names, not exact host-specific names, in user-facing explanations.

Some hosts also expose lower-level brief tools. Treat them as edit controls over the brief layer, not as substitutes for `record`:

- `get_brief` - read one selected brief when its summary is not enough.
- `suggest_brief_change` - attach a proposed delta without claiming the brief changed.
- `teach_brief` - save an explicit correction on a brief and teach it back to memory.
- `save_brief` or `save_brief_section` - create or edit a canonical brief only after approval or when the user directly asked for the edit.
- `set_brief_pin`, `share_brief`, `archive_brief`, and related controls - use only when the user asks to change surfacing, sharing, or lifecycle.

If a low-level brief tool stages work behind receipts or sessions, verify the receipt/session status before saying the edit landed. If it fails, continue with `record`/`recall` when possible and report the issue when appropriate.

## Mental Model

Memory Store has three different layers. Do not collapse them:

```text
recorded memories = raw evidence, decisions, corrections, events, outcomes
recall = evidence retrieval over those memories
briefs = sparse maintained synthesis over important evidence
living docs/wiki = portable views of those briefs for humans and agents
```

Briefs are not a dumping ground. A brief is a current operating map that tells future agents what matters, what is approved, what is stale, and what evidence to recall next.

## Sparse Brief Policy

Create or update a brief only when the information is:

- reusable across future work.
- approved by the user or backed by strong evidence.
- important enough to change future agent behavior.
- more useful as maintained synthesis than as a raw memory.
- scoped so future agents know when to use it.

Do **not** create a brief for:

- every brainstorm, draft, source, reply, lead, account, or one-off note.
- raw logs, CSV rows, monitor events, search results, or execution traces.
- speculative ideas that have not been approved or validated.
- overlapping "v1/v2/v3" documents that compete for authority.
- details that `recall` can retrieve when needed.

Most facts should be recorded as memories. Only a small number should change a brief.

## Canonical Brief Shape

When drafting or proposing a brief, use this shape:

```text
title:
scope:
owner_or_surface:
status: active | stale | archived | superseded
last_refreshed:
source_memory_ids:
source_artifacts:
current_position:
approved_rules:
open_questions:
staleness_triggers:
what_to_recall_for_detail:
supersedes:
do_not_use_for:
```

Keep the brief compact. It should point to evidence instead of copying every detail.

## Operating Loop

1. **Checkin.** Call `checkin` at the start of Memory Store-backed work. Capture `thread_id`.
2. **List briefs.** Call `list-briefs` when briefs may shape the work. Do not load every brief by default.
3. **Select briefs.** Pick the 1-3 relevant canonical briefs by title, summary, scope, and task fit.
4. **Use briefs as maps.** Treat selected briefs as current synthesis, not as complete evidence.
5. **Recall evidence.** Use focused `recall` calls for supporting memories, exact decisions, source IDs, customer language, or current facts.
6. **Act.** Do the requested work using the selected brief(s) plus recalled evidence.
7. **Record confirmed learning.** Call `record` only for confirmed rules, decisions, corrections, outcomes, or reusable learnings. Pass the active `thread_id`.
8. **Propose brief updates sparingly.** If the new learning changes operating truth, propose the specific brief delta. If the host exposes brief-editing tools, prefer `suggest_brief_change` for unapproved deltas and use `save_brief`, `save_brief_section`, or `teach_brief` only after approval or direct instruction.
9. **Report issues.** If Memory Store tools return inconsistent or broken behavior and the user wants it reported, call `report-issue`.

## Brief Selection Heuristic

Prefer a brief when it is:

- explicitly named by the user.
- pinned or surfaced by `checkin`.
- about the product, campaign, customer, plugin, or workflow being worked on.
- a current operating policy, not a historical artifact.

Skip a brief when it is:

- stale and superseded.
- only loosely related by keyword.
- broader than the task and likely to flood context.
- contradicted by newer recalled evidence.

If a brief and recalled memory conflict, say so. Use the newer confirmed evidence for immediate work and propose a brief refresh.

## Good Brief Types

Useful canonical briefs include:

- product thesis or positioning.
- current priorities.
- user/team preferences.
- approved claims and proof paths.
- GTM operating policy.
- ICP/persona map.
- customer/account brief for important accounts.
- connector/autopilot policy.
- campaign learning summary.
- marketplace/plugin architecture decisions.

Avoid creating many tiny briefs. If a topic is not stable enough for one of these surfaces, record it and rely on recall.

## Output Contract

When explaining Memory Store-backed work, include:

1. **briefs used** - selected brief IDs/titles, or "none".
2. **evidence recalled** - concise memory IDs or source descriptions when available.
3. **decision/action** - what changed or what work was done.
4. **record policy** - what was recorded, or what should be recorded after approval.
5. **brief delta** - any proposed sparse brief update, or "no brief update needed".

## Invariants

- Always run `checkin` at the start of Memory Store-backed work.
- Use `recall` for evidence. Do not create briefs just to make details findable.
- Use briefs as sparse synthesis, not as raw storage.
- Do not claim Memory Store learned unless `record` ran.
- Do not claim a brief was updated unless a brief-editing tool actually changed it, or the user approved a pending brief delta.
- Do not expose private memory content in shareable docs or outbound copy unless approved.
