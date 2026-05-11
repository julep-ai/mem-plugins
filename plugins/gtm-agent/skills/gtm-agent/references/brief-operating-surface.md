# Brief Operating Surface

Use this reference when deciding what should live in Memory Store briefs versus records, connector IDs, or local execution files.

## Principle

The GTM product surface is not a repo campaign folder. It is a small set of living Memory Store briefs that future agents can orient from.

```text
briefs = current operating truth
recall = evidence retrieval
record = confirmed learning and event stream
execution artifacts = temporary ledgers for running work
```

A folder, CSV, Webset, Gmail draft, monitor, or signal-card file is useful only when it helps execute or review a real run. It is not the canonical GTM state.

## Canonical GTM Briefs

Prefer updating a small number of briefs:

- **GTM Operating Brief** - what the GTM Agent is allowed to do, campaign modes, connector gates, approval gates, send policy, routine policy, and stop conditions.
- **ICP/Persona Brief** - current ICP cells, buyer/persona definitions, customer patterns that created each cell, excluded personas, unconventional bets, and evidence to recall.
- **Proof and Claims Brief** - approved public claims, private claims that cannot be used in outbound, customer stories, proof paths, demos, and taboo claims.
- **Campaign Learning Brief** - winning signals, dead signals, objections, copy lessons, channel lessons, proof paths, next experiments, and killed experiments.
- **Important Account/Relationship Brief** - only for accounts or partners that matter beyond one row or one touch.

Do not create separate briefs for every campaign, ICP experiment, reply, signal, source, account, or copy variant.

## What Belongs Where

| Need | Surface |
|------|---------|
| Current campaign policy | GTM Operating Brief |
| Current ICP/persona map | ICP/Persona Brief |
| Approved claims and proof | Proof and Claims Brief |
| Repeated campaign outcome pattern | Campaign Learning Brief |
| One reply, bounce, objection, or meeting | Memory Store record |
| One account or person researched | Webset row, signal card, or record |
| Gmail draft or send queue | Gmail / execution workspace |
| Webset/search/enrichment IDs | Websets plus a record when approved |
| Monitor IDs and cadence | Exa Monitor plus GTM Operating Brief if reusable |
| Batch review table | Temporary execution workspace |

## Planning Flow

For planning, produce a GTM operating profile, not a repo artifact by default:

```text
checkin
-> list/select 0-3 briefs
-> recall evidence behind the briefs
-> draft campaign operating profile
-> ask for approval on policy-changing decisions
-> record approved decisions
-> propose brief deltas only for reusable operating truth
```

The operating profile can be pasted in chat, recorded to Memory Store, or used to update briefs. Create a folder only when the user asks for local files, when the host needs a workspace for large batches, or when a connector export/import requires files.

## Execution Workspace

Use local files only as a working ledger:

- high-volume account review.
- CSV import/export.
- signal-card review queue.
- copy review before sending.
- send queue inspection.
- monitor/Webset specs before creation.
- handoff to a human or CRM.

The workspace should store IDs and summaries, not become a second memory system. After a run, record confirmed outcomes and update/propose brief deltas only when operating truth changed.

## Bad Repository Artifacts

Avoid committing seller-specific GTM plans, ICP universes, generated signal cards, draft copy, send queues, and event logs into the plugin repo. They age quickly and make the plugin look like one campaign instead of a reusable GTM engineering system.

Use examples only when they teach a reusable pattern. Prefer short schemas and reference examples over full campaign state.
