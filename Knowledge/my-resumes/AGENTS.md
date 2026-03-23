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

Use this default workflow unless the user explicitly asks for a lighter pass:

### Persona Mindsets

- `Candidate Strategist`
  - Think from the candidate side.
  - Goal: present the strongest honest version of the contributor for this role.
  - Focus on narrative strength, transferable fit, differentiated evidence, and what should be emphasized or cut.

- `HR Screener`
  - Think from the company side as a recruiter, recruiting coordinator, or first-pass hiring reviewer for this specific role.
  - Goal: decide whether the resume lands in the likely interview pile, and how to move it closer to that sweet spot.
  - Focus on top-third impression, scannability, role calibration, missing signals, likely rejection risks, and what would make the resume feel more obviously right for this company.
  - Do not behave like a pure keyword checker; act like a fast human screener using company-role judgment.

- `Truth Guard`
  - Think from a factual-risk and defensibility perspective.
  - Goal: ensure every claim remains supportable, calibrated, and interview-defensible.
  - Focus on ownership accuracy, metric scope, prototype-vs-production boundaries, and unsupported skills or wording.

### Pass 1: Structure

- `Candidate Strategist`: identify the strongest truthful role narrative, the top bullets to lead with, and the most relevant JD themes to surface
- choose which base bullets to keep, remove, and reorder
- draft `resume-tailored.md` with one-page fit in mind
- keep first-pass changes conservative:
  - reorder bullets
  - trim lower-value bullets
  - reorder `Additional`
  - add short company descriptors when useful and supported

### Pass 2: Selective Micro-Rewrite

- inspect every retained bullet, not just the top few
- rewrite only when all of the following are true:
  - the contributor story bank or existing resume content supports the change
  - the JD contains a meaningful keyword, theme, or framing improvement
  - the rewrite improves readability, scannability, or fit instead of just stuffing keywords
- allow light or moderate rewrites when helpful:
  - stronger verbs
  - clearer ownership
  - better metric placement
  - JD-aligned terminology
  - tighter business or domain framing
- skip rewrites for bullets that are already strong, already aligned, or would become riskier or stiffer after editing
- if a contributor-local Anderson-style guide exists, use it to shape bullet construction during this pass

### Pass 3: Truth + Fit Validation

- `HR Screener`: score recruiter/ATS content fit only, excluding visa and formal eligibility constraints; identify missing keywords, weak top-third signals, likely pass/fail concerns, and company-side adjustments needed to move the resume toward the interview sweet spot
- `Truth Guard`: check changed bullets for overclaiming, unsupported skills, overstated ownership, prototype-vs-production confusion, and metrics that need tighter scope
- revise the resume based on feedback that survives truth-checking
- re-check page fit and contributor-local compaction rules before DOCX generation
- if the draft appears materially underfilled while still fitting on one page, consider a judged re-expansion pass before finalizing

### Optional Re-Expansion Pass

- use this only when the resume appears meaningfully underfilled and adding relevant content would improve overall quality
- do not try to fill all available white space
- treat this as an iterative judgment loop, not a one-shot add-back
- make a judgment call after each iteration:
  - if remaining white space is small, leave the resume as-is
  - if remaining white space is clearly excessive, add back or slightly expand the highest-value supported content, then re-evaluate again
- prefer quality-improving additions in this order:
  - add back one strong experience bullet that improves JD fit
  - slightly expand a retained experience bullet where supported and useful
  - add or expand a high-value `Additional` item only if experience content is already strong
- never add filler just to consume space
- stop the loop when any of the following becomes true:
  - the page now looks balanced
  - the next addition would weaken focus or role fit
  - the next addition would create truth or readability risk
  - the page is becoming tight enough that further additions are not clearly worth it
- any re-added or expanded content must still pass truth-checking and page-fit validation

### Final Review

- `HR Screener`: re-review the updated draft for content fit only, still excluding visa and formal eligibility constraints, and focus only on remaining blockers, high-value improvements, and whether the resume now feels calibrated to the company's likely first-pass expectations
- `Truth Guard`: re-check only newly introduced or changed claims
- revise once more and stop by default

### Interaction Rules

- Truth wins over optimization
- Unsupported-but-plausible additions go into a `Needs user confirmation` section in `review-loop.md`
- Clearly unsupported additions must not be added to the resume
- If the JD introduces a business term, framing, or non-tool concept that is not stated verbatim in the base resume but is clearly supported by the contributor story bank or existing bullets, make the judgment directly and use it when it improves fit.
- If the JD introduces a specific tool, platform, system, certification, or other yes-or-no experience claim that is not supported by the base resume or contributor story bank, ask the user directly before adding it.
- Use targeted confirmation questions only when the answer changes whether a concrete tool or experience can be claimed.
- Limit each pass or final review to the highest-value changes; avoid endless polishing loops
- Enforce page-fit constraints during Markdown generation before DOCX generation
- Treat spare one-page space as something to use judgment on, not something to always minimize or always fill

