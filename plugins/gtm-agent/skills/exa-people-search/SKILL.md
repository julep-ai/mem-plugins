---
name: exa-people-search
description: Use when users ask to find, verify, dedupe, score, or map Exa-backed buyers, experts, team members, public profiles, LinkedIn identities, or work-email candidates.
---

# Exa People Search

Find likely buyers or public experts for already-qualified accounts. Production people search should join the same person's work email or explicit email-unavailable status, LinkedIn/profile URL, persona, and signal evidence so email and LinkedIn touches can be tracked together.

## Loop

1. Start with Memory Store `checkin`; use selected canonical brief context if provided by the main GTM agent, otherwise call `list-briefs` and select 0-3 relevant briefs; then recall buyer personas, known contacts, suppressions, relationship context, and account history.
2. Search people after account fit is clear unless the user asks for expert discovery.
3. Verify Exa Search is authenticated before production people discovery. If missing, return setup steps and query specs only.
4. Prefer active Exa Search tools: `web_search_advanced_exa` with `category: "people"`, plus `web_search_exa` and `web_fetch_exa` for verification.
5. Use deprecated `people_search_exa` or `linkedin_search_exa` only as host fallbacks.
6. Run title/function/account query variants in parallel when useful; dedupe and score by person identity, email, LinkedIn/profile URL, company, and source URL.
7. Classify the job-to-be-done. Do not use "founder" as the persona by itself.
8. Return safe public hooks, source URLs, confidence, suppression risk, and channel policy. Handoff to copy only after planner fields and channel identity fields are complete.

## Output

Return: people read, buyer rows, email/LinkedIn identity map, unavailable-email rows, safe hooks, suppression risks, and next action.

## Rules

Do not invent emails or infer private emails from weak evidence. If work email is unavailable, mark it unavailable and keep the row out of send-ready state unless another approved channel exists. Do not send Gmail from this skill. Do not put private Memory Store context directly in copy. Do not recommend dual-channel outreach unless the same-person identity match is moderate or high confidence. Do not create briefs for people rows, profile findings, or one-off contact decisions; return evidence and any brief-impact candidate to the main GTM agent.
