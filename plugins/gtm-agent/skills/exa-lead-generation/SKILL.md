---
name: exa-lead-generation
description: Use when generating Exa deep-search lead or account lists from ICPs with schemas, batching, dedupe, scoring, and Memory Store context.
---

# Exa Lead Generation

Generate high-signal account lists from a confirmed ICP. This skill adapts Exa's Lead Generation pattern to Memory Store-backed GTM campaigns.

Sources:

- https://exa.ai/docs/reference/lead-generation-claude-skill

## Requirements

- Memory Store MCP for context and learning.
- Exa MCP with `deep_search_exa` for structured lead generation.
- Exa API key configured in the host MCP config. Do not put real API keys in this repo.

## Operating Loop

1. **Checkin and recall.** Start with Memory Store `checkin`, then recall ICPs, customer examples, objections, successful segments, exclusions, taboo claims, and prior campaign outcomes.

2. **Research the seller first.** For a company-specific campaign, run one small ICP research pass before generating leads. Identify product description, sender persona, core claim, taboo pitches, target users, existing customers, ICP description, sub-verticals, demographic signals, and useful enrichments.

3. **Confirm or infer the campaign model.** For the default Memory Store GTM scale:
   - 20 ICP cells
   - 50 accepted companies or recipients per ICP
   - 1000 total targets
   - source extra candidates per ICP to survive dedupe and quality trims

4. **Generate micro-verticals.** Expand the ICP into specific, mostly non-overlapping micro-verticals. Use competitor mining, geography, stage, tech stack, use case, and buyer persona patterns.

5. **Design the output schema.** Keep schemas compact. Always include company name, website, product description, ICP fit score, and ICP fit reasoning. Add only the enrichments that improve action quality. For outbound-bound lists, include fields for persona, live signal, source URL, offer angle, proof path, next action, confidence, and exclusion risk.

6. **Respect Exa deep-search constraints.**
   - Use structured output.
   - Use `type: "deep"`.
   - Use low highlight size for structured output.
   - Keep item fields flat primitives.
   - Keep string fields bounded with word limits.
   - Keep schema property count small; warn the user if they request many columns.

7. **Batch work outside main context.** The main agent orchestrates. Batch workers run Exa calls, write JSON or CSV artifacts when available, and report only counts, top findings, exclusions, and file paths. Do not load 1000 raw rows into the main thread.

8. **Dedupe and score.** Deduplicate by normalized domain, company name, and obvious aliases. Score by ICP fit, signal strength, source confidence, exclusion risk, and Memory Store-backed fit. A website or founder title alone is not a signal; keep those rows in research-only state.

9. **Record confirmed results.** Record approved ICP rules, exclusion rules, winning micro-verticals, enrichment choices, and campaign outcomes to Memory Store.

## Output Contract

Return:

1. **ICP read** - confirmed or inferred ICP plus uncertainty.
2. **micro-vertical plan** - list of query cells and target counts.
3. **schema** - fields, reason for each field, and expected cost/latency risk.
4. **batch plan or result** - worker batches, counts, errors, and output files.
5. **shortlist summary** - top ICPs, signal patterns, exclusions, confidence, and draft eligibility.
6. **next action** - Websets persistence, people search, copy generation, monitor, or review.

## Do Not

- Do not run bulk lead generation without Memory Store exclusions.
- Do not expose raw private context in lead rows.
- Do not send emails from this skill. Lead generation ends at reviewed target data.
- Do not hand off to copy unless each row has persona, live signal, source, offer angle, proof path, next action, confidence, and exclusion risk.
- Do not claim the lead list is complete unless dedupe and quality checks ran.
