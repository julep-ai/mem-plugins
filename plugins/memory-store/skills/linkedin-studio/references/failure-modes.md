# Failure modes

How to handle the ways this skill breaks. Each mode lists symptoms, what to do, and what to record.

## Memory Store MCP unavailable

**Symptoms:** `checkin` or `recall` returns a connection error, auth error, or times out.

**Action:**

1. Say so explicitly in the response. Do not silently degrade.
2. Ask the user to paste source context — approved posts for voice, one or two source memories for material.
3. Produce drafts using only pasted context.
4. Mark every draft in the draft package as `ungrounded` with a one-line note.
5. Do not call `record`. The learning loop needs a thread_id.
6. Tell the user the system has not learned from this run.

**What not to do:** invent sources, fabricate memory IDs, or pretend recall succeeded with empty results.

## Checkin succeeds but recall returns empty

**Symptoms:** `recall` returns zero memories for both voice and source cues.

**Action:**

1. Follow the empty-recall fallback in [recall-cues.md](recall-cues.md): broaden, re-cue, then ask the user.
2. If still empty, ask the user for one seed: an author's approved post, a customer name, or a shipped feature.
3. Draft only what the seed supports. Flag every claim not traceable to the seed.
4. Do not fill the gap with generic B2B platitudes. An empty recall is a signal that today's run may not have enough to post — say that explicitly.

## Voice memory and user intent conflict

**Symptoms:** voice memory says "avoid the word X" but the user's current request uses X, or voice memory says "never use numbered lists" but the user asks for a numbered list.

**Action:**

1. Surface the conflict. Quote the voice rule and the conflicting request back to the user.
2. Ask which wins for this piece.
3. If the user resolves with a new preference, call `record` with a `voice_rule_update` event so the next run has the updated rule.
4. If the user does not resolve, defer to the stored voice rule. It represents past editorial decisions; today's ask is one data point against it.

## Two voice memories contradict each other

**Symptoms:** two stored rules for the same author disagree — "always end with a question" and "never end with a question".

**Action:**

1. Prefer the more recent rule. Voice evolves; the later editorial decision is usually the live one.
2. Flag the contradiction to the user and ask which one to keep.
3. Record the resolution as a `voice_rule_update` that supersedes.

## Draft contains an unsourced claim

**Symptoms:** a draft has a number, a customer name, a quote, or a category claim that does not trace to a source memory ID.

**Action:**

1. Do not present the draft with the claim as fact.
2. Either (a) cut the claim and rewrite the paragraph around a claim that is sourced, or (b) leave the claim in with a visible `[NEEDS APPROVAL]` marker and list it under `flagged_claims` in the draft package.
3. Do not record an approval/edit/publish outcome without listing the flagged claim(s) in the prose record.

## Draft violates a banned phrase

**Symptoms:** a banned phrase from the author's voice memory appears in a draft.

**Action:**

1. Rewrite the line before presenting. Banned phrases are hard constraints.
2. If the banned phrase is structurally load-bearing (e.g., it is the hook), drop that draft variant and try a different hook framework.
3. Do not ask the user to accept a banned-phrase violation — the rule exists precisely so this skill does not re-litigate it every run.

## User gives feedback but thread_id is missing

**Symptoms:** `checkin` failed earlier or was skipped; user approves, edits, or rejects a draft.

**Action:**

1. Tell the user the feedback cannot be recorded without a thread.
2. Offer to re-run `checkin` now to attach the feedback retroactively.
3. If the user declines, do not record the feedback. Say explicitly that this run will not improve the model for next time.

## Recall returns a memory marked internal-only

**Symptoms:** a recalled memory has an `internal_only` or equivalent tag, or its content is clearly sensitive (pricing internals, team disagreements, unshipped experiments, customer complaints not for public use).

**Action:**

1. Do not use it as a source for public drafts.
2. Do not cite its memory ID in the draft package.
3. If the internal memory is the only source for a candidate, drop that candidate.
4. Do not quote or paraphrase internal content in a way that leaks its substance.

## Customer name appears without public-use approval

**Symptoms:** a memory names a specific customer but no `customer_approved_public` record exists for them.

**Action:**

1. Anonymize per the convention in [format-templates.md](format-templates.md).
2. Offer the draft in both anonymized and named form so the user can approve the named version if appropriate.
3. If the user approves public use, call `record` with a `customer_approved_public` event before publishing the named version.

## Recall returns contradictory source facts

**Symptoms:** two memories describe the same event differently (different numbers, different outcomes, different customer roles).

**Action:**

1. Prefer the memory with more evidence (a direct quote, a source document, a specific timestamp).
2. If both are equally sourced, use the later one and note the earlier as superseded.
3. If neither has evidence, flag the fact as `[NEEDS APPROVAL]` and ask the user which is correct.

## User asks to record feedback for a different run

**Symptoms:** user says "record that feedback on yesterday's post" mid-conversation.

**Action:**

1. The current `thread_id` is for today's run. Yesterday's run has its own thread.
2. Ask the user for the `piece_id` or the thread that the feedback belongs to.
3. If the user does not have it, call `recall` with a cue like `<author> post_published <yesterday's date>` to locate the piece_id, then record against that.
4. Never record yesterday's feedback against today's `thread_id` — it breaks lineage.

## Platform quirks

- **Character limits:** LinkedIn hard-caps at 3,000 characters. Drafts over 2,100 should be shortened or converted to a carousel plan.
- **Links in posts:** putting a link in the main post body depresses reach. Move links to the first comment when a link is required.
- **Mentions:** only `@` a person or company if a memory confirms they are a public figure or have approved being mentioned.
- **Hashtags:** 0 to 3. Over 3 reads as spammy and does not improve reach in the 2026 algorithm.

## Report Memory Store tool issues

If Memory Store MCP is unavailable, returns inconsistent behavior, or tool contracts fail, call `report-issue` with a description of the behavior.
