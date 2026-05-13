# Memory Store Marketplace Installation

This repo publishes one marketplace:

```text
mem-plugins -> displayed as Memory Store
```

The marketplace currently contains these installable plugins:

- `memory-store` - core Memory Store workflows, including LinkedIn Studio and Marketplace Operator.
- `gtm-agent` - Memory Store-powered Sales/GTM autopilot workflows, including GTM planning, Exa research, Websets sourcing, Gmail execution, recurring routines, and campaign learning.

Install the marketplace once. Then install the plugin you want from that marketplace.

The source repository is `MemoryStore/plugins`. For external distribution, that repository must either be public or the installing user must have GitHub access. Private installs should set `GITHUB_TOKEN` or `GH_TOKEN` before relying on background updates.

## Claude Code

### First-Time Install

Add or refresh the marketplace:

```bash
claude plugin marketplace add MemoryStore/plugins@main
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
codex plugin marketplace add MemoryStore/plugins
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
- `list-briefs`
- `record`
- `report-issue`

`gtm-agent` requires the core `memory-store` plugin to be installed and authenticated. GTM Agent intentionally does not redeclare Memory Store MCP in its own `.mcp.json`, because doing so can create a second Memory Store auth prompt in hosts that scope MCP auth per plugin.

GTM Agent uses Memory Store as a proactive intelligence layer with long-term memory for agents, not just recall. During planning and execution it should select sparse canonical briefs, recall supporting evidence, and distill approved rules, user corrections, approval policies, connector expectations, persona decisions, sourcing gates, outcomes, sparse brief deltas, and skill-improvement candidates into Memory Store records so future runs inherit them, surface relevant context, and continue approved routines.

If the host exposes low-level brief-editing tools, GTM Agent should use them only after the sparse-brief gate passes: read selected briefs with `get-brief`, attach pending deltas with `propose-brief`, and confirm approved brief changes with `confirm-brief`. Most campaign execution events should still become records, not brief edits.

`gtm-agent` can additionally use:

- Exa Search MCP (`https://mcp.exa.ai/mcp`) for `web_search_exa`, `web_fetch_exa`, and `web_search_advanced_exa`. Deprecated tools such as `company_research_exa`, `people_search_exa`, and `deep_search_exa` are backward-compatibility fallbacks only.
- Websets MCP (`https://websetsmcp.exa.ai/mcp`) for persistent company/person sets — 22 tools across webset, items, search, enrichment, webhooks, imports.
- Exa Monitors REST API (`https://api.exa.ai/websets/v0/monitors`) for cron-scheduled Webset refresh. Monitors are not yet exposed as MCP tools; GTM Agent should create them through approved REST/API or host automation where possible.
- Gmail connector for inbox learning, approved GTM plan/autopilot sends, replies, and followups.
- Google Calendar connector for booking context after qualified replies.

Both Exa Search and Websets use the same Exa API key. Get one at `https://dashboard.exa.ai/api-keys`. The plugin's `.mcp.json` ships with `YOUR_EXA_API_KEY` placeholders; replace them in your host MCP settings, do not commit real keys. Free-plan Exa Search works without a key only for exploratory public lookup; Websets requires a key, and production GTM Agent runs should stop and ask for Exa/Websets setup before sourcing, persona discovery, email enrichment, signal cards, or outbound drafts.

When Exa/Websets are missing during GTM planning, the agent should give the API-key URL, ask the user to paste the key into a terminal prompt when possible, and run or output the host setup command. From a local checkout:

```bash
plugins/gtm-agent/scripts/setup_exa_connectors.sh --host codex --persist-shell
```

Production GTM research should verify `web_search_advanced_exa` is loaded for company, people, and article/news searches.

For a 5-10 minute step-by-step Exa setup walkthrough — including Monitors and Gmail/Calendar auth — see [EXA_SETUP.md](EXA_SETUP.md). For per-connector reference (URLs, header vs query-param auth, dashboard playground link) see [CONNECTORS.md](CONNECTORS.md).

## Plugin Commands

After GTM Agent is installed, these skills are available:

