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
- Optional contributor-specific story banks may live in `contributors/local-context/<name>.story-bank.local.md`.
- Optional contributor-specific bullet style guides may live in `contributors/local-context/<name>-style-guide.local.md` or similar local-only Markdown files.
- The structure for each contributor context file is documented in `contributors/local-context/README.md`.
- If a contributor-specific local context file exists and is relevant to the task, read it before making personalized recommendations.
- Never commit personal context files to the repository.

## Resume workflow

- For resume tailoring and job-description analysis tasks, first read `Knowledge/my-resumes/AGENTS.md`.
- Use `contributors/local-context/RESUME_INDEX.local.md` first when it exists, then `Knowledge/my-resumes/base/RESUME_INDEX.md`.
- Keep root-level instructions thin; the resume-specific workflow should live in `Knowledge/my-resumes/AGENTS.md`.

## Command shorthand

- If the user starts a request with `Tailor:` followed by a pasted job description, treat it as a resume-tailoring command.
- For `Tailor:` requests, run the full pipeline defined in `Knowledge/my-resumes/AGENTS.md` without asking the user to restate the workflow.
- If the user starts a request with `RenderPDF:` followed by a path to a resume `.docx` file, treat it as a PDF-generation command and export a submission-ready PDF using `scripts/render_docx_pdf.py` through Microsoft Word.
- If the user starts a request with `RenderDOCX:` followed by a path to a resume Markdown file, treat it as a Word-generation command and create a `.docx` in the same folder using `scripts/render_resume_docx.py`.
- If the user starts a request with `TestPDF:` followed by a path to a contributor-local `.docx` template, treat it as a local PDF-pipeline test and run `scripts/test_docx_pdf_pipeline.py`.
- When a contributor-specific local Word template exists, use it for `RenderDOCX:` tasks unless the user explicitly names a different template.
- When a contributor-specific local context file defines `Final resume PDF basename`, use that as the default PDF filename for `RenderPDF:` tasks unless the user explicitly asks for a different output name.
