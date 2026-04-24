# mem-plugins

This repo is agent-native. Treat README instructions as executable installation guidance, not just prose.

## Start here

1. For Codex installation, run `node scripts/install-codex.mjs` from the repo root.
2. If the user only wants to preview the install, run `node scripts/install-codex.mjs --dry-run`.
3. After installation, tell the user to restart Codex and complete Memory Store MCP auth when prompted.

## Product contract

`content-lead` requires Memory Store MCP for normal use. Without Memory Store MCP, the plugin can draft from pasted context, but it cannot recall company memory or record feedback.

Do not claim the system learned from a draft unless feedback was recorded through Memory Store.

## Supported targets

Codex is the supported install target in this repo today.

Claude Code, Claude cowork, and opencode should use the skill instructions as the canonical workflow until their adapters are tested and documented.

## Editing

Keep install instructions concrete. Prefer runnable commands over descriptions.

Before changing plugin files, run:

```bash
node /Users/a3fckx/.codex/plugins/cache/openai-curated/plugin-eval/f09cfd210e21e96a0031f4d247be5f2e416d23b1/scripts/plugin-eval.js analyze plugins/content-lead --format markdown
```
