---
name: exa-people-search
description: Use when finding likely buyers, public LinkedIn-style profiles, experts, team members, professional backgrounds, or contact research targets with Exa People Search plus Memory Store context.
---

# Exa People Search

Find public professional profiles and likely buyers for already-qualified accounts. This skill adapts Exa's People Search pattern to Memory Store-backed GTM campaigns.

Sources:

- https://exa.ai/docs/reference/people-search-claude-skill

## Operating Loop

1. **Checkin and recall.** Start with Memory Store `checkin`, then recall buyer personas, prior relationship context, known contacts, do-not-contact rules, successful titles, and account-specific history.

2. **Start from account fit.** Do people search after account qualification unless the user explicitly asks for expert discovery. Do not build people lists for weak-fit accounts.

3. **Use Exa as a worker.** Run people/profile searches in background workers when available. Return compact people rows, source URLs, and verification notes.

4. **Use the right category.**
   - `people` for public LinkedIn-style profiles and bios
   - `personal site` for personal sites and portfolios when available
   - `news` for interviews, speaker bios, and public mentions
   - no category for deeper individual background checks

5. **Respect People Search restrictions.** With `category: "people"`, avoid date filters, text filters, `excludeDomains`, and non-LinkedIn `includeDomains`. Public LinkedIn discovery should use `category: "people"` with minimal filters.

6. **Use query variations.** Generate 2-3 variations by title, function, account name, geography, and domain language. Merge and dedupe.

7. **Score buyer relevance.** Score each person by role fit, seniority, likely pain ownership, account trigger relevance, source quality, prior relationship, and suppression risk.

8. **Handoff to copy only after review.** People Search returns reviewed buyer candidates and personalization-safe public facts. It does not send or schedule outreach.

## Output Contract

Return:

1. **people read** - best buyer thesis and uncertainty.
2. **buyer rows** - name, title, company, location if available, profile URL, role fit, confidence.
3. **safe hooks** - public facts that can support personalization.
4. **suppression risks** - existing relationship, do-not-contact, ambiguity, or weak source.
5. **next action** - enrich, draft, research more, exclude, or route to human.

## Do Not

- Do not infer private emails or personal details from weak evidence.
- Do not treat a profile as the right person without title/company fit.
- Do not use private Memory Store context directly in copy.
- Do not send Gmail from this skill.
