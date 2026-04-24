# mem-plugins

Agent-native Memory Store plugins.

The first plugin is `content-lead`. It writes LinkedIn drafts from company memory: Slack threads, Granola notes, shipped work, customer conversations, prior posts, and editorial feedback.

This repo is private for now.

## Install for agents

If you are an LLM agent installing this repo for a user, prefer the Codex marketplace command:

```bash
codex plugin marketplace add "$(pwd)"
```

Use this when the repo is already cloned locally. It lets Codex track the repo marketplace instead of manually editing `~/.agents/plugins/marketplace.json`.

If the `codex plugin marketplace` command is unavailable, use the local installer:

```bash
node scripts/install-codex.mjs
```

For a preview:

```bash
node scripts/install-codex.mjs --dry-run
```

Then tell the user:

```text
Restart Codex and complete Memory Store MCP auth when prompted.
```

Do not say Content Lead is fully installed until the plugin is registered and Memory Store MCP is available.

## Install for humans

### Option 1: Add this marketplace with Codex

Use this when you have access to `julep-ai/mem-plugins` from your GitHub account:

```bash
codex plugin marketplace add julep-ai/mem-plugins --ref main
```

Then restart Codex, open the plugin directory, select `Memory Store Plugins`, and install `Content Lead`.

### Option 2: Clone the repo and add the local marketplace

Use this while the repo is private or while you are editing the plugin:

```bash
git clone https://github.com/julep-ai/mem-plugins.git
cd mem-plugins
codex plugin marketplace add "$(pwd)"
```

Then restart Codex, open the plugin directory, select `Memory Store Plugins`, and install `Content Lead`.

### Option 3: Local installer

Use this when you want the repo to wire the personal marketplace file directly:

```bash
node scripts/install-codex.mjs
```

Restart Codex after the installer finishes.

### Manual Codex install

If you do not want to use the marketplace command or installer, symlink the plugin:

```bash
mkdir -p ~/.codex/plugins ~/.agents/plugins
ln -sfn "$(pwd)/plugins/content-lead" ~/.codex/plugins/content-lead
```

Create or update `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "local",
  "interface": {
    "displayName": "Local Plugins"
  },
  "plugins": [
    {
      "name": "content-lead",
      "source": {
        "source": "local",
        "path": "./.codex/plugins/content-lead"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

Restart Codex after changing the marketplace file.

## Required MCP

`content-lead` requires Memory Store MCP for normal use. The plugin declares:

```text
https://memory.store/mcp
```

Without Memory Store MCP, the agent can only draft from pasted context. It cannot recall brand memory, find company stories, or record feedback for the next run.

The user installing the plugin must have access to Memory Store MCP and must complete the host's MCP auth flow when prompted.

## Supported targets

Codex is supported today.

Claude Code, Claude cowork, and opencode can use the skill as workflow source material, but their install adapters are not documented here yet.

## Build another plugin

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

Use this shape:

```json
{
  "name": "<plugin-name>",
  "source": {
    "source": "local",
    "path": "./plugins/<plugin-name>"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Run Plugin Eval before committing plugin changes:

```bash
node /Users/a3fckx/.codex/plugins/cache/openai-curated/plugin-eval/f09cfd210e21e96a0031f4d247be5f2e416d23b1/scripts/plugin-eval.js analyze plugins/<plugin-name> --format markdown
```

## Current plugin

`plugins/content-lead` is a Codex plugin with one skill:

- `daily-linkedin-content-lead`: starts with Memory Store `checkin`, recalls brand voice and recent source material, drafts LinkedIn posts, and records feedback when the user approves, rejects, edits, or posts a draft.

## Product loop

```text
checkin -> recall -> draft -> feedback -> record -> better recall
```

The important part is the last step. Content Lead should get better because Memory Store remembers the edits, final posts, and rejected angles.

## Use

Try:

```text
Draft today's LinkedIn posts from Memory Store.
```

The agent should start with `checkin`, recall brand and story context, draft sourced posts, and ask what feedback to record.

## Local evaluation

Use Plugin Eval against the skill:

```bash
node /Users/a3fckx/.codex/plugins/cache/openai-curated/plugin-eval/f09cfd210e21e96a0031f4d247be5f2e416d23b1/scripts/plugin-eval.js analyze plugins/content-lead/skills/daily-linkedin-content-lead --format markdown
```

Use the improvement workflow when the report shows what to fix first:

```bash
node /Users/a3fckx/.codex/plugins/cache/openai-curated/plugin-eval/f09cfd210e21e96a0031f4d247be5f2e416d23b1/scripts/plugin-eval.js analyze plugins/content-lead/skills/daily-linkedin-content-lead --brief-out .plugin-eval/content-lead-brief.json
```
