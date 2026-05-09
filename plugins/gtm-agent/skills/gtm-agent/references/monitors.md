# Exa Monitors

Use this reference when the campaign needs an always-on signal stream — new accounts entering an ICP, fresh launches in a category, recurring hiring/funding/news triggers, or competitor watch.

Monitors are a first-class production layer for GTM Agent. A campaign without monitors can still run one-off sourcing, but it is not always-on GTM. Mark it `monitoring_degraded` until monitor specs are approved and attached through an agent-run REST call, approved host automation, or another in-host routine. Dashboard setup is a last-resort fallback, not the normal user journey.

Monitors are **not exposed as MCP tools yet**. They run on the underlying Websets API. GTM Agent's job is to prepare the monitor spec, create it through REST when the user has approved API use and provided/authorized the Exa key, or emit an exact command the user can approve/run in the host. Only route to the Exa dashboard when the host cannot run the API call.

Do not POST monitor REST calls, create webhooks, or attach live monitor destinations unless the approved routine explicitly allows API creation and the user has provided or approved use of the Exa API key for that action. If approval or credentials are missing, keep the campaign in `monitoring_degraded` and output the smallest missing setup step.

## What a Monitor does

A Monitor re-runs a search against an existing Webset on a cron schedule. New verified results either append to the Webset (default) or replace prior ones (`override`). Monitors emit webhook events as items land, get enriched, or the run goes idle.

A Monitor is the right tool when:

- the search is repeated work, not one-shot research.
- the result set is meant to grow over time.
- timing matters and the user wants notifications.
- the same Webset will be scored, sent, or learned-from across batches.

A Monitor is the wrong tool when:

- the user just needs a one-off list (use Websets search directly).
- the search will fire more than once per day (Monitors hard-cap at one run per day).
- the cadence is event-triggered, not time-triggered (use webhooks on an existing Webset instead).

## High-Leverage Monitor Patterns

Apply these patterns to whatever the seller actually cares about; the categories are stable across sellers, the queries are not.

**ICP / target-pool monitors:**

- new entrants matching ICP cell criteria (e.g., new companies posting jobs that match a buyer profile, new properties matching a listing thesis, new public filings matching a vertical).
- buyer role changes — new VPs, founders, owners, decision-makers entering accounts on the watchlist.
- expansion signals — funding, hiring surges, new locations, geographic moves.

**Competitor monitors** (one per named competitor):

- changelog / release-notes / pricing page changes.
- new customer logos or case studies appearing on the competitor's site.
- competitor's public hiring page (what they hire reveals what they think they need next).
- public reviews on G2, Capterra, Trustpilot, Yelp, Reddit, HN, Glassdoor depending on category — flag negative reviews as objection-handling and copy-hook source.
- press mentions and conference appearances.

**Pain / objection monitors:**

- public complaints in forums, subreddits, review sites, or community Slack/Discord channels mentioning the pain the seller solves.
- "how do I" / "why does X keep" / "we tried X but" pattern monitors targeting buyer pain language.
- ex-customer signals — people publicly switching away from a competitor are pre-qualified leads if the seller honestly does it better.

**Channel / event monitors:**

- launch / event / sponsor lists for relevant industry events.
- newsletter or podcast guest lists overlapping the seller's ICP.
- regulatory or policy changes that create timing in the seller's vertical.

For each monitor: document the parent Webset ID, the cron + timezone, the entity type, the query, the count, the behavior (`append` vs `override`), the webhook destination if any, and the Memory Store thread the monitor reports into. Recurring competitor and pain monitors should usually run weekly anchored to a buyer-friendly timezone; ICP / target-pool monitors usually run daily in fast-moving categories and weekly in slow-moving ones.

## Required inputs

Before the user creates a Monitor, GTM Agent must know:

