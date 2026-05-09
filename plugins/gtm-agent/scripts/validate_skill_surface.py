#!/usr/bin/env python3
"""Validate GTM Agent skill routing metadata and eval fixtures."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PLUGIN_ROOT / "skills"
EVAL_FILE = PLUGIN_ROOT / "evals" / "skill-routing-cases.json"
DESCRIPTION_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_frontmatter(skill_md: Path) -> dict[str, str]:
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        fail(f"{skill_md} is missing YAML frontmatter")

    data: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return data
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')

    fail(f"{skill_md} has unterminated YAML frontmatter")


def description_word_count(description: str) -> int:
    return len(DESCRIPTION_WORD_RE.findall(description))


def resolve_reference(skill_name: str, reference: str) -> Path:
    return (SKILLS_ROOT / skill_name / reference).resolve()


def main() -> None:
    if not EVAL_FILE.exists():
        fail(f"missing eval fixture: {EVAL_FILE}")

    evals = json.loads(EVAL_FILE.read_text(encoding="utf-8"))
    budget = int(evals.get("description_budget_words", 50))

    skills = sorted(path.name for path in SKILLS_ROOT.iterdir() if (path / "SKILL.md").exists())
    if not skills:
        fail("no skills found")

    for skill_name in skills:
        frontmatter = read_frontmatter(SKILLS_ROOT / skill_name / "SKILL.md")
        if frontmatter.get("name") != skill_name:
            fail(f"{skill_name}: frontmatter name does not match directory")

        description = frontmatter.get("description", "")
        if not description.startswith("Use when "):
            fail(f"{skill_name}: description must start with 'Use when '")
        words = description_word_count(description)
        if words > budget:
            fail(f"{skill_name}: description has {words} words, budget is {budget}")

    positive_cases = evals.get("positive_cases", [])
    negative_cases = evals.get("negative_cases", [])
    reference_cases = evals.get("reference_read_cases", [])
    if not positive_cases:
        fail("positive_cases must not be empty")
    if not negative_cases:
        fail("negative_cases must not be empty")

    positive_by_skill = {skill: 0 for skill in skills}
    for case in positive_cases:
        expected = case.get("expected_skill")
        if expected not in positive_by_skill:
            fail(f"{case.get('id')}: unknown expected_skill {expected!r}")
        if not case.get("query"):
            fail(f"{case.get('id')}: query is required")
        positive_by_skill[expected] += 1

    missing_positive = [skill for skill, count in positive_by_skill.items() if count == 0]
    if missing_positive:
        fail(f"missing positive routing cases for: {', '.join(missing_positive)}")

    known_skills = set(skills)
    for case in negative_cases:
        forbidden = case.get("forbidden_skills", [])
        if not case.get("query"):
            fail(f"{case.get('id')}: query is required")
        if not forbidden:
            fail(f"{case.get('id')}: forbidden_skills is required")
        unknown = sorted(set(forbidden) - known_skills)
        if unknown:
            fail(f"{case.get('id')}: unknown forbidden skills: {', '.join(unknown)}")

    for case in reference_cases:
        skill = case.get("skill")
        if skill not in known_skills:
            fail(f"{case.get('id')}: unknown skill {skill!r}")
        references = case.get("required_references", [])
        if not references:
            fail(f"{case.get('id')}: required_references is required")
        for reference in references:
            path = resolve_reference(skill, reference)
            if not path.exists():
                fail(f"{case.get('id')}: missing reference {reference!r} from {skill}")

    print(
        "OK: "
        f"{len(skills)} skills, "
        f"{len(positive_cases)} positive cases, "
        f"{len(negative_cases)} negative cases, "
        f"{len(reference_cases)} reference-read cases"
    )


if __name__ == "__main__":
    main()
