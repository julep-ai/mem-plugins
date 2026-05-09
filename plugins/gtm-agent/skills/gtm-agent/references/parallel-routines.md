# Parallel Routines

Use this reference whenever the campaign can be decomposed into independent work. GTM Agent should push as much work as possible into bounded background agents or host workers, then merge compact artifacts. Use [automation-routines.md](automation-routines.md) when repeated parallel work should become a scheduled host automation.

## Core Rule

Default to parallel execution.

The main agent owns the campaign planner, dependency graph, approvals, merge, and final recommendation. Background agents own bounded slices: ICP research, signal discovery, Websets batches, account evidence cards, buyer discovery, copy variants, Gmail inspection, Calendar context, monitor specs, and learning synthesis.

Do not make the main agent read raw search dumps, full inboxes, or 1000-row lead lists. Workers should return compact scored artifacts, links, IDs, files, and uncertainty notes.

## Spawn Decision

Spawn background agents when work is:

- independent from the next blocking decision.
- naturally partitioned by ICP cell, signal family, account batch, Webset, geography, persona, copy angle, or connector.
- likely to return compact structured output.
- expensive in search, enrichment, or reading.
- reusable as a future routine.

Keep work local when it is:

- the immediate critical-path blocker.
- a policy/approval decision the user must make.
- a merge or conflict-resolution step.
- a send/delete/schedule action with external side effects.
- too ambiguous to scope safely.

## Dependency Graph

Use this dependency order:

```text
checkin
  -> setup packet / approved policy
  -> campaign planner
  -> parallel ICP and signal research
  -> parallel Websets / Exa lead batches
  -> parallel people search
  -> parallel evidence cards
  -> merge + score + exclusion pass
  -> parallel copy variants for send-eligible rows
  -> review gate
  -> Gmail send/followup workers inside policy
  -> engagement inspection workers
  -> learning synthesis
  -> scheduled routines
```

Only send/follow up after setup approval. Research, sourcing, enrichment, evidence cards, draft generation, and monitor specs can run before send approval only when the needed connector gates pass. Draft generation requires authenticated Exa/Websets evidence rows, planner gates, private-context policy, and connector scope; Gmail absence may produce import-ready drafts only when Gmail is the only execution gap.

## Workstream Matrix

Use this matrix when building the work plan:

| Workstream | Parallel key | Worker output | Merge key | Can become routine |
| --- | --- | --- | --- | --- |
| ICP research | ICP cluster | ICP cell, buyer, pain, trigger, exclusions | ICP cell name | yes |
| Signal discovery | signal family | signals, source URLs, confidence, query notes | domain + signal URL | yes |
| Websets sourcing | Webset or ICP batch | Webset/search IDs, counts, false positives, top rows | Webset ID + domain | yes |
| Lead generation | micro-vertical | CSV/JSON path, accepted count, rejected count, reasons | normalized domain | sometimes |
| People search | account batch | buyer candidates, titles, sources, risk | domain + person URL | no |
| Evidence cards | account batch | send-ready/research/exclude rows | normalized domain + persona | no |
| Copy variants | copy angle | variants, hypothesis, risk, recommended variant | account + persona + angle | no |
| Gmail scan | campaign label/thread batch | replies, bounces, suppressions, owner actions | Gmail thread ID | yes |
| Calendar context | qualified replies | availability/context summary, conflicts, no action | Gmail thread ID | yes |
| Monitor design | signal family | monitor spec, cadence, schema, destination | monitor name | yes |
| Learning synthesis | batch or routine | confirmed learnings and record proposals | Memory Store thread | yes |

## Worker Contract

Worker contract is elastic. Tier the shape to the work, not the other way around.

### Prompt (main agent → worker)

Minimum required:

```text
role:
scope:
inputs:
tools_allowed:
output_schema:
```

Add when work crosses approval boundaries, batch processes large volumes, or interacts with external connectors:

```text
campaign_context:        # active campaign thread, ICP cell, prior learnings
approved_policy:         # send ramp, exclusions, taboo claims, suppression rules
tools_forbidden:         # tools the worker must not call
quality_gate:            # signal card requirements, scoring thresholds
stop_conditions:         # when to abort and return partial results
```

### Return (worker → main agent)

Minimum required, all workers:

```text
scope:
top_findings:
output_artifact:
recommended_next_action:
```

Add when work is a batch (Websets, lead-gen, evidence cards, copy variants):

```text
sources_used:
count_processed:
accepted:
rejected:
risks:
dedupe_keys:
```