- `websetId` — the parent Webset that will receive new items.
- `query` — natural-language search, 2-10,000 chars, narrow enough to verify entity fit.
- `entity` — `company`, `person`, `article`, `research_paper`, or `custom`.
- `count` — positive integer; how many new items per run.
- `criteria` — optional, max 5 hard filters every result must pass.
- `behavior` — `append` (default) or `override`.
- `cadence` — valid 5-field Unix cron expression. Must trigger at most once per day.
- `timezone` — IANA timezone string. Defaults to `Etc/UTC` if omitted.
- `metadata` — optional key/value pairs for routing and learning.

## REST API

Authenticate with `Authorization: Bearer YOUR_EXA_API_KEY`. Endpoint:

```text
POST https://api.exa.ai/websets/v0/monitors
```

Sample request body:

```json
{
  "websetId": "webset_xxx",
  "cadence": {
    "cron": "0 9 * * 1",
    "timezone": "America/New_York"
  },
  "behavior": {
    "type": "search",
    "config": {
      "query": "AI GTM teams hiring sales engineer with explicit AI outbound mention",
      "entity": "company",
      "count": 25,
      "behavior": "append"
    }
  },
  "metadata": {
    "campaign_thread": "T-XXXXXX",
    "icp_cell": "ai-gtm-teams"
  }
}
```

Sample response (HTTP 201):

```json
{
  "id": "monitor_xxx",
  "object": "monitor",
  "status": "enabled",
  "websetId": "webset_xxx",
  "cadence": { "cron": "0 9 * * 1", "timezone": "America/New_York" },
  "behavior": { "type": "search", "config": { ... } },
  "lastRun": null,
  "nextRunAt": "2026-05-11T13:00:00Z",
  "metadata": { ... },
  "createdAt": "...",
  "updatedAt": "..."
}
```

Other endpoints (same auth):

- `GET https://api.exa.ai/websets/v0/monitors/{id}` — read.
- `PATCH https://api.exa.ai/websets/v0/monitors/{id}` — change cadence, query, status.
- `DELETE https://api.exa.ai/websets/v0/monitors/{id}` — remove.
- `GET https://api.exa.ai/websets/v0/monitors/{id}/runs` — run history.

## Manual fallback

Use this only when the host cannot run the REST call or the user explicitly wants UI setup. From a Webset detail page, attach a Monitor and pick cadence/query/behavior. Direct playground for new Websets:

```text
https://dashboard.exa.ai/playground/create-websets?q=<query>
```

## Webhook events

Subscribe a webhook on the parent Webset to react to monitor output:

- `webset.item.created` — new item passed verification.
- `webset.item.enriched` — an enrichment finished for a previously-created item.
- `webset.idle` — the run completed and no more items are pending.

Webhook secrets are shown once on creation. Store them immediately for signature verification.

## Cron patterns worth memorizing

```text
0 9 * * 1     Mondays 9am
0 13 * * *    daily 1pm
0 8 * * 1-5   weekdays 8am
0 7 * * 1,4   Mondays + Thursdays 7am
```

Cron must trigger at most once per day. Use timezone to anchor to the buyer's working window, not the user's.

## Spec output contract

When GTM Agent recommends a Monitor, output:

```text
creation_mode: agent_rest | host_automation | manual_dashboard_fallback
parent_webset_id:
query:
entity:
count:
criteria:
behavior:
cadence:
timezone:
webhook_events:
expected_signal:
expected_volume_per_run:
stop_conditions:
memory_thread_to_record:
```

Recommend monitors only after the user approved the parent Webset and one manual run produced acceptable signal quality. Manual-only first; auto-cadence second.

## Recording

After the user creates the Monitor, record to Memory Store:

- monitor `id`
- parent Webset `id`
- cadence, timezone, behavior
- expected signal type and ICP cell
- which campaign thread owns it
- planned learning cadence (how often to compare yields and update ICP confidence)

## Do Not

- Do not invent a `monitor_id`. Wait for the API or dashboard response.
- Do not set sub-daily cadence. Exa rejects it.
- Do not create monitors before a parent Webset exists and has produced acceptable items.
- Do not let monitors run silently — pair them with a webhook or a daily digest routine that reports yield, exclusion rate, and signal quality back to the user.
