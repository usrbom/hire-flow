# Build AI Product Sense

This repo is a personal learning and recruiting system for an MBA student (Anderson) on an F-1 visa targeting summer 2026 PM and PMM internships. It has two main areas: **resume tailoring** and **goal/task tracking**.

## Goals

Goals live in `GOALS.md`. Active tasks live under `Tasks/` as individual Markdown files. When helping with recruiting strategy or planning, read these files first to stay aligned with current priorities.

## Resume Tailoring

Two trigger modes:

- **`Tailor:`** — fast default. Runs Pass 1 + light truth check. Outputs: `jd.md`, `analysis.md`, `resume-tailored.md`.
- **`Tailor (full review):`** — full 3-pass review loop. Outputs all 5 files including `review-loop.md` and `diff.md`.

Full instructions are in `Knowledge/my-resumes/AGENTS.md`. Read that file for:
- Session file caching rules (skip re-reading files already in context)
- How to choose the right base resume from `Knowledge/my-resumes/base/`
- The full 3-pass review loop (Structure → Micro-Rewrite → Truth + Fit Validation)
- Output folder structure (`tailored/<Company>/<Role>/`)
- DOCX and PDF generation pipelines
- Bullet ranking framework and page-fit rules

## Key Conventions

- **Never read files inside either `tailored/` directory** (`tailored/` at repo root or `Knowledge/my-resumes/tailored/`) unless the user explicitly asks.
- Base resumes live in `Knowledge/my-resumes/base/` — never invent or assume a default without reading the index first.
- `archive/old-variants/` is fallback reference only.
- Contributor-local context lives in `contributors/local-context/` at the repo root and takes priority over base defaults.
- The user is on an F-1 visa — always assess visa applicability as part of analysis.
- All tailored resumes must stay on one page unless the user explicitly requests otherwise.

## Repo Structure

```
GOALS.md                              # Current goals
Tasks/                                # Active task tracking
contributors/local-context/           # Contributor-specific overrides (priority over base)
scripts/                              # DOCX/PDF render scripts
tailored/                             # Output folder — do not read unless asked
Knowledge/
  reference-resumes/                  # Anderson resume books (style reference)
  my-resumes/
    AGENTS.md                         # Full resume tailoring instructions
    base/                             # Source resumes and index
    archive/                          # Old variants (fallback only)
    tailored/                         # Legacy output folder — do not read unless asked
```
