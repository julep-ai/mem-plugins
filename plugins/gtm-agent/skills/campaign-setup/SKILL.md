---
name: campaign-setup
description: Use when setting up GTM Agent, discovering website/demo links, learning from Gmail, configuring Calendar policy, or enabling autopilot.
---

# Campaign Setup

Set up GTM Agent once so campaigns can run continuously from Memory Store, public signals, Gmail, and Google Calendar. This skill is the first-run GTM engineer interview: infer what can be inferred, ask only unresolved blockers, then create the approved operating profile used by the main `gtm-agent` skill.

Use this for:

- first-run GTM Agent setup.
- campaign autopilot configuration.
- website and demo-link discovery.
- sender voice and prior-touch learning from the current Gmail inbox and sent mail.
- Google Calendar booking context after qualified replies.
- defining the send ramp, followup cadence, suppression rules, and monitoring routines.

## Requirements

- Memory Store MCP for `checkin`, `recall`, and later `record`.
- Exa/Web fetch when available for website, demo link, docs, changelog, customer, and proof-path discovery.
- Gmail connector when available for inbox/sent-mail learning and campaign execution.
- Google Calendar connector when available for availability and scheduling context.

If any connector is missing, do not block setup. Return the missing connector in `approval_needed_before_start` and produce import-ready setup instructions or manual assumptions.

## Operating Loop

1. **Checkin and recall.** Start with Memory Store `checkin`. Recall the company, product, offer profiles, customer language, voice, ICPs, exclusions, approved claims, prior campaigns, known objections, demos, calendar preferences, and do-not-contact rules.

2. **Discover company website.** If the user did not provide a website, infer it from Memory Store first, then public search. If multiple likely domains exist, show the candidates and choose only the highest-confidence one for setup.

3. **Research website assets.** Use Exa/Web fetch when available. Inspect homepage, product, pricing, docs, customers, blog/changelog, integration pages, demo/contact pages, and proof assets. Do not treat the website itself as a signal; use it to understand offer, proof, claims, and CTA.

4. **Discover demo CTA.** Find Cal, Calendly, demo, contact, signup, waitlist, or meeting links. The user must confirm the discovered demo link once before campaigns use it. Until confirmed, use reply-first or teardown CTAs.

5. **Learn from Gmail.** Treat Gmail as a first-class setup source. Use bounded searches over current inbox and sent mail to extract sender voice, prior warm paths, objections, demo language, existing customer/prospect threads, reply patterns, suppressions, and do-not-contact signals. Do not read broad private mail unnecessarily; summarize scope and confidence.

6. **Learn scheduling context.** Use Google Calendar only for availability and booking context after qualified replies. If calendar is unavailable, keep the confirmed demo link usable and disable scheduling automation.

7. **Run the repeatable setup interview.** Use `references/onboarding-questions.md`. Ask only for blockers that Memory Store, website research, Gmail, or Calendar could not infer. Group unresolved inputs as `inferred`, `needs_confirmation`, and `unknown_blocker`.

8. **Define the active campaign planner.** Use `../gtm-agent/references/campaign-planner.md`. Select the active offer profile, sender persona, brand voice, ICP cells, company-size range, signal sources, proof path, CTA policy, media policy, and exclusion rules.

9. **Configure full autopilot.** Use `references/first-run-autopilot.md`. After setup approval, GTM Agent may send and follow up without per-batch approval inside the approved policy. Use ramped limits and stop on risk.

10. **Return the setup packet.** Use `references/setup-packet.md`. When useful, run `scripts/render_setup_packet_template.py` to emit the packet skeleton. Be concise, but do not omit unknowns; mark them as `unknown`, `missing_connector`, or `needs_user_confirmation`.

11. **Record only after approval.** Do not claim setup was learned until the user approves or edits the setup packet and the approved decision is recorded to Memory Store.

## Setup Packet

Return this exact packet shape:

```text
company_profile:
offer_profiles:
sender_voice:
website_findings:
demo_cta:
icp_matrix:
signal_sources:
gmail_learnings:
calendar_policy:
send_ramp_policy:
autopilot_routines:
approval_needed_before_start:
```

The field-level contract lives in `references/setup-packet.md`. The defaults and stop conditions live in `references/first-run-autopilot.md`.

## Do Not

- Do not send during setup before the setup packet is approved.
- Do not use a discovered demo link before the user confirms it once.
- Do not infer private facts from Gmail without saying the search scope.
- Do not attach screenshots by default.
- Do not position full autopilot as uncontrolled bulk sending; it is bounded by the approved send ramp and stop conditions.
