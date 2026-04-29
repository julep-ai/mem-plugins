# Annotated example posts

Six examples. Three good, three that fail in ways this skill is likely to fail. Read these before presenting drafts.

Examples use varied industries and author roles — B2B SaaS founder, services agency owner, indie consultant — so you can see how the same structures adapt. The specifics in each example are illustrative; your drafts should use your own company's memory, not these.

## Good 1 — B2B SaaS: customer story with a dramatic hook

Author: founder of a B2B observability startup. Audience: infra-team leads at 50–500 person companies.

```
"We need to pull the integration tomorrow."

That was the subject line at 2:13 AM.

An infra team had spent three weeks wiring our alerting into their on-call loop. The pager kept firing on false positives and their rotation was done pretending otherwise.

We asked one question: what do you do when you dismiss an alert?

Turns out they already had the answer — in the Slack replies and the retro docs nobody fed back into the alerting system.

We logged every dismissal as its own record, tagged with who dismissed it and why. Two weeks later the on-call noise dropped 63%. No model change. No new rules. One feedback loop nobody had closed.

The lesson is not "use our tool." The lesson is: the signal you need is almost always already written down by the person closest to the problem. You just have to keep it.

What is the last alert you dismissed that mattered?
```

**Why it works:**

- Hook: dramatic-moment framework; first two lines under 200 characters; opens with stakes.
- Specificity: concrete numbers (63%, two weeks, 2:13 AM), concrete workflow (Slack replies, retro docs).
- No product pitch in the first 1,000 characters; the tool is incidental to the lesson.
- CTA asks for the reader's version of the arc, not a vibe check.
- Ends with a saveable takeaway, which is what the 2026 algorithm rewards.

**Depth Score forecast:** high save rate, comments likely to be specific (people will name their own dismissed alerts).

## Good 2 — Services agency: founder POV with teeth

Author: founder of a five-person creative services agency. Audience: founders and CMOs who have burned on agency relationships before.

```
Most agency pitch decks are written to win the meeting, not the work.

I wrote ours like this for two years. We booked meetings. We closed maybe one in four.

Three things I changed:

- I stopped promising strategies and started attaching the last brief we shipped that looked like theirs.
- I stopped ending with "let's talk" and started ending with a 15-minute teardown of one thing on their current homepage they could fix without us.
- I stopped counting meetings booked and started counting meetings where the prospect asked when we could start.

Close rate went from 22% to 61% over six months. Same team. Same pricing. Different pitch.

If your last five pitches did not win the work, try sending the thing you would have done in week one before they sign. The people who hire you are the people who can picture it.

Where do you disagree?
```

**Why it works:**

- Hook: uncomfortable-truth; defensible claim from someone with standing.
- Body has three specific changes, each testable against the reader's own behavior.
- Numbers are real-shaped (22% → 61%, six months) and sourced to the author's own book of business.
- CTA invites disagreement, which generates longer comments than agreement does.

## Good 3 — Indie consultant: shipped-work post that is not a changelog

Author: independent pricing consultant. Audience: B2B SaaS founders sitting on revenue plateaus.

```
Shipped a pricing teardown template this week. A founder cut their annual-contract close time from 19 days to 4 after using it on one call.

The problem it solves is the one I watch every week: a SaaS founder whose pricing page reads like a menu, with buyers treating it like one.

The old options were both bad. Hide the prices and lose the self-serve pipeline. Show everything and lose the enterprise upside.

What shipped:

- A one-page teardown the founder fills in before the call — not after.
- Three pricing anchors the buyer sees before the founder names a number.
- A template for the one question that closes: "which of these three worlds are you trying to live in?"

What I am watching next: whether this pushes founders toward three-tier structures or toward custom-on-every-deal. Different teams, different right answer.

If you are mid-plateau on pricing, what is the last deal you lost where you think the pricing page was the actual problem?
```

**Why it works:**

- Hook: unexpected-number (19 days → 4 days).
- The "what shipped" section is three lines, not the whole post.
- The post opens a larger question at the end — invites the reader to think past the launch.
- Specific enough that it could only be about this consultant's practice.
- Works for a solo creator with no team, no customers public yet, no VC-scale numbers.

## Bad 1 — generic thought leadership

```
In today's fast-moving B2B landscape, the companies that win are the ones that listen to their customers.

We have been thinking a lot about what makes great product decisions lately. Here is what we have learned:

- Talk to your customers.
- Listen more than you talk.
- Build what they actually need.

The best companies do not guess. They observe. And then they act.

Thoughts?
```

**Why it fails:**

- Generic opener ("In today's fast-moving B2B landscape") — the 2026 algorithm downranks this.
- Could be any company, any industry, any year. No specificity.
- The three bullets are platitudes. A reader learns nothing.
- CTA is "thoughts?" — engagement bait, actively downranked.
- Zero sourcing. Nothing to save, nothing to forward.

**What this skill should do instead:** drop this candidate at the shortlist stage. It has no concrete source, no named audience, and no reason to stop scrolling.

## Bad 2 — unsourced claim posing as insight

```
75% of B2B teams are drowning in customer context they cannot search.

We have seen this across hundreds of conversations. Teams know the answer is in a Slack thread somewhere, but they cannot find it. The cost is slower onboarding, missed renewals, and the slow death of institutional memory.

The solution is not more tools. It is one system of record for customer truth.

If this resonates, let's talk.
```

**Why it fails:**

- The 75% stat is invented. The skill's invariants forbid this. If no memory supports it, the claim must be flagged or cut.
- "Hundreds of conversations" is vague and unverifiable.
- The post ends in a sales CTA ("let's talk"), which the 2026 algorithm treats as low-intent.
- No named customer, no anonymized role, no specific workflow.

**What this skill should do instead:** flag the 75% for approval and replace "hundreds of conversations" with one specific customer arc. Rewrite the CTA to a question that invites a story.

## Bad 3 — customer story with invented quotes

```
One of our customers told us last week: "This is the most important tool we have adopted this year."

Their team had been struggling with onboarding for months. After switching to us, everything changed. Onboarding is fast. Morale is high. The team is shipping more than ever.

This is the power of getting the right tool.
```

**Why it fails:**

- The quote is almost certainly invented in this shape. Even if a memory has a positive customer sentiment, the exact quote must come from a memory, not be composed.
- "Everything changed" is abstract. No before state, no turning point, no measurable after.
- No customer role, no industry, no concrete workflow.
- The final line is a slogan, not an insight.

**What this skill should do instead:** pull the exact quoted language from the memory. If no memory has the quote, do not write it. Replace the vague arc with the specific before/turning-point/after the memory actually supports.
