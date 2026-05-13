# Memory Store Marketplace

Memory Store plugin marketplace for agent-native workflows built by Memory Store. Apache-2.0 licensed so it can be forked, extended, and used as the reference shape for new Memory Store-backed plugins.

Add this marketplace once, then install the plugin you need. The source repo is `MemoryStore/plugins`, but the marketplace identity is Memory Store. The repo exposes multiple installable Memory Store-built plugins from one marketplace.

The core `memory-store` plugin provides Memory Store-native workflows, teaches the Memory Store basics loop, and owns Memory Store MCP auth. `gtm-agent` is a separate installable **GTM engineering agent** — it engineers GTM campaigns and runs them autonomously for **any seller** (software, infrastructure, services, real estate, consumer goods, vertical SaaS, agencies, consulting). The seller's Memory Store is the proactive intelligence layer for agents: it remembers offer, ICPs, customers, competitors, objections, claims, outcomes, obligations, approved rules, and sparse canonical briefs so each new batch is smarter than the last. Install `memory-store` once, then GTM Agent reuses that Memory Store auth instead of prompting again.

GTM Agent treats Exa as the only supported web/research backend in v1. Both Exa Search MCP and Exa Websets MCP use a single Exa API key — get one at [https://dashboard.exa.ai/api-keys](https://dashboard.exa.ai/api-keys) and paste it into your host MCP settings. No-key Exa is exploratory only; a real campaign must stop and ask for Exa/Websets configuration before production ICP discovery, sourcing, signal cards, persona discovery, email enrichment, or outbound drafts. Exa Monitors (cron-scheduled Webset refresh) are not exposed as MCP tools yet; GTM Agent should create them through an approved REST call or host automation where possible, with dashboard setup as a fallback only. For a step-by-step setup walkthrough see [docs/EXA_SETUP.md](docs/EXA_SETUP.md).

## Marketplace Model

There is one marketplace:

```text
mem-plugins -> displayed as Memory Store
```

The repo has two marketplace metadata files because Codex and Claude Code use different formats:

```text
.agents/plugins/marketplace.json
.claude-plugin/marketplace.json
```

Those are host adapters for the same Memory Store marketplace, not two separate marketplaces.

Inside that marketplace there can be many plugins:

```text
plugins/memory-store
plugins/gtm-agent
plugins/<next-memory-store-backed-product>
```

Each plugin should read as built by Memory Store. Do not create a new marketplace for every plugin, and do not present public marketplace metadata under any local workspace or agency identity. The local checkout path is an implementation detail, not the marketplace publisher.

## Installation

Full installation and troubleshooting details are in [docs/INSTALLATION.md](docs/INSTALLATION.md). Connector setup for Memory Store, Exa, Websets, Gmail, and Google Calendar is in [docs/CONNECTORS.md](docs/CONNECTORS.md). For a shareable install and builder reproduction guide, see [docs/PLUGIN_INSTALL_AND_REPRODUCTION.md](docs/PLUGIN_INSTALL_AND_REPRODUCTION.md). The operator guide for running GTM Agent with Memory Store, Websets, Attio-style campaign panels, sending rails, and Hermes background routines is in [docs/GTM_AGENT_OPERATING_GUIDE.md](docs/GTM_AGENT_OPERATING_GUIDE.md).

The short version:

- Add/update the marketplace first.
- Install the plugin if it is not installed.
- Update the plugin only after it is installed.
- Restart/reload the host and authenticate Memory Store MCP.

If you see `Plugin "gtm-agent" is not installed`, run `claude plugin install gtm-agent@mem-plugins`; do not run `claude plugin update gtm-agent@mem-plugins` yet.

## Quick Install For Humans

### Claude Code

```bash
claude plugin marketplace add MemoryStore/plugins@main
claude plugin marketplace update mem-plugins
claude plugin install memory-store@mem-plugins
claude plugin install gtm-agent@mem-plugins
```

Then `/reload-plugins` (or restart). If prompted, authenticate the Memory Store MCP server with `/mcp`.

To verify:

```bash
claude plugin list
```

### Codex CLI

```bash
codex plugin marketplace add MemoryStore/plugins
```

Then restart Codex or reload plugins. Current Codex CLI builds expose marketplace management from the terminal, but plugin install/enable happens in the Codex plugin UI. Open the plugin directory, select the `Memory Store` marketplace, then install or enable `Memory Store` and `GTM Agent`.

Install GTM Agent after Memory Store MCP is connected by selecting `GTM Agent` from the same marketplace in the Codex plugin UI.

If a future Codex build adds plugin-level CLI commands, prefer the CLI help shown by `codex plugin --help` over older README snippets.

### Claude Cowork — UI install

Cowork has no CLI. Install via the plugin directory:

1. Click the **+** icon in the chat input bar
2. Hover **Plugins** → click **Add plugin** (or **Manage plugins** to open the Directory directly)

   ![Cowork: + menu → Plugins → Add plugin](docs/images/cowork-add-plugin-menu.png)

3. In the **Directory** modal, switch to the **Plugins** tab, then the **Personal** sub-tab
4. Click the **+** next to **Local uploads** and add the marketplace: `MemoryStore/plugins`
5. The `Memory Store` plugin appears in the list — click to install

   ![Cowork: Directory showing mem-plugins + sync controls](docs/images/cowork-directory-mem-plugins.png)

Once added, the marketplace chip has a **⋯** menu with:

- **Synced commit** — the current git SHA Cowork is running
- **Sync automatically** — toggle this **on** so Cowork pulls new commits without asking
- **Check for updates** — manual refresh
- **Remove** — disconnect the marketplace

Connect Memory Store MCP in Cowork's MCP settings if it is not already configured.

## Keep Up To Date

### Claude Code

First refresh the marketplace:

```bash
claude plugin marketplace update mem-plugins
```

Then update only the plugins that are already installed:

```bash
claude plugin update memory-store@mem-plugins
claude plugin update gtm-agent@mem-plugins
```

If `gtm-agent` is not installed yet:

```bash
claude plugin install gtm-agent@mem-plugins
```

### Codex CLI

```bash
codex plugin marketplace upgrade mem-plugins
```

Then restart/reload Codex. The upgraded marketplace root will contain the latest plugin metadata; plugin install/enable still happens in the Codex plugin UI on current CLI builds.

## Auto-Updates

Claude Code runs background auto-updates at startup against every registered marketplace. Once you've added `MemoryStore/plugins@main`, new plugin versions flow in automatically — no action required from installed users.

For external distribution, `MemoryStore/plugins` must either be public or the installing user must have GitHub access. Private installs, private forks, and private mirrors should export a token so the background update path can authenticate non-interactively:

```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
# or: export GH_TOKEN=...
```

Without this on a private source, interactive updates still work via your keychain or `gh auth`, but the silent startup auto-update path cannot prompt and will skip.

**Cowork tracks commits, not versions.** Claude Cowork's Directory shows the synced commit SHA and has a **Sync automatically** toggle on each marketplace chip. When that toggle is on, Cowork pulls every new `main` commit automatically — no `version` bump required. The notes below about the `version` field only apply to Claude Code (and Codex CLI if you use the marketplace UI there).

**How versioning controls auto-updates in Claude Code.** Claude Code only treats a commit as a new plugin version when the declared `version` field changes. This marketplace pins `version` on each plugin, so Claude Code clients pull updates only when that string is bumped. To ship a release:

1. Bump `version` in `plugins/<plugin-name>/.claude-plugin/plugin.json`
2. Bump the matching entry in `.claude-plugin/marketplace.json`
3. Commit and push to `main`

Background auto-updates at every client startup will pick up the bump. Manual refresh is still available with the update commands above.

**Auto-register the marketplace in your team repo.** If you want teammates to be prompted to install `mem-plugins` when they open your project in Claude Code, drop this into that repo's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "mem-plugins": {
      "source": { "source": "github", "repo": "MemoryStore/plugins" }
    }
  }
}
```

When a teammate trusts the folder, Claude Code prompts them to add the marketplace — one less manual step.

Restart or reload your host after manual updates. To run update commands on a cadence, wrap either line in a cron job, a launchd plist, or a shell alias you run at session start — both commands are idempotent and safe to re-run.

## Marketplace Upgrade Routine

Use the core `memory-store` plugin's `marketplace-operator` skill to audit whether the marketplace, a plugin, or a skill needs an update.

Run it:

```text
/memory-store:marketplace-operator
```

Or in free text:

```text
Check the Memory Store marketplace for new plugin opportunities, stale skills, manifest drift, and upgrade work.
```

The intended recurring loop is:

```text
checkin -> recall marketplace context -> inspect manifests/docs/skills -> scan requested market references -> identify upgrade needs -> validate -> record decisions
```

This can be run manually before releases or scheduled as a Codex automation. The automation should report recommended updates first; it should not publish releases, push changes, or send external messages without explicit approval.

## Claude Desktop (Not Supported)

Claude Desktop (the claude.ai app) does not have a plugin system. It supports MCP connectors only. Installing this marketplace from Claude Desktop by asking it to "install Memory Store from MemoryStore/plugins" will not work — the app will try to fetch the repo and stop there.

If you are on Claude Desktop, connect the Memory Store MCP server at `https://memory.store/mcp` as a connector. The agent can then drive the memory loop (`checkin`, `recall`, `record`, `report-issue`), but the `memory-store` plugin skills are not loaded — drafting quality will be lower than in Claude Code or Codex.

