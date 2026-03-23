# Resume Tailoring Instructions

This directory is for internship resume tailoring.

## Start Here

- Read `contributors/local-context/RESUME_INDEX.local.md` if it exists, then read `base/RESUME_INDEX.md` (local wins on conflict; if no local file, only read `base/RESUME_INDEX.md`).
- **Do not assume a single default file until you have compared options.** After you have the job description, inventory **`base/`** (see *Choosing the base resume* below), pick the best match, then read **only that** Markdown file for tailoring.
- If relevant contributor-local files exist, read them before drafting:
  - `contributors/local-context/<name>.local.md`
  - `contributors/local-context/<name>.story-bank.local.md`
  - contributor-local Anderson-style guide or similar bullet-style local notes
- Treat `archive/old-variants/` as fallback reference only

## Choosing the base resume

- **When:** After the index files are read and the **job description** is available (from the user message or `tailored/.../jd.md`).
- **Where:** `Knowledge/my-resumes/base/`
- **What to consider:** Every **`.md`** file in that folder **except** `README.md` and `RESUME_INDEX.md`. Quickly compare each candidate to the JD: job title and level, required skills and stack, research vs product/engineering emphasis, data/ML vs general software, and which variant tells the strongest honest story for this posting.
- **Choose:** One file. Use that file’s work-experience bullets and structure as the **sole** source for first-pass tailoring (reorder/trim/reframe per rules—no inventing roles).
- **Document:** At the **top** of `analysis.md`, record **Base resume selected:** `<path>` and **Why:** one to three sentences. Then continue with F-1, graduate/MBA fit, and alignment as usual.
- **Hints:** `RESUME_INDEX.local.md` may list usual variants or tie-breakers—apply them when fit is close or ambiguous.

## User Workflow

- The user will paste the full job description in chat
- If the user starts the message with `Tailor:`, treat that as the trigger for this workflow
- Extract:
  - company name
  - role title
  - F-1 visa applicability signals
  - whether the role appears open to graduate or MBA candidates
  - core requirements
  - preferred requirements
  - keywords
  - main themes for prioritizing bullets
- **Select the best-matching base resume from `base/`** (see *Choosing the base resume*), then create outputs from that file
- Create a folder at `tailored/<Company_Name>/<Role_Name>/` at the repository root
- Save the pasted JD as `jd.md`
- Save your extraction and prioritization logic as `analysis.md` (include base resume choice and rationale first)
- Save the two-round critique and revision process as `review-loop.md`
- Save a change log as `diff.md` that compares the selected base resume against the tailored resume and explains why each change improves fit for the JD
- Save the tailored resume as `resume-tailored.md` only if there is no material eligibility concern, or if the user explicitly asks to proceed despite the concern
- When Word output is requested, generate `resume-tailored.docx` using `scripts/render_resume_docx.py` and prefer a contributor-specific local template over `base/template.docx` when one exists
- When submit-ready PDF output is requested, export `resume-tailored.docx` using the Word PDF pipeline in `base/PDF_PIPELINE.md`. If the contributor's local context defines `Final resume PDF basename`, use that filename by default in the same tailored folder.

## Review Loop

Use this default two-round workflow unless the user explicitly asks for a lighter pass:

### Round 1

- `Candidate Strategist`: identify the strongest truthful role narrative, the top bullets to lead with, and the most relevant JD themes to surface
- draft `resume-tailored.md`
- `HR Screener`: score recruiter/ATS fit, identify missing keywords, weak top-third signals, and major pass/fail concerns
- `Truth Guard`: check for overclaiming, unsupported skills, overstated ownership, prototype-vs-production confusion, and metrics that need tighter scope
- revise the resume based on feedback that survives truth-checking

### Round 2

- `HR Screener`: re-review the updated draft and focus only on remaining blockers or high-value improvements
- `Truth Guard`: re-check only newly introduced or changed claims
- revise once more and stop by default

### Interaction Rules

- Truth wins over optimization
- Unsupported-but-plausible additions go into a `Needs user confirmation` section in `review-loop.md`
- Clearly unsupported additions must not be added to the resume
- Limit each review round to the highest-value changes; avoid endless polishing loops

## Resume Constraints

