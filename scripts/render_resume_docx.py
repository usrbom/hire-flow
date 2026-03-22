#!/usr/bin/env python3
"""Render fixed-structure resume Markdown into a .docx by cloning template paragraph formatting."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.etree import ElementTree as ET

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

ET.register_namespace("w", W_NS)


def w_tag(name: str) -> str:
    return f"{{{W_NS}}}{name}"


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def nonempty(lines: list[str]) -> list[str]:
    return [line.rstrip() for line in lines if line.strip()]


def split_bold_line(line: str) -> tuple[str, str]:
    if not line.startswith("**") or "**" not in line[2:]:
        raise ValueError(f"Expected bold line, got: {line}")
    end = line.find("**", 2)
    return line[2:end].strip(), line[end + 2 :].strip()


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
    current = None
    buf: list[str] = []
    while idx < len(lines):
        line = lines[idx].rstrip()
        if line.startswith("## "):
            if current is not None:
                sections[current] = buf[:]
            current = line[3:].strip().upper()
            buf = []
        elif current is not None:
            buf.append(line)
        idx += 1
    if current is not None:
        sections[current] = buf[:]

    return {
        "name": name,
        "contact": contact,
        "education": parse_education(sections.get("EDUCATION", [])),
        "experience": parse_experience(sections.get("EXPERIENCE", [])),
        "additional": parse_additional(sections.get("ADDITIONAL", [])),
    }


def parse_education(lines: list[str]) -> list[dict]:
    items = nonempty(lines)
    out = []
    idx = 0
    while idx < len(items):
        school, location = split_bold_line(items[idx])
        idx += 1
        degree = items[idx].strip()
        idx += 1
        bullets = []
        while idx < len(items) and not items[idx].startswith("**"):
            if items[idx].startswith("- "):
                bullets.append(items[idx][2:].strip())
            idx += 1
        out.append({"school": school, "location": location, "degree": degree, "bullets": bullets})
    return out


def parse_experience(lines: list[str]) -> list[dict]:
    items = lines[:]
    out = []
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
        title_line = items[idx].strip()
        idx += 1
        groups = []
        current = None
        while idx < len(items):
            stripped = items[idx].strip()
            if not stripped:
                idx += 1
                continue
            if stripped.startswith("**"):
                break
            if stripped.startswith("### "):
                current = {"name": stripped[4:].strip(), "bullets": []}
                groups.append(current)
            elif stripped.startswith("- "):
                if current is None:
                    current = {"name": "", "bullets": []}
                    groups.append(current)
                current["bullets"].append(stripped[2:].strip())
            idx += 1
        out.append({"company": company, "location": location, "title_line": title_line, "groups": groups})
    return out


def parse_additional(lines: list[str]) -> list[dict]:
    out = []
    for line in nonempty(lines):
        if not line.startswith("- "):
            continue
        content = line[2:].strip()
        if ":" in content:
            label, value = content.split(":", 1)
            out.append({"label": label.strip(), "value": value.strip()})
        else:
            out.append({"label": "", "value": content})
    return out


def load_template(template_path: Path) -> tuple[ET.ElementTree, ET.Element, dict[str, ET.Element]]:
    with ZipFile(template_path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
    body = root.find(w_tag("body"))
    paras = body.findall(w_tag("p"))
    sect_pr = body.find(w_tag("sectPr"))
    if sect_pr is None:
        raise ValueError("Template missing section properties.")
    prototypes = {
        "name": paras[0],
        "contact": paras[1],
        "section_heading": paras[2],
        "edu_school": paras[3],
        "edu_degree": paras[4],
        "edu_bullet": paras[5],
        "edu_school_spaced": paras[8],
        "edu_bullet_last": paras[10],
        "exp_company": paras[12],
        "exp_title": paras[13],
        "exp_group": paras[14],
        "exp_bullet": paras[15],
        "exp_bullet_after_group": paras[18],
        "exp_bullet_after_resume_section": paras[27],
        "additional": paras[29],
    }
    return ET.ElementTree(root), sect_pr, prototypes


def clear_content(paragraph: ET.Element) -> ET.Element:
    ppr = paragraph.find(w_tag("pPr"))
    for child in list(paragraph):
        if child is not ppr:
            paragraph.remove(child)
    return ppr


def first_run_rpr(prototype: ET.Element, run_index: int = 0) -> ET.Element | None:
    runs = [child for child in prototype if child.tag == w_tag("r")]
    if run_index >= len(runs):
        return None
    rpr = runs[run_index].find(w_tag("rPr"))
    return copy.deepcopy(rpr) if rpr is not None else None


def hyperlink_run_rpr(prototype: ET.Element, hyperlink_index: int = 0, run_index: int = 0) -> ET.Element | None:
    hyperlinks = [child for child in prototype if child.tag == w_tag("hyperlink")]
    if hyperlink_index >= len(hyperlinks):
        return None
    runs = [child for child in hyperlinks[hyperlink_index] if child.tag == w_tag("r")]
    if run_index >= len(runs):
        return None
    rpr = runs[run_index].find(w_tag("rPr"))
    return copy.deepcopy(rpr) if rpr is not None else None


def set_run_size(rpr: ET.Element | None, half_points: int) -> ET.Element | None:
    if rpr is None:
        return None
    for child in rpr.findall(w_tag("sz")):
        child.set(w_tag("val"), str(half_points))
    for child in rpr.findall(w_tag("szCs")):
        child.set(w_tag("val"), str(half_points))
    return rpr


def make_run(text: str, rpr: ET.Element | None = None, *, tab=False) -> ET.Element:
    run = ET.Element(w_tag("r"))
    if rpr is not None:
        run.append(copy.deepcopy(rpr))
    if tab:
        run.append(ET.Element(w_tag("tab")))
    if text:
        t = ET.SubElement(run, w_tag("t"))
        t.set(f"{{{XML_NS}}}space", "preserve")
        t.text = text
    return run


def clone_para(prototype: ET.Element) -> ET.Element:
    return copy.deepcopy(prototype)


def set_single_text(paragraph: ET.Element, text: str, *, rpr: ET.Element | None = None) -> ET.Element:
    clear_content(paragraph)
    paragraph.append(make_run(text, rpr or first_run_rpr(paragraph)))
    return paragraph


def build_name_para(prototype: ET.Element, name: str) -> ET.Element:
    para = clone_para(prototype)
    set_single_text(para, name, rpr=first_run_rpr(prototype, 0))
    return para


def build_contact_para(prototype: ET.Element, contact: str) -> ET.Element:
    para = clone_para(prototype)
    clear_content(para)
    parts = [part.strip() for part in contact.split("|")]
    phone = parts[0] if len(parts) > 0 else ""
    email = parts[1] if len(parts) > 1 else ""
    linkedin = parts[2] if len(parts) > 2 else "linkedin.com/in/utkarsh-rawat"

    para.append(make_run(f"{phone} | ", first_run_rpr(prototype, 0)))
    para.append(make_run(f"{email} | ", first_run_rpr(prototype, 2) or first_run_rpr(prototype, 0)))

    hyperlink = ET.Element(w_tag("hyperlink"))
    hyperlink.set(f"{{{R_NS}}}id", "rId7")
    hyperlink.append(
        make_run(
            "linkedin.com/in/utkarsh-rawat",
            hyperlink_run_rpr(prototype, 1, 0) or first_run_rpr(prototype, 0),
        )
    )
    para.append(hyperlink)
    return para


def build_section_heading(prototype: ET.Element, text: str) -> ET.Element:
    para = clone_para(prototype)
    set_single_text(para, text, rpr=first_run_rpr(prototype, 0))
    return para


def build_school_para(prototype: ET.Element, school_text: str, location_text: str) -> ET.Element:
    para = clone_para(prototype)
    clear_content(para)
    school_rpr = set_run_size(first_run_rpr(prototype, 0), 22)
    para.append(make_run(school_text, school_rpr))
    para.append(make_run("", first_run_rpr(prototype, 0), tab=True))
    has_spell_markers = any(child.tag == w_tag("proofErr") for child in prototype)
    if has_spell_markers and "," in location_text:
        city, country = location_text.split(",", 1)
        proof_start = ET.Element(w_tag("proofErr"))
        proof_start.set(w_tag("type"), "spellStart")
        para.append(proof_start)
        para.append(make_run(city.strip(), first_run_rpr(prototype, 2) or first_run_rpr(prototype, 1)))
        proof_end = ET.Element(w_tag("proofErr"))
        proof_end.set(w_tag("type"), "spellEnd")
        para.append(proof_end)
        para.append(make_run("," + country, first_run_rpr(prototype, 3) or first_run_rpr(prototype, 2)))
    else:
        para.append(make_run(" ", first_run_rpr(prototype, 1) or first_run_rpr(prototype, 0)))
        para.append(make_run(location_text, first_run_rpr(prototype, 2) or first_run_rpr(prototype, 1)))
    return para


def build_company_para(prototype: ET.Element, company_text: str, location_text: str) -> ET.Element:
    para = clone_para(prototype)
    clear_content(para)
    para.append(make_run(company_text, first_run_rpr(prototype, 0)))
    para.append(make_run("", first_run_rpr(prototype, 1) or first_run_rpr(prototype, 0), tab=True))
    para.append(make_run("          ", first_run_rpr(prototype, 1) or first_run_rpr(prototype, 0)))
    para.append(make_run(location_text, first_run_rpr(prototype, 2) or first_run_rpr(prototype, 1)))
    return para


def build_edu_degree_para(prototype: ET.Element, degree_text: str, date_text: str) -> ET.Element:
    para = clone_para(prototype)
    clear_content(para)
    para.append(make_run(degree_text, first_run_rpr(prototype, 0)))
    para.append(make_run("", first_run_rpr(prototype, 1) or first_run_rpr(prototype, 0), tab=True))
    para.append(make_run("", first_run_rpr(prototype, 1) or first_run_rpr(prototype, 0), tab=True))
    para.append(make_run("            ", first_run_rpr(prototype, 1) or first_run_rpr(prototype, 0)))
    para.append(make_run(date_text, first_run_rpr(prototype, 3) or first_run_rpr(prototype, 1)))
    return para


def build_exp_title_para(prototype: ET.Element, title_text: str, date_text: str) -> ET.Element:
    para = clone_para(prototype)
    clear_content(para)
    para.append(make_run(title_text, first_run_rpr(prototype, 0)))
    para.append(make_run("", first_run_rpr(prototype, 1) or first_run_rpr(prototype, 0), tab=True))
    para.append(make_run("       ", first_run_rpr(prototype, 1) or first_run_rpr(prototype, 0)))
    if " - " in date_text:
        start, end = date_text.split(" - ", 1)
        para.append(make_run(start + " ", first_run_rpr(prototype, 2) or first_run_rpr(prototype, 1)))
        para.append(make_run("- ", first_run_rpr(prototype, 3) or first_run_rpr(prototype, 2)))
        para.append(make_run(end, first_run_rpr(prototype, 4) or first_run_rpr(prototype, 2)))
    else:
        para.append(make_run(date_text, first_run_rpr(prototype, 2) or first_run_rpr(prototype, 1)))
    return para


def build_labeled_bullet(prototype: ET.Element, label: str, value: str) -> ET.Element:
    para = clone_para(prototype)
    clear_content(para)
    para.append(make_run(label, first_run_rpr(prototype, 0)))
    para.append(make_run(value, first_run_rpr(prototype, 1)))
    return para


def build_group_heading(prototype: ET.Element, text: str) -> ET.Element:
    para = clone_para(prototype)
    set_single_text(para, text, rpr=first_run_rpr(prototype, 0))
    return para


def build_bullet_para(prototype: ET.Element, text: str) -> ET.Element:
    para = clone_para(prototype)
    clear_content(para)
    para.append(make_run(text, first_run_rpr(prototype, 0)))
    return para


def split_title_date(title_line: str) -> tuple[str, str]:
    marker = " — "
    if marker in title_line:
        return tuple(title_line.rsplit(marker, 1))
    marker = " - "
    if marker in title_line:
        return tuple(title_line.rsplit(marker, 1))
    raise ValueError(f"Expected title/date separator in line: {title_line}")


def normalize_right_column(text: str) -> str:
    return text.lstrip("—-– ").strip()


def split_label_value(bullet_text: str) -> tuple[str, str]:
    if ":" not in bullet_text:
        return "", bullet_text
    label, value = bullet_text.split(":", 1)
    return label.strip() + ": ", value.strip()


def build_additional_para(prototype: ET.Element, label: str, value: str) -> ET.Element:
    para = clone_para(prototype)
    clear_content(para)
    if label:
        para.append(make_run(label + ": ", first_run_rpr(prototype, 0)))
    para.append(make_run(value, first_run_rpr(prototype, 1)))
    return para


def render_document_xml(data: dict, sect_pr: ET.Element, prototypes: dict[str, ET.Element]) -> bytes:
    document = ET.Element(w_tag("document"))
    body = ET.SubElement(document, w_tag("body"))

    body.append(build_name_para(prototypes["name"], data["name"]))
    body.append(build_contact_para(prototypes["contact"], data["contact"]))

    body.append(build_section_heading(prototypes["section_heading"], "EDUCATION"))
    for i, entry in enumerate(data["education"]):
        school_proto = prototypes["edu_school_spaced"] if i > 0 else prototypes["edu_school"]
        school_para = build_school_para(
            school_proto,
            entry["school"],
            normalize_right_column(entry["location"]),
        )
        body.append(school_para)
        degree, date = split_title_date(entry["degree"])
        body.append(build_edu_degree_para(prototypes["edu_degree"], degree, date))
        for bullet_index, bullet in enumerate(entry["bullets"]):
            label, value = split_label_value(bullet)
            bullet_proto = (
                prototypes["edu_bullet_last"]
                if i == len(data["education"]) - 1 and bullet_index == len(entry["bullets"]) - 1
                else prototypes["edu_bullet"]
            )
            body.append(build_labeled_bullet(bullet_proto, label, value))

    body.append(build_section_heading(prototypes["section_heading"], "EXPERIENCE"))
    for entry_index, entry in enumerate(data["experience"]):
        body.append(
            build_company_para(
                prototypes["exp_company"],
                entry["company"],
                normalize_right_column(entry["location"]),
            )
        )
        title, date = split_title_date(entry["title_line"])
        body.append(build_exp_title_para(prototypes["exp_title"], title, date))
        for group_index, group in enumerate(entry["groups"]):
            if group["name"]:
                body.append(build_group_heading(prototypes["exp_group"], group["name"]))
            for bullet_index, bullet in enumerate(group["bullets"]):
                is_last_bullet = bullet_index == len(group["bullets"]) - 1
                is_last_group = group_index == len(entry["groups"]) - 1
                is_last_entry = entry_index == len(data["experience"]) - 1
                bullet_proto = prototypes["exp_bullet"]
                if is_last_bullet and not is_last_group:
                    bullet_proto = prototypes["exp_bullet_after_group"]
                elif is_last_bullet and is_last_group and is_last_entry:
                    bullet_proto = prototypes["exp_bullet_after_resume_section"]
                body.append(build_bullet_para(bullet_proto, bullet))

    body.append(build_section_heading(prototypes["section_heading"], "ADDITIONAL"))
    for item in data["additional"]:
        body.append(build_additional_para(prototypes["additional"], item["label"], item["value"]))

    body.append(copy.deepcopy(sect_pr))
    return ET.tostring(document, encoding="utf-8", xml_declaration=True)


def write_docx(template_path: Path, output_path: Path, document_xml: bytes) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(template_path) as src, ZipFile(output_path, "w", ZIP_DEFLATED) as dst:
        for info in src.infolist():
            data = src.read(info.filename)
            if info.filename == "word/document.xml":
                data = document_xml
            elif info.filename == "word/_rels/document.xml.rels":
                text = data.decode("utf-8").replace(
                    'Target="http://www.linkedin.com/in/utkarsh-rawat"',
                    'Target="https://www.linkedin.com/in/utkarsh-rawat"',
                )
                data = text.encode("utf-8")
            dst.writestr(info, data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown_path", help="Path to resume Markdown file")
    parser.add_argument("-o", "--output", help="Output .docx path")
    parser.add_argument(
        "--template",
        default="Knowledge/my-resumes/base/template.docx",
        help="Template .docx path",
    )
    args = parser.parse_args()

    markdown_path = Path(args.markdown_path).resolve()
    if not markdown_path.exists():
        print(f"Missing input file: {markdown_path}", file=sys.stderr)
        return 1
    template_path = Path(args.template).resolve()
    if not template_path.exists():
        print(f"Missing template file: {template_path}", file=sys.stderr)
        return 1

    output_path = Path(args.output).resolve() if args.output else markdown_path.with_suffix(".docx")
    try:
        data = parse_resume(markdown_path)
        _, sect_pr, prototypes = load_template(template_path)
        document_xml = render_document_xml(data, sect_pr, prototypes)
        write_docx(template_path, output_path, document_xml)
    except Exception as exc:  # noqa: BLE001
        print(f"DOCX generation failed: {exc}", file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
