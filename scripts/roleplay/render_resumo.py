"""markup do Resumo -> HTML no padrão do ResumoRolePlay35-39.
Uso: render_resumo.py markup.txt meta.json saida.html"""
import re, sys, json, html, os
src, metaf, dst = sys.argv[1:4]
M = json.load(open(metaf))
style = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "res_style.css")).read()
if "body_css" in M: style = style.replace("</style>", M["body_css"] + "\n</style>")
E = lambda x: html.escape(x, quote=False)
turns = []; cur = None
for ln in open(src).read().split("\n#cards")[0].splitlines():
    if not ln.strip(): continue
    if ln.endswith(":") and "|" not in ln: k, v = ln[:-1], ""
    else: k, _, v = ln.partition("| ")
    if k == "q": cur = {"q": v, "items": []}; turns.append(cur); continue
    cur["items"].append((k, v))
assert len(turns) == len(M["secs"]), (len(turns), len(M["secs"]))
num = lambda x: re.sub(r'^\d+\.\s*', '', x)
out = []
for n, t in enumerate(turns):
    out.append(f'  <!-- {n+1:02d} -->\n  <section class="turn{" first" if n == 0 else ""}">')
    out.append(f'    <div class="sec">{n+1:02d} — {E(M["secs"][n])}</div>')
    out.append(f'    <div class="q"><span class="k">Pergunta</span>{t["q"]}</div>')
    items = t["items"]; i = 0; body = []
    while i < len(items):
        k, v = items[i]
        if k == "li":
            buf = []
            while i < len(items) and items[i][0] == "li": buf.append(f"      <li>{items[i][1]}</li>"); i += 1
            body.append("    <ul>\n" + "\n".join(buf) + "\n    </ul>"); continue
        if k == "n":
            buf = []
            while i < len(items) and items[i][0] in ("n", "sub", "subli"):
                if items[i][0] == "n": buf.append(f"      <li>{num(items[i][1])}</li>"); i += 1
                else:
                    kind = items[i][0]; sub = []
                    while i < len(items) and items[i][0] == kind: sub.append(f"<li>{num(items[i][1]) if kind == 'sub' else items[i][1]}</li>"); i += 1
                    tag = "ol" if kind == "sub" else "ul"
                    buf[-1] = buf[-1][:-5] + f"<{tag}>" + "".join(sub) + f"</{tag}></li>"
            body.append("    <ol>\n" + "\n".join(buf) + "\n    </ol>"); continue
        if k in ("th", "tr"):
            rows = []
            while i < len(items) and items[i][0] in ("th", "tr"):
                kk, vv = items[i]; tag = "th" if kk == "th" else "td"
                rows.append("      <tr>" + "".join(f"<{tag}>{c.strip()}</{tag}>" for c in vv.split(" | ")) + "</tr>"); i += 1
            body.append("    <table>\n" + "\n".join(rows) + "\n    </table>"); continue
        if k == "code":
            i += 1; buf = []
            while items[i][0] == "c": buf.append(f"<div>{E(items[i][1])}</div>"); i += 1
            body.append("    <blockquote>" + "".join(buf) + "</blockquote>")
            if items[i][0] == "endnote": i += 1; continue
            if items[i][0] == "endcode": body.append('    <div class="codenote">Use o código com cuidado.</div>'); i += 1
            continue
        if k == "flow":
            buf = []
            while i < len(items) and items[i][0] == "flow": buf.append(f"<div>{E(items[i][1])}</div>"); i += 1
            body.append('    <div class="flow">' + '<div class="ar">↓</div>'.join(buf) + "</div>"); continue
        if k == "h": body.append(f"    <h3>{v}</h3>")
        elif k == "h4": body.append(f"    <h4>{v}</h4>")
        elif k == "diag": body.append(f'    <div class="flow"><em>Diagrama no original (os rótulos dos blocos não aparecem na página impressa):</em><br>{v}</div>')
        elif k == "p": body.append(f"    <p>{v}</p>")
        else: raise SystemExit(f"tipo desconhecido: {k}")
        i += 1
    if len(body) >= 2 and body[-1].startswith("    <ul>") and body[-2].startswith("    <p>") and body[-2].rstrip().endswith(":</p>"):
        body[-2:] = ['    <div class="follow">' + body[-2].strip() + "\n" + body[-1] + "</div>"]
    elif len(body) >= 3 and body[-2].startswith("    <ul>") and body[-3].rstrip().endswith(":</p>") and body[-1].startswith("    <p>"):
        body[-3:] = ['    <div class="follow">' + body[-3].strip() + "\n" + body[-2] + "\n" + body[-1].strip() + "</div>"]
    out += body
    if n == len(turns) - 1: out.append(f'    <div class="foot">{M["foot"]}</div>')
    out.append("  </section>\n")
doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Resumo — Role Play {M['rp']}</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
{style}
</head>
<body>
<div class="wrap">
  <div class="eyebrow">✳ Formação Claude Code 2026 · Role play {M['rp']}</div>
  <h1>{E(M['h1'])}</h1>
  <p class="lead">{E(M['lead'])}</p>
  <div class="byline">{E(M['byline'])}</div>

{chr(10).join(out)}</div>
</body>
</html>
"""
open(dst, "w").write(doc)
