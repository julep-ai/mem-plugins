# Memory Store Plugin Install And Reproduction Guide

This guide is for two audiences:

- people who want to install Memory Store plugins and start using company memory
  inside their agent host.
- builders who want to reproduce the Memory Store plugin pattern for a new use
  case.

The product model is one marketplace with many Memory Store-backed plugins:

```text
Memory Store marketplace
  memory-store       # core install, Memory Store MCP auth, basics loop
  gtm-agent          # GTM engineering and outbound workflows
  future plugins     # customer docs, support memory, meeting prep, PLG, etc.
```

Install Memory Store once. Then install use-case plugins that reuse the same
Memory Store context layer.

The marketplace source is `MemoryStore/plugins`. To distribute it outside the
team, make that repository public or ensure each installer has GitHub access and
a `GITHUB_TOKEN` or `GH_TOKEN` for non-interactive background updates.

## What Good Looks Like

A good Memory Store plugin should make one workflow work better because the
agent has durable context:

```text
checkin -> recall relevant memory and briefs -> act -> record confirmed learning
```

The plugin should not be just a prompt bundle. It should encode a repeatable job:

```text
workflow
  + Memory Store context
  + external connectors where needed
  + strict approval boundaries
  + records back to Memory Store
  + reusable brief updates only when operating truth changes
```

GTM Agent is the first flagship example of this pattern. It uses Memory Store as
the seller's operating memory, Websets/Exa for sourcing, Gmail or another rail
for approved execution, and Hermes or host automation for recurring routines.

## Install Flow For Users

### Claude Code

```bash
claude plugin marketplace add MemoryStore/plugins@main
claude plugin marketplace update mem-plugins
claude plugin install memory-store@mem-plugins
claude plugin install gtm-agent@mem-plugins
```

Then restart Claude Code or run:

```text
/reload-plugins
```

Authenticate Memory Store MCP when prompted:

```text
/mcp
```

Verify:

```bash
claude plugin marketplace list
claude plugin list
```

If Claude says a plugin is not installed, use `install`, not `update`:

```bash
claude plugin install gtm-agent@mem-plugins
```

### Codex

Add the marketplace:

```bash
codex plugin marketplace add MemoryStore/plugins
```

Then restart or reload Codex and use the plugin UI to install or enable:

```text
Memory Store
GTM Agent
```

Current Codex CLI builds expose marketplace add/upgrade from the terminal, while
plugin install/enable is UI-driven. Prefer `codex plugin --help` when a newer
Codex build exposes additional commands.

Update the marketplace:

```bash
codex plugin marketplace upgrade mem-plugins
```

### Claude Cowork

Cowork install is UI-driven:

1. Open the plugin directory from the chat input menu.
2. Add the marketplace source: `MemoryStore/plugins`.
3. Install `Memory Store`.
4. Install `GTM Agent` or another use-case plugin.
5. Enable automatic sync if Cowork exposes it.
6. Connect Memory Store MCP in Cowork's connector/MCP settings.

### Other Hosts

For hosts without marketplace support, use the plugin skills directly as a
portable workflow reference until the host adapter exists:

```text
plugins/memory-store/skills/memory-store-basics/SKILL.md
plugins/gtm-agent/skills/gtm-agent/SKILL.md
```

The host still needs access to Memory Store MCP:

```text
https://memory.store/mcp
```

Required operations:

```text
checkin
recall
list-briefs
record
report-issue
```

## First Useful Moment

After installing `memory-store`, the agent should immediately prove that memory
works:

```text
1. Run checkin.
2. List/select relevant briefs.
3. Recall useful context for the current task.
4. Ask the user which workflow to run next.
```

Recommended first prompt:

```text
Use Memory Store. Check in, show me what context matters right now, and suggest
three useful workflows I can run from my company memory.
```

For GTM Agent:

```text
Start GTM Agent autopilot. Recall Memory Store context, research our website
and demo CTA, learn from Gmail if available, define daily/weekly routines, build
the GTM operating profile, and ask for approval before sending.
```

## Connector Readiness

Core Memory Store plugin:

```text
Memory Store MCP = required
```

GTM Agent:

```text
Memory Store MCP = required
Exa Search MCP = required for production research
Websets MCP = required for production sourcing and enrichment
Gmail = required for Gmail sending, followups, reply scans, and mailbox learning
Calendar = useful after qualified replies
Hermes or host automation = useful for recurring routines
Attio = useful visual CRM/funnel surface when available
Agent Mail or Resend = optional sending rails when wired and approved
```

Missing connectors should create a degraded mode, not fake execution:

```text
missing Memory Store -> pasted-context drafting only
missing Exa/Websets -> plan_only, no production sourcing or send-ready copy
missing Gmail/sending rail -> drafts/import-ready queues only
missing automation host -> manual routine specs
```

## Reproducing The Plugin Pattern

Use this sequence when building a new Memory Store-backed plugin.

### 1. Decide Plugin Or Skill

Create a new skill inside `plugins/memory-store` when the workflow is core
Memory Store usage:

```text
checkin/recall/record behavior
brief and living-doc workflows
marketplace maintenance
general memory onboarding
```

