# mem-plugins

Public Memory Store plugins for agent-native workflows.

The first plugin is `content-lead`. It turns Memory Store insights into engagement-driving LinkedIn drafts and learns per-author voice from edits, approvals, and post performance. Sources are abstracted behind Memory Store — the skill operates on memories, not on specific upstreams.

## Install In Codex

Ask Codex:

```text
Install Memory Store Plugins from julep-ai/mem-plugins.
```

Codex should run:

```bash
codex plugin marketplace add julep-ai/mem-plugins --ref main
```

Then restart Codex, open the plugin directory, select `Memory Store Plugins`, and install `Content Lead`.

Update later with:

```bash
codex plugin marketplace upgrade mem-plugins
```

Do not say Content Lead is fully installed until the marketplace is added, `Content Lead` is installed, and Memory Store MCP auth is complete.

## Install In Claude Code

Ask Claude Code:

```text
Install the Content Lead plugin from the julep-ai/mem-plugins marketplace.
```

Claude Code should run:

```bash
claude plugin marketplace add julep-ai/mem-plugins@main
claude plugin install content-lead@mem-plugins
```

Then run `/reload-plugins` or restart Claude Code. Use `/mcp` if Claude asks you to authenticate the Memory Store MCP server.

Update later with:

```bash
claude plugin marketplace update mem-plugins
claude plugin update content-lead@mem-plugins
```

For local testing from a cloned checkout:

```bash
claude --plugin-dir ./plugins/content-lead
```

## Required MCP

`content-lead` requires Memory Store MCP for normal use. The plugin declares:

```text
https://memory.store/mcp
```

The MCP server provides the required `checkin`, `recall`, `record`, and `report-issue` operations. Tool names may be namespaced by the host, but those operations must be available.

Without Memory Store MCP, the agent can only draft from pasted context. It cannot recall brand memory, find company stories, or record feedback for the next run.

## Supported Targets

Codex and Claude Code have marketplace metadata in this repo.

Claude Cowork and OpenCode can use `plugins/content-lead/skills/linkedin-studio/SKILL.md` as the canonical workflow when Memory Store MCP is configured in that host. Do not call those installs verified until they are tested in those hosts.

## Current Plugin

`plugins/content-lead` includes one skill:

- `linkedin-studio`: starts with Memory Store `checkin`, recalls per-author voice and source material, drafts 2–3 grounded LinkedIn posts optimized for Depth Score (saves, dwell, meaningful comments), and records structured feedback — approvals, edits, rejections, published text, and 24h/7d performance — against a content-lineage schema so voice improves per author over time. Craft rules, format templates, annotated examples, recall cues, record schemas, and failure modes live in `references/` under the skill.

Product loop:

```text
checkin -> recall -> draft -> feedback -> record -> better recall
```

Try:

```text
Draft today's LinkedIn posts from Memory Store.
```

## Build Another Plugin

Use one marketplace for this repo. Do not create a new marketplace per plugin.

For a new Codex plugin, ask Codex to use `$plugin-creator`:

```text
Use $plugin-creator to create a repo-local plugin named <plugin-name> with skills and a marketplace entry.
```

The plugin should live at:

```text
plugins/<plugin-name>/
```

Required structure:

```text
plugins/<plugin-name>/
  .codex-plugin/plugin.json
  skills/
```

If the plugin needs Memory Store, add:

```text
plugins/<plugin-name>/.mcp.json
```

Then add one entry to:

```text
.agents/plugins/marketplace.json
```

Use Plugin Eval before committing plugin changes:

```text
Use $plugin-eval to evaluate plugins/<plugin-name>.
```
