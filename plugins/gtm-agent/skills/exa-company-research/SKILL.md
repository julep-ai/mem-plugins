---
name: exa-company-research
description: Use when users ask for Exa-backed company, market, competitor, news, account, public-proof, or buyer-context research for GTM decisions.
---

# Exa Company Research

Research companies and markets for Memory Store-backed GTM decisions.

## Loop

1. Start with Memory Store `checkin` and recall ICPs, exclusions, prior account history, approved claims, and campaign goal.
2. Classify the request: company deep dive, market scan, competitor map, target-account research, news/timing, or profile/team discovery.
3. Prefer active Exa Search MCP tools at `https://mcp.exa.ai/mcp`: `web_search_advanced_exa`, `web_search_exa`, and `web_fetch_exa`.
4. Use `web_search_advanced_exa` categories deliberately: `company` for company metadata, `news` for timing, `people` for public profiles.
5. Run query variants in parallel when possible; return distilled rows, source URLs, confidence, and uncertainty notes.
6. If outbound-bound, include planner fields: why this account/person, why now, persona, offer angle, proof path, next action, remember-after-touch, confidence, and exclusion risk.
7. Record only confirmed research learnings to Memory Store.

Deprecated Exa tools such as `company_research_exa`, `linkedin_search_exa`, `crawling_exa`, and `deep_search_exa` are backward-compatible fallbacks only.

## Output

Return: research read, company/account rows, market notes, Memory Store impact, and next action.

## Rules

No invented funding, customers, headcount, metrics, buyer names, or source-less claims. A website, category fit, or founder title is not enough for draft-ready outreach.
