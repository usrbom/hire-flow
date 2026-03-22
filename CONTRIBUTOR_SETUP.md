# Contributor Setup

This document explains how a new contributor should set up the repo locally for personalized resume tailoring and document generation without committing private files.

## Goal

Keep the shared repository public-safe while allowing each contributor to use their own:

- career context
- resume preferences
- Word resume template
- local formatting notes

## What stays shared

These files are part of the shared repo workflow:

- `AGENTS.md`
- `Knowledge/my-resumes/AGENTS.md`
- `Knowledge/my-resumes/base/RESUME_INDEX.md`
- `Knowledge/my-resumes/base/PDF_EXPORT_SPEC.md`
- `Knowledge/my-resumes/base/PDF_PIPELINE.md`
- `Knowledge/my-resumes/base/DOCX_PIPELINE.md`

## What stays local

Each contributor should create their own local-only files under:

- `contributors/local-context/`

These are ignored by Git and should not be committed.

## Required local setup

### 1. Personal context file

Create:

- `contributors/local-context/<name>.local.md`

Use:

- `contributors/local-context/USER_CONTEXT.template.md`

This file should include:

- degree and graduation timeline
- target roles
- work authorization or visa details
- location preferences
- preferred base resume

## Optional local setup

### 2. Resume index override

Create:

- `contributors/local-context/RESUME_INDEX.local.md`

Use this only if you want local tie-breakers for choosing between multiple base resumes.

### 3. Personal Word template

Create:

- `contributors/local-context/<name>.resume-template.local.docx`

This should be a `.docx` version of your preferred resume format.

The agent can use this file as the formatting reference for generated Word resumes.

### 4. DOCX formatting notes

Create:

- `contributors/local-context/<name>.docx-format.local.md`

Use this for template-specific instructions that may not be obvious from the `.docx` alone.

Examples:

- exact font sizes for certain lines
- date and location alignment rules
- hyperlink display and target rules
- section spacing expectations
- single-page requirement

## Shared fallback files

If no contributor-local Word template exists, the agent falls back to:

- `Knowledge/my-resumes/base/template.docx`

If no contributor-local resume index exists, the agent falls back to:

- `Knowledge/my-resumes/base/RESUME_INDEX.md`

## Recommended setup flow for a new contributor

1. Clone the repo.
2. Read `AGENTS.md`.
3. Copy `contributors/local-context/USER_CONTEXT.template.md` into `contributors/local-context/<name>.local.md`.
4. Fill in your personal context.
5. If you have a preferred Word resume format, add `contributors/local-context/<name>.resume-template.local.docx`.
6. If needed, add `contributors/local-context/<name>.docx-format.local.md`.
7. Keep all local files uncommitted.

## How to ask the agent for help

Examples:

- `Tailor: <paste job description>`
- `RenderPDF: tailored/<Company>/<Role>/resume-tailored.md`
- `RenderDOCX: tailored/<Company>/<Role>/resume-tailored.md`

If your local Word template exists, the agent should prefer it for DOCX generation and tuning.

## Privacy reminder

Do not commit:

- personal resumes
- tailored application folders
- local context files
- local Word templates
- local DOCX formatting notes
