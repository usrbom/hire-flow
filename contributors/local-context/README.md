# Local Contributor Context

This folder is for private contributor-specific files. Do not commit them.

For full setup instructions, read:

- `CONTRIBUTOR_SETUP.md`

## Common local file patterns

- `<name>.local.md`
- `<name>.resume-template.local.docx`
- `<name>.docx-format.local.md`
- `<name>.story-bank.local.md`
- `<name>-style-guide.local.md`
- `RESUME_INDEX.local.md`

## Agent behavior

- Read `RESUME_INDEX.local.md` before the shared resume index when it exists.
- Use `<name>.local.md` for contributor context.
- Use `<name>.story-bank.local.md` for truthful deeper rewrites.
- Use local style guides for bullet-writing rules when they exist.
- Use `<name>.resume-template.local.docx` and optional `.docx-format.local.md` for document generation and tuning.

## Notes

- Final PDF naming can be set in `<name>.local.md` with:
  - `Final resume PDF basename: <filename_without_.pdf>`
- The shared fallback DOCX template is `Knowledge/my-resumes/base/template.docx`.
