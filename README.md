# mem-plugins

Public Memory Store plugin marketplace for agent-native workflows.

Add this marketplace once, then install the Memory Store plugins that are relevant for your agent. Today the marketplace exposes `content-lead`; future plugins should be added to the same marketplace instead of creating new marketplace repos.

`content-lead` turns Memory Store insights into engagement-driving LinkedIn drafts and learns per-author voice from edits, approvals, and post performance. Sources are abstracted behind Memory Store — the skill operates on memories, not on specific upstreams.

## Quick Install

### Claude Code — one-liner

```bash
claude plugin marketplace add julep-ai/mem-plugins@main && claude plugin install content-lead@mem-plugins
```

Then `/reload-plugins` (or restart). If prompted, authenticate the Memory Store MCP server with `/mcp`.

### Codex CLI — one-liner

```bash
codex plugin marketplace add julep-ai/mem-plugins && codex plugin install content-lead@mem-plugins
```

Then restart Codex. If your Codex build does not yet expose `plugin install` on the CLI, the `marketplace add` half still works — open the plugin directory, select `Memory Store Plugins`, and install `Content Lead` from the UI.

### Claude Cowork — UI install

Cowork has no CLI. Install via the plugin directory:

1. Click the **+** icon in the chat input bar
2. Hover **Plugins** → click **Add plugin** (or **Manage plugins** to open the Directory directly)

   ![Cowork: + menu → Plugins → Add plugin](docs/images/cowork-add-plugin-menu.png)

3. In the **Directory** modal, switch to the **Plugins** tab, then the **Personal** sub-tab
4. Click the **+** next to **Local uploads** and add the marketplace: `julep-ai/mem-plugins`
5. The `Content lead` plugin appears in the list — click to install

   ![Cowork: Directory showing mem-plugins + sync controls](docs/images/cowork-directory-mem-plugins.png)

Once added, the `mem-plugins` chip has a **⋯** menu with:

- **Synced commit** — the current git SHA Cowork is running
- **Sync automatically** — toggle this **on** so Cowork pulls new commits without asking
- **Check for updates** — manual refresh
- **Remove** — disconnect the marketplace

Connect Memory Store MCP in Cowork's MCP settings if it is not already configured.

## Keep Up To Date

### Claude Code — one-liner

```bash
claude plugin marketplace update mem-plugins && claude plugin update content-lead@mem-plugins
```

### Codex CLI — one-liner

```bash
codex plugin marketplace upgrade mem-plugins && codex plugin update content-lead@mem-plugins
```

## Auto-Updates

Claude Code runs background auto-updates at startup against every registered marketplace. Once you've added `julep-ai/mem-plugins@main`, new plugin versions flow in automatically — no action required from installed users.

Because this marketplace is public, no token is needed. If you ever install against a private fork or mirror, export a token so the background update path can authenticate non-interactively:

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

Background auto-updates at every client startup will pick up the bump. Manual refresh is still available with the update one-liners above.

**Auto-register the marketplace in your team repo.** If you want teammates to be prompted to install `mem-plugins` when they open your project in Claude Code, drop this into that repo's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "mem-plugins": {
      "source": { "source": "github", "repo": "julep-ai/mem-plugins" }
    }
  }
}
```

When a teammate trusts the folder, Claude Code prompts them to add the marketplace — one less manual step.

Restart or reload your host after manual updates. To run update commands on a cadence, wrap either line in a cron job, a launchd plist, or a shell alias you run at session start — both commands are idempotent and safe to re-run.

## Claude Desktop (Not Supported)

Claude Desktop (the claude.ai app) does not have a plugin system. It supports MCP connectors only. Installing this marketplace from Claude Desktop by asking it to "install Memory Store Plugins from julep-ai/mem-plugins" will not work — the app will try to fetch the repo and stop there.

If you are on Claude Desktop, connect the Memory Store MCP server at `https://memory.store/mcp` as a connector. The agent can then drive the memory loop (`checkin`, `recall`, `record`, `report-issue`), but the `content-lead` skill files are not loaded — drafting quality will be lower than in Claude Code or Codex.

For the full plugin experience, use Claude Code or Codex CLI.

## Required MCP

`content-lead` requires Memory Store MCP for normal use. The plugin declares:

```text
https://memory.store/mcp
```

The MCP server provides the required `checkin`, `recall`, `record`, and `report-issue` operations. Tool names may be namespaced by the host, but those operations must be available.

Without Memory Store MCP, the agent can only draft from pasted context. It cannot recall brand memory, find company stories, or record feedback for the next run.

## Supported Targets

| Host | Install primitive | Status |
|------|-------------------|--------|
| Claude Code | `claude plugin install` CLI | verified |
| Codex CLI | `codex plugin install` CLI (or marketplace UI) | verified |
| Claude Cowork | marketplace UI (Add a plug-in → Personal → add marketplace) | verified |
| Claude Desktop | MCP connector only, no plugin install | not supported |
| OpenCode | skill files via MCP configuration | not verified |

OpenCode can in principle use `plugins/content-lead/skills/linkedin-studio/SKILL.md` as the canonical workflow when Memory Store MCP is configured in that host, but the install path is not tested and not recommended yet.

## Available Plugins

### `content-lead`

Path: `plugins/content-lead`

Includes one skill:

- `linkedin-studio`: starts with Memory Store `checkin`, recalls per-author voice, brand context, and source material, drafts 2–3 grounded LinkedIn posts optimized for Depth Score (saves, dwell, meaningful comments), and records feedback — approvals, edits, rejections, published text, and 24h/7d performance — so future runs improve per author. Craft rules, format templates, examples, recall cues, voice/brand bootstrap, record templates, and failure modes live in `references/` under the skill.

**First-run experience.** If Memory Store has no explicit brand or voice profile for the company/author, the skill infers both from existing memories (recent posts, shipped work, customer conversations, founder threads, edit diffs) and asks the user for a one-shot confirmation. A short interview bootstrap only runs when inference cannot cover enough dimensions. For teams with even a few weeks of Memory Store history, first-run setup is usually a confirmation, not a questionnaire.

Product loop:

```text
checkin -> recall -> draft -> feedback -> record -> better recall
```

Run it:

```text
/content-lead:linkedin-studio
```

Or in free text:

```text
Draft today's LinkedIn posts from Memory Store.
```

## Local Testing

For local testing from a cloned checkout without installing via marketplace:

```bash
claude --plugin-dir ./plugins/content-lead
```

## Build Another Plugin

Use one marketplace for this repo. Do not create a new marketplace per plugin.

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