`output_artifact` is a path inside the campaign folder (`campaigns/<slug>/...`), a Webset/search/enrichment ID, a Gmail draft ID, or a monitor ID. No raw dumps in the return. The main agent reads from the artifact, not from the worker's text.

### Recording is the main agent's job

Workers do not flag what to record to Memory Store. The main agent decides what is durable learning **after** merge — which ICP confidence shifted, which copy angle won, which signal source paid off, which objection pattern repeated. Then it calls Memory Store `record` with the active campaign `thread_id`. Use Memory Store comprehensively; just record from the layer that sees the whole picture.

## Merge Protocol

The main agent merges workers in this order:

1. Normalize domains, person URLs, Gmail thread IDs, Webset IDs, and Memory Store thread IDs.
2. Dedupe by normalized domain first, then company name aliases, then source URL.
3. Preserve source URLs and worker confidence notes.
4. Prefer fresher authoritative sources over older scraped summaries.
5. Resolve conflicting evidence by marking the row `research_more`, not by averaging.
6. Apply exclusions: customers, competitors, do-not-contact, bounces, unsubscribes, active threads, low-confidence data.
7. Promote rows only when they pass the signal card gate.
8. Keep weak rows in `watch`, `research_more`, or `exclude`.

## Quality Gates

No row becomes send-ready unless it has:

- why this person.
- why now.
- signal source URL or Memory Store ID.
- persona.
- offer angle.
- proof path.
- next action.
- confidence.
- exclusion risk.

No worker may send, delete, archive, bulk-label, create calendar events, call Memory Store `record`, or change a live monitor unless the approved policy explicitly allows it. Even when `record` is allowed by policy, the main agent should own durable learning after merge.

## Concurrency Guidance

Start wide on research, narrow on execution:

- Setup and planning: 2-4 side workers maximum.
- ICP and signal research: 5-20 workers depending on requested scale.
- Websets and lead-gen batches: one worker per ICP cell or micro-vertical, but report only summaries and artifacts.
- Copy variants: one worker per angle or persona after evidence gates pass.
- Gmail and Calendar: keep conservative, usually one worker per campaign label/thread batch.
- Learning synthesis: one worker after results exist.

When connector limits, API quotas, or mailbox health are uncertain, cap concurrency and output the worker plan rather than pretending the work ran.

## Failure Handling

Workers should fail small:

- If Exa is missing, return exact queries and required tool setup.
- If Websets is missing, return Webset specs and imports/enrichments.
- If Gmail is missing, return draft/import-ready queues only after Exa/Websets evidence and planner gates pass.
- If Calendar is missing, keep demo-link CTA and mark calendar automation disabled.
- If a worker times out or returns low confidence, mark its slice `incomplete` and keep the campaign moving with other slices.
- If two workers disagree, preserve both sources and route to `research_more`.

## Thread Mapping

Every durable worker or routine should map to Memory Store thread/context:

```text
campaign thread
  ICP thread
    Webset ID
    Monitor IDs
    account batch IDs
    Gmail thread IDs
    learning records
```

Use thread IDs in record background when available. This is how the system learns per ICP, per account, per copy angle, and per monitor.

## Routine Promotion

Promote repeated work into routines:

- daily industry scan
- weekly ICP refresh
- funding/news monitor
- hiring monitor
- competitor-changelog monitor
- GitHub/docs activity monitor
- Websets enrichment refresh
- Gmail reply scan every 2 hours
- Gmail followup check
- Google Calendar booking-context check for qualified replies
- daily campaign digest
- weekly ICP/signal/copy learning summary
- reply/objection learning summary
- suppression list update
- campaign postmortem

For Exa Monitors, create or propose monitors only after the user approves query, cadence, output schema, and destination. Use manual-only monitors first when uncertain.

For full autopilot, create routines only after the setup packet is approved. Autopilot routines may keep researching while paused, but they must not send if a stop condition is active. Every scheduled routine should carry the exact routine spec from [automation-routines.md](automation-routines.md).

## Self-Evolving Loop

After every batch or routine:

1. Summarize what changed.
2. Compare against prior Memory Store learnings.
3. Update ICP confidence.
4. Update signal quality.
5. Update copy angle confidence.
6. Add suppressions.
7. Recommend next experiment.
8. Record confirmed learnings to Memory Store.

This is the compounding loop: search creates evidence, outreach creates outcomes, Memory Store makes the next search and message smarter.
