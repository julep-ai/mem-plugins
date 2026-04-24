# Format templates

Five formats that perform on LinkedIn. Each template shows the structure and a filled example. Use these as scaffolding, not fill-in-the-blank output — the post must sound like the author, not the template.

Every template ends with the same anonymization convention for customer references.

## 1. Customer story

**When:** a memory shows a customer moving from a before-state to an after-state with a concrete turning point.

**Structure:**

```
[Dramatic moment or time-bound hook]

[One-line setup: who the customer is, anonymized if needed]

Before: [old workflow, what hurt about it]
Turning point: [the moment something changed — a conversation, a shipped feature, a new process]
After: [new state, ideally with a specific outcome]

The lesson: [one sentence; why this matters beyond the customer]

[CTA: a specific question inviting the reader's version of the same arc]
```

**Filled example (anonymized):**

```
"We need to pull the integration tomorrow."

That was the subject line at 2:13 AM on a Tuesday.

Before: a B2B infra team was piping errors into three dashboards and still missing the ones that mattered.
Turning point: they started recording every false-positive back into one memory — what fired, why, who dismissed it.
After: their on-call noise dropped 63% in eight weeks. No new tool. One feedback loop.

The lesson: the signal you need is already in your team's dismissals. You just have to write it down.

What is the last alert you dismissed that mattered?
```

## 2. User insight

**When:** a repeated pattern shows up across customer memories — a pain, a workaround, a question.

**Structure:**

```
[Pattern hook: the non-obvious thing customers are telling you]

[Three bullets: concrete instances, each with its own specificity — role, workflow, or moment]

What this says about [category]: [one-line category-level takeaway]

What [company] is doing about it: [one line — shipped work, in-progress change, or stance]

[CTA: ask readers in the same role for their version]
```

**Filled example:**

```
Sales leaders are not asking us for "AI." They are asking us to stop losing context between calls.

Three versions of the same ask in the last month:
- A VP Sales who rewrites her CRM notes after every demo because "the AI summary is too generic to forward."
- A founder who copy-pastes Slack threads into a doc before his QBRs because "the meeting tool loses the jokes that were the reason they liked us."
- A CS lead who still writes her own handoff notes because "the auto-ones lose the one thing the customer actually said yes to."

What this says about the category: context is not a summary problem. It is a retention problem.

What we are doing: we record the moments your team flags as the ones that mattered, not the ones a generic summarizer thinks mattered.

What is one thing you still write by hand because the tools lose it?
```

## 3. Shipped work

**When:** the team shipped something worth telling the audience about.

**Structure:**

```
[Mini case-study hook or unexpected-number hook]

What shipped: [one line — what, for whom]

Why it exists: [one line — the customer or team pain that forced it]

Who asked for it: [name the customer pattern or internal observation, anonymized]

What changes for the user: [two or three bullets, concrete]

What we are watching next: [one line — the next question this opens]

[CTA: invite the reader to try it or to name what they would want next]
```

**Filled example:**

```
We shipped memory-scoped access control this week. A customer onboarded their sales team in 47 minutes after three weeks of waiting.

What shipped: per-department memory scopes with role-based access.

Why it exists: teams were either over-sharing every memory or hiding everything and losing the value.

Who asked for it: a YC-backed team where Sales and Engineering needed the same memory store but could not legally see each other's customer notes.

What changes for you:
- Memories can belong to a department, not just a person.
- Access is role-first; onboarding is one config.
- Cross-department recall is explicit, not accidental.

What we are watching next: whether this pushes teams toward department-specific agents instead of one global one.

If you have a team memory store, how are you handling cross-department access today?
```

## 4. Founder POV

**When:** the founder holds a defensible view backed by customer or shipped-work evidence.

**Structure:**

```
[Uncomfortable-truth or unopular-opinion hook — one line]

[Two or three lines expanding the view: what you believe and why the mainstream disagrees]

Evidence: [one to three concrete observations, each anchored in a customer interaction, shipped feature, or measurable change — anonymized]

Practical implication: [one line — what a reader should do differently on Monday]

[CTA: invite disagreement, not agreement]
```

**Filled example:**

```
Most B2B content is written to be admired, not to be used.

It reads well, gets likes, and helps nothing. I wrote like this for a year before I noticed the saves were flat and the DMs were all from peers, not buyers.

Evidence from the last 30 days:
- Our top-saved post was a 1,400-character teardown of a single customer's onboarding arc.
- Our most-commented post was a founder-voice piece with a specific, defensible claim.
- Our "thought leadership" listicle — the one I was proudest of — did nothing.

Practical implication: if your last five posts were not used by anyone, write one a buyer could forward to their team.

Where do you disagree?
```

## 5. Objection

**When:** a memory captures a repeated customer concern that is reasonable and worth addressing publicly.

**Structure:**

```
[Question-everyone-is-asking hook]

The concern: [one line, stated fairly — steelman it]

Why it is reasonable: [one or two lines — acknowledge the legitimate fear]

How we think about it: [two or three lines — the company's actual stance, not a deflection]

What this means for you: [one line — the practical takeaway]

[CTA: invite the reader's version of the concern]
```

**Filled example:**

```
"Why would I hand my customer conversations to a memory system?"

The concern: handing raw customer context to a third-party is a trust and compliance bet, especially for regulated teams.

Why it is reasonable: if the system can read everything, the blast radius of a misconfiguration is the whole team's trust with customers.

How we think about it:
- Memories are scoped by department and role by default, not globally readable.
- Every recall call is logged and auditable.
- Redaction runs before storage for the fields your team marks as sensitive.

What this means for you: the right question is not whether to trust the tool; it is whether your team's access model is explicit enough to make the trust question answerable.

What would make you comfortable enough to try?
```

## Anonymization convention

Unless a memory says a customer name is approved for public use:

- Use a neutral descriptor: "a YC-backed B2B infra team", "a 40-person sales org", "an enterprise CS lead".
- Keep enough specificity that the story is not generic: role + industry + size is usually enough.
- Do not invent or generalize details that are not in the memory. If the memory only says "a customer", the post says "a customer".
- When quoting, quote only what the memory quotes. Paraphrase is fine; invented quotes are not.
- If the author wants to name the customer, call `record` to mark that specific customer as publicly approved for future runs.

## Picking a format

| The memory contains... | Use this format |
| --- | --- |
| A specific customer arc with a turning point | Customer story |
| A repeated pattern across several customer memories | User insight |
| Something the team just shipped or updated | Shipped work |
| A founder-held belief with evidence | Founder POV |
| A customer concern that keeps coming back | Objection |

If a candidate does not cleanly fit one of the five, it probably is not sharp enough to post. Drop it.
