# Memory Store Marketplace Installation

This repo publishes one marketplace:

```text
mem-plugins -> displayed as Memory Store
```

The marketplace currently contains these installable plugins:

- `memory-store` - core Memory Store workflows, including LinkedIn Studio and Marketplace Operator.
- `gtm-agent` - Memory Store-powered GTM workflows, including Exa Company Research, Exa Lead Generation, Exa People Search, and Websets Sourcing.

Install the marketplace once. Then install the plugin you want from that marketplace.

## Claude Code

### First-Time Install

Add or refresh the marketplace:

```bash
claude plugin marketplace add julep-ai/mem-plugins@main
claude plugin marketplace update mem-plugins
```

Install the core Memory Store plugin:

```bash
claude plugin install memory-store@mem-plugins
```

Install GTM Agent:

```bash
claude plugin install gtm-agent@mem-plugins
```

Restart Claude Code or run `/reload-plugins`, then authenticate Memory Store MCP with `/mcp` if prompted.

### Verify Install

```bash
claude plugin marketplace list
claude plugin list
```

You should see:

```text
mem-plugins
memory-store@mem-plugins
gtm-agent@mem-plugins
```

### Update Existing Installs

Use `update` only for plugins that are already installed.

```bash
claude plugin marketplace update mem-plugins
claude plugin update memory-store@mem-plugins
claude plugin update gtm-agent@mem-plugins
```

If Claude says:

```text
Plugin "gtm-agent" is not installed
```

then run install, not update:

```bash
claude plugin install gtm-agent@mem-plugins
```

### Enable Or Disable

If the plugin is installed but disabled:

```bash
claude plugin enable gtm-agent@mem-plugins
```

To disable without uninstalling:

```bash
claude plugin disable gtm-agent@mem-plugins
```

## Codex

Current Codex CLI builds manage marketplaces from the terminal, but plugin install/enable is handled in the Codex plugin UI.

### First-Time Marketplace Add

```bash
codex plugin marketplace add julep-ai/mem-plugins --ref main
```

Then restart/reload Codex, open the plugin UI, choose the `Memory Store` marketplace, and install or enable:

- `Memory Store`
- `GTM Agent`

### Marketplace Refresh

```bash
codex plugin marketplace upgrade mem-plugins
```

Then restart/reload Codex. If a plugin is not enabled, enable it in the Codex plugin UI.

Do not run these commands on current Codex CLI builds:

```bash
codex plugin install gtm-agent@mem-plugins
codex plugin update gtm-agent@mem-plugins
codex plugin list
```

Those subcommands are not available in the current Codex CLI. Prefer `codex plugin --help` when in doubt.

## Required MCP And Connectors

`memory-store` requires Memory Store MCP:

```text
https://memory.store/mcp
```

Required Memory Store operations:

- `checkin`
- `recall`
- `record`
- `report-issue`

`gtm-agent` requires Memory Store MCP and can additionally use:

- Exa MCP with `web_search_advanced_exa` for company and people research.
- Exa MCP with `deep_search_exa` for lead generation.
- Websets MCP for persistent account and people sets.
- Exa Monitors API for recurring signal monitoring.
- Gmail connector for approved drafts, sends, and followups.

Do not commit Exa API keys. Configure Exa and Websets keys in the host MCP settings.

## Plugin Commands

After GTM Agent is installed, these skills are available:

```text
/gtm-agent:gtm-agent
/gtm-agent:exa-company-research
/gtm-agent:exa-lead-generation
/gtm-agent:exa-people-search
/gtm-agent:websets-sourcing
```

After Memory Store is installed, these skills are available:

```text
/memory-store:linkedin-studio
/memory-store:marketplace-operator
```

## Troubleshooting

### `Plugin "gtm-agent" is not installed`

Cause: you ran update before the plugin was installed.

Fix:

```bash
claude plugin marketplace update mem-plugins
claude plugin install gtm-agent@mem-plugins
```

### Marketplace refreshed but GTM Agent is missing

Check:

```bash
claude plugin marketplace list
claude plugin marketplace update mem-plugins
claude plugin install gtm-agent@mem-plugins
```

If using Codex, run:

```bash
codex plugin marketplace upgrade mem-plugins
```

Then use the Codex plugin UI.

### Memory Store tools are unavailable

Restart/reload the host and complete Memory Store MCP auth. The plugin can draft from pasted context without MCP, but it cannot recall or record durable context.

### Exa or Websets tools are unavailable

The GTM Agent should still produce query plans, Websets specs, monitor specs, and draft-ready output. To execute sourcing directly, configure Exa/Websets MCP with a valid Exa API key in the host.
