# Connector Setup

GTM Agent is a workflow bundle. It can declare some tools, but it cannot safely ship private API keys or automatically reuse every connector from another plugin in every host.

## Memory Store

Install and authenticate the core plugin once:

```bash
claude plugin install memory-store@mem-plugins
```

GTM Agent expects the Memory Store MCP tools from that core plugin:

- `checkin`
- `recall`
- `record`
- `report-issue`

GTM Agent does **not** redeclare Memory Store MCP in its own `.mcp.json`. That avoids a second Memory Store auth prompt when `memory-store` is already installed.

## Exa Search MCP

GTM Agent declares Exa Search MCP for general company, people, and web research:

```text
https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,web_fetch_exa,deep_search_exa
```

For Claude Code, add or override Exa with an API key when you need production limits or lead generation:

```bash
claude mcp add --transport http exa "https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,web_fetch_exa,deep_search_exa" --header "x-api-key: YOUR_EXA_API_KEY"
```

For Codex:

```bash
codex mcp add exa --url "https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,web_fetch_exa,deep_search_exa"
```

Codex supports bearer-token environment variables for remote MCP auth. If your Exa setup requires API-key auth, configure the key in host MCP settings rather than committing it to this repo.

## Websets MCP

Websets needs an Exa API key in the server URL, so the plugin cannot ship a ready-to-run Websets MCP config without leaking or hardcoding a secret.

For Claude Code:

```bash
claude mcp add --transport http websets "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
```

For Codex:

```bash
codex mcp add websets --url "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
```

After Websets is connected, GTM Agent can use `websets-sourcing` for persistent company/person sets, enrichments, imports, and async sourcing.

## Gmail

The Codex plugin declares the Gmail app connector through `plugins/gtm-agent/.app.json`. The user still has to authorize Gmail in the host because Gmail access is account-scoped.

Claude Code does not get Gmail merely because GTM Agent is installed. If Gmail is unavailable, GTM Agent should produce reviewed drafts, followup timing, and import-ready output instead of claiming it sent or threaded emails.

## Why Tools May Not Appear Immediately

- The marketplace was refreshed, but the plugin was not installed or enabled.
- The host needs a restart or plugin reload.
- Memory Store MCP is authenticated under `memory-store`, not `gtm-agent`.
- Exa is available without your API key only within public/free limits.
- Websets requires a real Exa API key in the MCP URL.
- Gmail requires a separate account authorization in the host.
