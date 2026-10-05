"""Troca marcadores {{CODE:arquivo:ini-fim}} de um corpo de aula pelas linhas reais do arquivo.

Uso: python3 scripts/aulas/incluir_codigo.py corpo.html saida.html [pasta_base]

- arquivo é relativo a pasta_base (padrão: a pasta do corpo); ini-fim são linhas (1-based,
  inclusive); sem o intervalo, entra o arquivo inteiro.
- O recuo comum do trecho é removido; o código é escapado para HTML e comentários (# … ou -- …) ganham <span class="c">.
- {{OUT:arquivo.py}} roda o script com python3 (na pasta dele, com arquivo.in como entrada,
  se existir) e insere a saída real, inclusive mensagens de erro (stderr).
- Assim, o código e a saída mostrados no deck são sempre os do arquivo testado.
"""
import html, os, re, subprocess, sys, textwrap

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


ECO = """import builtins, runpy, sys
_input = builtins.input
def _eco(prompt=""):
    valor = _input(prompt)
    print(valor)  # no terminal, o que você digita aparece depois da pergunta
    return valor
builtins.input = _eco
sys.argv = [sys.argv[1]]
runpy.run_path(sys.argv[0], run_name="__main__")
"""


def limpar_traceback(erro, pasta, nome):
    """Deixa o traceback como o terminal mostraria: caminho curto e só os quadros do script."""
    erro = erro.replace(pasta + os.sep, "")
    saida, manter = [], True
    for l in erro.splitlines():
        if l.startswith("  File "):
            manter = l.startswith(f'  File "{nome}"') or not ("<string>" in l or "runpy" in l)
            if manter:
                saida.append(l)
        elif l.startswith("    "):
            if manter:
                saida.append(l)
        else:
            manter = True
            saida.append(l)
    return "\n".join(saida) + ("\n" if saida else "")


def executar(m):
    """Roda o script e devolve a saída como apareceria no terminal."""
    caminho = os.path.join(base, m.group(1))
    pasta, nome = os.path.split(caminho)
    entrada = os.path.splitext(caminho)[0] + ".in"
    dados = open(entrada, encoding="utf-8").read() if os.path.exists(entrada) else None
    cmd = [sys.executable, "-c", ECO, nome] if dados is not None else [sys.executable, nome]
    r = subprocess.run(cmd, cwd=pasta, input=dados or "", capture_output=True, text=True,
                       timeout=60, env=dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONHASHSEED="0"))
    erro = limpar_traceback(r.stderr, pasta, nome)
    return html.escape((r.stdout + erro).rstrip("\n"), quote=False)


texto = open(corpo, encoding="utf-8").read()
texto, n = re.subn(r"\{\{CODE:([^:}]+)(?::(\d+-\d+))?\}\}", trecho, texto)
texto, n_out = re.subn(r"\{\{OUT:([^}]+)\}\}", executar, texto)
n += n_out
open(saida, "w", encoding="utf-8").write(texto)
print(f"{n} trecho(s) de código incluído(s) em {saida}")
