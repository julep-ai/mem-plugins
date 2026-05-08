#!/usr/bin/env python3
"""Print the GTM Agent campaign setup packet template."""

PACKET = """inferred:
needs_confirmation:
unknown_blocker:

company_profile:
campaign_mode:
context_sources:
offer_profiles:
sender_voice:
website_findings:
demo_cta:
funnel_system:
icp_matrix:
signal_sources:
gmail_learnings:
calendar_policy:
send_ramp_policy:
autopilot_routines:
approval_needed_before_start:
"""


def main() -> None:
    print(PACKET, end="")


if __name__ == "__main__":
    main()
