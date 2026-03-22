# Resume PDF Pipeline

This repository can generate a submit-ready PDF from a generated resume `.docx` file using Microsoft Word.

## Source of truth

- Content source for final PDF export: `resume-tailored.docx`
- Shared fallback DOCX template: `Knowledge/my-resumes/base/template.docx`
- Contributor-local override: `contributors/local-context/<name>.resume-template.local.docx`

## Generator

Use:

```bash
python3 scripts/render_docx_pdf.py <path-to-resume-docx>
```

Example:

```bash
python3 scripts/render_docx_pdf.py tailored/Nasuni/MBA_Product_Marketing_Intern/resume-tailored.docx
```

This will generate:

```text
tailored/Nasuni/MBA_Product_Marketing_Intern/resume-tailored.pdf
```

## Requirements

- Python 3
- Microsoft Word installed locally
- macOS with `osascript` available

The current renderer uses Microsoft Word automation to export the `.docx` to PDF.

## For tailored applications

Standard expected files per completed application:

- `jd.md`
- `analysis.md`
- `diff.md`
- `resume-tailored.md`
- `resume-tailored.pdf` when a submission PDF has been generated locally

## Notes

- The recommended path is `Markdown -> DOCX -> PDF`
- The PDF is exported from Word so it can preserve the tuned DOCX layout more reliably than direct Markdown-to-PDF conversion
- No direct Markdown-to-PDF path is used in the current workflow

## Local pipeline test

To test Word export against a contributor-local reference pair:

```bash
python3 scripts/test_docx_pdf_pipeline.py contributors/local-context/<name>.resume-template.local.docx
```

This expects a matching file:

```text
contributors/local-context/<name>.resume-template.expected.local.pdf
```

The test writes:

```text
contributors/local-context/<name>.resume-template.generated.local.pdf
```

and reports:

- generated path
- expected and generated file sizes
- expected and generated page counts
- expected and generated SHA1 values

`byte_identical=false` does not necessarily mean the export is visually wrong, since PDF metadata may differ across exports.
