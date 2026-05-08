# Exa Setup Guide

End-to-end walkthrough for getting GTM Agent operational with Exa Search MCP, Exa Websets MCP, and Exa Monitors. Estimated time: 5-10 minutes.

GTM Agent v1 supports Exa as the only research/sourcing backend. There is no swappable provider — pick this path or run with research disabled.

## 1. Get an Exa API key

```text
https://dashboard.exa.ai/api-keys
```

Sign in, create a key, copy it. The same key authenticates both Exa Search MCP and Websets MCP. Free-plan keys work but are rate-limited; paid plans are required for production-scale Websets.

Store the key once in your shell profile if you plan to install across hosts:

```bash
export EXA_API_KEY=your-key-here
```

## 2. Install GTM Agent (if you haven't)

```bash
claude plugin marketplace add julep-ai/mem-plugins@main
claude plugin install memory-store@mem-plugins
claude plugin install gtm-agent@mem-plugins
```

The plugin's bundled `.mcp.json` ships Exa Search and Websets entries with `YOUR_EXA_API_KEY` placeholders. The next steps replace those placeholders in your host MCP settings.

## 3. Configure Exa Search MCP

### Claude Code

```bash
claude mcp add --transport http exa https://mcp.exa.ai/mcp \
  --header "x-api-key: $EXA_API_KEY"
```

### Codex CLI

```bash
codex mcp add exa --url https://mcp.exa.ai/mcp
```

Current Codex CLI supports `--url` and `--bearer-token-env-var`, but not arbitrary `x-api-key` headers. The command above uses Exa Search's free/rate-limited path. For production Exa Search limits in Codex, configure the `x-api-key` header in the Codex app/host MCP settings or config file.

Do not use `--bearer-token-env-var` for Exa Search unless Exa explicitly documents Bearer auth for that endpoint; Websets uses Bearer auth, Exa Search uses `x-api-key`.

### Claude Cowork (UI)

Open MCP settings, add a new HTTP MCP, paste:

```text
URL:    https://mcp.exa.ai/mcp
Header: x-api-key: <your key>
```

### Free-plan fallback (no key)

```bash
claude mcp add --transport http exa https://mcp.exa.ai/mcp
codex mcp add exa --url https://mcp.exa.ai/mcp
```

This works but is rate-limited and lacks Websets access.

## 4. Configure Websets MCP

Websets requires a real key. Authentication is preferred via Bearer header; fall back to query parameter for older hosts.

### Claude Code

```bash
claude mcp add --transport http websets https://websetsmcp.exa.ai/mcp \
  --header "Authorization: Bearer $EXA_API_KEY"
```

### Codex CLI

```bash
EXA_API_KEY=$EXA_API_KEY codex mcp add websets \
  --url https://websetsmcp.exa.ai/mcp \
  --bearer-token-env-var EXA_API_KEY
```

### Claude Cowork (UI)

```text
URL:    https://websetsmcp.exa.ai/mcp
Header: Authorization: Bearer <your key>
```

### Header-less fallback

```bash
claude mcp add --transport http websets \
  "https://websetsmcp.exa.ai/mcp?exaApiKey=$EXA_API_KEY"
```

## 5. Reload your host

- **Claude Code:** `/reload-plugins` or restart.
- **Codex:** restart the CLI or reload plugins from the UI.
- **Cowork:** the MCP picks up automatically; refresh if tools do not appear.

## 6. Verify the tools loaded

In your host's MCP/tool list, confirm these appear:

**Exa Search MCP** (3 active tools):

- `web_search_exa`
- `web_fetch_exa`
- `web_search_advanced_exa`

Older hosts may also surface deprecated tools (`company_research_exa`, `people_search_exa`, `linkedin_search_exa`, `crawling_exa`, `deep_search_exa`, `get_code_context_exa`). They still work but should not be the default.

**Websets MCP** (22 tools across 6 groups):

```text
webset:     create_webset, list_websets, get_webset, update_webset, delete_webset, preview_webset
items:      list_webset_items, get_item
search:     create_search, get_search, cancel_search
enrichment: create_enrichment, get_enrichment, cancel_enrichment
webhooks:   create_webhook, list_webhooks, get_webhook, update_webhook, delete_webhook
imports:    create_import, get_import, list_imports, list_events
```

