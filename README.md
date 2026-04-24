# mem-plugins

Public Memory Store plugin marketplace for agent-native workflows.

Add this marketplace once, then install the Memory Store plugins that are relevant for your agent. Today the marketplace exposes `content-lead`; future plugins should be added to the same marketplace instead of creating new marketplace repos.

`content-lead` turns Memory Store insights into engagement-driving LinkedIn drafts and learns per-author voice from edits, approvals, and post performance. Sources are abstracted behind Memory Store — the skill operates on memories, not on specific upstreams.

## Install In Codex

Ask Codex:

```text
Install Memory Store Plugins from julep-ai/mem-plugins.
```

Codex should run:

```bash
codex plugin marketplace add julep-ai/mem-plugins --ref main
```

Then restart Codex, open the plugin directory, select `Memory Store Plugins`, and install the plugins you want. Today that means installing `Content Lead`.

To get new plugins or newer plugin versions later, refresh the marketplace:

```bash
codex plugin marketplace upgrade mem-plugins
```

Then restart or reload Codex, open `Memory Store Plugins` again, and install or update any relevant plugins shown there.

Do not say a Memory Store plugin is fully installed until the marketplace is added or upgraded, the specific plugin is installed/enabled, and Memory Store MCP auth is complete.

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

To get new plugins or newer plugin versions later:

```bash
claude plugin marketplace update mem-plugins
claude plugin update content-lead@mem-plugins
```

If more plugins are added to this marketplace, install each relevant one with:

```bash
claude plugin install <plugin-name>@mem-plugins
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

## Available Plugins

### `content-lead`

Path: `plugins/content-lead`

Includes one skill:

- `linkedin-studio`: starts with Memory Store `checkin`, recalls per-author voice, brand context, and source material, drafts 2–3 grounded LinkedIn posts optimized for Depth Score (saves, dwell, meaningful comments), and records feedback — approvals, edits, rejections, published text, and 24h/7d performance — so future runs improve per author. Craft rules, format templates, examples, recall cues, voice/brand bootstrap, record templates, and failure modes live in `references/` under the skill.

**First-run experience.** If Memory Store has no explicit brand or voice profile for the company/author, the skill infers both from existing memories (recent posts, shipped work, customer conversations, founder threads, edit diffs) and asks the user for a one-shot confirmation. A short interview bootstrap only runs when inference cannot cover enough dimensions. For teams with even a few weeks of Memory Store history, first-run setup is usually a confirmation, not a questionnaire.

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
