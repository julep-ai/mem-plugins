# Failure Modes

Use this reference when a GTM run is blocked, low-confidence, or unsafe to execute.

## Memory Store MCP Unavailable

Do not run a memory-native GTM campaign if Memory Store is unavailable.

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

For Exa Search MCP:

```bash
codex mcp add exa --url https://mcp.exa.ai/mcp
```

For Websets MCP:

```text
https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY
```

## Gmail Missing

If Gmail is missing:

- Output ready-to-import drafts and followup timing.
- Do not claim emails were sent, scheduled, labeled, or threaded.
- Keep recipient data in a reviewable table or CSV-shaped output.

## No Explicit Send Approval

If the user asks for a campaign but does not explicitly approve sending:

- Stop at draft/review queue.
- Show representative copy.
- Ask for approval before any external action.

## Low Signal Quality

If most accounts only match static firmographics:

- Mark the batch as research-only.
- Recommend more precise ICP cells or stronger trigger sources.
- Do not move the batch to send-ready.

## Stale Or Conflicting Evidence

If sources conflict or are stale:

- Prefer the newest source only if it is authoritative.
- Flag the claim and fetch/verify before using it in copy.
- Avoid referencing exact dates, funding, hiring, or people changes unless verified.

## Scale Risk

For 1000-recipient campaigns:

- Require representative samples before send.
- Batch by ICP cell and sender.
- Keep exclusions and unsubscribes explicit.
- Record outcomes by batch before expanding.
- If deliverability or compliance risk is high, recommend a smaller pilot.
