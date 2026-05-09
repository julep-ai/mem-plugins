# Copy And Sequences

Use this reference when drafting outbound copy, followups, Gmail drafts, or campaign variants.

Drafting starts only after the campaign planner gate passes. If the signal card does not have `why this person`, `why now`, source, persona, customer-story/persona pattern, offer angle, proof path, next action, learning intent, confidence, and exclusion risk, do not compensate with smoother copy. Return the missing fields and the research needed.

For Memory Store-built offers, choose the sender and offer profile from the campaign planner. For Memory Store core, Shubham as technical founder/operator and "Agents have amnesia. A wiki will not fix it." may be right. For GTM Agent, briefs, customer insights, context engineering, or future distribution plugins, the copy must use that offer's own angle and proof path.

Default CTA is a clear next step tied to the signal and persona. Avoid lazy asks such as "open to me sending a teardown?" when the email has not earned the ask. Use a useful concrete offer: a short teardown, a specific example, a founder-to-founder note, a relevant customer-pattern readout, or a direct call ask for high-intent rows. Do not use a discovered demo link before it is confirmed once in campaign setup.

## Variant Model

For each recipient/account, create five candidate variants with distinct jobs:

1. **Trigger-led** - opens with the timely signal and why it matters.
2. **Pain-mirror** - mirrors the prospect's likely pain using Memory Store customer language.
3. **Customer-story/peer-pattern** - uses an approved customer, segment, or remembered pattern as proof. Flag unapproved proof.
4. **Insight-led** - offers a concrete observation or contrarian view about their situation.
5. **Founder/operator-led** - introduces the sender's credible role and why this pattern matters to them without making the email about the sender.

Pick one recommended first-touch variant. Do not send all five variants to the same person unless the user explicitly asks for a multi-touch experiment.

## Personalization Stack

Personalize from strongest to weakest evidence:

- **Direct memory** - prior meeting, Slack thread, customer note, CRM fact, or approved account history.
- **Direct public signal** - source URL with recent event, launch, hiring, funding, post, or docs change.
- **Approved customer story or persona pattern** - a remembered usage pattern, objection, segment, or outcome that explains why this prospect's persona should care.
- **Role-specific pain** - buyer owns a known workflow or problem.
- **Segment-level pattern** - similar companies show the same issue.
- **Generic category claim** - use only if everything else is thin; flag low confidence.

Never imply personal familiarity from weak evidence.

## First Touch Shape

Keep cold email short:

- Subject: 2-6 words, concrete, tied to the prospect's signal or persona. Avoid vague subjects such as "context layer for your agent workflows."
- Line 1: the live signal and why it makes this touch timely.
- Line 2: why people in this persona/use case have found the underlying product useful, grounded in approved customer-story or segment evidence.
- Line 3: the offer angle and proof path relevant to that persona.
- Line 4: a concrete ask or useful next step that matches the signal; no filler CTA.

Use one idea per sentence. Avoid bloated claims, fake urgency, and "hope you are well" filler unless matching the sender's known voice.

## Sender Credibility

If the sender is a founder, founding engineer, or operator, say that plainly when it improves trust:

- "I'm Shubham, one of the people building Memory Store."
- "I'm a founding engineer working on the memory layer behind this."
- "We've been seeing this pattern with teams using agents across Slack, meetings, and coding tools."

Do not over-index on biography. The sender line should support the prospect's problem, not replace the signal.

## Bad Copy Patterns

Reject drafts that:

- open with a generic category claim instead of the prospect's signal.
- use a generic subject line that could fit anyone.
- ask permission to send value instead of giving a useful concrete observation.
- mention a customer story without approval or without mapping it to the recipient's persona.
- describe Memory Store as generic memory, RAG, CRM, or "AI-powered" anything when that flattens the offer.
- use the same words for LinkedIn and email touches.
- lack an explicit experiment hypothesis for what this copy is testing.

## Channel-Specific Copy

For email plus LinkedIn:

- Email carries the fuller signal, proof path, and concrete ask.
- LinkedIn should be shorter, conversational, and anchored to the same high-intent signal.
- Do not paste the same body into both channels.
- Track the same person across both channels and label the experiment `email_only`, `linkedin_only`, or `email_plus_linkedin`.

## Followup Sequence

Default sequence after the first touch:

- **Followup 1, 3-4 business days later:** add one new piece of evidence or clarify relevance.
- **Followup 2, 6-8 business days later:** offer a concrete asset, demo path, or useful teardown.
- **Breakup, 12-15 business days later:** politely close the loop and ask who owns the problem if not them.

Stop or reroute on replies, bounces, unsubscribes, objections, meeting booked, or do-not-contact signals.

## Gmail Safety

When Gmail is available:

- Before setup approval, draft first and do not send.
- After setup approval, autopilot may send inside the approved ramp and stop conditions.
- Preserve exact recipients, subjects, and thread context.
- Use reply threads for followups when a conversation exists.
- Do not mass-send from a generated batch before setup approval, representative samples, and send criteria are approved.
- Report assumptions and missing fields before asking the Gmail connector to act.

## Media And Screenshots

Default to text-first outreach:

- Do not attach screenshots by default.
- Collect screenshots, product images, diagrams, or proof assets as optional proof paths when discovered.
- Use an attachment or screenshot only when it materially improves the CTA and the user approved the media policy during setup.

## Copy Checklist

Before presenting copy, verify:

- The signal card is complete enough to justify a draft.
- The persona is specific; "founder" alone is not enough.
- The first sentence has a real reason to engage now.
- The offer is specific to the recipient's likely job.
- The customer-story/persona pattern is approved or kept internal.
- Every claim is sourced or flagged.
- The ask is concrete, useful, and not a lazy permission ask.
- The copy does not expose internal-only Memory Store context.
- The variant label and hypothesis are explicit enough to learn from later.