For the full plugin experience, use Claude Code or Codex CLI.

## Required MCP

`memory-store` requires Memory Store MCP for normal use. The plugin declares:

```text
https://memory.store/mcp
```

The MCP server provides the required `checkin`, `recall`, `list-briefs`, `record`, and `report-issue` operations. Tool names may be namespaced by the host, but those operations must be available.

Without Memory Store MCP, the agent can only draft from pasted context. It cannot recall brand memory, find company stories, or record feedback for the next run.

`gtm-agent` requires the core `memory-store` plugin to be installed and authenticated, but it does not redeclare Memory Store MCP in its own `.mcp.json`. That avoids duplicate Memory Store auth prompts in hosts that scope MCP auth per plugin. GTM Agent uses Memory Store as a proactive intelligence layer and long-term operating memory for agents: plan rules, user corrections, approval policies, persona decisions, connector expectations, campaign outcomes, sparse canonical brief deltas, and skill-improvement candidates should be distilled and recorded so future runs can surface context, continue work, and improve without re-asking. If low-level brief tools are available, use them for controlled brief reads, proposed deltas, explicit corrections, and approved canonical edits; do not use them to turn every campaign event into a brief.

High-quality sourcing expects Exa MCP and Websets MCP when available:

- Exa Search MCP at `https://mcp.exa.ai/mcp`. Active tools: `web_search_exa`, `web_fetch_exa`, `web_search_advanced_exa`. Deprecated tools (`company_research_exa`, `people_search_exa`, `linkedin_search_exa`, `crawling_exa`, `deep_search_exa`, `get_code_context_exa`) are backward-compatibility fallbacks only.
- Websets MCP at `https://websetsmcp.exa.ai/mcp`. 22 tools across webset, items, search, enrichment, webhooks, and imports for criteria-verified persistent lists.
- Exa Monitors REST API at `https://api.exa.ai/websets/v0/monitors`. Cron-scheduled (max once per day, 5-field expression, IANA timezone). Not exposed as MCP yet; the agent should create the monitor through approved REST/API or host automation when available, and use dashboard setup only as a manual fallback.

