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

### Resume workflow (local index)

- **Optional:** `RESUME_INDEX.local.md` — read **first** when it exists, then read `Knowledge/my-resumes/base/RESUME_INDEX.md`. Where this file conflicts with the shared index, follow the local file. If this file is missing, use only the shared `RESUME_INDEX.md`.
- Tailoring still requires **JD-aware choice** among all resume `.md` files in `Knowledge/my-resumes/base/`; the local index may list usual variants and tie-breakers only.

## How the agent should use this folder

- Shared workflow rules live in `AGENTS.md` and `Knowledge/my-resumes/base/RESUME_INDEX.md`.
- For resume tailoring, read `RESUME_INDEX.local.md` first if it exists, then the shared resume index (merge: local wins on conflict).
- Personal context should be read from the relevant `<name>.local.md` file when a task requires personalized recommendations.
- If no local context file is available, the agent should continue with the shared workflow and ask for missing personal context only when needed.

## Recommended structure

Copy the headings from `USER_CONTEXT.template.md` into your own local file and fill them in with your details.

Keep entries concise and easy to scan.
