# PDF Export Spec

This document defines the fixed Markdown structure required for generating a submission-ready PDF that matches the shared resume layout as closely as possible.

Reference layout:

- `Knowledge/my-resumes/base/Tech_8.pdf`

## Goal

Keep `resume-tailored.md` structured tightly enough that a future PDF renderer can map it into a stable one-page resume format without manual cleanup.

This spec does not itself generate the PDF. It defines the Markdown contract needed for reliable export.

## Required section order

Use this exact top-level order:

1. Name and contact line
2. `## EDUCATION`
3. `## EXPERIENCE`
4. `## ADDITIONAL`

Do not add other top-level sections unless the shared resume format changes for everyone.

## Header format

The first lines of the file must follow this pattern:

`FULL NAME`  
`phone | email | linkedin`

Keep the contact line on one line.

## Education format

Each school entry should use:

`**SCHOOL NAME** — City, State`  
`Degree / Program — Date`

Follow with concise bullets only when needed.

## Experience format

Use this order:

`**COMPANY** — City, Country`  
`Title progression — Date range`

Then use grouped subsection headers only if they already exist in the selected base resume and are part of the shared structure.

Current shared subsection pattern:

- `### Product Management`
- `### Cross-Functional Leadership`
- `### Data-Driven Impact`

Do not invent new subsection names unless the base resume variant already uses them.

## Bullet constraints

- Keep bullets concise and single-paragraph
- Do not create nested bullets
- Preserve strong measurable outcomes where possible
- Avoid bullets so long that they would likely force line-wrap expansion beyond the original template density

## Additional section format

Keep the section as a flat list of labeled lines, such as:

- `Competitions: ...`
- `Internship: ...`
- `Patent Application: ...`
- `Project: ...`
- `Skills: ...`
- `Courses: ...`
- `Certifications: ...`
- `Interests: ...`

Keep `Skills` to no more than 2 lines and `Courses` to 1 line.

## Export-safety rules

- Do not add tables
- Do not add images
- Do not add footnotes
- Do not add code blocks
- Do not add multi-column constructs
- Do not add arbitrary bolded summary paragraphs above `EDUCATION`
- Do not change heading capitalization

## PDF generation expectation

For future PDF export, `resume-tailored.md` should be treated as the source of truth for content, and `Tech_8.pdf` should be treated as the visual reference for layout.

If exact visual parity becomes a requirement, a dedicated rendering template will be needed. This spec is the content contract that makes that possible.
