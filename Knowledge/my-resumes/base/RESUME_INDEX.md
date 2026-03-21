# Resume Index

## Canonical Base Resume

- Primary source for all future tailoring: `Tech_8.md`
- Matching PDF reference: `Tech_8.pdf`

## Default Workflow

1. Read `Tech_8.md` first.
2. Save the pasted job description under `tailored/<Company>/<Role>/jd.md` at the repository root.
3. First assess F-1 visa applicability and whether the role appears open to graduate or MBA candidates.
4. Extract role requirements, keywords, alignment score, bullet removals, and resume priorities into `tailored/<Company>/<Role>/analysis.md` at the repository root.
5. If there is a material eligibility concern, pause and ask the user whether to proceed.
6. First-pass tailoring rules:
   - work experience: reorder bullets and remove low-priority bullets
   - do not change work-experience bullet wording
   - before trimming, preserve bullets with strong company or industry resonance
   - additional: reframe the competition item if useful and reorder items by JD importance
   - reorder skills internally so the most relevant skills appear first
   - reorder courses internally so the most relevant courses appear first
   - skills: keep to 2 lines maximum
   - courses: keep to 1 line maximum
   - rank bullets using this order: eligibility fit, job function fit, industry/company resonance, seniority fit, customer proximity, cross-functional relevance, outcome strength, readability, distinctiveness
7. Save the tailored output to `tailored/<Company>/<Role>/resume-tailored.md` at the repository root.
8. After the first pass, ask the user whether they want a second pass with deeper edits to work-experience bullets.

## Archive

- Older resume variants are stored under `../archive/old-variants/`.
- Reference them only if the base resume lacks a clearly relevant bullet or phrasing pattern.

## Naming Convention

- Company folder: `Company_Name`
- Role folder: `Role_Name`
- Required files per role:
  - `jd.md`
  - `analysis.md`
  - `resume-tailored.md`
  - `notes.md` (optional)
