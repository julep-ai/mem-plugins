# Annotated example posts

Six examples. Three good, three that fail in ways this skill is likely to fail. Read these before presenting drafts.

## Good: specific customer story, dramatic hook, earned CTA

```
"We need to pull the integration tomorrow."

That was the subject line at 2:13 AM.

A B2B infra team had spent three weeks wiring our memory into their on-call loop. The pager kept firing on false positives and their rotation was done pretending otherwise.

We asked one question: what do you do when you dismiss an alert?

Turns out they already had the answer — in the Slack replies and the retro docs nobody fed back into the alerting system.

We recorded every dismissal as its own memory, tagged with who dismissed it and why. Two weeks later the on-call noise dropped 63%. No model change. No new rules. One feedback loop nobody had closed.

The lesson is not "use our tool." The lesson is: the signal you need is almost always already written down by the person closest to the problem. You just have to keep it.

What is the last alert you dismissed that mattered?
```

**Why it works:**

- Hook: dramatic-moment framework; first two lines under 200 characters; opens with stakes.
- Specificity: real numbers (63%, two weeks, 2:13 AM), real workflow (Slack replies, retro docs).
- No product pitch in the first 1,000 characters; the tool is incidental to the lesson.
- CTA asks for the reader's version of the arc, not a vibe check.
- Ends with a saveable takeaway, which is what the 2026 algorithm rewards.

**Depth Score forecast:** high save rate, comments likely to be specific (people will name their own dismissed alerts).

## Good: founder POV with teeth

```
Most B2B content is written to be admired, not to be used.

I wrote like this for a year. My posts got likes. My DMs were all from other founders telling me the writing was "sharp." Not one buyer forwarded one to their team.

Three things I changed:
- I stopped writing posts that could have been about any company.
- I stopped ending with "thoughts?" and started ending with questions only someone in the job could answer.
- I stopped counting likes and started counting which posts got saved.

The post you are reading is draft five. The first four were better writing and worse content.

If your last five posts were not used by anyone, write one a buyer could forward to their team.

Where do you disagree?
```

**Why it works:**

- Hook: uncomfortable-truth; defensible claim.
- Body has three specific changes, each testable against the reader's own behavior.
- The meta line ("draft five") earns authority by showing the work.
- CTA invites disagreement, which generates longer comments than agreement does.

## Good: shipped-work post that is not a changelog

```
We shipped memory-scoped access control this week. A YC-backed team onboarded their sales department in 47 minutes after three weeks of waiting.

The problem they had is the one every team eventually hits: a shared memory store where Sales and Engineering need the same system but cannot legally see each other's customer notes.

The old options were both bad. Over-share and violate the access model. Silo per team and lose the cross-department recall that was the whole point of a shared memory.

What shipped:
- Memories now belong to a department, not just a person.
- Access is role-first; onboarding a team is one config.
- Cross-department recall is explicit — you ask for it, it is logged.

What we are watching next: whether this pushes teams toward department-specific agents instead of one global one. If it does, the interesting question is not "which agent is smartest" but "which department's memory is richest."

If you are running a team memory store, how are you handling cross-department access today?
```

**Why it works:**

- Hook: unexpected-number (47 minutes after three weeks).
- The changelog section is three lines, not the whole post.
- The post opens a larger question at the end — invites the reader to think past the launch.
- Specific enough that it could only be about this company.

## Bad: generic thought leadership

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

- Generic opener ("In today's fast-moving B2B landscape") — the algorithm downranks this.
- Could be any company, any industry, any year. No specificity.
- The three bullets are platitudes. A reader learns nothing.
- CTA is "thoughts?" — engagement bait, actively downranked.
- Zero sourcing. Nothing to save, nothing to forward.

**What this skill should do instead:** drop this candidate at the shortlist stage. It has no concrete source, no named audience, and no reason to stop scrolling.

## Bad: unsourced claim posing as insight

```
75% of B2B teams are drowning in customer context they cannot search.

We have seen this across hundreds of conversations. Teams know the answer is in a Slack thread somewhere, but they cannot find it. The cost is slower onboarding, missed renewals, and the slow death of institutional memory.

The solution is not more tools. It is one system of record for customer truth.

If this resonates, let's talk.
```

**Why it fails:**

- The 75% stat is invented. The skill's invariants forbid this. If no memory supports it, the claim must be flagged or cut.
- "Hundreds of conversations" is vague and unverifiable.
- The piece ends in a sales CTA ("let's talk"), which the 2026 algorithm treats as low-intent.
- No named customer, no anonymized role, no specific workflow.

**What this skill should do instead:** flag the 75% for approval and replace "hundreds of conversations" with one specific customer arc. Rewrite the CTA to a question that invites a story.

## Bad: customer story with invented quotes

```
One of our customers told us last week: "Memory Store is the most important tool we have adopted this year."

Their team had been struggling with onboarding for months. After switching to Memory Store, everything changed. Onboarding is fast. Morale is high. The team is shipping more than ever.

This is the power of company memory.
```

**Why it fails:**

- The quote is almost certainly invented in this shape. Even if a memory has a positive customer sentiment, the exact quote must come from a memory, not be composed.
- "Everything changed" is abstract. No before state, no turning point, no measurable after.
- No customer role, no industry, no concrete workflow.
- The final line is a slogan, not an insight.

**What this skill should do instead:** pull the exact quoted language from the memory. If no memory has the quote, do not write it. Replace the vague arc with the specific before/turning-point/after the memory actually supports.
