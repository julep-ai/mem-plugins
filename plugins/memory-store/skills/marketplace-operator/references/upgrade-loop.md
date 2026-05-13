# Marketplace Upgrade Loop

Use this reference when a user asks whether the Memory Store marketplace, plugins, or skills need to be updated.

## Upgrade Sources

Check these inputs:

- Memory Store recalls for prior marketplace decisions, plugin feedback, install issues, and rejected ideas
- Marketplace architecture/install/release-policy briefs (via `list-briefs`/`get-brief`)
- repo manifests and marketplace files
- skill descriptions and reference files
- plugin-eval reports
- connector/MCP availability assumptions
- current docs for external dependencies
- competitor and adjacent workflow products when the user asks for market scanning

## Upgrade Questions

Ask these questions every run:

- Does the marketplace still read as one Memory Store marketplace?
- Are all installable plugins shown as Memory Store-built products?
- Is any workflow incorrectly placed as a skill when it should be a plugin, or as a plugin when it should be a skill?
- Did any plugin gain a new skill without a version bump?
- Are install and update commands still concrete?
- Are required MCPs/connectors declared and described?
- Are placeholders clearly marked and safe?
- Are skill files too large for active context?
- Did external APIs, docs, or product capabilities change?
- Did user feedback or Memory Store outcomes reveal a better workflow?

## Routine Cadence

Use these routine levels:

- **weekly marketplace scout** - look for new Memory Store-backed workflow opportunities and competitor patterns.
- **weekly upgrade audit** - inspect repo metadata, manifests, docs, plugin-eval results, and version drift.
- **release-gate audit** - run before publishing or tagging a marketplace update.
- **incident audit** - run after a user reports install, MCP auth, or plugin invocation failure.

## Automation Prompt Shape

When setting up a Codex automation, use a prompt with this structure:

```text
Check the Memory Store plugin marketplace for update needs.

Start with Memory Store checkin and recall for prior marketplace decisions, plugin feedback, and known install/update issues.
Inspect the mem-plugins repo metadata, manifests, README, AGENTS.md, and skill files.
Identify whether any plugin, skill, MCP declaration, install instruction, version, or marketplace category needs an update.
If market scanning is requested, research adjacent agent/plugin/workflow products and map only concrete, sourced opportunities to Memory Store-backed plugins.
Return a concise report with file-level recommendations, upgrade priority, validation commands, and what should be recorded to Memory Store.
Do not send messages, publish releases, or push changes without explicit user approval.
```

## Report Format

Return:

1. **status** - current marketplace health.
2. **changed context** - new Memory Store or market signals since the last run.
3. **needed updates** - exact plugin/skill/docs/manifest updates.
4. **new opportunities** - candidate plugins or skills with confidence.
5. **risks** - auth, privacy, connector, scale, or token-budget risks.
6. **validation** - commands to run before release.
7. **record candidate** - concise prose to store in Memory Store after confirmation.

## Release Gate

Before saying an upgrade is ready:

- parse all JSON manifests
- run `plugin-eval` on changed plugins or skills when available
- run `git diff --check`
- search for stale plugin paths and old invocation names
- MCP tool name drift checked against actual available tools
- confirm version bumps for changed Claude plugins
- record confirmed marketplace decisions in Memory Store
- Use `propose-brief` for durable marketplace policy changes, `confirm-brief` only after approval.
