---
name: marketplace-operator
description: Use when maintaining the Memory Store plugin marketplace, scouting new Memory Store-backed plugin opportunities, checking whether plugins or skills need updates, planning marketplace releases, or designing recurring upgrade routines. Requires Memory Store MCP.
---

# Marketplace Operator

Operate the Memory Store plugin marketplace as one branded marketplace with multiple Memory Store-built plugins inside it.

This skill is for marketplace maintenance and expansion. It is not a customer-facing GTM campaign skill and it is not a separate marketplace. Use it to decide what Memory Store-backed plugins should exist, whether existing skills need upgrades, and what recurring checks should run.

## Product Boundary

- The marketplace is **Memory Store**.
- The source repo is `julep-ai/mem-plugins`.
- `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` are host adapters for the same marketplace, not separate marketplace products.
- The repo may contain many installable plugins under `plugins/<plugin-name>/`.
- Each plugin should be authored and presented as built by Memory Store unless the user explicitly asks for another publisher.
- Do not create one marketplace per plugin.
- Do not describe plugins under a local workspace or agency identity in public marketplace metadata.
- Use separate plugins only when install, auth, positioning, or user mental model differs. Use separate skills inside an existing plugin when the workflow shares the same product surface.

## Operating Loop

1. **Checkin.** Call Memory Store `checkin` with the repo, current user request, and marketplace maintenance goal. Capture `thread_id`.

2. **Recall marketplace context.** Recall prior plugin architecture decisions, existing Memory Store plugin ideas, user feedback, product constraints, similar companies/products, and known install/update issues.

3. **Inspect current marketplace state.** Read:
   - `README.md`
   - `AGENTS.md`
   - `.agents/plugins/marketplace.json`
   - `.claude-plugin/marketplace.json`
   - `plugins/*/.codex-plugin/plugin.json`
   - `plugins/*/.claude-plugin/plugin.json`
   - `plugins/*/skills/*/SKILL.md`

4. **Scout opportunities.** Look for workflow categories where Memory Store makes the plugin better than a generic agent: company memory, customer context, private preferences, prior outcomes, feedback loops, or team-specific operating history.

5. **Classify the opportunity.** Decide whether the work is:
   - a new plugin under `plugins/<plugin-name>/`
   - a new skill under an existing plugin
   - a reference/update to an existing skill
   - an MCP/app connector requirement
   - an automation/routine
   - not worth building yet

6. **Run the upgrade audit.** Use [references/upgrade-loop.md](references/upgrade-loop.md). Check stale APIs, outdated positioning, missing metadata, version drift, weak install docs, token-heavy skill loads, broken MCP assumptions, and plugin-eval warnings.

7. **Recommend or edit.** If the needed change is clear and low risk, update the repo. If the change depends on product direction, output a decision memo with exact options.

8. **Record.** Record confirmed architecture decisions, shipped plugin changes, rejected ideas, and upgrade outcomes back to Memory Store with the active `thread_id`.

## Output Contract

Return in this order:

1. **marketplace read** - one paragraph describing the current marketplace shape and the main issue.
2. **plugin inventory** - each plugin, category, author/publisher, required MCPs/connectors, and active skills.
3. **opportunity map** - candidate plugins or skills with target user, workflow, memory advantage, dependencies, and build priority.
4. **upgrade findings** - stale docs, manifest drift, missing version bumps, weak categories, broken auth assumptions, or skill quality issues.
5. **recommended changes** - concrete file-level changes, separated into safe edits and product decisions.
6. **routine candidates** - recurring marketplace checks worth running in Codex automation.
7. **memory record** - what should be recorded once the user confirms.

## Invariants

- Keep one marketplace root for the repo.
- Keep marketplace identity as Memory Store.
- Do not call the marketplace by a local workspace or agency identity in public metadata.
- Do not invent external company facts. Use web sources or mark as hypothesis.
- Do not claim an update shipped unless files changed or the marketplace was actually updated.
- Do not claim Memory Store learned unless `record` ran.
- Prefer concrete install and update commands over prose.
- Run plugin validation before saying the marketplace is ready.

## Reference Files

- [references/upgrade-loop.md](references/upgrade-loop.md) - recurring marketplace audit and upgrade routine.
