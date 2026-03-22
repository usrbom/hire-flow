# Local Contributor Context

This folder supports contributor-specific context without putting personal details into the shared repository.

## Purpose

Use this folder for local-only files that capture the context needed to personalize guidance for a specific contributor.

Examples:

- target roles
- graduation timeline
- work authorization or visa status
- location preferences
- preferred base resume
- application constraints

## File naming

Create one local file per contributor using this pattern:

- `<name>.local.md`

Examples:

- `utkarsh.local.md`
- `alex.local.md`
- `sam.local.md`

These files are ignored by Git and should not be committed.

## How the agent should use this folder

- Shared workflow rules live in `AGENTS.md`.
- Personal context should be read from the relevant `*.local.md` file when a task requires personalized recommendations.
- If no local context file is available, the agent should continue with the shared workflow and ask for missing personal context only when needed.

## Recommended structure

Copy the headings from `USER_CONTEXT.template.md` into your own local file and fill them in with your details.

Keep entries concise and easy to scan.
