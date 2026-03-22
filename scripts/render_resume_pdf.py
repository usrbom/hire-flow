#!/usr/bin/env python3
"""Render a fixed-structure resume Markdown file to PDF via headless Chrome."""

from __future__ import annotations

import argparse
import html
import shutil
import subprocess
import sys
from pathlib import Path


SECTION_EDUCATION = "EDUCATION"
SECTION_EXPERIENCE = "EXPERIENCE"
SECTION_ADDITIONAL = "ADDITIONAL"


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def nonempty(lines: list[str]) -> list[str]:
    return [line.rstrip() for line in lines if line.strip()]


def parse_resume(path: Path) -> dict:
    lines = read_lines(path)
    idx = 0

    while idx < len(lines) and (not lines[idx].strip() or lines[idx].startswith("# ")):
        idx += 1
    if idx + 1 >= len(lines):
        raise ValueError("Resume Markdown is missing name/contact header.")

    name = lines[idx].strip()
    contact = lines[idx + 1].strip()
    idx += 2

    sections: dict[str, list[str]] = {}
    current_section = None
    buffer: list[str] = []

    while idx < len(lines):
        line = lines[idx].rstrip()
        if line.startswith("## "):
            if current_section is not None:
                sections[current_section] = buffer[:]
            current_section = line[3:].strip().upper()
            buffer = []
        elif current_section is not None:
            buffer.append(line)
        idx += 1

    if current_section is not None:
        sections[current_section] = buffer[:]

    return {
        "name": name,
        "contact": contact,
        "education": parse_education(sections.get(SECTION_EDUCATION, [])),
        "experience": parse_experience(sections.get(SECTION_EXPERIENCE, [])),
        "additional": parse_additional(sections.get(SECTION_ADDITIONAL, [])),
    }


def split_bold_line(line: str) -> tuple[str, str]:
    if not line.startswith("**") or "**" not in line[2:]:
        raise ValueError(f"Expected bold entry line, got: {line}")
    end = line.find("**", 2)
    primary = line[2:end].strip()
    secondary = line[end + 2 :].strip()
    return primary, secondary


def parse_education(lines: list[str]) -> list[dict]:
    items = nonempty(lines)
    entries: list[dict] = []
    idx = 0
    while idx < len(items):
        school, location = split_bold_line(items[idx])
        idx += 1
        if idx >= len(items):
            raise ValueError("Education entry missing degree line.")
        degree = items[idx]
        idx += 1
        bullets: list[str] = []
        while idx < len(items) and not items[idx].startswith("**"):
            if items[idx].startswith("- "):
                bullets.append(items[idx][2:].strip())
            idx += 1
        entries.append(
            {"school": school, "location": location, "degree": degree, "bullets": bullets}
        )
    return entries


def parse_experience(lines: list[str]) -> list[dict]:
    items = lines[:]
    entries: list[dict] = []
    idx = 0
    while idx < len(items):
        line = items[idx].strip()
        if not line:
            idx += 1
            continue
        company, location = split_bold_line(line)
        idx += 1
        while idx < len(items) and not items[idx].strip():
            idx += 1
        if idx >= len(items):
            raise ValueError("Experience entry missing title line.")
        title_line = items[idx].strip()
        idx += 1
        groups: list[dict] = []
        current_group = None
        while idx < len(items):
            raw = items[idx].rstrip()
            stripped = raw.strip()
            if not stripped:
                idx += 1
                continue
            if stripped.startswith("**"):
                break
            if stripped.startswith("### "):
                current_group = {"name": stripped[4:].strip(), "bullets": []}
                groups.append(current_group)
            elif stripped.startswith("- "):
                if current_group is None:
                    current_group = {"name": "", "bullets": []}
                    groups.append(current_group)
                current_group["bullets"].append(stripped[2:].strip())
            idx += 1
        entries.append(
            {"company": company, "location": location, "title_line": title_line, "groups": groups}
        )
    return entries


def parse_additional(lines: list[str]) -> list[dict]:
    items = []
    for line in nonempty(lines):
        if not line.startswith("- "):
            continue
        content = line[2:].strip()
        if ":" in content:
            label, value = content.split(":", 1)
            items.append({"label": label.strip(), "value": value.strip()})
        else:
            items.append({"label": "", "value": content})
    return items


def esc(value: str) -> str:
    return html.escape(value, quote=False)