```text
/gtm-agent:campaign-setup
/gtm-agent:gtm-agent
/gtm-agent:exa-company-research
/gtm-agent:exa-lead-generation
/gtm-agent:exa-people-search
/gtm-agent:websets-sourcing
```

Recommended first run:

```text
/gtm-agent:campaign-setup

Start GTM Agent autopilot. Recall Memory Store context, research our website and demo CTA, learn from Gmail, define Google Calendar booking policy, define daily/weekly automation routines, build the GTM operating profile, and ask for approval before sending.
```

GTM Agent should send only after the GTM operating profile is approved. Autopilot means approved, goal-scoped asynchronous routines; it does not mean hidden bulk sending. The planner still needs a complete campaign unit: `persona + live signal + offer angle + proof path + next action`.

The first operating-profile flow is reusable, not ad hoc. GTM Agent should infer from Memory Store, website research, Gmail, and Google Calendar first, then ask only unresolved blockers. The onboarding questions live in `plugins/gtm-agent/skills/campaign-setup/references/onboarding-questions.md`, the GTM plan contract lives in `plugins/gtm-agent/skills/campaign-setup/references/gtm-plan.md`, and the profile skeleton can be printed with:

```bash
python3 plugins/gtm-agent/skills/campaign-setup/scripts/render_gtm_plan_template.py
```

### First Usable Autopilot Run

Start small and make every routine precise:

1. Install and authenticate `memory-store`.
2. Install `gtm-agent`.
3. Configure Exa Search and Websets with a real Exa API key.
4. Authorize Gmail and Google Calendar if the host supports them.
5. Run `/gtm-agent:campaign-setup` to produce the first GTM operating profile.
6. Approve the GTM operating profile: campaign mode, context sources, canonical briefs used, funnel system, offer, sender, CTA, ICP cells, claims, send ramp, followups, suppressions, stop conditions, routine specs, memory distillation items, sparse brief deltas, and background-worker graph.
7. Run a small pilot, usually day 1 max 10 sends.
8. Turn approved recurring work into automations: daily Websets/monitor review, Gmail reply scan, followup check, daily digest, and weekly Memory Store learning summary.

Each automation needs one goal, one cadence, one Memory Store thread/context, required tools, allowed actions, forbidden actions, stop conditions, expected output, and the background workers it should spawn. Local folders are optional execution ledgers for review/import/export, not the GTM Agent product surface. Codex can run these as recurring automations; Claude Code, Claude Cowork, and OpenCode should use their host scheduling mechanism when available or run the same routine prompt manually until scheduling is exposed.

After Memory Store is installed, these skills are available:

```text
/memory-store:memory-store-basics
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

The GTM Agent should still produce the GTM plan, exact research queries, Websets specs, monitor specs, and connector setup instructions. It should not produce send-ready lead lists or outbound copy from website-only research. To execute sourcing directly:

1. Get an Exa API key at https://dashboard.exa.ai/api-keys.
2. Replace `YOUR_EXA_API_KEY` in your host MCP settings for both `exa` and `websets` entries (the plugin's `.mcp.json` ships placeholders).
3. Reload the host so the new headers take effect.
4. Verify in the host's MCP/tool list that `web_search_exa`, `web_fetch_exa`, and `create_webset` are present.

If only Exa Search appears but Websets does not, the Websets header is still set to the placeholder. If neither appears, the plugin was not enabled or the host did not reload after the install.

### Setting up Exa Monitors

Monitors are not exposed as MCP tools yet. Once a Webset exists, the normal path is for GTM Agent to create or propose creation through an approved REST/API call or host automation. Use dashboard setup only when the current host cannot run the REST call.

- REST API: `POST https://api.exa.ai/websets/v0/monitors` with `Authorization: Bearer YOUR_EXA_API_KEY`. Body needs `websetId`, `cadence` (cron + IANA timezone, max once per day), and `behavior` (type `search`, with `query`, `count`, `behavior: "append" | "override"`). Optional webhook events: `webset.item.created`, `webset.item.enriched`, `webset.idle`.
- Manual fallback: open the Webset at https://dashboard.exa.ai and add a Monitor.

Record the returned `monitor_id` so GTM Agent can map the routine to Memory Store.
