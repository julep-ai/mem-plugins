# mem-plugins

This repo is agent-native. Treat README instructions as executable installation guidance, not just prose.

## Start Here

1. Codex install: `codex plugin marketplace add julep-ai/mem-plugins --ref main`.
2. Claude Code install: `claude plugin marketplace add julep-ai/mem-plugins@main` then `claude plugin install content-lead@mem-plugins`.
3. Codex update: `codex plugin marketplace upgrade mem-plugins`.
4. Claude update: `claude plugin marketplace update mem-plugins` then `claude plugin update content-lead@mem-plugins`.
5. After install, tell the user to restart or reload plugins and complete Memory Store MCP auth.

Do not use a custom installer script for normal installs. Marketplace commands keep the source trackable and updateable.

## Product Contract

`content-lead` requires Memory Store MCP for normal use. Without Memory Store MCP, the plugin can draft from pasted context, but it cannot recall company memory or record feedback.

Required Memory Store operations are `checkin`, `recall`, `record`, and `report-issue`. Tool names may be namespaced by the host.

Do not claim the system learned from a draft unless feedback was recorded through Memory Store.

## Supported Targets

Codex and Claude Code have marketplace metadata in this repo today.

Claude Cowork and OpenCode should use `plugins/content-lead/skills/linkedin-studio/SKILL.md` as the canonical workflow until their adapters are tested and documented.

## Marketplace Metadata Contract

Every Codex plugin must have:

- `.codex-plugin/plugin.json`
- `skills/`
- an entry in `.agents/plugins/marketplace.json` with `policy.installation`, `policy.authentication`, and `category`
- `.mcp.json` when the plugin needs Memory Store or another MCP server

Every Claude Code plugin must have:

- `.claude-plugin/plugin.json`
- `skills/`
- an entry in `.claude-plugin/marketplace.json`
- `.mcp.json` when the plugin needs Memory Store or another MCP server

Keep a single marketplace for the repo. Do not create one marketplace per plugin.

## Editing

Use `$plugin-creator` for new Codex plugins when available. Add new plugins under `plugins/<plugin-name>/`.

Keep install instructions concrete. Prefer runnable marketplace commands over prose.

Use `$plugin-eval` before committing plugin changes:

```text
Use $plugin-eval to evaluate plugins/content-lead.
```
