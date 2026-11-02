#!/usr/bin/env python3
"""Build printable mock papers (PDF) and answer keys (Markdown).

Usage: python3 Notes/mocks/build_mocks.py
Outputs (in Notes/mocks/): MOCK-B.pdf (+ -print-safe.pdf image copy for fussy printers), MOCK-C-part1.pdf, MOCK-B-key.md, MOCK-C-part1-key.md
Question data lives in mock_data.py. PDFs are rendered with headless Chrome/Chromium.
"""
import html, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mock_data as D  # noqa: E402

CHROMES = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/opt/pw-browsers/chromium",
           shutil.which("chromium") or "", shutil.which("google-chrome") or ""]
CHROME = next((c for c in CHROMES if c and Path(c).exists()), None)

CSS = """
@page { size: A4 portrait; margin: 16mm 16mm 18mm 16mm;
        @bottom-center { content: counter(page) " / " counter(pages); font: 9pt Arial; color: #555; }
        @top-right { content: string(papertitle); font: 9pt Arial; color: #555; } }
body { font: 10.5pt/1.38 Arial, Helvetica, sans-serif; color: #000; }
h1 { font-size: 18pt; margin: 0 0 2mm; string-set: papertitle content(); }
h2 { font-size: 12.5pt; margin: 5mm 0 2mm; border-bottom: 1.2pt solid #000; padding-bottom: 1mm; break-after: avoid; }
.sub { font-size: 11pt; margin: 0 0 4mm; color: #333; }
.meta { width: 100%; border-collapse: collapse; margin: 2mm 0 3mm; }
.meta td { border: 0.6pt solid #666; padding: 2mm 3mm; font-size: 10pt; }
ul.rules { margin: 1mm 0 3mm 5mm; padding: 0; } ul.rules li { margin: 0.8mm 0; }
.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0 5mm; margin-top: 2mm; padding-right: 2mm; }
.grow { display: flex; align-items: center; gap: 1.6mm; padding: 1.1mm 0; border-bottom: 0.4pt dotted #999; font-size: 10pt; }
.grow b { width: 6mm; text-align: right; }
.bub { display: inline-block; width: 5.4mm; height: 5.4mm; border: 0.7pt solid #000; border-radius: 50%; text-align: center;
       font-size: 7.5pt; line-height: 5.4mm; color: #444; }
.gs { margin-left: auto; margin-right: 1mm; font-size: 8pt; color: #555; white-space: nowrap; } .gs i { display: inline-block; width: 3.2mm; height: 3.2mm; border: 0.7pt solid #000; vertical-align: -0.6mm; margin-left: 0.8mm; }
.q { break-inside: avoid; margin: 0 0 5.5mm; }
.qh { display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 1mm; }
.qh span.m { font-weight: normal; font-size: 9pt; color: #444; }
.qt p { margin: 0 0 1mm; }
.opt { display: flex; gap: 2mm; margin: 0.9mm 0 0.9mm 5mm; } .opt b { flex: none; width: 5mm; }
table.data { border-collapse: collapse; margin: 2mm 0 1mm 5mm; font-size: 9.5pt; }
table.data th, table.data td { border: 0.6pt solid #444; padding: 1mm 2.5mm; text-align: left; }
table.data th { background: #eee; }
.lines { margin-top: 2mm; border: 0.6pt solid #777; }
.ln { height: 8mm; border-bottom: 0.5pt solid #bbb; box-sizing: border-box; } .ln:last-child { border-bottom: none; }
.sa { break-inside: avoid; }
.pb { break-before: page; }
.gb { display: inline-block; width: 3.2mm; height: 3.2mm; border: 0.7pt solid #000; vertical-align: -0.6mm; }
.foot { margin-top: 6mm; font-size: 9pt; color: #555; text-align: center; }
"""


def esc(t):
    return html.escape(t, quote=False)


def paras(t):
    return "".join(f"<p>{esc(p)}</p>" for p in t.split("\n"))