## Resume Constraints

- Keep the final resume to one page unless the user explicitly asks for a longer document
- Use contributor-local fit and formatting rules when they exist.
- Otherwise use conservative defaults that aim to keep the resume on one page before DOCX generation.
- For work experience, only reorder existing bullets from the **selected** base resume file based on JD importance in the first pass
- Trim lower-priority work-experience bullets in the first pass by removing bullets that are not important for the JD
- Do not invent experience
- Do not change the content of work-experience bullets in the first pass
- After the first-pass structure draft, run a selective micro-rewrite pass across retained bullets
- In that micro-rewrite pass:
  - evaluate each retained bullet for possible JD-aligned improvement
  - rewrite only when the change is supported and materially improves fit or readability
  - do not rewrite bullets just to inject keywords
  - keep bullet meaning stable even when wording changes
- During that pass, distinguish between:
  - supported business-language adaptation, which can be applied directly
  - unsupported tool or platform claims, which require user confirmation before being added
- Use the contributor story bank to validate whether wording changes are supported before making them
- If a contributor-local Anderson-style guide exists, use it to shape bullet construction, verb choice, metric placement, semicolon usage, and overall bullet rhythm
- Before removing bullets, check for domain or industry alignment signals that may be uniquely valuable even if they are not the most direct functional match
- Preserve distinctive bullets that create strong industry resonance for the target company or user story, such as healthcare, security, AI, or developer-workflow alignment
- If the resume appears too sparse after compaction, selectively re-add or expand relevant material when that improves quality more than it harms concision
- Produce the final tailored resume in Markdown
- It is acceptable to add a very short JD-aligned descriptor next to `SERVICENOW` when it materially improves fit, but it must remain short enough that `Hyderabad, India` stays on the same line in DOCX/PDF output
- In the `Additional` section:
  - reframe the competition item as needed to better match the JD
  - reorder items by JD importance
  - reorder skills internally by JD relevance so the most relevant skills appear first
  - reorder courses internally by JD relevance so the most relevant courses appear first
  - avoid redundant signals across work experience and `Additional`
  - use contributor-local fit rules for project count, competition length, and other compaction choices when those rules exist
- Keep `Skills` to no more than 2 lines
- Keep `Courses` to 1 line
- In `analysis.md`, start with:
  - **Base resume selected** (path) and **rationale** for choosing it over other files in `base/`
  - F-1 visa applicability assessment
  - graduate/MBA eligibility assessment
  - current alignment score out of 10 for content fit, excluding visa and formal eligibility constraints
- In `analysis.md`, explicitly suggest bullets that should be deprioritized or removed for the role
- In `analysis.md`, explicitly call out any domain-aligned bullets that should be preserved because they strengthen company or industry fit
- In `review-loop.md`, summarize for each round:
  - `Candidate Strategist` view
  - `HR Screener` feedback and score for content fit only
  - `Truth Guard` feedback
  - edits applied
  - `Needs user confirmation` items, if any
  - `Page Fit` status if compaction was needed
- In `review-loop.md`, make the viewpoint switch explicit:
  - note what the `Candidate Strategist` wants to emphasize from the candidate side
  - note what the `HR Screener` would likely react to from the company side
  - note what the `Truth Guard` allows, softens, or blocks from the defensibility side
- In `review-loop.md`, make the pass structure clear:
  - `Pass 1: Structure`
  - `Pass 2: Selective Micro-Rewrite`
  - `Pass 3: Truth + Fit Validation`
  - `Final Review`
- End `review-loop.md` with a required `Improvement Opportunities` section.
- In `Improvement Opportunities`:
  - include only the highest-value remaining improvements, usually 3 to 6 items
  - explain what is still underused, imperfect, or missing for the JD
  - note why it matters for this role
  - state whether it can be fixed now, later, or only with user confirmation
  - when suggesting a language improvement, include a concrete copy-paste example of how the bullet could be rewritten
  - when suggesting an unsupported tool or platform claim, do not provide copy-paste resume language unless the user confirms the claim
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
- If the draft risks exceeding one page, compact in this order:
  - follow contributor-local fit rules first when they exist
  - then remove or compress the lowest-value non-core content while preserving JD fit and truthfulness
- If the draft remains well under one page after compaction, consider a judged re-expansion:
  - first add back the highest-value removed experience bullet, if one materially improves fit
  - then consider modest expansion of retained bullets
  - then consider one stronger `Additional` item if it improves role fit
  - after each addition, re-evaluate whether another iteration is still quality-improving
  - stop once the resume looks balanced; do not optimize for zero white space

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
