"""Gera um guia A4 no tema escuro do curso a partir de um markup simples.

Uso: python3 scripts/guia_para_html.py fonte.txt saida.html "Título da aba"

Markup (uma linha por bloco):
  @cover            capa; linhas t| título, s| subtítulo, d| descrição, u| atualização, a| autoria
  @toc              sumário; "## PARTE…" abre um grupo, as outras linhas são itens
  # N. Título       nova seção (nova página)
  ## Subtítulo      subtítulo da seção
  ### Rótulo        rótulo menor (antes de exemplos)
  p| texto          parágrafo
  table: … endtable:   tabela; células separadas por " ;; ", primeira linha = cabeçalho
  code: … endcode:     bloco de prompt/código, linha a linha
  tip| texto        caixa "Dica"
  @conclusao        bloco de conclusão (na mesma página da seção anterior)
  @end              última página (colofão)
"""
import html, sys

fonte, saida, titulo = sys.argv[1], sys.argv[2], sys.argv[3]
E = lambda s: html.escape(s, quote=False)

CSS = """
@page{size:A4;margin:16mm 15mm;background:#171310}
:root{--bg:#171310;--surface:#1F1A15;--surface-2:#271F18;--border:#3A2F24;--border-2:#4A3C2D;--ink:#F3ECE2;--muted:#AE9F8C;
--accent:#DE8B62;--accent-ink:#F0AB86;--accent-soft:#3A281F;--good:#8FC0A8;--good-soft:#243128;--warn:#DDB662;--warn-soft:#362A16;
--mono:'IBM Plex Mono',ui-monospace,monospace;--display:'Fraunces',Georgia,serif;--body-f:'Inter',system-ui,sans-serif}
*{box-sizing:border-box}
html,body{background:var(--bg);color:var(--ink);font-family:var(--body-f);font-size:10.6pt;line-height:1.55;margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.wrap{max-width:740px;margin:0 auto}
.pg{page-break-before:always}
.cover{min-height:255mm;display:flex;flex-direction:column;justify-content:center;padding:0 6mm}
.eyebrow{font-family:var(--mono);font-size:9pt;letter-spacing:.14em;text-transform:uppercase;color:var(--accent-ink);margin-bottom:14px}
.cover h1{font-family:var(--display);font-size:36pt;line-height:1.08;margin:0 0 14px;font-weight:600}
.cover h1 em{color:var(--accent);font-style:italic}
.cover .sub{font-family:var(--display);font-size:20pt;color:var(--accent-ink);margin:0 0 18px}
.cover .lead{font-size:13pt;color:var(--ink);max-width:560px;margin:0 0 22px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}
.chips span{background:var(--accent-soft);color:var(--accent-ink);border-radius:999px;padding:4px 12px;font-size:9pt;font-family:var(--mono)}
.byline{font-family:var(--mono);font-size:8.5pt;color:var(--muted)}
h2.sec{font-family:var(--display);font-size:21pt;margin:0 0 10px;font-weight:600;line-height:1.15}
h2.sec .n{color:var(--accent);margin-right:8px}
h3{font-size:12.5pt;color:var(--accent-ink);margin:16px 0 7px;font-weight:600}
h4{font-family:var(--mono);font-size:8.6pt;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:14px 0 6px;font-weight:500}
p{margin:0 0 9px}
.table-wrap{border:1px solid var(--border);border-radius:10px;overflow:hidden;margin:6px 0 10px}
table{width:100%;border-collapse:collapse;font-size:9.4pt}
th{background:var(--surface-2);font-family:var(--mono);font-size:8pt;text-transform:uppercase;letter-spacing:.06em;color:var(--accent-ink);text-align:left;padding:7px 9px;font-weight:500}
td{border-top:1px solid var(--border);padding:6px 9px;vertical-align:top}
td:first-child{font-weight:600;color:var(--ink)}
tr:nth-child(even) td{background:rgba(255,255,255,.015)}
.term{background:#100D0A;border:1px solid var(--border-2);border-radius:10px;padding:10px 13px;font-family:var(--mono);font-size:8.8pt;line-height:1.55;white-space:pre-wrap;color:var(--ink);margin:4px 0 10px}
.callout{border-radius:10px;padding:9px 13px;margin:10px 0;font-size:9.8pt;background:var(--good-soft);border:1px solid #35503f}
.callout b{color:var(--good)}
.toc h3{margin:10px 0 4px;font-family:var(--mono);font-size:9pt;letter-spacing:.1em;text-transform:uppercase;color:var(--accent-ink)}
.toc ol{list-style:none;padding:0;margin:0;columns:1}
.toc li{display:flex;gap:10px;padding:2.2px 0;border-bottom:1px dashed var(--border);font-size:10pt}
.toc li b{font-family:var(--mono);color:var(--accent);min-width:24px}
.concl{margin-top:12px;border-top:1px solid var(--border-2);padding-top:10px}
.concl h2.sec{font-size:17pt}
.ultima td{padding:4px 9px}.ultima .callout{margin:6px 0}.ultima h3{margin:10px 0 5px}
.colofao{min-height:250mm;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:9pt;color:var(--muted)}
"""

