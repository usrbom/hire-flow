# Resume PDF Pipeline

This repository can generate a submit-ready PDF from a fixed-structure resume Markdown file.

## Source of truth

- Content source: `resume-tailored.md` or another resume Markdown file that follows `PDF_EXPORT_SPEC.md`
- Visual contract: `Knowledge/my-resumes/base/Tech_8.pdf`
- Structure contract: `Knowledge/my-resumes/base/PDF_EXPORT_SPEC.md`

## Generator

Use:

```bash
python3 scripts/render_resume_pdf.py <path-to-resume-markdown>
```

Example:

```bash
python3 scripts/render_resume_pdf.py tailored/Nasuni/MBA_Product_Marketing_Intern/resume-tailored.md
```

This will generate:

```text
tailored/Nasuni/MBA_Product_Marketing_Intern/resume-tailored.pdf
```

## Requirements

- Python 3
- Google Chrome or Chromium installed locally

The current renderer uses headless Chrome to print a fixed HTML layout to PDF.

## For tailored applications

Standard expected files per completed application:

- `jd.md`
- `analysis.md`
- `diff.md`
- `resume-tailored.md`
- `resume-tailored.pdf` when a submission PDF has been generated locally

## Expected output behavior

- one-page resume layout optimized for U.S. letter size
- fixed section order
- stable typography and spacing
- predictable export from the shared Markdown schema

## Notes

- The PDF is generated from the Markdown content, not copied from the original base PDF
- Exact visual parity with the original PDF may still require CSS tuning over time
- The renderer assumes the resume follows the shared section and line structure
- If the Markdown breaks the shared contract, the renderer may fail or produce poor layout
