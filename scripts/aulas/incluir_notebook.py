"""Troca marcadores de um corpo de aula pelo código e pela saída gravados num notebook .ipynb.

Uso: python3 scripts/aulas/incluir_notebook.py corpo.html saida.html [pasta_base]

- {{NB:caderno.ipynb:N}}         código da célula N (0-based, como no Jupyter de cima para baixo).
- {{NB:caderno.ipynb:N:ini-fim}} só as linhas ini-fim (1-based, inclusive) da célula; se sobrar código, entra "…".
- {{NBOUT:caderno.ipynb:N}}      saída de texto gravada na célula N (stdout/resultado), como o Jupyter mostra.
- {{NBOUT:caderno.ipynb:N:ini-fim}} só essas linhas da saída; se sobrar texto depois, entra uma linha "…".
- caderno.ipynb é relativo a pasta_base (padrão: a pasta do corpo).
- O código é escapado para HTML e os comentários (# …) ganham <span class="c">, como no incluir_codigo.py.

Serve para aulas cujo código roda numa API paga ou com chave (ex.: Groq): o deck mostra a saída
real que ficou gravada no notebook, em vez de rodar o código de novo.
"""
import html, json, os, re, sys, textwrap

corpo, saida = sys.argv[1], sys.argv[2]
base = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.abspath(corpo))
_cache = {}


def celula(caminho, n):
    if caminho not in _cache:
        _cache[caminho] = json.load(open(os.path.join(base, caminho), encoding="utf-8"))["cells"]
    return _cache[caminho][int(n)]


def recorte(linhas, intervalo):
    if not intervalo:
        return linhas, False
    ini, fim = (int(x) for x in intervalo.split("-"))
    return linhas[ini - 1:fim], fim < len(linhas)


def codigo(m):
    linhas = "".join(celula(m.group(1), m.group(2))["source"]).rstrip("\n").split("\n")
    linhas, cortou = recorte(linhas, m.group(3))
    out = []
    for l in textwrap.dedent("\n".join(linhas)).split("\n"):
        e = html.escape(l, quote=False)
        e = re.sub(r"^(\s*)(#.*)$", r'\1<span class="c">\2</span>', e)
        e = re.sub(r"(\s\s)(# [^\"']*)$", r'\1<span class="c">\2</span>', e)
        out.append(e)
    if cortou:
        out.append('<span class="c">…</span>')
    return "\n".join(out)


def saida_celula(m):
    texto = ""
    for o in celula(m.group(1), m.group(2)).get("outputs", []):
        t = o.get("text") or o.get("data", {}).get("text/plain") or ""
        texto += "".join(t) if isinstance(t, list) else t
    linhas = texto.rstrip("\n").split("\n")
    linhas, cortou = recorte(linhas, m.group(3))
    while linhas and not linhas[-1].strip():
        linhas.pop()
    while linhas and not linhas[0].strip():
        linhas.pop(0)
    if cortou:
        linhas.append("…")
    return html.escape("\n".join(linhas), quote=False)


texto = open(corpo, encoding="utf-8").read()
texto, n1 = re.subn(r"\{\{NB:([^:}]+):(\d+)(?::(\d+-\d+))?\}\}", codigo, texto)
texto, n2 = re.subn(r"\{\{NBOUT:([^:}]+):(\d+)(?::(\d+-\d+))?\}\}", saida_celula, texto)
open(saida, "w", encoding="utf-8").write(texto)
print(f"{n1} trecho(s) de código e {n2} saída(s) do notebook incluídos em {saida}")
