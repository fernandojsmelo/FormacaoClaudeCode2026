"""markup -> HTML no padrão do RolePlay35-39. Uso: render_rp.py markup.txt saida.html "Role Play NN" [css extra]"""
import re, sys, html, os
src, dst, label = sys.argv[1], sys.argv[2], sys.argv[3]
extra = sys.argv[4] if len(sys.argv) > 4 else ""
style = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rp_style.css")).read()
if extra: style = style.replace("</style>", extra + "\n</style>")
E = lambda x: html.escape(x, quote=False)
def inline(x):
    x = re.sub(r"\*\*(.+?)\*\*", "\u0001\\1\u0002", x)
    x = E(x).replace("\u0001", "<strong>").replace("\u0002", "</strong>")
    m = re.match(r"^((?:\d+\.\s)?[^:.!?]{2,80}?):\s(.+)$", x)
    if m and not m.group(1).startswith(("Ex", "Em resumo")) and "(Tipo" not in m.group(1) and "(ex" not in m.group(1) and "<strong>" not in m.group(1):
        return f"<strong>{m.group(1)}:</strong> {m.group(2)}"
    return x
def cell(x):
    """célula de tabela: **negrito** e ⏎ para quebra de linha"""
    x = re.sub(r"\*\*(.+?)\*\*", "\u0001\\1\u0002", x)
    return E(x).replace("\u0001", "<strong>").replace("\u0002", "</strong>").replace(" ⏎ ", "<br>")
title = meta = ""
turns = []; cur = None
for ln in open(src).read().splitlines():
    if ln.startswith("@title "): title = ln[7:]; continue
    if ln.startswith("@meta "): meta = ln[6:]; continue
    if ln.startswith("@turn "):
        who, tm = ln[6:].split("|"); cur = {"who": who, "time": tm, "items": []}; turns.append(cur); continue
    if not ln.strip(): continue
    if ln.endswith(":") and "|" not in ln: k, v = ln[:-1], ""
    else: k, _, v = ln.partition("| ")
    cur["items"].append((k.strip(), v))
out = []
for t in turns:
    ai = t["who"] == "Você"
    if ai: out.append(f'  <div class="turn ai"><div class="who">{t["time"]} <b>Você</b></div><div class="msg">')
    else: out.append(f'  <div class="turn user"><div class="who"><b>{E(t["who"])}</b> {t["time"]}</div><div class="msg">')
    end = False
    items = t["items"]; i = 0
    while i < len(items):
        k, v = items[i]
        if k in ("li", "ol"):
            tag = "ul" if k == "li" else "ol"; buf = []
            while i < len(items) and items[i][0] == k:
                vv = re.sub(r"^\d+\.\s*", "", items[i][1]) if k == "ol" else items[i][1]
                buf.append(f"<li>{inline(vv)}</li>"); i += 1
            out.append(f"    <{tag}>" + "\n    ".join(buf) + f"</{tag}>"); continue
        if k in ("th", "tr"):
            rows = []
            while i < len(items) and items[i][0] in ("th", "tr"):
                kk, vv = items[i]; tag = "th" if kk == "th" else "td"
                rows.append("<tr>" + "".join(f"<{tag}>{cell(c.strip())}</{tag}>" for c in vv.split(" | ")) + "</tr>"); i += 1
            out.append("    <table>" + "\n    ".join(rows) + "</table>"); continue
        if k == "code":
            i += 1; buf = []
            while items[i][0] == "c": buf.append(f"<div>{E(items[i][1])}</div>"); i += 1
            out.append("    <blockquote>" + "".join(buf) + "</blockquote>")
            if items[i][0] == "endnote": i += 1; continue
            if items[i][0] == "endcode": out.append('    <div class="codenote">Use o código com cuidado.</div>'); i += 1
            continue
        if k == "flow":
            buf = []
            while i < len(items) and items[i][0] == "flow": buf.append(f"<div>{E(items[i][1])}</div>"); i += 1
            out.append('    <div class="flow">' + '<div class="ar">↓</div>'.join(buf) + "</div>"); continue
        if k == "h": out.append(f"    <h4>{E(v)}</h4>")
        elif k == "p":
            if (re.match(r"^\d+\.\s", v) and ": " not in v or ai) and len(v) < 110 and not v.rstrip().endswith((".", ":", "?", "!", ",")):
                out.append(f"    <h4>{E(v)}</h4>")
            else: out.append(f"    <p>{inline(v) if re.match(r'^\d+\.', v) or '**' in v else E(v)}</p>")
        elif k == "end": end = True
        else: raise SystemExit(f"tipo desconhecido: {k} {v[:40]}")
        i += 1
    out.append("  </div></div>\n")
    if end: out.append('  <div class="end">Fim da sessão</div>')
doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{label} — Transcrição</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
{style}
</head>
<body>
<div class="wrap">
  <div class="eyebrow">✳ Formação Claude Code 2026 · IA com Claude e Cowork</div>
  <h1>{E(title)}</h1>
  <div class="meta">{E(meta.replace(' | ', ' · '))}</div>

{chr(10).join(out)}
  <div class="foot">Esta transcrição inclui conteúdo gerado por IA e é fornecida para seus propósitos de aprendizado pessoal.</div>
</div>
</body>
</html>
"""
open(dst, "w").write(doc)
