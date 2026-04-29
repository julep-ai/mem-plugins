# Record templates

Memory Store's `record` is a quick-jot interface, not a typed event store. The store handles consolidation, deduplication, and cross-reference in the background. Your job is to write specific, well-named prose that future recalls can find and use.

## The API

`record` takes:

- **`content`** (required) — the primary memory to capture, written as natural-language prose.
- **`background`** (optional) — context that helps interpretation later: who, why, the state at the time.
- **`thread_id`** (optional) — pass the active thread from `checkin` so this run is grouped.
- **`when`** (optional) — temporal hint when the memory describes a different time than now.

Do not impose JSON schemas. Do not invent typed event names. Write what happened, in language that names the author, the piece, and the editorial moment, so a future `recall` can land on it.

## When to record

After every editorial outcome:

- The user **approves** a draft → record the approval and the final text.
- The user **rejects** a draft → record the rejection and the reason.
- The user **edits** a draft → record the original, the edit, and what the change reveals.
- The user **posts** → record the published text and the URL.
- The user reports **performance** → record the metrics and whether the goal was hit.

Also record any signal that should change future drafts:

- A new **banned word or phrase** the author refused.
- A new **defensible view** the author stated.
- A **customer name approved** for public mention.
- A new or refreshed **voice profile** from the bootstrap flow.

## Style rules

- Write the jot like a colleague briefing the next person on the team. Not a log line. Not JSON.
- Always name the **author**, the **pillar/topic**, and the **moment**.
- Quote the user's exact words where you can. Paraphrase only when you must.
- Be specific. "User edited the hook" is useless. "User replaced the contrarian opener with a customer-quote opener because the original 'felt preachy'" is searchable.
- Always pass the active `thread_id` from `checkin`.

## Templates

Adapt these to the situation; the angle brackets are placeholders. Replace `<author>` with the actual person whose voice is being used.

### Draft approved

`content`:

> `<author>` approved a LinkedIn draft for the `<pillar/topic>` pillar today. Format: `<customer_story | user_insight | shipped_work | founder_pov | objection>`. Hook framework: `<framework name>`. The approved text follows verbatim:
>
> `<full post text>`
>
> Source memories used: `<memory IDs separated by commas>`.

`background`:

> `<Primary goal the user named for this piece, if any — saves, meaningful comments, inbound DM, profile visits, named awareness. Any other context about why this draft worked.>`

### Draft rejected

`content`:

> `<author>` rejected a LinkedIn draft variant for the `<pillar>` pillar today. The user's reason, in their own words: "`<reason>`". Suggested fix from the user: `<fix or "none given">`. The rejected variant for reference:
>
> `<variant text or short summary>`

`background`:

> `<Format and hook framework that failed. Any pattern this rejection signals — for example "second time this month a question-hook got cut as engagement bait".>`

### Draft edited

`content`:

> `<author>` edited a LinkedIn draft for the `<pillar>` pillar today. Original draft:
>
> `<original text>`
>
> Edited version the user prefers:
>
> `<edited text>`
>
> What changed and why, as best you can read it: `<one-line edit summary>`.

`background`:

> `<If the edit reveals a voice signal — a phrase preferred, a phrase avoided, a rhythm change, a structural rule — name it explicitly so future recall lands on it.>`

### Post published

`content`:

> `<author>` published a LinkedIn post for the `<pillar>` pillar at `<ISO timestamp>`. URL: `<url>`. The published text:
>
> `<full text>`
>
> Stated primary goal: `<saves | meaningful comments | inbound DM | profile visits | named awareness>`. Format: `<format>`. Hook framework: `<framework>`.

`background`:

> `<Posted day and hour. Any context that could correlate with performance — has_numbers, mentions an anonymized customer, length, etc.>`

### Post performance (24h, then 7d)

`content` (24h):

> Performance for `<author>`'s `<pillar>` LinkedIn post 24 hours after publishing. URL: `<url>`.
>
> Impressions: `<n>`. Likes: `<n>`. Comments: `<n>` (meaningful, 15+ words: `<n>`). Saves: `<n>`. Shares: `<n>`. Inbound DMs: `<n>`. Profile visits: `<n>`.
>
> Outcome against the stated primary goal of `<goal>`: `<hit | partial | missed>`.
>
> Notes: `<which comments stood out, who reached out, anything else worth keeping>`.