If only Exa Search shows up, the Websets header is still set to the placeholder or your host did not reload. If neither shows up, the plugin is disabled or your host is offline.

## 7. (Optional) Try a Webset from the dashboard

The fastest sanity check is to build one Webset manually. Open the playground and submit a query:

```text
https://dashboard.exa.ai/playground/create-websets?q=AI+GTM+teams+hiring+a+sales+engineer
```

Pick `company` as the entity, set criteria, run. Once you see verified rows, the same Webset ID can be reused from the MCP via `get_webset` and enriched with `create_enrichment`.

## 8. (Optional) Attach an Exa Monitor

Monitors keep a Webset fresh. They are not exposed as MCP tools yet — use the REST API or dashboard.

### REST API

```bash
curl -X POST https://api.exa.ai/websets/v0/monitors \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "websetId": "webset_xxx",
    "cadence": { "cron": "0 9 * * 1", "timezone": "America/New_York" },
    "behavior": {
      "type": "search",
      "config": {
        "query": "AI GTM teams hiring a sales engineer",
        "entity": "company",
        "count": 25,
        "behavior": "append"
      }
    }
  }'
```

Cadence rules: 5-field Unix cron, must trigger at most once per day, IANA timezone (defaults to `Etc/UTC`).

### Dashboard

Open the Webset at `https://dashboard.exa.ai`, attach a Monitor, pick cadence/query/behavior, save.

### Webhook events

To react to monitor output, attach a webhook to the parent Webset:

- `webset.item.created` — new item passed verification.
- `webset.item.enriched` — an enrichment finished.
- `webset.idle` — the run completed.

Webhook secrets are shown once on creation. Save them immediately for signature verification.

## 9. Connect Gmail and Google Calendar

Exa handles research and sourcing. Outreach and booking context need separate connectors authorized in your host:

- Gmail: authorize the Gmail connector in your host MCP/connector settings. GTM Agent uses it for sender voice learning, drafting, sending after setup approval, replies, and followups.
- Google Calendar: authorize the calendar connector for booking context after qualified replies.

Both are account-scoped; the plugin cannot ship them ready-to-run.

## 10. Run campaign setup

```text
/gtm-agent:campaign-setup

Set up GTM Agent autopilot. Recall Memory Store context, research our website and demo CTA, learn from Gmail, define Google Calendar booking policy, define daily/weekly automation routines, build the setup packet, and ask for setup approval before sending.
```

The skill returns a setup packet — review it, approve it, and the orchestrator can start sourcing and drafting on real Exa data. No sends happen before setup approval.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|------|
| Exa tools missing | Plugin disabled, host not reloaded | Enable plugin; `/reload-plugins` |
| Only `web_search_exa` and `web_fetch_exa` appear | Default tool set, advanced not enabled | Re-add Exa with `?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa` or accept that advanced is optional |
| Websets tools missing | Placeholder key, header rejected, plan limits | Replace `YOUR_EXA_API_KEY`; verify `Authorization: Bearer` is being sent; check Exa dashboard plan |
| 401 on REST monitor call | Wrong header form | Use `Authorization: Bearer <key>`, not `x-api-key` |
| Free-plan rate limits | No API key configured | Get a key at [https://dashboard.exa.ai/api-keys](https://dashboard.exa.ai/api-keys) |
| Codex says `--header` not supported | Current Codex CLI does not expose arbitrary HTTP headers | For Exa Search, configure `x-api-key` in Codex app/host MCP settings or use the free/rate-limited URL; for Websets, use `--bearer-token-env-var EXA_API_KEY` |
| Webset returns zero items | Criteria too strict, query off | Loosen criteria, broaden the query, run `preview_webset` first |
| Monitor not firing | Cron triggers more than once/day, cadence rejected | Use a once-per-day cron like `0 9 * * 1` |

For broader installation issues see [INSTALLATION.md](INSTALLATION.md). For per-connector reference details see [CONNECTORS.md](CONNECTORS.md). For Monitor specs and the campaign-side workflow see [../plugins/gtm-agent/skills/gtm-agent/references/monitors.md](../plugins/gtm-agent/skills/gtm-agent/references/monitors.md).
