#!/usr/bin/env python3
"""Export a DOCX file to PDF using Microsoft Word via AppleScript."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCAL_CONTEXT_DIR = ROOT / "contributors" / "local-context"


def run_osascript(docx_path: Path, pdf_path: Path) -> None:
    script = f'''
on run
  set inputPath to POSIX file "{docx_path}" as alias
  set outputPath to "{pdf_path}"
  tell application "Microsoft Word"
    activate
    open inputPath
    set docRef to active document
    save as docRef file name outputPath file format format PDF
    close docRef saving no
  end tell
end run
'''
    subprocess.run(["osascript", "-e", script], check=True)


def read_pdf_basename(local_context_path: Path) -> str | None:
    try:
        text = local_context_path.read_text(encoding="utf-8")
    except Exception:  # noqa: BLE001
        return None

    match = re.search(r"^- Final resume PDF basename:\s*(.+?)\s*$", text, re.MULTILINE)
    if not match:
        return None

    basename = match.group(1).strip()
    if not basename or "/" in basename:
        return None
    return basename


def infer_contributor() -> str | None:
    if not LOCAL_CONTEXT_DIR.exists():
        return None

    candidates: list[str] = []
    for path in LOCAL_CONTEXT_DIR.glob("*.local.md"):
        if path.name == "RESUME_INDEX.local.md":
            continue
        if not re.fullmatch(r"[^.]+\.local\.md", path.name):
            continue
        if not read_pdf_basename(path):
            continue
        candidates.append(path.stem.removesuffix(".local"))

    candidates.sort()
    if len(candidates) == 1:
        return candidates[0]
    return None


def resolve_output_path(docx_path: Path, explicit_output: str | None, contributor: str | None) -> Path:
    if explicit_output:
        return Path(explicit_output).resolve()

    contributor_name = contributor or infer_contributor()
    if contributor_name:
        local_context_path = LOCAL_CONTEXT_DIR / f"{contributor_name}.local.md"
        pdf_basename = read_pdf_basename(local_context_path)
        if pdf_basename:
            return docx_path.with_name(f"{pdf_basename}.pdf")

    return docx_path.with_suffix(".pdf")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx_path", help="Path to source .docx file")
    parser.add_argument("-o", "--output", help="Output .pdf path")
    parser.add_argument(
        "--contributor",
        help="Contributor name matching contributors/local-context/<name>.local.md",
    )
    args = parser.parse_args()

    docx_path = Path(args.docx_path).resolve()
    if not docx_path.exists():
        print(f"Missing input file: {docx_path}", file=sys.stderr)
        return 1
    if docx_path.suffix.lower() != ".docx":
        print("Input file must be a .docx", file=sys.stderr)
        return 1

    output_path = resolve_output_path(docx_path, args.output, args.contributor)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        run_osascript(docx_path, output_path)
    except Exception as exc:  # noqa: BLE001
        print(f"PDF export via Word failed: {exc}", file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
