# Resume Index

## How agents should read this

1. **First:** If **`contributors/local-context/RESUME_INDEX.local.md`** exists, read it. It is **gitignored** (pattern `contributors/local-context/*.local.md`). Do not commit it.
2. **Then:** Read this file, **`Knowledge/my-resumes/base/RESUME_INDEX.md`**.
3. **Merge rule:** If both were read, use the local file wherever it **conflicts** with this document; for anything not specified in the local file, use this file.

If **`RESUME_INDEX.local.md` does not exist**, read **only** this file.

---

## Canonical base resume (shared default)

- When only one Markdown resume exists in `base/`, or when no better match is identified, primary source: `Tech_8.md`
- Matching PDF reference: `Tech_8.pdf`

Tailoring always uses **one** chosen base Markdown file from `Knowledge/my-resumes/base/` (see workflow step 2).

---

## Default workflow (shared)

1. Read the merged resume index (local file if present, then this file).
2. **Choose the base resume for this JD:** With the job description available, inspect **`Knowledge/my-resumes/base/`** for Markdown resumes. Treat **`README.md`** and **`RESUME_INDEX.md`** as documentation, not resumes. For every other **`.md`** file in that folder, compare its emphasis (role titles, skills, projects, section balance) to the JD—function (e.g. ML/research vs software engineering), stack, and seniority. **Select the single best-matching file** and use **only** that file as the source for reordering, trimming, and keyword alignment. If two are equally strong, use tie-breakers from `RESUME_INDEX.local.md` or, if none, from the *Canonical base resume* section above. State the **chosen file path** and a **short rationale** at the top of `analysis.md` (before visa and alignment sections).
3. Read the **selected** base resume in full.
4. Save the pasted job description under `tailored/<Company>/<Role>/jd.md` at the repository root.
5. First assess F-1 visa applicability and whether the role appears open to graduate or MBA candidates.
6. Extract role requirements, keywords, alignment score, bullet removals, and resume priorities into `tailored/<Company>/<Role>/analysis.md` at the repository root.
7. Save `tailored/<Company>/<Role>/diff.md` describing the differences between the selected base resume and the tailored resume, including why each change improves JD fit.
8. If there is a material eligibility concern, pause and ask the user whether to proceed.
9. First-pass tailoring rules:
  - work experience: reorder bullets and remove low-priority bullets
  - do not change work-experience bullet wording
  - before trimming, preserve bullets with strong company or industry resonance
  - additional: reframe the competition item if useful and reorder items by JD importance
  - reorder skills internally so the most relevant skills appear first
  - reorder courses internally so the most relevant courses appear first
  - skills: keep to 2 lines maximum
  - courses: keep to 1 line maximum
  - rank bullets using this order: eligibility fit, job function fit, industry/company resonance, seniority fit, customer proximity, cross-functional relevance, outcome strength, readability, distinctiveness
10. Save the tailored output to `tailored/<Company>/<Role>/resume-tailored.md` at the repository root.
11. When submit-ready output is requested, generate `tailored/<Company>/<Role>/resume-tailored.pdf` from the Markdown using `scripts/render_resume_pdf.py`.
12. After the first pass, ask the user whether they want a second pass with deeper edits to work-experience bullets.

---

## Archive

- Older resume variants are stored under `../archive/old-variants/`.
- Reference them only if the base resume lacks a clearly relevant bullet or phrasing pattern.

---

## Naming convention

- Company folder: `Company_Name`
- Role folder: `Role_Name`
- Required files per role:
  - `jd.md`
  - `analysis.md`
  - `diff.md`
  - `resume-tailored.md`
  - `resume-tailored.pdf` when generated locally for submission
  - `notes.md` (optional)
