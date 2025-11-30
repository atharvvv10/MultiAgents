# Contributing to MultiAgents

Thanks for contributing! This document explains how to use issue levels, first-time flags, and how moderation works.

## Issue Levels
Each issue template includes:
- beginner
- intermediate
- advanced

Workflows automatically label issues based on your choice.

## First-time Contributors
If you check *“This is my first issue”*, the bot labels it as `good first issue`.

## Moderation System
Moderators are listed in `.github/MODERATORS.yml`.

Issues or PRs touching core directories:
- `agent_monitoring/`
- `ai-agent/`
- `llm_project/`

are automatically labeled:
- `needs-moderation`
- `awaiting-moderator`

Moderators must add:
- `moderator-approved`

to allow merge.

## Steps to Contribute
1. Open an issue from one of the templates.
2. Wait for triage labels.
3. Open a PR referencing the issue.
4. If PR touches core code, it will require moderator approval.
5. Once approved, maintainers merge it.
