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

## Session File Caching

- If any of the following files were already read earlier in the current conversation session, **do not re-read them** — use the version already in context:
  - `contributors/local-context/<name>.local.md`
  - `contributors/local-context/<name>.story-bank.local.md`
  - contributor-local Anderson-style guide
  - the selected base resume (e.g. `base/Tech_8.md`)
  - `base/RESUME_INDEX.md`
- Only re-read a file if the user indicates it has changed, or if it was not read in this session.
- This rule applies across multiple `Tailor:` commands within the same conversation.

## Choosing the base resume

- **When:** After the index files are read and the **job description** is available (from the user message or `tailored/.../jd.md`).
- **Where:** `Knowledge/my-resumes/base/`
- **What to consider:** Every **`.md`** file in that folder **except** `README.md` and `RESUME_INDEX.md`. Quickly compare each candidate to the JD: job title and level, required skills and stack, research vs product/engineering emphasis, data/ML vs general software, and which variant tells the strongest honest story for this posting.
- **Choose:** One file. Use that file’s work-experience bullets and structure as the **sole** source for first-pass tailoring (reorder/trim/reframe per rules—no inventing roles).
- **Document:** At the **top** of `analysis.md`, record **Base resume selected:** `<path>` and **Why:** one to three sentences. Then continue with F-1, graduate/MBA fit, and alignment as usual.
- **Hints:** `RESUME_INDEX.local.md` may list usual variants or tie-breakers—apply them when fit is close or ambiguous.

## User Workflow

There are two trigger modes with different output sets and review depth:

### Default Mode — `Tailor:`

Use when the user starts the message with `Tailor:` (no qualifier).

- Extract from the JD:
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
- **Required output files (default mode):**
  - `jd.md` — the pasted job description
  - `analysis.md` — base resume choice, eligibility assessment, fit score, bullet selection rationale
  - `resume-tailored.md` — the tailored resume (only if no material eligibility concern, or user confirms)
- Run **Pass 1 (Structure)** and a **light truth check** only — no full persona review loop, no Pass 2 micro-rewrite, no Narrative Gap Check
- After generating the resume, ask the user if they want a second pass that modifies bullets further
- `review-loop.md` and `diff.md` are **not generated** in default mode unless the user requests them

### Full Review Mode — `Tailor (full review):`

Use when the user starts the message with `Tailor (full review):`.

- Follow all steps in the Default Mode above, **plus:**
- Run the complete Review Loop (Pass 1 → Pass 2 → Pass 3 → Narrative Gap Check → Domain Resonance Check → Final Review)
- **Required output files (full review mode):**
  - `jd.md`
  - `analysis.md`
  - `review-loop.md` — full multi-pass critique and revision log
  - `diff.md` — change log comparing base resume to tailored resume
  - `resume-tailored.md`

### Shared Rules (both modes)

- When Word output is requested, generate a company-and-role-named `.docx` using `scripts/render_resume_docx.py` and prefer a contributor-specific local template over `base/template.docx` when one exists
  - default naming convention: `tailored/<Company>/<Role>/<Company>_<Role>.docx`
  - use filesystem-safe names that match the tailored folder naming style
- When submit-ready PDF output is requested, export `resume-tailored.docx` using the Word PDF pipeline in `base/PDF_PIPELINE.md`. If the contributor's local context defines `Final resume PDF basename`, use that filename by default in the same tailored folder.

## Review Loop

**This section applies only in `Tailor (full review):` mode**, or when the user explicitly requests a full review pass after an initial tailoring. In default `Tailor:` mode, skip this section entirely and run Pass 1 + light truth check only.

Use this workflow in full review mode:

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
- while editing each bullet, enforce contributor-local length rules immediately instead of waiting for a final cleanup pass:
  - standard bullets must stay at or under 230 characters when a contributor-local rule says `Standard bullet max length: 230 characters`
  - competition bullets may exceed the standard cap only when a contributor-local exception allows it
  - if a rewrite improves fit but breaks the character cap, trim it in the same editing pass before moving on
- skip rewrites for bullets that are already strong, already aligned, or would become riskier or stiffer after editing
- if a contributor-local Anderson-style guide exists, use it to shape bullet construction during this pass

### Pass 3: Truth + Fit Validation

- `HR Screener`: score recruiter/ATS content fit only, excluding visa and formal eligibility constraints; identify missing keywords, weak top-third signals, likely pass/fail concerns, and company-side adjustments needed to move the resume toward the interview sweet spot
- `Truth Guard`: check changed bullets for overclaiming, unsupported skills, overstated ownership, prototype-vs-production confusion, and metrics that need tighter scope
- revise the resume based on feedback that survives truth-checking
- re-check page fit and contributor-local compaction rules before DOCX generation
- during this page-fit check, use recent rendered DOCX calibration to estimate whether the draft is likely to leave more than about 2 to 3 blank lines at the bottom of the final Word document
- if the draft appears materially underfilled while still fitting on one page, consider a judged re-expansion pass before finalizing

