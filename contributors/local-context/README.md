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
- preferred final resume PDF basename
- preferred Word template
- application constraints

## File naming

Create one local file per contributor using this pattern:

- `<name>.local.md`
- `<name>.resume-template.local.docx`
- `<name>.docx-format.local.md` (optional)
- `<name>.story-bank.local.md` (optional)
- `<name>-style-guide.local.md` or similar local-only style reference (optional)

Examples:

- `utkarsh.local.md`
- `utkarsh.resume-template.local.docx`
- `utkarsh.docx-format.local.md`
- `utkarsh.story-bank.local.md`
- `anderson-style-guide.local.md`
- `alex.local.md`
- `sam.local.md`

These files are ignored by Git and should not be committed.

### Resume workflow (local index)

- **Optional:** `RESUME_INDEX.local.md` — read **first** when it exists, then read `Knowledge/my-resumes/base/RESUME_INDEX.md`. Where this file conflicts with the shared index, follow the local file. If this file is missing, use only the shared `RESUME_INDEX.md`.
- Tailoring still requires **JD-aware choice** among all resume `.md` files in `Knowledge/my-resumes/base/`; the local index may list usual variants and tie-breakers only.

### Word template workflow

- **Optional:** `<name>.resume-template.local.docx` — your local Word reference template for DOCX generation and formatting matching
- **Optional:** `<name>.docx-format.local.md` — notes about layout rules that are specific to your Word template, such as font sizes, section spacing, hyperlink formatting, date alignment, or single-page constraints
- **Optional:** `<name>.story-bank.local.md` — expanded bullet facts, safe phrasing, deeper project context, and adjacent skills that support truthful tailoring
- **Optional:** local bullet-style guide such as `anderson-style-guide.local.md` — a reusable writing guide for bullet rhythm, verb choice, metric placement, and tone
- These files are local-only and ignored by Git
- If both exist, the agent should use the `.docx` file as the source of truth for structure and use the `.md` notes as contributor-specific exceptions or clarifications
- If no contributor-local Word template exists, the shared fallback is `Knowledge/my-resumes/base/template.docx`

## How the agent should use this folder

- Shared workflow rules live in `AGENTS.md` and `Knowledge/my-resumes/base/RESUME_INDEX.md`.
- For resume tailoring, read `RESUME_INDEX.local.md` first if it exists, then the shared resume index (merge: local wins on conflict).
- Personal context should be read from the relevant `<name>.local.md` file when a task requires personalized recommendations.
- For resume tailoring, the agent should also use the relevant story bank and bullet-style guide when those files exist.
- For DOCX generation or DOCX tuning, use `<name>.resume-template.local.docx` when available.
- If no local context file is available, the agent should continue with the shared workflow and ask for missing personal context only when needed.

## Recommended structure

Copy the headings from `USER_CONTEXT.template.md` into your own local file and fill them in with your details.

Keep entries concise and easy to scan.

## How to provide a personal Word template

1. Export or save a Word version of your preferred resume format as `.docx`.
2. Place it in this folder using the name pattern:
   - `<name>.resume-template.local.docx`
3. If needed, add a notes file:
   - `<name>.docx-format.local.md`
4. In that notes file, capture only template-specific rules that are not obvious from the document itself.

Useful notes include:

- exact font sizes for key lines
- date and location alignment expectations
- hyperlink display and target rules
- section spacing rules
- whether the resume must stay on one page

For contributor-specific final PDF naming, add this field to `<name>.local.md`:

- `Final resume PDF basename: <your_preferred_filename_without_.pdf>`

Example:

- `Final resume PDF basename: utkarsh_rawat_resume`

If this field exists, the PDF export pipeline should write `<your_preferred_filename_without_.pdf>.pdf` into the same folder as the source `.docx` by default.

Once those files exist, the agent can compare generated `.docx` output against the contributor's template and tune the generator accordingly.
