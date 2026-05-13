# mem-plugins

This repo is agent-native. Treat README instructions as executable installation guidance, not just prose.

## Start Here

1. Codex install: `codex plugin marketplace add MemoryStore/plugins`, then install/enable `memory-store` or `gtm-agent` from the Codex plugin UI.
2. Claude Code first install: `claude plugin marketplace add MemoryStore/plugins@main`, `claude plugin marketplace update mem-plugins`, then `claude plugin install memory-store@mem-plugins` and/or `claude plugin install gtm-agent@mem-plugins`.
3. Codex update: `codex plugin marketplace upgrade mem-plugins`, then restart/reload Codex and install/enable the desired plugin from the Codex plugin UI if needed.
4. Claude update: `claude plugin marketplace update mem-plugins`, then run `claude plugin update <plugin-name>@mem-plugins` only if `claude plugin list` shows that plugin is already installed. If Claude says the plugin is not installed, use `claude plugin install <plugin-name>@mem-plugins`.
5. After install, tell the user to restart or reload plugins and complete Memory Store MCP auth.

Do not use a custom installer script for normal installs. Marketplace commands keep the source trackable and updateable. Keep `README.md` and `docs/INSTALLATION.md` in sync for human-facing installation guidance.

## Agent Install Checklist

Before giving install/update commands:

1. Identify the host: Claude Code, Codex, Cowork, Claude Desktop, or another MCP host.
2. For Claude Code, run or recommend `claude plugin marketplace list` and `claude plugin list` when diagnosing state.
3. For Claude Code, use `install` for absent plugins and `update` only for installed plugins.
4. For Codex, use only `codex plugin marketplace add` and `codex plugin marketplace upgrade` in CLI docs unless `codex plugin --help` shows more subcommands. Plugin install/enable is currently UI-driven.
5. After install/update, tell the user to restart/reload plugins and complete Memory Store MCP auth.
6. If the user is adding GTM Agent, mention that Exa/Websets/Gmail are optional for planning mode but required for production sourcing, sending, reply monitoring, and campaign learning. Memory Store MCP is required for normal use.

## Product Contract

`memory-store` requires Memory Store MCP for normal use. Without Memory Store MCP, the plugin can draft from pasted context, but it cannot recall company memory or record feedback.

This repo represents one marketplace: Memory Store. `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` are host adapters for that same marketplace, not two product marketplaces. The local checkout path is an implementation detail; public marketplace metadata should present plugins as built by Memory Store.

`memory-store` is the core installable Memory Store plugin surface. It includes marketplace maintenance workflows such as `marketplace-operator`. Add workflows as skills under an existing plugin only when they share that product surface. Create separate plugins under `plugins/<plugin-name>/` when the workflow should be installed, authorized, or presented as a distinct product, even if it still requires Memory Store MCP.

`gtm-agent` is a separate installable plugin that requires Memory Store MCP. It may also use Exa Search MCP, Websets MCP, Exa Monitors API, and Gmail connectors for sourcing, monitoring, outreach, and learning loops.

Required Memory Store operations are `checkin`, `recall`, `list-briefs`, `record`, and `report-issue`. Tool names may be namespaced by the host. If low-level brief tools are available, use them only for selected brief reads, pending brief deltas, explicit corrections, and approved canonical edits; they do not replace `record`.

Use briefs sparingly: briefs are canonical maintained synthesis, not raw storage. For Memory Store-backed plugin work, prefer `checkin -> list/select relevant briefs -> recall supporting evidence -> act -> record confirmed learning -> propose brief deltas only when operating truth changes`.

Do not claim the system learned from a draft unless feedback was recorded through Memory Store.

## Supported Targets

Codex and Claude Code have marketplace metadata in this repo today.

Claude Cowork and OpenCode should use the relevant `plugins/<plugin-name>/skills/<skill-name>/SKILL.md` workflow until their adapters are tested and documented.

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

Keep a single marketplace for the repo. Do not create one marketplace per plugin. Keep both host metadata files aligned because they describe the same Memory Store marketplace. New Memory Store-backed products should appear as plugins inside this marketplace, authored by Memory Store.

## Editing

Use `$plugin-creator` for new Codex plugins when available. Add new plugins under `plugins/<plugin-name>/`.

Keep install instructions concrete. Prefer runnable marketplace commands over prose.

Use `$plugin-eval` before committing plugin changes:

```text
Use $plugin-eval to evaluate plugins/memory-store.
```
