# mem-plugins

This repo is agent-native. Treat README instructions as executable installation guidance, not just prose.

## Start here

1. For user installation, run `codex plugin marketplace add julep-ai/mem-plugins --ref main`.
2. For local development from a cloned checkout, run `codex plugin marketplace add "$(pwd)"`.
3. To update an existing install, run `codex plugin marketplace upgrade mem-plugins`.
4. After installation, tell the user to restart Codex, install `Content Lead` from the plugin directory, and complete Memory Store MCP auth when prompted.

Do not use a custom installer script for normal installs. Codex marketplace commands keep the source trackable and updateable.

For private repo installs, GitHub access is not enough by itself. Git must have non-interactive credentials available, such as `gh auth login`, an authorized PAT, or SSH.

## Product contract

`content-lead` requires Memory Store MCP for normal use. Without Memory Store MCP, the plugin can draft from pasted context, but it cannot recall company memory or record feedback.

Do not claim the system learned from a draft unless feedback was recorded through Memory Store.

## Supported targets

Codex is the supported install target in this repo today.

Claude Code, Claude cowork, and opencode should use the skill instructions as the canonical workflow until their adapters are tested and documented.

## Adding plugins

Use `$plugin-creator` for new Codex plugins when available. Add new plugins under `plugins/<plugin-name>/` and add one entry to `.agents/plugins/marketplace.json`.

Keep a single marketplace for the repo. Do not create one marketplace per plugin.

## Editing

Keep install instructions concrete. Prefer runnable commands over descriptions.

Before changing plugin files, run:

```bash
node /Users/a3fckx/.codex/plugins/cache/openai-curated/plugin-eval/f09cfd210e21e96a0031f4d247be5f2e416d23b1/scripts/plugin-eval.js analyze plugins/content-lead --format markdown
```
