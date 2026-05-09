---
name: exa-people-search
description: Use when finding Exa-backed buyers, experts, team members, or public profiles.
---

# Exa People Search

Find likely buyers or public experts for already-qualified accounts. Production people search should join the same person's work email, LinkedIn profile, persona, and signal evidence so email and LinkedIn touches can be tracked together.

## Loop

1. Start with Memory Store `checkin` and recall buyer personas, known contacts, suppressions, relationship context, and account history.
2. Search people after account fit is clear unless the user asks for expert discovery.
3. Verify Exa Search is authenticated before production people discovery. If missing, return setup steps and query specs only.
4. Prefer active Exa Search tools: `web_search_advanced_exa` with `category: "people"`, plus `web_search_exa` and `web_fetch_exa` for verification.
5. Use deprecated `people_search_exa` or `linkedin_search_exa` only as host fallbacks.
6. Run title/function/account query variants in parallel when useful; dedupe and score by person identity, email, LinkedIn URL, company, and source URL.
7. Classify the job-to-be-done. Do not use "founder" as the persona by itself.
8. Return safe public hooks, source URLs, confidence, suppression risk, and channel policy. Handoff to copy only after planner fields are complete.

## Output

Return: people read, buyer rows, email/LinkedIn identity map, safe hooks, suppression risks, and next action.

## Rules

Do not infer private emails or personal details from weak evidence. Do not send Gmail from this skill. Do not put private Memory Store context directly in copy. Do not recommend dual-channel outreach unless the same-person identity match is moderate or high confidence.
