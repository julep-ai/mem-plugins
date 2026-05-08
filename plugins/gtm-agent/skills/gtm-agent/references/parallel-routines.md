# Parallel Routines

Use this reference when the user wants speed, background agents, recurring work, or a self-evolving GTM loop.

## Parallelization

Split independent work aggressively:

- one worker per ICP cluster for research
- one worker per signal family for monitor design
- one worker per Websets batch for sourcing/enrichment
- one worker per account batch for evidence cards
- one worker per copy angle for variant generation
- one worker for Gmail reply/followup inspection
- one worker for Memory Store learning synthesis

The main agent should orchestrate and merge. It should not ingest raw search dumps or 1000 account rows into main context.

## Worker Output Contract

Each worker should return:

- scope
- sources used
- count processed
- top findings
- excluded items and why
- risks
- recommended next action
- file or Webset/monitor ID if applicable

No raw dumps unless the user asks.

## Thread Mapping

Every durable routine should map to Memory Store thread/context:

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

## Routine Types

Promote repeated work into routines:

- daily industry scan
- weekly ICP refresh
- funding/news monitor
- hiring monitor
- competitor-changelog monitor
- GitHub/docs activity monitor
- Websets enrichment refresh
- Gmail followup check
- reply/objection learning summary
- suppression list update
- campaign postmortem

For Exa Monitors, create or propose monitors only after the user approves query, cadence, output schema, and destination. Use manual-only monitors first when uncertain.

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
