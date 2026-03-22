# Base Resumes

This directory is reserved for local-only base resume files.

Expected local contents may include:

- `Tech_8.md`
- `Tech_8.pdf`
- other private base variants as needed

Do not commit personal resume content to the public repository.

`RESUME_INDEX.md` remains tracked because it documents the shared workflow. Optional per-machine overrides belong in `contributors/local-context/RESUME_INDEX.local.md` (gitignored); agents read that file first when present, then this file.

When tailoring, agents compare **all resume `.md` files** in this folder (excluding `README.md` and `RESUME_INDEX.md`) to the job description and pick the best match before editing.
