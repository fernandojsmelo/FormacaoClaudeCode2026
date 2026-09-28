"""Gera o material de apoio (.md + .pdf no tema escuro) a partir de notebooks .ipynb.

Para cada notebook, grava `<nome>.md` (células sem saídas) e `<nome>.pdf` na mesma
pasta, seguindo o design system descrito no CLAUDE.md do repositório.

Uso (a partir da raiz do repositório):
    .venv/bin/python scripts/notebook_to_pdf.py "<módulo>/<aula>/notebook.ipynb" [...]

Dependências: `pip install nbconvert markdown` e google-chrome no PATH.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from nbconvert import MarkdownExporter

CSS = """
:root{
  --bg:#171310; --surface:#1F1A15; --surface-2:#271F18;
  --border:#3A2F24; --border-2:#4A3C2D;
  --ink:#F3ECE2; --muted:#AE9F8C;
  --accent:#DE8B62; --accent-ink:#F0AB86; --accent-soft:#3A281F;
  --good:#8FC0A8; --good-soft:#243128;
  --warn:#DDB662; --warn-soft:#362A16;
  --danger:#DE8A80; --danger-soft:#3A2321;
  --mono:'IBM Plex Mono', ui-monospace, monospace;
  --display:'Fraunces', Georgia, serif;
  --body-f:'Inter', system-ui, sans-serif;
}
@page{ size:A4; margin:13mm 14mm; background:#171310 }
html,body{background:var(--bg);color:var(--ink);margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:var(--body-f);font-size:10pt;line-height:1.5}
.wrap{max-width:730px;margin:0 auto}
.header{border-bottom:1px solid var(--border);padding-bottom:14px;margin-bottom:18px}
.eyebrow{font-family:var(--mono);font-size:8.5pt;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-ink);margin-bottom:8px}
h1{font-family:var(--display);font-weight:600;font-size:24pt;line-height:1.15;margin:0}
h2{font-family:var(--display);font-weight:600;font-size:15pt;color:var(--ink);margin:16px 0 6px;padding-top:8px;border-top:1px solid var(--border);break-after:avoid}
h3{font-family:var(--display);font-weight:600;font-size:12pt;color:var(--accent-ink);margin:16px 0 6px;break-after:avoid}
p{margin:6px 0 8px}
strong{color:var(--accent-ink);font-weight:600}
code{font-family:var(--mono);font-size:.88em;background:var(--accent-soft);color:var(--accent-ink);padding:1px 5px;border-radius:4px}
pre.term{background:#100D0A;border:1px solid var(--border);border-radius:8px;padding:8px 11px;margin:6px 0 10px;white-space:pre-wrap;word-break:break-word;font-size:7.9pt;line-height:1.4}
pre.term code{background:none;color:var(--ink);padding:0;font-size:1em}
pre.term .c{color:var(--muted)}
.bullets{list-style:none;padding-left:4px;margin:6px 0 10px}
.bullets li{position:relative;padding-left:18px;margin:4px 0}
.bullets li::before{content:"●";position:absolute;left:0;top:.05em;color:var(--accent);font-size:.75em}
.bullets .bullets{margin:4px 0}
ol{padding-left:22px;margin:6px 0 10px} ol li{margin:4px 0} ol li::marker{color:var(--accent);font-family:var(--mono)}
.table-wrap{border:1px solid var(--border);border-radius:8px;overflow:hidden;margin:8px 0 14px;break-inside:avoid}
table{width:100%;border-collapse:collapse;font-size:9.3pt}
th{background:var(--surface-2);font-family:var(--mono);text-transform:uppercase;font-size:7.8pt;letter-spacing:.06em;color:var(--muted);text-align:left;padding:7px 10px;font-weight:500}
td{border-top:1px solid var(--border);padding:5px 9px;vertical-align:top;background:var(--surface)}
"""

FONTS = ("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;"
         "9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap")

# Emojis que renderizam quebrados no Chrome deste ambiente (ver CLAUDE.md).
EMOJI_FIXES = {"🎚️": "🔧", "🎚": "🔧", "📈": "🚀"}


def strip_number(name):
    return re.sub(r"^\d+\s*-\s*", "", name)


def eyebrow_for(nb_path):
    aula = strip_number(nb_path.parent.name)
    modulo = strip_number(nb_path.parent.parent.name).replace(" - ", " · ")
    return f"{modulo} · {aula}"


def notebook_to_markdown(nb_path):
    exporter = MarkdownExporter()
    exporter.exclude_output = True
    md, _ = exporter.from_filename(str(nb_path))
    return md


def markdown_to_html(md, eyebrow):
    for bad, good in EMOJI_FIXES.items():
        md = md.replace(bad, good)
    # Sublistas com 2 espaços (padrão do Jupyter) precisam de 4 para o python-markdown.
    md = re.sub(r"^  - ", "    - ", md, flags=re.M)
    body = markdown.markdown(md, extensions=["fenced_code", "tables", "sane_lists"])

    m = re.match(r"\s*<h1>(.*?)</h1>\s*", body, re.S)
    title = m.group(1) if m else eyebrow
    if m:
        body = body[m.end():]
    body = re.sub(r"<pre><code[^>]*>", '<pre class="term"><code>', body)
    body = re.sub(r"(<pre class=\"term\"><code>.*?</code></pre>)",
                  lambda x: re.sub(r"^(\s*#.*)$", r'<span class="c">\1</span>', x.group(1), flags=re.M),
                  body, flags=re.S)
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    body = body.replace("<ul>", '<ul class="bullets">').replace("<hr />", "")

    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>{title}</title>
<link href="{FONTS}" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">
<div class="header"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1></div>
{body}
</div></body></html>"""


def html_to_pdf(html_path, pdf_path):
    subprocess.run(
        ["google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
         "--run-all-compositor-stages-before-draw", "--virtual-time-budget=4000",
         "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True, capture_output=True, timeout=120,
    )


def page_count(pdf_path):
    out = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True).stdout
    return next((line.split()[-1] for line in out.splitlines() if line.startswith("Pages:")), "?")


def main(paths):
    if not paths:
        sys.exit(__doc__)
    with tempfile.TemporaryDirectory() as tmp:
        for arg in paths:
            nb_path = Path(arg).resolve()
            md = notebook_to_markdown(nb_path)
            md_path = nb_path.with_suffix(".md")
            md_path.write_text(md, encoding="utf-8")

            html_path = Path(tmp) / f"{nb_path.stem}.html"
            html_path.write_text(markdown_to_html(md, eyebrow_for(nb_path)), encoding="utf-8")
            pdf_path = nb_path.with_suffix(".pdf")
            html_to_pdf(html_path, pdf_path)
            print(f"{pdf_path.relative_to(Path.cwd()) if pdf_path.is_relative_to(Path.cwd()) else pdf_path}"
                  f" -> {page_count(pdf_path)} págs")


if __name__ == "__main__":
    main(sys.argv[1:])
