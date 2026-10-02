"""Troca marcadores {{CODE:arquivo:ini-fim}} de um corpo de aula pelas linhas reais do arquivo.

Uso: python3 scripts/aulas/incluir_codigo.py corpo.html saida.html [pasta_base]

- arquivo é relativo a pasta_base (padrão: a pasta do corpo); ini-fim são linhas (1-based,
  inclusive); sem o intervalo, entra o arquivo inteiro.
- O recuo comum do trecho é removido; o código é escapado para HTML e comentários (# … ou -- …) ganham <span class="c">.
- Assim, o código mostrado no deck é sempre o mesmo que foi testado.
"""
import html, os, re, sys, textwrap

corpo, saida = sys.argv[1], sys.argv[2]
base = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.abspath(corpo))


def trecho(m):
    caminho, intervalo = m.group(1), m.group(2)
    linhas = open(os.path.join(base, caminho), encoding="utf-8").read().splitlines()
    if intervalo:
        ini, fim = (int(x) for x in intervalo.split("-"))
        linhas = linhas[ini - 1:fim]
    linhas = textwrap.dedent("\n".join(linhas)).split("\n")  # tira o recuo comum do trecho
    out = []
    for l in linhas:
        e = html.escape(l, quote=False)
        e = re.sub(r"^(\s*)(#.*)$", r'\1<span class="c">\2</span>', e)          # linha de comentário
        e = re.sub(r"(\s\s)(# [^\"']*)$", r'\1<span class="c">\2</span>', e)    # comentário no fim da linha
        out.append(e)
    return "\n".join(out)


texto = open(corpo, encoding="utf-8").read()
texto, n = re.subn(r"\{\{CODE:([^:}]+)(?::(\d+-\d+))?\}\}", trecho, texto)
open(saida, "w", encoding="utf-8").write(texto)
print(f"{n} trecho(s) de código incluído(s) em {saida}")
