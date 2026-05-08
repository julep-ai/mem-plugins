---
name: exa-company-research
description: Use when researching companies, markets, competitors, accounts, news, or public profiles with Exa and Memory Store context.
---

# Exa Company Research

Research companies and markets for GTM decisions. This skill adapts Exa's Company Research pattern to Memory Store-backed campaigns.

Sources:

- https://exa.ai/docs/reference/company-research-claude-skill

## Operating Loop

1. **Checkin and recall.** Start with Memory Store `checkin`, then recall the company/product being sold, target ICPs, customer language, exclusions, competitors, prior account history, and approved outbound claims.

2. **Define the research question.** Classify the ask:
   - company deep dive
   - competitor map
   - market/category scan
   - target account list
   - news/timing research
   - public profile/team discovery

3. **Use Exa as a worker, not the main context.** Never dump raw search results into the main thread. Run searches in background workers when available, and return only distilled briefs, structured rows, source URLs, and uncertainty notes.

4. **Use the right Exa category.**
   - `company` for company discovery and company metadata
   - `news` for announcements and timing
   - `people` for public professional profiles
   - no category with `type: "auto"` or `type: "deep"` for broader investigation

5. **Vary queries.** Generate 2-3 query variations, run them in parallel when possible, merge, dedupe, and score.

6. **Respect filter restrictions.** With `category: "company"`, do not use domain/date filters. With broad web or news searches, domain/date filters are allowed. `includeText` and `excludeText` should stay single-item arrays.

7. **Build account briefs.** For each company, return fit, timing, trigger, source URLs, confidence, and what Memory Store context changes about the angle. If the result is meant for outbound, include the campaign-planner fields: why this person/account, why now, persona, offer angle, proof path, next action, remember-after-touch, and exclusion risk.

8. **Record only confirmed learnings.** If the user confirms a market thesis, competitor map, account fit rule, or exclusion rule, record it to Memory Store with the active `thread_id`.

## Output Contract

Return:

1. **research read** - one paragraph with the strongest finding and biggest uncertainty.
2. **company/account rows** - company, website, ICP fit, signal, source URL, persona, offer angle, proof path, next action, confidence, exclusion risk.
3. **market notes** - competitors, trends, timing, buying triggers.
4. **memory impact** - what prior Memory Store context changed.
5. **next action** - lead-gen, people search, Websets, monitor, copy, or discard.

## Do Not

- Do not invent funding, customers, headcount, metrics, or buyer names.
- Do not use Exa results without source URLs.
- Do not treat a website, category fit, or founder title as a draft-ready signal.
- Do not put private Memory Store context into public outbound copy.
- Do not treat an auth-gated LinkedIn result as verified unless fetched through an approved browser workflow.