def render_html(data: dict, title: str) -> str:
    education_html = "".join(render_education_entry(entry) for entry in data["education"])
    experience_html = "".join(render_experience_entry(entry) for entry in data["experience"])
    additional_html = "".join(render_additional_item(item) for item in data["additional"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <style>
    @page {{
      size: Letter;
      margin: 0.42in 0.52in 0.42in 0.52in;
    }}
    html, body {{
      margin: 0;
      padding: 0;
      background: white;
      color: #111;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    body {{
      font-size: 9.2pt;
      line-height: 1.22;
    }}
    .page {{
      width: 100%;
    }}
    .header {{
      text-align: center;
      margin-bottom: 0.12in;
    }}
    .name {{
      font-size: 16.5pt;
      font-weight: 700;
      letter-spacing: 0.4px;
      margin-bottom: 3px;
    }}
    .contact {{
      font-size: 9pt;
    }}
    .section {{
      margin-top: 0.08in;
    }}
    .section-title {{
      font-size: 9.2pt;
      font-weight: 700;
      letter-spacing: 0.7px;
      border-bottom: 1px solid #111;
      padding-bottom: 2px;
      margin-bottom: 6px;
    }}
    .entry {{
      margin-bottom: 6px;
    }}
    .entry-head {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: baseline;
      font-weight: 700;
    }}
    .entry-subhead {{
      margin-top: 1px;
      margin-bottom: 2px;
    }}
    .location {{
      white-space: nowrap;
      text-align: right;
      font-weight: 700;
    }}
    .group-title {{
      font-style: italic;
      font-weight: 700;
      margin: 4px 0 1px 0;
    }}
    ul {{
      margin: 2px 0 0 14px;
      padding: 0;
    }}
    li {{
      margin: 0 0 1px 0;
    }}
    .additional-list {{
      margin-top: 1px;
    }}
    .additional-item {{
      margin-bottom: 2px;
    }}
    .additional-label {{
      font-weight: 700;
    }}
  </style>
</head>
<body>
  <main class="page">
    <header class="header">
      <div class="name">{esc(data["name"])}</div>
      <div class="contact">{esc(data["contact"])}</div>
    </header>
    <section class="section">
      <div class="section-title">EDUCATION</div>
      {education_html}
    </section>
    <section class="section">
      <div class="section-title">EXPERIENCE</div>
      {experience_html}
    </section>
    <section class="section">
      <div class="section-title">ADDITIONAL</div>
      <div class="additional-list">{additional_html}</div>
    </section>
  </main>
</body>
</html>
"""


def render_education_entry(entry: dict) -> str:
    bullets = "".join(f"<li>{esc(bullet)}</li>" for bullet in entry["bullets"])
    bullet_block = f"<ul>{bullets}</ul>" if bullets else ""
    return f"""
    <div class="entry">
      <div class="entry-head">
        <div>{esc(entry["school"])}</div>
        <div class="location">{esc(entry["location"])}</div>
      </div>
      <div class="entry-subhead">{esc(entry["degree"])}</div>
      {bullet_block}
    </div>
    """


def render_experience_entry(entry: dict) -> str:
    groups_html = []
    for group in entry["groups"]:
        group_title = (
            f'<div class="group-title">{esc(group["name"])}</div>' if group["name"] else ""
        )
        bullets = "".join(f"<li>{esc(bullet)}</li>" for bullet in group["bullets"])
        groups_html.append(f"{group_title}<ul>{bullets}</ul>")
    return f"""
    <div class="entry">
      <div class="entry-head">
        <div>{esc(entry["company"])}</div>
        <div class="location">{esc(entry["location"])}</div>
      </div>
      <div class="entry-subhead">{esc(entry["title_line"])}</div>
      {''.join(groups_html)}
    </div>
    """


def render_additional_item(item: dict) -> str:
    if item["label"]:
        return (
            f'<div class="additional-item"><span class="additional-label">{esc(item["label"])}:'
            f'</span> {esc(item["value"])}</div>'
        )
    return f'<div class="additional-item">{esc(item["value"])}</div>'


def find_chrome() -> str:
    candidates = [
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise FileNotFoundError("Could not find a Chrome/Chromium binary for PDF generation.")


def render_pdf(markdown_path: Path, output_pdf: Path, keep_html: bool) -> None:
    data = parse_resume(markdown_path)
    html_path = output_pdf.with_suffix(".html")
    html_path.write_text(render_html(data, markdown_path.stem), encoding="utf-8")

    chrome = find_chrome()
    command = [
        chrome,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output_pdf}",
        "--no-pdf-header-footer",
        html_path.resolve().as_uri(),
    ]
    subprocess.run(command, check=True)

    if not keep_html:
        html_path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown_path", help="Path to resume Markdown file")
    parser.add_argument(
        "-o",
        "--output",
        help="Output PDF path. Defaults to the same path with .pdf extension.",
    )
    parser.add_argument(
        "--keep-html",
        action="store_true",
        help="Keep the intermediate HTML file for debugging.",
    )
    args = parser.parse_args()

    markdown_path = Path(args.markdown_path).resolve()
    if not markdown_path.exists():
        print(f"Missing input file: {markdown_path}", file=sys.stderr)
        return 1

    output_pdf = Path(args.output).resolve() if args.output else markdown_path.with_suffix(".pdf")
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    try:
        render_pdf(markdown_path, output_pdf, args.keep_html)
    except Exception as exc:  # noqa: BLE001
        print(f"PDF generation failed: {exc}", file=sys.stderr)
        return 1

    print(output_pdf)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
