#!/usr/bin/env python3
"""Export a DOCX file to PDF using Microsoft Word via AppleScript."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_osascript(docx_path: Path, pdf_path: Path) -> None:
    script = f'''
on run
  set inputPath to POSIX file "{docx_path}" as alias
  set outputPath to "{pdf_path}"
  tell application "Microsoft Word"
    activate
    open inputPath
    save as active document file name outputPath file format format PDF
    close active document saving no
  end tell
end run
'''
    subprocess.run(["osascript", "-e", script], check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx_path", help="Path to source .docx file")
    parser.add_argument("-o", "--output", help="Output .pdf path")
    args = parser.parse_args()

    docx_path = Path(args.docx_path).resolve()
    if not docx_path.exists():
        print(f"Missing input file: {docx_path}", file=sys.stderr)
        return 1
    if docx_path.suffix.lower() != ".docx":
        print("Input file must be a .docx", file=sys.stderr)
        return 1

    output_path = Path(args.output).resolve() if args.output else docx_path.with_suffix(".pdf")
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