Both Exa Search and Websets share one API key from [https://dashboard.exa.ai/api-keys](https://dashboard.exa.ai/api-keys) and accept it as `x-api-key` (Exa Search) or `Authorization: Bearer` (Websets). The plugin's `.mcp.json` ships placeholders — replace them in your host's MCP settings, never commit real keys. Free-plan Exa Search works without a key only for exploratory lookup; Websets requires a real key, and GTM Agent must ask for that key before production ICP discovery, sourcing, persona discovery, email enrichment, signal cards, or outbound drafts.

When Exa/Websets are missing, GTM Agent should guide setup instead of stopping at documentation: open the Exa API-key URL, ask the user to paste the key into a terminal prompt when possible, then run `plugins/gtm-agent/scripts/setup_exa_connectors.sh --host codex --persist-shell` or the host equivalent. Production research should verify `web_search_advanced_exa` is available for company, people, and article/news searches.

Gmail outreach and followups require the host's Gmail connector. Google Calendar booking context requires the host's Google Calendar connector. Gmail is the default founder-led first-touch and reply-learning channel. If Gmail/Calendar are missing, the skill outputs connector gaps and routine specs instead of pretending actions happened. If Exa/Websets are missing, the skill must keep the campaign in planning mode and ask for the Exa API key before production sourcing or drafting.

## Supported Targets

| Host | Install primitive | Status |
|------|-------------------|--------|
| Claude Code | `claude plugin install` CLI | verified |
| Codex CLI | `codex plugin marketplace add/upgrade` plus plugin UI install/enable | verified |
| Claude Cowork | marketplace UI (Add a plug-in → Personal → add marketplace) | verified |
| Claude Desktop | MCP connector only, no plugin install | not supported |
| OpenCode | skill files via MCP configuration | not verified |

OpenCode can in principle use the skill files under `plugins/<plugin-name>/skills/` when the required MCP servers are configured in that host, but the install path is not tested and not recommended yet.

## Available Plugins

### `memory-store`

Path: `plugins/memory-store`

Includes these skills:

- `memory-store-basics`: teaches the Memory Store operating loop: `checkin`, sparse `list-briefs`, targeted `recall`, confirmed `record`, controlled low-level brief edits when available, and `report-issue`. It keeps briefs as canonical living maps, uses recall for evidence, and avoids turning briefs into another raw-memory dump.
- `linkedin-studio`: acts as a Memory Store-powered content strategist and copywriter. It starts with Memory Store `checkin`, recalls brand voice, author voice, prior performance, and source material, identifies publishable memory opportunities from customer context, shipped work, team discussions, internal artifacts, and prior content learnings, drafts grounded LinkedIn posts with a fitting CTA, and records feedback — approvals, edits, rejections, published text, and 24h/7d performance — so future runs improve.
- `marketplace-operator`: maintains the Memory Store marketplace. It starts with Memory Store `checkin`, recalls marketplace decisions and plugin feedback, inspects manifests/docs/skills, scouts new Memory Store-backed plugin opportunities, audits upgrade needs, recommends file-level changes, and records confirmed marketplace decisions.

**LinkedIn Studio first-run experience.** If Memory Store has no explicit brand or voice profile for the company/author, the skill infers both from existing memories (recent posts, shipped work, customer conversations, founder threads, edit diffs) and asks the user for a one-shot confirmation. A short interview bootstrap only runs when inference cannot cover enough dimensions. For teams with even a few weeks of Memory Store history, first-run setup is usually a confirmation, not a questionnaire.

Product loop:

```text
checkin -> list/select briefs -> recall evidence -> act -> record confirmed learning -> brief delta only when operating truth changes
```

Run it:

```text
/memory-store:memory-store-basics
/memory-store:linkedin-studio
/memory-store:marketplace-operator
```

Or in free text:

```text
Draft today's LinkedIn posts from Memory Store.
```

### `gtm-agent`

Path: `plugins/gtm-agent`

Includes these skills:

- `campaign-setup`: creates the GTM plan from Memory Store, uploaded or pasted context, prior campaigns, website research, demo CTA discovery, Gmail learning, Google Calendar policy, send ramp, and goal-scoped autopilot routines.
- `gtm-agent`: orchestrates the full Memory Store-powered GTM campaign loop: campaign engineering, campaign planning, ICP design, Exa/Websets sourcing, people search, Gmail outreach/followups, Google Calendar booking context, asynchronous routines, engagement capture, and learning records.
- `exa-company-research`: researches companies, competitors, market categories, account context, public profiles, news, and company lists with Exa Company Research plus Memory Store context.
- `exa-lead-generation`: generates enriched account lists from a confirmed ICP with Exa advanced search, micro-vertical batching, structured schemas, dedupe, scoring, and CSV/import-ready output.
- `exa-people-search`: finds likely buyers, public professional profiles, experts, and team members for already-qualified accounts.
- `websets-sourcing`: creates, previews, enriches, imports, refreshes, and inspects persistent Exa Websets for GTM account and people sourcing.

GTM loop:

```text
checkin -> list/select canonical briefs -> recall durable rules/evidence -> context ingestion -> campaign mode -> funnel/ICP system -> campaign planner -> Exa/Websets sourcing -> people search -> signal cards -> approved automation routines -> Gmail autopilot -> Calendar booking context -> engagement -> distill rules/outcomes -> record -> sparse brief deltas -> better targeting
```

The campaign engineering layer runs before copy. It classifies whether this is a new campaign, a continuation, a refresh, an expansion, a rescue, a reactivation, or an event/launch campaign; ingests Memory Store briefs, uploaded/pasted docs, prior records/artifacts, website, Gmail, Calendar, and public context; and maps the funnel system. The planner unit is still `persona + live signal + offer angle + proof path + next action`. A homepage, generic company category, founder title, or website-only scrape is not enough signal to draft.

The first GTM operating profile is the repeatable GTM engineer onboarding script. It infers from Memory Store, website research, Gmail, and Google Calendar first, then asks only unresolved blockers. The reusable planning questions live in `plugins/gtm-agent/skills/campaign-setup/references/onboarding-questions.md`, the GTM plan contract lives in `plugins/gtm-agent/skills/campaign-setup/references/gtm-plan.md`, and agents can print the profile skeleton with `plugins/gtm-agent/skills/campaign-setup/scripts/render_gtm_plan_template.py`.

Autopilot is the point of GTM Agent, but it is precise rather than vague. A user engineers the campaign once: offer, sender, ICP cells, signal sources, proof path, CTA, send ramp, stop conditions, routine specs, canonical briefs, and background-worker graph. During that conversation, GTM Agent distills durable operating memory into records and sparse brief deltas. After approval, the host can run recurring goal-scoped automations that spawn bounded workers: daily Websets/monitor review, Gmail reply scan, followup check, daily digest, and weekly Memory Store learning summary. Local folders are optional execution ledgers for review/import/export, not the product surface. Start with a small ramp, record outcomes, and let future runs use those learnings instead of re-asking or re-sourcing from scratch.

Run it:

```text
/gtm-agent:campaign-setup
/gtm-agent:gtm-agent
/gtm-agent:exa-company-research
/gtm-agent:exa-lead-generation
/gtm-agent:exa-people-search
/gtm-agent:websets-sourcing
```

Or in free text:

```text
Set up and run a 1000-recipient GTM autopilot with 20 ICPs, 50 targets each, Exa/Websets sourcing, monitors, Gmail sending/followups, and Memory Store learning.
```

For the first GTM operating profile:

```text
Start GTM Agent autopilot. Recall Memory Store context, research our website and demo CTA, learn from Gmail, define Google Calendar booking policy, define daily/weekly automation routines, build the GTM operating profile, and ask for approval before sending.
```

GTM Agent expects Memory Store MCP first. Exa, Websets, Exa Monitors, Gmail, Google Calendar, and host automations make it operational: Exa researches companies and people, Exa advanced search generates structured lead pools, Websets persists verified lists, Monitors keep new high-intent signals flowing, Gmail learns from the current inbox and sends/follows up after operating-profile approval, Google Calendar provides booking context after qualified replies, host automations run the approved routines, and Memory Store records the learning loop. High-scale campaigns may source around 1000 leads/emails per day, but sends remain gated by signal-card quality, suppressions, Gmail health, and the approved ramp.

For the operating model across campaign panels, PLG signals, Hermes background goals, and alternate sending rails such as Agent Mail or Resend, see [docs/GTM_AGENT_OPERATING_GUIDE.md](docs/GTM_AGENT_OPERATING_GUIDE.md).

## Local Testing

For local testing from a cloned checkout without installing via marketplace:

```bash
claude --plugin-dir ./plugins/memory-store
claude --plugin-dir ./plugins/gtm-agent
```

Run the GTM Agent skill-surface checks before changing skill descriptions, routing boundaries, or required reference files:

```bash
python3 plugins/gtm-agent/scripts/validate_skill_surface.py
python3 plugins/gtm-agent/skills/campaign-setup/scripts/test_render_gtm_plan_template.py
```

## Build Another Skill Or Plugin

Use one marketplace for this repo. Do not create a new marketplace per plugin. The Codex and Claude marketplace files are host adapters for the same marketplace. New products go inside the Memory Store marketplace as plugins built by Memory Store.

For a new workflow that belongs under an existing plugin surface, add it as a skill under:

```text
plugins/<plugin-name>/skills/<skill-name>/
```

Create a separate plugin only when it should be installed, authorized, or presented as a distinct product.

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

Use Plugin Eval before committing plugin changes:

```text
Use $plugin-eval to evaluate plugins/<plugin-name>.
```

## License

Apache License 2.0. See [LICENSE](LICENSE) for full text.

Copyright 2026 Julep AI, Inc.
