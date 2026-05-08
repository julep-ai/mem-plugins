# Failure Modes

Use this reference when a GTM run is blocked, low-confidence, or unsafe to execute.

## Memory Store MCP Unavailable

Do not run a memory-native GTM campaign if Memory Store is unavailable.

GTM Agent expects Memory Store MCP to come from the installed `memory-store@mem-plugins` plugin or an existing host-level Memory Store connector. It intentionally does not redeclare Memory Store MCP in its own `.mcp.json`, because that can force a second auth prompt.

Fallback:

- Say Memory Store MCP is unavailable.
- Ask for pasted company context or continue with a clearly ungrounded draft.
- Do not claim the system learned.
- Do not record anything unless `record` becomes available.

## Empty Or Thin Recall

If recall lacks product, ICP, customer language, or approved claims:

- Infer only from public sources and label confidence.
- Ask for the smallest missing blocker: product, ICP, existing customers, exclusions, sender, or send policy.
- Prefer a small pilot batch over a 1000-recipient plan.

## Exa Or Websets Missing

If Exa/Websets tools are missing:

- Produce exact search queries, Websets criteria, enrichments, and batching plan.
- Tell the user which MCP to connect.
- Do not fabricate lead lists.
- If only `web_search_exa` appears, treat the Exa surface as exploratory research only. Deep lead generation and source fetching still require `deep_search_exa`, `web_search_advanced_exa`, or `web_fetch_exa` to be exposed by the host.

For Exa Search MCP:

```bash
codex mcp add exa --url https://mcp.exa.ai/mcp
```

For Websets MCP:

```bash
codex mcp add websets --url "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
```

GTM Agent also declares this Websets placeholder in `plugins/gtm-agent/.mcp.json`; the user still has to replace `YOUR_EXA_API_KEY` in host MCP settings because the plugin cannot safely ship a real Exa key.

## Gmail Missing

If Gmail is missing:

- Output ready-to-import drafts and followup timing.
- Do not claim emails were sent, scheduled, labeled, or threaded.
- Keep recipient data in a reviewable table or CSV-shaped output.
- Mark full autopilot sending disabled until Gmail is connected.

## Google Calendar Missing

If Google Calendar is missing:

- Keep the confirmed demo link usable.
- Mark scheduling automation disabled.
- Do not claim availability was checked or events were created.

## Setup Not Approved

If the user asks for autonomous GTM but the setup packet is not approved:

- Route to `campaign-setup`.
- Show representative copy and send criteria.
- Do not send until setup approval covers sender, CTA, ICPs, claims, ramp, stop conditions, and connector gaps.

After setup approval, per-batch approval is not required unless the approved policy says draft-first.

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
