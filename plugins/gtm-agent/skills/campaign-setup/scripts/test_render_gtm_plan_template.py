#!/usr/bin/env python3
"""Tests for the GTM Agent GTM plan template script."""

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("render_gtm_plan_template.py")


class RenderGtmPlanTemplateTest(unittest.TestCase):
    def test_outputs_required_gtm_plan_keys(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            check=True,
            capture_output=True,
            text=True,
        )

        required_keys = [
            "inferred:",
            "needs_confirmation:",
            "unknown_blocker:",
            "company_profile:",
            "campaign_mode:",
            "context_sources:",
            "connector_status:",
            "briefs_used:",
            "offer_profiles:",
            "customer_usage_map:",
            "sender_voice:",
            "website_findings:",
            "demo_cta:",
            "funnel_system:",
            "icp_matrix:",
            "signal_sources:",
            "gmail_learnings:",
            "calendar_policy:",
            "channel_policy:",
            "send_ramp_policy:",
            "autopilot_routines:",
            "memory_distillation:",
            "brief_delta:",
            "approval_needed_before_start:",
        ]

        self.assertEqual(result.stdout.splitlines(), required_keys[:3] + [""] + required_keys[3:])


if __name__ == "__main__":
    unittest.main()
