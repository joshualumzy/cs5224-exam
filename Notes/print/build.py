#!/usr/bin/env python3
"""Render Notes/INDEX.md to Notes/INDEX.pdf for printing.

Supports only the Markdown the INDEX uses: #/##/###/#### headings, ---, paragraphs,
pipe tables (a cell may use <br> for a line break), "- " bullets, **bold**, *italic* and `code`. Anything else stops
the build with an error, so the PDF never silently drops content.
Cross-references become clickable: "L03-11" anywhere, and "row 10" / "table 10"
within the same lecture. A reference to a row or table that does not exist
stops the build.
Usage: python3 Notes/print/build.py
"""
import html, re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "INDEX.md"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "INDEX.pdf"
CHROME = next((c for c in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/opt/pw-browsers/chromium",
               shutil.which("chromium") or "", shutil.which("google-chrome") or "") if c and Path(c).exists()), None)


def inline(text):
    parts = re.split(r"(`[^`]+`)", text)
    out = []
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append("<code>" + html.escape(p[1:-1]) + "</code>")
            continue
        p = html.escape(p, quote=False)
        p = p.replace("&lt;br&gt;", "<br>")
        p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", p)
        if "*" in p.replace("★", ""):
            raise ValueError(f"unmatched * in: {text[:80]}")
        out.append(p)
    return "".join(out)


REF = re.compile(r"\b(L\d\d)-(\d+)\b|\b(row|table) (\d+)\b")


def link(text, lec, refs):
    """Turn row/table references into in-document links."""
    def sub(m):
        target = f"{m.group(1)}-{m.group(2)}" if m.group(1) else f"{lec}-{m.group(4)}"
        if lec is None and not m.group(1):
            return m.group(0)
        refs.add(target)
        return f'<a href="#{target}">{m.group(0)}</a>'
    return REF.sub(sub, text)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def convert(lines):
    out, i, lec, ids, refs = [], 0, None, set(), set()

    def anchor(num):
        key = f"{lec}-{num}"
        if lec is None or key in ids:
            return ""
        ids.add(key)
        return f' id="{key}"'

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif m := re.match(r"(#{1,4}) (.+)", line):
            n = len(m.group(1))
            if n == 3:
                # A ### heading starts a lecture ("L03 — ...") or a non-lecture section
                # (e.g. the concept map), where bare "row N" references are not linked.
                lec = lm.group(0) if (lm := re.match(r"L\d\d", m.group(2))) else None
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            i += 1
        elif line.strip() == "---":
            i += 1  # section breaks come from the stylesheet
        elif line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i]); i += 1
            if len(block) < 2 or not re.fullmatch(r"[|\s:-]+", block[1]):
                raise ValueError(f"table without a separator row near: {block[0][:80]}")
            head, rows = cells(block[0]), [cells(r) for r in block[2:]]
            cls = "concepts" if head[0] == "#" else "tactics" if head[0] == "Ask" else "compare"
            t = [f'<table class="{cls}"><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"]
            for r in rows:
                if len(r) != len(head):
                    raise ValueError(f"row has {len(r)} cells, header has {len(head)}: {r[0][:60]}")
                rid = anchor(r[0]) if cls == "concepts" and r[0].isdigit() else ""
                t.append(f"<tr{rid}>" + "".join(f"<td>{link(inline(c), lec, refs)}</td>" for c in r) + "</tr>")
            out.append("".join(t) + "</tbody></table>")
        elif line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{link(inline(lines[i][2:]), lec, refs)}</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
        elif m := re.fullmatch(r"!\[(.*)\]\((.+\.svg)\)", line.strip()):
            svg = (SRC.parent / m.group(2)).read_text()
            out.append(f'<figure>{svg[svg.index("<svg"):]}</figure>')
            i += 1
        elif re.match(r"\s|>|\d+\.\s|```|<|!\[|\[", line):
            raise ValueError(f"unsupported Markdown at line {i + 1}: {line[:80]}")
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"[#|>-]|!\[", lines[i]):
                para.append(lines[i].strip()); i += 1
            text = " ".join(para)
            cap = re.fullmatch(r"\*\*(\d+) · .+", text)
            attrs = ' class="caption"' + anchor(cap.group(1)) if cap else ""
            out.append(f"<p{attrs}>{link(inline(text), lec, refs)}</p>")
    if missing := sorted(refs - ids):
        raise ValueError(f"links to rows/tables that do not exist: {', '.join(missing)}")
    return "\n".join(out)


def main():
    try:
        body = convert(SRC.read_text().split("\n"))
    except ValueError as e:
        sys.exit(f"build.py: {e}")
    css = (HERE / "print.css").read_text()
    page = f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "index.html"
        src.write_text(page)
        subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={OUT}", src.as_uri()],
                       check=True, capture_output=True, timeout=120)
    if not OUT.exists() or OUT.stat().st_size == 0:
        sys.exit("build.py: Chrome produced no PDF")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
