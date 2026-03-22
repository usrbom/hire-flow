# Resume Tailoring Instructions

This directory is for internship resume tailoring.

## Start Here

- Read `contributors/local-context/RESUME_INDEX.local.md` if it exists, then read `base/RESUME_INDEX.md` (local wins on conflict; if no local file, only read `base/RESUME_INDEX.md`).
- **Do not assume a single default file until you have compared options.** After you have the job description, inventory **`base/`** (see *Choosing the base resume* below), pick the best match, then read **only that** Markdown file for tailoring.
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
- Save a change log as `diff.md` that compares the selected base resume against the tailored resume and explains why each change improves fit for the JD
- Save the tailored resume as `resume-tailored.md` only if there is no material eligibility concern, or if the user explicitly asks to proceed despite the concern
- When Word output is requested, generate `resume-tailored.docx` using `scripts/render_resume_docx.py` and prefer a contributor-specific local template over `base/template.docx` when one exists
- When submit-ready PDF output is requested, export `resume-tailored.docx` to `resume-tailored.pdf` using the Word PDF pipeline in `base/PDF_PIPELINE.md`

## Resume Constraints

- For work experience, only reorder existing bullets from the **selected** base resume file based on JD importance in the first pass
- Trim lower-priority work-experience bullets in the first pass by removing bullets that are not important for the JD
- Do not invent experience
- Do not change the content of work-experience bullets in the first pass
- Before removing bullets, check for domain or industry alignment signals that may be uniquely valuable even if they are not the most direct functional match
- Preserve distinctive bullets that create strong industry resonance for the target company or user story, such as healthcare, security, AI, or developer-workflow alignment
- Produce the final tailored resume in Markdown
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
4. `tailored/<Company_Name>/<Role_Name>/jd.md` if it already exists
5. `tailored/<Company_Name>/<Role_Name>/analysis.md` if it already exists

If you are continuing work on an existing `tailored/...` folder and `analysis.md` already states which base was used, you may re-read that same base file unless the user asks to switch variants.

## Goal

Create a JD-optimized resume for internship applications with minimal file reading and minimal repeated context gathering.
