# Resume DOCX Pipeline

This repository supports generating resume `.docx` files from fixed-structure Markdown and tuning the output against a contributor-specific Word template.

## Source of truth

- Content source: `resume-tailored.md`
- Shared fallback template: `Knowledge/my-resumes/base/template.docx`
- Contributor-local override: `contributors/local-context/<name>.resume-template.local.docx`
- Optional contributor-local notes: `contributors/local-context/<name>.docx-format.local.md`

## Generator

Use:

```bash
python3 scripts/render_resume_docx.py <path-to-resume-markdown>
```

Example:

```bash
python3 scripts/render_resume_docx.py tailored/Nasuni/MBA_Product_Marketing_Intern/resume-tailored.md
```

To use a contributor-specific local template explicitly:

```bash
python3 scripts/render_resume_docx.py tailored/Nasuni/MBA_Product_Marketing_Intern/resume-tailored.md --template contributors/local-context/utkarsh.resume-template.local.docx
```

## Expected output

By default the generator writes a `.docx` into the same folder as the Markdown source:

```text
tailored/<Company>/<Role>/resume-tailored.docx
```

## Contributor-local template workflow

Each contributor can keep their own Word format by adding local-only files:

- `contributors/local-context/<name>.resume-template.local.docx`
- `contributors/local-context/<name>.docx-format.local.md` (optional)

These should stay uncommitted.

## How the agent should use local templates

When a contributor-specific template exists:

1. Use that `.docx` file as the primary formatting reference for DOCX generation and tuning.
2. Use the optional `.md` notes file only for exceptions or explicit formatting rules.
3. Keep the Markdown schema stable unless a layout requirement makes a schema change necessary.

If no local template exists, fall back to the shared `template.docx`.

## Tuning process

When generated DOCX output does not match the contributor template:

1. Compare the generated `.docx` against the contributor template at the Word XML level.
2. Identify mismatches in paragraph structure, tabs, numbering, spacing, font sizes, hyperlink styling, and page-length behavior.
3. Update the generator to clone or mimic the correct template paragraph structures.
4. Regenerate and iterate until the layout matches closely enough for submission.
