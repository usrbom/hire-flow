# Resume Index

This file is a lightweight index, not the full tailoring workflow.

For the detailed tailoring process, read:

- `Knowledge/my-resumes/AGENTS.md`

## Read Order

1. First read `contributors/local-context/RESUME_INDEX.local.md` if it exists.
2. Then read this file.
3. If both exist, the local file wins on conflict.

---

## Shared Default

- When only one Markdown resume exists in `base/`, or when no better match is identified, primary source: `Tech_8.md`
- Matching PDF reference: `Tech_8.pdf`

Tailoring should still choose a single best base Markdown resume for the JD.

---

## Base Resume Selection Rules

- Inspect all Markdown resumes in `Knowledge/my-resumes/base/` except `README.md` and `RESUME_INDEX.md`.
- Compare them against the JD for function, seniority, stack, and narrative fit.
- Choose one file only for first-pass tailoring.
- State the chosen file path and rationale at the top of `analysis.md`.

---

## Archive

- Older variants in `../archive/` are fallback reference only.
- Do not treat them as default tailoring inputs.

---

## Naming Convention

- Company folder: `Company_Name`
- Role folder: `Role_Name`
- Standard files per role:
  - `jd.md`
  - `analysis.md`
  - `review-loop.md`
  - `diff.md`
  - `resume-tailored.md`
  - `resume-tailored.docx` when Word output is generated locally
  - contributor-specific final PDF when exported locally for submission
