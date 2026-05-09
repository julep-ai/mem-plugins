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

## Get an Exa API key

Both Exa Search MCP and Websets MCP use the same key.

```text
https://dashboard.exa.ai/api-keys
```

The free plan works without a key only for shallow exploratory search; it is not enough for a real GTM campaign. It lacks Websets access and should not be used for production ICP discovery, sourcing, enrichment, send-ready rows, or always-on monitoring. For any real campaign, create a key and configure it in both Exa Search and Websets server entries before expecting execution-grade sourcing.

## Exa Search MCP

GTM Agent declares Exa Search MCP for company, people, and web research. The plugin's bundled `.mcp.json` ships with `YOUR_EXA_API_KEY` placeholders in headers; replace them in host MCP settings.

Server URL:

```text
https://mcp.exa.ai/mcp
```

Active tools:

- `web_search_exa` (default on) - clean web search results.
- `web_fetch_exa` (default on) - full webpage content as markdown.
- `web_search_advanced_exa` (optional) - category, domain, date range, highlights, summaries, subpage crawling.

Deprecated but still callable for backwards compat:
`company_research_exa`, `people_search_exa`, `crawling_exa`, `linkedin_search_exa`, `get_code_context_exa`, `deep_search_exa`. GTM Agent skills should prefer `web_search_advanced_exa` and treat deprecated tools as host/backward-compatibility fallbacks only.

Manual host configuration (if not relying on the plugin's `.mcp.json`):

```bash
# Claude Code
claude mcp add --transport http exa https://mcp.exa.ai/mcp --header "x-api-key: YOUR_EXA_API_KEY"

# Codex
codex mcp add exa --url https://mcp.exa.ai/mcp
```

Current Codex CLI builds support `--url` and `--bearer-token-env-var`, not arbitrary `x-api-key` headers. If you need Exa Search production limits in Codex, configure the `x-api-key` header in the host MCP settings or config file; otherwise the URL above runs on Exa's free plan and GTM Agent must keep the campaign in planning mode.

Free-plan usage (no key, rate-limited):

```bash
claude mcp add --transport http exa https://mcp.exa.ai/mcp
codex mcp add exa --url https://mcp.exa.ai/mcp
```

Use free-plan Exa only to inspect public pages and prepare the setup packet. If the user asks to run a campaign, create ICP depth, build lead lists, generate account evidence cards, or draft outbound, stop and ask them to configure the Exa API key first.

## Websets MCP

Websets is the persistent sourcing layer: criteria-verified company/person lists with enrichments, imports, webhooks, and async events. It is where reusable GTM account/person pools live between asynchronous automation runs. Authentication is usually either a Bearer token in the `Authorization` header or the hosted MCP URL with `?exaApiKey=YOUR_EXA_API_KEY`; use the form your host supports.

Server URL:

```text
https://websetsmcp.exa.ai/mcp
```

Manual host configuration:

```bash
# Claude Code
claude mcp add --transport http websets https://websetsmcp.exa.ai/mcp --header "Authorization: Bearer YOUR_EXA_API_KEY"

# Codex
export EXA_API_KEY=YOUR_EXA_API_KEY
codex mcp add websets --url https://websetsmcp.exa.ai/mcp --bearer-token-env-var EXA_API_KEY

# Header-less fallback (older hosts)
claude mcp add --transport http websets "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
codex mcp add websets --url "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
```

Direct dashboard playground for previewing or building Websets without code:

```text
https://dashboard.exa.ai/playground/create-websets?q=<your+query>
```

If Websets tools do not appear after install, the usual causes: API key still set to placeholder, host did not reload after MCP config change, or the host scoped Websets auth to the wrong plugin.

## Exa Monitors

Monitors keep an existing Webset fresh by re-running a search on a cron schedule and appending or overriding results. Monitors are **not currently exposed as MCP tools**. Use one of:

- Dashboard UI: https://dashboard.exa.ai (open the Webset, attach a Monitor).
- REST API: `POST https://api.exa.ai/websets/v0/monitors` with `{ websetId, cadence: { cron, timezone }, behavior: { type: "search", config: { query, count, behavior: "append" | "override" } } }`. Cron must be a valid 5-field expression that triggers at most once per day; timezone is IANA (defaults to `Etc/UTC`).
- Webhook events: `webset.item.created`, `webset.item.enriched`, `webset.idle`.

GTM Agent's `websets-sourcing` skill outputs a Monitor spec when a monitor is needed; the user creates the monitor through the dashboard or REST API and pastes the resulting `monitor_id` back when recording the routine to Memory Store.

## Automation Hosts

Autopilot is a host-level automation pattern, not an uncontrolled background daemon hidden inside the plugin. In Codex, use recurring automations for daily digests, Websets refresh checks, monitor reviews, Gmail reply scans, and weekly learning summaries. In Claude Code, Claude Cowork, or OpenCode, use the host's scheduled-task or recurring-agent mechanism when available, or run the same routine prompt manually until that host exposes scheduling.

Each automation should have one precise goal, one cadence, one Memory Store thread/context, required connectors, allowed actions, forbidden actions, stop conditions, and expected output. The GTM Agent skill should record approved routine specs to Memory Store so future runs know what they are allowed to do.

## Gmail

The Codex plugin declares the Gmail app connector through `plugins/gtm-agent/.app.json`. The user still has to authorize Gmail in the host because Gmail access is account-scoped.

Campaign Setup uses the existing Gmail inbox and sent mail for sender voice, prior touches, warm paths, objections, demo language, suppressions, and reply learning. Gmail is part of the onboarding evidence, not only the sending channel. After setup approval, GTM Agent can send and follow up through Gmail inside the approved ramp and stop conditions.

Claude Code does not get Gmail merely because GTM Agent is installed. If Gmail is unavailable, GTM Agent should produce reviewed drafts, followup timing, and import-ready output instead of claiming it sent or threaded emails.

## Google Calendar

The Codex plugin declares the Google Calendar app connector through `plugins/gtm-agent/.app.json` for booking context after qualified replies:

```json
"google-calendar": {
  "id": "connector_947e0d954944416db111db556030eea6"
}
```

Google Calendar is used for availability and scheduling context, not as the first CTA source. Campaign Setup should first discover and confirm a demo/Cal link from Memory Store, website, or Gmail. If Calendar is unavailable, the confirmed demo link still works and scheduling automation is marked disabled.

Outlook Email and Outlook Calendar are future connector paths for GTM Agent; v1 is optimized for Gmail and Google Calendar.

## Why Tools May Not Appear Immediately

- The marketplace was refreshed, but the plugin was not installed or enabled.
- The host needs a restart or plugin reload.
- Memory Store MCP is authenticated under `memory-store`, not `gtm-agent`.
- Exa is available without your API key only within public/free limits.
- Websets requires a real Exa API key in the MCP URL.
- Gmail requires a separate account authorization in the host.
- Google Calendar requires a separate account authorization in the host.