def build_html(m):
    mcqs = [D.MCQ[s] for s in m["mcq"]]
    sas = [D.SA[s] for s in m["sa"]]
    nm, ns = len(mcqs), len(sas)
    marks = nm + 2 * ns
    out = [f"<!doctype html><html><head><meta charset='utf-8'><title>{m['title']}</title><style>{CSS}</style></head><body>"]
    out.append(f"<h1>{esc(m['title'])}</h1><div class='sub'>{m['minutes']} min &middot; {marks} marks &middot; {nm} MCQ + {ns} short answer &middot; open book, no internet or AI. Circle one option per MCQ; tick <b>guessed</b> if unsure.</div>")
    out.append("<h2>Section A: Multiple choice (1 mark each)</h2>")
    for i, q in enumerate(mcqs, 1):
        out.append(f"<div class='q'><div class='qh'><span>Question {i}</span><span class='m'>guessed <i class='gb'></i> &nbsp; [1 mark]</span></div><div class='qt'>")
        lines = q["text"].split("\n")
        out.append("".join(f"<p>{esc(p)}</p>" for p in lines))
        out.append("</div>")
        for L, o in zip("abcde", q["opts"]):
            out.append(f"<div class='opt'><b>({L})</b><span>{esc(o)}</span></div>")
        out.append("</div>")

    out.append(f"<h2>Section B: Short answer (2 marks each)</h2>")
    for j, q in enumerate(sas, nm + 1):
        out.append(f"<div class='q sa'><div class='qh'><span>Question {j}</span><span class='m'>[2 marks]</span></div><div class='qt'>{paras(q['text'])}</div>")
        if q["table"]:
            t = q["table"]
            out.append("<table class='data'><tr>" + "".join(f"<th>{esc(h)}</th>" for h in t["head"]) + "</tr>")
            for r in t["rows"]:
                out.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>")
            out.append("</table>")
        out.append(f"<div class='lines'>" + "<div class='ln'></div>" * q['lines'] + "</div></div>")
    out.append("</body></html>")
    return "".join(out)


def to_pdf(htm, dest):
    if not CHROME:
        sys.exit("No Chrome/Chromium found. Edit CHROMES in build_mocks.py.")
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "m.html"
        f.write_text(htm, encoding="utf-8")
        subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={dest}", f.as_uri()], check=True, capture_output=True)


def rasterize(pdf, dest, dpi=200):
    """Image-only copy of the PDF: no fonts, shadings or transparency, so any PostScript printer accepts it."""
    from PIL import Image
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-r", str(dpi), "-gray", "-png", str(pdf), f"{td}/p"], check=True)
        pages = [Image.open(f).convert("L") for f in sorted(Path(td).glob("p-*.png"))]
        pages[0].save(dest, "PDF", resolution=dpi, save_all=True, append_images=pages[1:])


def build_key(m):
    mcqs = [D.MCQ[s] for s in m["mcq"]]
    sas = [D.SA[s] for s in m["sa"]]
    nm = len(mcqs)
    k = [f"# {m['title']}: answer key and source map\n",
         "Do not open before sitting the paper. Source codes: 24S2 = 2425-Sem2 paper, 25S1 = 2526-Sem1, 25S2 = 2526-Sem2, OWN = written for this mock. "
         "Question wording is the past paper's own, except arrows fixed, a stray backtick removed (25S2 Q6 not used here) and the `deployment*` correction in 24S2 Q25 applied.\n",
         f"Marks: {nm} MCQ x 1 + {len(sas)} short answers x 2 = {nm + 2 * len(sas)}. Time: {m['minutes']} min.\n",
         "## MCQ\n", "| # | Source | Lecture | Answer | Official note |", "|---|---|---|---|---|"]
    for i, q in enumerate(mcqs, 1):
        k.append(f"| {i} | {q['src']} | {q['lec']} | ({q['ans']}) | {q['why'].replace('|', '/')} |")
    k.append("\n## Short answer\n")
    for j, q in enumerate(sas, nm + 1):
        k.append(f"### Q{j} ({q['src']}, {q['lec']})\n\n**Sample answer:** {q['sample']}\n\n**Marking:** {q['marking']}\n")
    return "\n".join(k) + "\n"


def check(m):
    for key, kind in (("mcq", D.MCQ), ("sa", D.SA)):
        assert len(set(m[key])) == len(m[key]), f"duplicate in {m['code']} {key}"
        missing = [s for s in m[key] if s not in kind]
        assert not missing, f"unknown {missing}"
    for q in (D.MCQ[s] for s in m["mcq"]):
        assert len(q["opts"]) == 5, q["src"]
        assert q["ans"] in "abcde"


def main():
    check(D.MOCK_B), check(D.MOCK_C)
    # Every real question exactly once across B and C
    used = [s for m in (D.MOCK_B, D.MOCK_C) for s in m["mcq"] + m["sa"] if not s.startswith("OWN")]
    assert len(used) == len(set(used)) == 51, len(used)
    for m, name in ((D.MOCK_B, "MOCK-B"), (D.MOCK_C, "MOCK-C-part1")):
        to_pdf(build_html(m), HERE / f"{name}.pdf")
        rasterize(HERE / f"{name}.pdf", HERE / f"{name}-print-safe.pdf")
        (HERE / f"{name}-key.md").write_text(build_key(m), encoding="utf-8")
        print("built", name)


if __name__ == "__main__":
    main()