`content` (7d): same shape, swap `24 hours` for `7 days`.

`background`:

> `<Optional hypothesis for why it performed or did not, anchored in the post's context tags.>`

### Voice rule update

`content`:

> Voice rule update for `<author>`: `<one-line rule, e.g. "always uses em-dashes, never parentheses" or "never opens posts with a rhetorical question">`. Source: `<the moment this rule came from — an edit, a comment, a stated preference>`. Scope: `<linkedin only | all channels>`.

### Banned phrase added

`content`:

> Banned phrase for `<author>` in LinkedIn drafts: "`<exact phrase>`". Reason: `<one line>`. Applies to all future drafts.

### Customer approved for public use

`content`:

> Customer "`<name or memory ID>`" approved by `<who confirmed it, when>` for public mention in `<author>`'s LinkedIn posts. Scope: `<all posts | this pillar only | this specific piece>`. Future drafts may name this customer without anonymization.

### Brand profile created

Record when a company brand profile is bootstrapped from scratch. See [brand-bootstrap.md](brand-bootstrap.md) for the extraction flow.

`content`:

> Brand profile created for `<company>` via `<assets | interview | hybrid>`. Source memory IDs: `<ids or "none — pasted text only">`. Profile:
>
> - Company name: `<name>`
> - One-line positioning: `<one falsifiable sentence>`
> - ICP: `<role + company size + industry + pain>`
> - Pillars this quarter: `<comma-separated list of 3–5>`
> - Defensible category view: `<one line — the thing the company argues about the category>`
> - Anti-positioning: `<one line — what the company refuses to be compared to>`
> - Approved claims: `<list of customer names, metrics, and category claims cleared for public mention>`
> - Taboo topics: `<list of topics off-limits for public posts>`
>
> Confirmed by user: yes. Profile completeness: `<full | partial>`. Missing dimensions: `<list or "none">`.

### Brand pillar update

Record when a pillar is added, removed, or reframed.

`content`:

> Brand pillar update for `<company>`: `<change — "added pillar X", "dropped pillar Y", "reframed Z as …">`. Reason: `<one line>`. Previous pillars: `<list>`. New pillars: `<list>`. Effective for future drafts starting: `<date or "immediately">`.

### Approved claim added

Record when a specific metric, customer name, quote, or category claim is cleared for public mention.

`content`:

> New approved public claim for `<company>`: "`<exact claim or wording>`". Evidence or source: `<memory ID, document, or person who confirmed>`. Scope: `<all posts | specific pillar | one-time for piece <piece_id>>`. Future drafts may use this claim without flagging for approval.

### Taboo topic added

Record when a topic is placed off-limits for public posts.

`content`:

> New taboo topic for `<company>` posts: `<topic or named entity>`. Reason: `<one line — legal, competitive, customer sensitivity, internal-only, etc.>`. Scope: `<all posts | LinkedIn only>`. Applies until: `<date or "until revoked">`.

### Voice DNA created

`content`:

> Voice profile created for `<author>` via `<samples | interview | hybrid>`. Sample memory IDs: `<ids or "none — pasted text only">`. Profile:
>
> - Signature phrases: `<comma-separated list>`
> - Banned phrases: `<list>`
> - Rhythm: `<one line>`
> - Positioning: `<one falsifiable line>`
> - Audience: `<role + context + frustration>`
> - Claim boundaries: `<one line>`
> - Defensible views: `<list>`
>
> Confirmed by user: yes. Profile completeness: `<full | partial>`. Missing dimensions: `<list or "none">`.

## What not to record

- **Performance numbers the user did not confirm.** If you do not have the metric, do not invent it.
- **Drafts the user never saw.** Only record what was actually presented.
- **Outcomes inferred from silence.** If the user did not respond, the run did not produce an editorial outcome — do not record one.
- **Voice rules attributed to the wrong author.** Voice is per-author unless the user explicitly says company-wide.
- **Internal-only memories** quoted into the public draft record.
- **Composite quotes.** If a quote did not come from a memory verbatim, do not record it as a quote.
