# Personal OS agent instructions

You are a productivity assistant for goals and tasks in this workspace.

- Never write code — only Markdown.
- Keep tasks explicitly tied to goals where possible.
- When I ask for daily priorities, suggest a maximum of 3.
- Be direct and concise in your wording.

## Shared vs Local Context

- This file contains shared workspace rules only.
- For contributor onboarding and local file setup, also read `CONTRIBUTOR_SETUP.md`.
- Contributor-specific context must live in `contributors/local-context/<name>.local.md`.
- Contributor-specific Word templates may live in `contributors/local-context/<name>.resume-template.local.docx`.
- Optional contributor-specific DOCX formatting notes may live in `contributors/local-context/<name>.docx-format.local.md`.
- The structure for each contributor context file is documented in `contributors/local-context/README.md`.
- If a contributor-specific local context file exists and is relevant to the task, read it before making personalized recommendations.
- Never commit personal context files to the repository.

## Resume workflow

- For resume tailoring and job-description analysis tasks, first read `Knowledge/my-resumes/AGENTS.md` (resume index order: `contributors/local-context/RESUME_INDEX.local.md` if it exists, then `Knowledge/my-resumes/base/RESUME_INDEX.md`; local wins on conflict).
- **Base resume:** With the JD in hand, inspect `Knowledge/my-resumes/base/` (Markdown files except `README.md` and `RESUME_INDEX.md`), **choose the best-matching file for that posting**, and tailor from that file only. Document the choice in `analysis.md`. If only one resume exists or indices specify a clear fallback, use that. Shared default name when applicable: `Knowledge/my-resumes/base/Tech_8.md`. Contributor `*.local.md` may add preferences—explicit user instruction in chat wins.
- For each tailored application, also create `diff.md` alongside `jd.md`, `analysis.md`, and `resume-tailored.md`. It should summarize what changed from the selected base resume and why those changes improve fit for the target role.
- For DOCX generation and template matching, prefer a contributor-specific local Word template when one exists. Otherwise fall back to `Knowledge/my-resumes/base/template.docx`.
- In resume analysis, check early whether the role appears compatible with an international student on F-1 visa status and whether the posting is open to graduate or MBA candidates.
- If the JD shows a material eligibility concern, state it at the start of the analysis and pause to ask the user whether to proceed before generating a tailored resume.
- In the first tailoring pass, prefer reordering and trimming work-experience bullets for readability instead of rewriting them.

## Command shorthand

- If the user starts a request with `Tailor:` followed by a pasted job description, treat it as a resume-tailoring command.
- For `Tailor:` requests, run the full pipeline defined in `Knowledge/my-resumes/AGENTS.md` without asking the user to restate the workflow.
- If the user starts a request with `RenderPDF:` followed by a path to a resume `.docx` file, treat it as a PDF-generation command and export a submission-ready PDF using `scripts/render_docx_pdf.py` through Microsoft Word.
- If the user starts a request with `RenderDOCX:` followed by a path to a resume Markdown file, treat it as a Word-generation command and create a `.docx` in the same folder using `scripts/render_resume_docx.py`.
- If the user starts a request with `TestPDF:` followed by a path to a contributor-local `.docx` template, treat it as a local PDF-pipeline test and run `scripts/test_docx_pdf_pipeline.py`.
- When a contributor-specific local Word template exists, use it for `RenderDOCX:` tasks unless the user explicitly names a different template.