- Keep the final resume to one page unless the user explicitly asks for a longer document
- For work experience, only reorder existing bullets from the **selected** base resume file based on JD importance in the first pass
- Trim lower-priority work-experience bullets in the first pass by removing bullets that are not important for the JD
- Do not invent experience
- Do not change the content of work-experience bullets in the first pass
- Use the contributor story bank to validate whether deeper wording changes are supported before making a stronger second-pass rewrite
- If a contributor-local Anderson-style guide exists, use it to shape bullet construction, verb choice, metric placement, and semicolon usage
- Before removing bullets, check for domain or industry alignment signals that may be uniquely valuable even if they are not the most direct functional match
- Preserve distinctive bullets that create strong industry resonance for the target company or user story, such as healthcare, security, AI, or developer-workflow alignment
- Produce the final tailored resume in Markdown
- It is acceptable to add a very short JD-aligned descriptor next to `SERVICENOW` when it materially improves fit, but it must remain short enough that `Hyderabad, India` stays on the same line in DOCX/PDF output
- In the `Additional` section:
  - reframe the competition item as needed to better match the JD
  - reorder items by JD importance
  - reorder skills internally by JD relevance so the most relevant skills appear first
  - reorder courses internally by JD relevance so the most relevant courses appear first
- Keep `Skills` to no more than 2 lines
- Keep `Courses` to 1 line
- In `analysis.md`, start with:
  - **Base resume selected** (path) and **rationale** for choosing it over other files in `base/`
  - F-1 visa applicability assessment
  - graduate/MBA eligibility assessment
  - current alignment score out of 10
- In `analysis.md`, explicitly suggest bullets that should be deprioritized or removed for the role
- In `analysis.md`, explicitly call out any domain-aligned bullets that should be preserved because they strengthen company or industry fit
- In `review-loop.md`, summarize for each round:
  - `Candidate Strategist` view
  - `HR Screener` feedback and score
  - `Truth Guard` feedback
  - edits applied
  - `Needs user confirmation` items, if any
- In `diff.md`, summarize:
  - bullets moved up and why
  - bullets removed or trimmed and why
  - reordered skills, courses, or additional items and why
  - any reframed non-work-experience items and why
  - any important JD themes that became more visible after tailoring
- If the JD appears incompatible with the user's profile, pause after the analysis and ask whether to proceed with tailoring
- After generating the first tailored resume, ask the user whether they want a second pass that modifies work-experience bullets further by removing bullets or changing language

## Bullet Ranking Framework

When deciding bullet order and which bullets to keep, optimize for likely HR or recruiter review first. Use this ranking framework:

1. eligibility fit
2. job function fit
3. industry and company resonance
4. seniority fit
5. customer or market proximity
6. cross-functional relevance
7. outcome strength
8. readability and scannability
9. distinctiveness

Additional guidance:

- Prefer bullets whose value is easy for a non-specialist reader to understand quickly
- Preserve bullets that create a clear narrative in the first 10 seconds of scanning
- Keep a balance of direct JD fit, company-specific resonance, and strong measurable outcomes
- Avoid overloading the resume with too many equally dense bullets
- For internship roles, make sure the overall story feels calibrated to internship-level hiring rather than overshooting the level

## File Priority

When working on a new application, read files in this order:

1. `contributors/local-context/RESUME_INDEX.local.md` if it exists
2. `base/RESUME_INDEX.md`
3. **Inventory** all resume candidates in `base/` (all `.md` except `README.md` and `RESUME_INDEX.md`); **with the JD in mind, pick one** and read it in full
4. relevant contributor-local files (`<name>.local.md`, `<name>.story-bank.local.md`, local style guide) if they exist and are relevant
5. `tailored/<Company_Name>/<Role_Name>/jd.md` if it already exists
6. `tailored/<Company_Name>/<Role_Name>/analysis.md` if it already exists
7. `tailored/<Company_Name>/<Role_Name>/review-loop.md` if it already exists

If you are continuing work on an existing `tailored/...` folder and `analysis.md` already states which base was used, you may re-read that same base file unless the user asks to switch variants.

## Goal

Create a JD-optimized resume for internship applications with minimal file reading and minimal repeated context gathering.
