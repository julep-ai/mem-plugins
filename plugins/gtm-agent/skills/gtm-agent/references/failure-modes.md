# Failure Modes

Use this reference when a GTM run is blocked, low-confidence, or unsafe to execute.

## Memory Store MCP Unavailable

Do not run a memory-native GTM campaign if Memory Store is unavailable.

GTM Agent expects Memory Store MCP to come from the installed `memory-store@mem-plugins` plugin or an existing host-level Memory Store connector. It intentionally does not redeclare Memory Store MCP in its own `.mcp.json`, because that can force a second auth prompt.

Fallback:

- Say Memory Store MCP is unavailable.
- Continue only as generic planning or copy assistance from pasted/public context, not as GTM Agent.
- Do not run production sourcing, autopilot routines, or learning workflows.
- Do not claim the system learned.
- Do not record anything unless `record` becomes available.

## Empty Or Thin Recall

If recall lacks product, ICP, customer language, or approved claims:

- Infer only from public sources and label confidence.
- Ask for the smallest missing blocker: product, ICP, existing customers, exclusions, sender, or send policy.
- Prefer a small pilot batch over a 1000-recipient plan.

## Exa, Websets, Or Monitors Missing

If Exa/Websets/Monitor support is missing, the GTM plan can continue, but production GTM is blocked or degraded:

- Produce exact search queries, Websets criteria, enrichments, and batching plan.
- Tell the user which MCP to connect and ask for Exa API key setup immediately when Exa/Websets credentials are missing. Give `https://dashboard.exa.ai/api-keys`, ask for a terminal-safe API-key paste/setup, and run or output `plugins/gtm-agent/scripts/setup_exa_connectors.sh --host codex --persist-shell` or the host-specific equivalent.
- Output monitor specs when always-on signal detection is part of the plan.
- Do not fabricate lead lists.
- Do not draft campaign copy or mark accounts send-ready from website-only research.
- Do not claim production sourcing, deeper ICP discovery, verified enrichment, refresh, or always-on monitoring happened.
- Use explicit status labels: `plan_only`, `research_blocked_for_production`, `sourcing_blocked_for_production`, `monitoring_degraded`.
- If only `web_search_exa` appears, treat the Exa surface as exploratory research only. Execution-grade lead generation and source fetching need `web_search_advanced_exa` and `web_fetch_exa`. Advanced company, people, and article/news searches are required for deep GTM sourcing. Use deprecated tools such as `deep_search_exa` only when the host still exposes them.

For Exa Search MCP:

```bash
# Production Exa Search in Codex:
export EXA_API_KEY=YOUR_EXA_API_KEY
codex mcp add exa --url "https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa&exaApiKey=$EXA_API_KEY"
```

For Websets MCP:

```bash
export EXA_API_KEY=YOUR_EXA_API_KEY
codex mcp add websets --url https://websetsmcp.exa.ai/mcp --bearer-token-env-var EXA_API_KEY
```

GTM Agent also declares Websets in `plugins/gtm-agent/.mcp.json` with a `YOUR_EXA_API_KEY` placeholder; the user still has to replace it in host MCP settings because the plugin cannot safely ship a real Exa key.

For Exa Monitors, use [monitors.md](monitors.md) to output the REST/API or host-automation spec. Monitors are not currently exposed as MCP tools, but they are still the production path for recurring signal streams. Dashboard setup is a manual fallback only.

## Gmail Missing

If Gmail is missing:

- Output ready-to-import drafts and followup timing only after planner/copy gates pass.
- Gmail-missing draft fallback does not override Exa/Websets draft blocks; if Exa/Websets are missing, do not produce send-ready rows or outbound copy.
- Do not claim emails were sent, scheduled, labeled, or threaded.
- Do not claim production execution, reply monitoring, suppression checks, or mailbox learning.
- Keep recipient data in a reviewable table or CSV-shaped output.
- Mark full autopilot sending disabled until Gmail is connected. Use `sending_blocked_for_production`.

## Google Calendar Missing

If Google Calendar is missing:

- Keep the confirmed demo link usable.
- Mark scheduling automation disabled.
- Do not claim availability was checked or events were created.

## Plan Not Approved

If the user asks for autonomous GTM but the GTM plan is not approved:

- Route to `campaign-setup`.
- Show representative copy and send criteria.
- Do not send until plan approval covers sender, CTA, ICPs, claims, ramp, stop conditions, and connector gaps.

After plan approval, per-batch approval is not required unless the approved policy says draft-first.

## Low Signal Quality

If most accounts only match static firmographics:

- Mark the batch as research-only.
- Recommend more precise ICP cells or stronger trigger sources.
- Do not move the batch to send-ready.

## Generic Email Drift

If drafts sound generic, diagnose upstream before rewriting:

- Did the agent treat a homepage or category as a live signal?
- Did the agent treat "founder" or "CEO" as the persona instead of classifying the job-to-be-done?
- Is the offer angle mapped to the recipient's actual workflow?
- Is there a proof path, or is the copy hiding an unsupported claim?
- Is the next action specific enough to learn from?

If any answer is weak, rebuild the campaign planner and signal cards. Do not iterate copy on top of a bad planner.

## Generic ICP Drift

If ICPs sound like broad market labels before they sound like actual customers:

- Stop public sourcing and rebuild the customer-consumer mining pass from Memory Store.
- Require cells tied to real seller customer/user patterns when available: paid customers, direct power users, internal dogfood users, passive workspaces, reactivation lists, public case studies, testimonials, reviews, customer logos, failed/thin accounts, or prior GTM plans.
- Treat labels such as "founder-led AI teams", "AI GTM teams", "CS/FDE/support", or "platform operators" as unfinished shorthand unless each has a source Memory Store pattern and a job-to-be-done.
- Use Exa/Websets to find the seller's customers/users when public, derive customer proxies when direct customer evidence is absent, expand a customer-derived pool, and verify account/person signals. Do not use Exa to invent a market from scratch when customer evidence exists.
- Keep Memory Store IDs in the ICP evidence fields. Do not treat a list of IDs as the customer usage map.
- Keep lead volume separate from send volume. Source broadly, score strictly, and send only rows that pass the planner gate and the approved quality-based ramp.

## Stale Or Conflicting Evidence

If sources conflict or are stale:

- Prefer the newest source only if it is authoritative.
- Flag the claim and fetch/verify before using it in copy.
- Avoid referencing exact dates, funding, hiring, or people changes unless verified.

## Scale Risk

For 1000-recipient campaigns:

- Require representative samples during setup before autopilot starts.
- Batch by ICP cell and sender.
- Keep exclusions and unsubscribes explicit.
- Record outcomes by batch before expanding.
- If deliverability or compliance risk is high, recommend a smaller pilot.