linhas = open(fonte, encoding="utf-8").read().split("\n")
out, i, modo = [], 0, None
capa = {}
while i < len(linhas):
    l = linhas[i]
    if l == "@cover":
        i += 1
        while i < len(linhas) and linhas[i].strip():
            k, v = linhas[i].split("| ", 1); capa[k] = v; i += 1
        t = capa["t"]
        partes = t.split(" DE ", 1)
        h1 = f'{E(partes[0])} DE<br><em>{E(partes[1])}</em>' if len(partes) == 2 else E(t)
        out.append(f'<section class="cover"><div class="eyebrow">Formação Claude Code 2026 · Engenharia de Prompts · Aula 16</div>'
                   f'<h1>{h1}</h1><div class="sub">{E(capa["s"])}</div><p class="lead">{E(capa["d"])}</p>'
                   f'<div class="byline">{E(capa["u"])}<br>{E(capa["a"])}</div></section>')
        continue
    if l == "@toc":
        out.append('<section class="pg toc"><h2 class="sec">Sumário</h2>')
        i += 1; aberto = False
        while i < len(linhas) and linhas[i].strip():
            x = linhas[i]
            if x.startswith("## "):
                if aberto: out.append("</ol>")
                out.append(f"<h3>{E(x[3:])}</h3><ol>"); aberto = True
            else:
                n, t = x.split(". ", 1)
                out.append(f"<li><b>{E(n)}</b><span>{E(t)}</span></li>")
            i += 1
        out.append("</ol></section>")
        continue
    if l.startswith("# "):
        n, t = l[2:].split(". ", 1)
        ult = ' ultima' if not any(x.startswith('# ') for x in linhas[i + 1:]) else ''
        out.append(f'<section class="pg{ult}"><h2 class="sec"><span class="n">{E(n)}.</span>{E(t)}</h2>')
    elif l.startswith("## "):
        out.append(f"<h3>{E(l[3:])}</h3>")
    elif l.startswith("### "):
        out.append(f"<h4>{E(l[4:])}</h4>")
    elif l.startswith("p| "):
        out.append(f"<p>{E(l[3:])}</p>")
    elif l.startswith("tip| "):
        out.append(f'<div class="callout"><b>Dica:</b> {E(l[5:])}</div>')
    elif l == "table:":
        i += 1; rows = []
        while linhas[i] != "endtable:":
            rows.append(linhas[i].split(" ;; ")); i += 1
        th = "".join(f"<th>{E(c)}</th>" for c in rows[0])
        tb = "".join("<tr>" + "".join(f"<td>{E(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
        out.append(f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
    elif l == "code:":
        i += 1; cod = []
        while linhas[i] != "endcode:":
            cod.append(linhas[i]); i += 1
        out.append(f'<pre class="term">{E(chr(10).join(cod))}</pre>')
    elif l == "@conclusao":
        out.append('<div class="concl"><h2 class="sec">Conclusão</h2>')
        modo = "concl"
    elif l == "@end":
        if modo == "concl": out.append("</div>")
        out.append("</section>")
        i += 1
        while i < len(linhas) and not linhas[i].startswith("p| "): i += 1
        out.append(f'<section class="pg colofao">{E(linhas[i][3:])}</section>')
        break
    elif not l.strip() and out and out[-1] != "</section>" and i + 1 < len(linhas) and linhas[i + 1].startswith("# "):
        out.append("</section>")
    i += 1

doc = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(titulo)}</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body><div class="wrap">
{chr(10).join(out)}
</div></body></html>
"""
open(saida, "w", encoding="utf-8").write(doc)
print("ok:", saida)
