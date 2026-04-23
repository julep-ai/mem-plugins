# mem-plugins

Installable Memory Store plugins.

The first plugin is `content-lead`. It writes LinkedIn drafts from company memory: Slack threads, Granola notes, shipped work, customer conversations, prior posts, and editorial feedback.

This repo is private for now.

## Current plugin

`plugins/content-lead` is a Codex plugin with one skill:

- `daily-linkedin-content-lead`: starts with Memory Store `checkin`, recalls brand voice and recent source material, drafts LinkedIn posts, and records feedback when the user approves, rejects, edits, or posts a draft.

## Product loop

```text
checkin -> recall -> draft -> feedback -> record -> better recall
```

The important part is the last step. Content Lead should get better because Memory Store remembers the edits, final posts, and rejected angles.

## Local evaluation

Use Plugin Eval against the skill:

```bash
node /Users/a3fckx/.codex/plugins/cache/openai-curated/plugin-eval/f09cfd210e21e96a0031f4d247be5f2e416d23b1/scripts/plugin-eval.js analyze plugins/content-lead/skills/daily-linkedin-content-lead --format markdown
```

Use the improvement workflow when the report shows what to fix first:

```bash
node /Users/a3fckx/.codex/plugins/cache/openai-curated/plugin-eval/f09cfd210e21e96a0031f4d247be5f2e416d23b1/scripts/plugin-eval.js analyze plugins/content-lead/skills/daily-linkedin-content-lead --brief-out .plugin-eval/content-lead-brief.json
```