### Optional Re-Expansion Pass

- use this only when the resume appears meaningfully underfilled and adding relevant content would improve overall quality
- do not try to fill all available white space
- treat this as an iterative judgment loop, not a one-shot add-back
- use recent rendered DOCX files in the same template as calibration references when estimating page fill from Markdown
- current calibration reference:
  - the Gen / MoneyLion marketplace resume left about 5 blank lines in the rendered Word document
  - that draft had 9 standard experience bullets mostly in the 176 to 212 character range
  - it also had 1 long competition bullet at 317 characters, 1 project bullet at 181 characters, and compact `Skills`, `Courses`, and `Interests` lines
  - practical takeaway: this content density is still slightly underfilled in the current template
- future estimation heuristic from that sample:
  - standard bullets around 175 to 210 characters usually behave like dense 2-line bullets in the current Word template
  - a long competition bullet around 300 to 370 characters usually behaves like a 3-line exception
  - if a draft with roughly the Gen density still shows about 5 blank lines, add back about 2 more lines of high-value content to target a final gap of 2 to 3 lines
  - the safest way to add those 2 lines is usually one more strong standard bullet or two modest bullet expansions of about 20 to 35 characters each
- target state for modification and finalization:
  - aim for no more than about 2 to 3 visible blank lines at the bottom of the rendered Word document
  - use Markdown-only estimates as a drafting heuristic, but treat the rendered DOCX as the final authority whenever it is available
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

### Narrative Gap Check

- `HR Screener` must explicitly identify:
  - the target role persona the JD wants
  - the current persona the resume projects
  - the top narrative gaps between the two
- for each major gap, classify the fix as one of:
  - fix now with reordering
  - fix now with supported rewrite
  - fix now with re-expansion
  - needs user confirmation
  - cannot fix honestly
- use this step to catch issues such as:
  - enterprise tone versus consumer-app tone
  - backend-heavy tone versus UX or customer-experience tone
  - underused company or domain language
  - missing but important role-language such as onboarding, user journey, usability, GTM, or roadmap

### Domain Resonance Check

- Before final compaction and again before DOCX generation, explicitly ask:
  - `Is there any domain-aligned story that materially improves company or industry fit even if it is not the strongest direct functional match?`
  - `Would removing it make the resume more generic for this company?`
- Run this check especially for roles in:
  - healthcare
  - education / edtech
  - cybersecurity
  - fintech / payments
  - developer tools
  - infrastructure / cloud
- For each domain-aligned story considered, classify it as:
  - `Must preserve`
  - `Nice to preserve`
  - `Safe to cut`
- A domain-aligned story should be marked `Must preserve` when all of the following are true:
  - it is truthful and supportable
  - it materially strengthens company or industry resonance
  - removing it would make the resume noticeably more generic
- Domain resonance can outweigh a weaker direct functional match when the story:
  - maps clearly to the target company's problem space
  - differentiates the candidate from a generic PM or technical resume
  - still fits on one page without forcing filler elsewhere
- Do not cut a `Must preserve` domain story unless:
  - it creates a truth risk
  - it creates a severe page-fit problem
  - a stronger domain-aligned story already covers the same signal
- In `review-loop.md`, explicitly note:
  - `Domain-specific stories preserved`
  - `Domain-specific stories removed`
  - a one-line reason for each meaningful preserve/remove decision

### Post-Render Validation

- after DOCX generation, treat the actual rendered page appearance as a final validation signal, not just the Markdown budget
- if the DOCX or exported PDF still looks materially underfilled, send the resume back through the iterative re-expansion loop
- do not rely only on Markdown bullet counts or character limits to judge balance
- use rendered appearance to make the final call on whether the page looks too sparse

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
- Treat post-render white space as a workflow signal: if the actual DOCX/PDF still looks too sparse, iterate again

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
- Treat contributor-local bullet-length rules as hard constraints during drafting, micro-rewrite, and re-expansion passes rather than as optional post-processing checks
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
- After `Final Review`, include a required `Narrative Gap Check` section.
- In `Narrative Gap Check`:
  - state the `Target Persona`
  - state the `Current Resume Persona`
  - list the `Top Narrative Gaps`
  - add a `Gap-to-Fix Mapping` that labels each gap as:
    - `Fix now with reordering`
    - `Fix now with supported rewrite`
    - `Fix now with re-expansion`
    - `Needs user confirmation`
    - `Cannot fix honestly`
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
- After DOCX generation, re-check whether the actual rendered page still looks underfilled; if it does, continue the same judged re-expansion logic until the page looks balanced or the next addition is no longer worth it

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
