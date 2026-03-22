#!/usr/bin/env python3
"""Test the local DOCX-to-PDF pipeline against a contributor-local reference pair."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path


def sha1(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def page_count(path: Path) -> int | None:
    try:
        data = path.read_bytes()
    except Exception:  # noqa: BLE001
        return None
    return len(re.findall(rb"/Type\s*/Page\b", data))


def render_pdf(docx_path: Path, output_pdf: Path) -> None:
    subprocess.run(
        [
            sys.executable,
            "scripts/render_docx_pdf.py",
            str(docx_path),
            "-o",
            str(output_pdf),
        ],
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx_path", help="Path to contributor-local .docx template")
    parser.add_argument(
        "--expected-pdf",
        help="Path to expected reference PDF. Defaults to swapping .docx for .expected.local.pdf",
    )
    args = parser.parse_args()

    docx_path = Path(args.docx_path).resolve()
    if not docx_path.exists():
        print(f"Missing DOCX: {docx_path}", file=sys.stderr)
        return 1

    expected_pdf = (
        Path(args.expected_pdf).resolve()
        if args.expected_pdf
        else docx_path.with_name(docx_path.name.replace(".resume-template.local.docx", ".resume-template.expected.local.pdf"))
    )
    if not expected_pdf.exists():
        print(f"Missing expected PDF: {expected_pdf}", file=sys.stderr)
        return 1

    generated_pdf = docx_path.with_name(docx_path.name.replace(".resume-template.local.docx", ".resume-template.generated.local.pdf"))

    try:
        render_pdf(docx_path, generated_pdf)
    except Exception as exc:  # noqa: BLE001
        print(f"Test export failed: {exc}", file=sys.stderr)
        return 1

    expected_size = expected_pdf.stat().st_size
    generated_size = generated_pdf.stat().st_size
    expected_pages = page_count(expected_pdf)
    generated_pages = page_count(generated_pdf)
    expected_sha = sha1(expected_pdf)
    generated_sha = sha1(generated_pdf)

    print(f"expected_pdf={expected_pdf}")
    print(f"generated_pdf={generated_pdf}")
    print(f"expected_size={expected_size}")
    print(f"generated_size={generated_size}")
    print(f"expected_pages={expected_pages}")
    print(f"generated_pages={generated_pages}")
    print(f"expected_sha1={expected_sha}")
    print(f"generated_sha1={generated_sha}")
    print(f"page_count_match={expected_pages == generated_pages}")
    print(f"byte_identical={expected_sha == generated_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
