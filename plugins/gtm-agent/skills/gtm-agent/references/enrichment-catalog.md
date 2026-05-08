# Enrichment Catalog

Use this reference when defining Websets enrichments, Exa structured output, account evidence cards, or monitor schemas.

## Core Account Enrichments

Always prefer fields that can change action quality:

- `company_name`
- `website`
- `one_line_description`
- `icp_cell`
- `icp_fit_score`
- `icp_fit_reason`
- `trigger_signal`
- `trigger_source_url`
- `trigger_freshness_date`
- `buyer_titles`
- `public_language_snippet`
- `personalization_hook`
- `exclusion_risk`
- `recommended_angle`
- `confidence`

## High-Intent Signal Enrichments

Useful signal fields:

- recent funding or Form D
- new executive or team movement
- new GTM, AI, support, data, or platform roles
- launch/changelog/docs update
- integration or partnership announcement
- GitHub, package, API, or developer-docs activity
- competitor mention, migration, or comparison
- event attendance, sponsor, speaker, or community appearance
- public pain language, complaint, workaround, or manual process
- content theme that maps to a Memory Store customer pain

## Contact Enrichments

Use contact enrichment only after account fit is good:

- likely buyer title
- name if public and relevant
- email if available with confidence
- LinkedIn/profile URL if public
- role-persona fit
- prior relationship from Memory Store
- do-not-contact or suppression status

## Memory Enrichments

These come from Memory Store, not Exa:

- similar customer story
- known objection
- prior campaign outcome
- approved claim
- taboo claim or topic
- sender voice preference
- account history
- internal hypothesis confidence

Never put raw private memory into copy. Use it to select angle and ask for approval when needed.

## Monitor Output Schema

For monitor routines, prefer compact structured outputs:

- `headline`
- `signal_type`
- `company`
- `source_url`
- `summary`
- `why_it_matters`
- `matched_icp`
- `recommended_next_action`
- `confidence`

If the output becomes too broad, split the monitor by ICP cell or signal type.
