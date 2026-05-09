#!/usr/bin/env python3
"""Print the GTM Agent GTM plan template."""

PLAN = """inferred:
needs_confirmation:
unknown_blocker:

company_profile:
campaign_mode:
context_sources:
connector_status:
offer_profiles:
customer_usage_map:
sender_voice:
website_findings:
demo_cta:
funnel_system:
icp_matrix:
signal_sources:
gmail_learnings:
calendar_policy:
channel_policy:
send_ramp_policy:
autopilot_routines:
memory_distillation:
approval_needed_before_start:
"""


def main() -> None:
    print(PLAN, end="")


if __name__ == "__main__":
    main()