Create a separate plugin under `plugins/<plugin-name>/` when the workflow has a
distinct user job, install surface, connector set, or product identity:

```text
gtm-agent
customer-docs
support-memory
meeting-intelligence
engineering-memory
founder-os
plg-agent
```

### 2. Define The Workflow Contract

Every plugin should answer:

```text
who uses it?
what job does it perform?
what Memory Store context does it need?
what external tools/connectors does it need?
what can it do without approval?
what always requires approval?
what does it record back to Memory Store?
what would become a brief only after approval?
```

### 3. Add The Plugin Shape

Expected layout:

```text
plugins/<plugin-name>/
  .codex-plugin/plugin.json
  .claude-plugin/plugin.json
  .mcp.json                  # only if the plugin needs MCP servers
  .app.json                  # only if the host supports app connectors
  skills/
    <skill-name>/
      SKILL.md
      references/
      scripts/
      agents/
```

The `memory-store` plugin owns Memory Store MCP auth. New use-case plugins should
reuse that auth when the host permits it instead of creating duplicate Memory
Store prompts.

### 4. Add Marketplace Metadata

Update both marketplace adapters:

```text
.agents/plugins/marketplace.json
.claude-plugin/marketplace.json
```

Each public plugin entry should describe the publisher as Memory Store and make
install/auth requirements explicit.

Do not create one marketplace per plugin. This repo is one marketplace:

```text
mem-plugins -> displayed as Memory Store
```

### 5. Write The Skill As An Operating Loop

A good skill has this shape:

```text
role identity
when to use
required memory loop
workflow steps
approval gates
connector gates
failure modes
output contract
what to record
what not to do
references/scripts
```

For Memory Store-backed plugins, start with:

```text
checkin -> list/select 0-3 briefs -> recall evidence -> act -> record confirmed learning
```

### 6. Provide A First-Run Prompt

Every plugin should include a copy-pasteable first-run prompt:

```text
Use <plugin>. Check Memory Store context, infer what you can, ask only blockers,
produce the first operating profile, and do not take external action until I
approve the plan.
```

For GTM Agent:

```text
Use GTM Agent to build a campaign for <seller>. Start with Memory Store checkin,
select relevant briefs, recall product and customer context, create the GTM
operating profile, define connector status, and ask for approval before sourcing
or sending.
```

### 7. Validate Before Publishing

Minimum checks:

```bash
python3 plugins/gtm-agent/skills/campaign-setup/scripts/test_render_gtm_plan_template.py
python3 plugins/gtm-agent/scripts/validate_skill_surface.py
git diff --check
```

If plugin-eval is available, run it before release:

```text
Use plugin-eval to evaluate plugins/<plugin-name>.
```

## Builder Invitation

The marketplace should invite builders to create Memory Store-backed workflows:

```text
Build plugins that remember.
```

Useful plugin opportunities:

```text
customer-docs        -> turn account context into customer briefs and PDFs
support-memory       -> recall support history and community context
meeting-intelligence -> prepare and follow up from meetings
engineering-memory   -> repo, PR, standup, and incident continuity
plg-agent            -> turn product events into activation and sales signals
founder-os           -> founder/operator context, tasks, followups, decisions
research-memory      -> durable research threads and evidence briefs
```

Each should be packaged as:

```text
installable plugin
first-run prompt
connector list
example output
approval policy
record/brief policy
host compatibility notes
```

## GTM Agent As Flagship Proof

GTM Agent is currently the best proof of the system because it uses the full
Memory Store loop:

```text
Memory Store context
  -> campaign profile
  -> Websets/Exa sourcing
  -> signal cards
  -> copy and send policy
  -> Gmail/Agent Mail/Resend execution rail
  -> Hermes routines
  -> reply/outcome learning
  -> Memory Store records and sparse brief deltas
```

For external distribution, GTM Agent needs:

```text
one clean install page
one demo campaign
one sample CSV/export
one short video or walkthrough
one first-run prompt
one clear "what it will not do without approval" section
one builder-facing explanation of how to copy the pattern
```

## Public Distribution Checklist

Before sharing a plugin publicly:

```text
README install commands are current
docs/INSTALLATION.md is current
plugin manifests are aligned across Codex and Claude
Memory Store auth path is clear
required connectors are named
first-run prompt exists
degraded modes are explicit
example output exists
validation passes
no secrets are committed
seller-specific campaign data is excluded or clearly marked as an example
```

## How To Explain The Product

Short version:

```text
Memory Store lets agents ship with company memory. Install it once, then add
use-case plugins like GTM Agent, customer briefs, meeting prep, support memory,
and engineering continuity.
```

Builder version:

```text
Memory Store is a memory layer for plugin ecosystems. Use it to build workflows
that recall company context, act with that context, and record what changed so
future agents get smarter.
```

GTM Agent version:

```text
GTM Agent is a Memory Store-backed GTM engineering plugin. It plans campaigns,
sources accounts, creates signal cards, drafts approved copy, runs bounded
background routines, and records campaign learning back to Memory Store.
```
