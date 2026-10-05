"""Refaz os blocos de código do markup da transcrição com o texto e o recuo exatos do PDF.

Uso: python3 scripts/roleplay/codigo_xml.py RolePlayNN.pdf rpNN.txt rpNN.codigo.txt

O parse_rp.py perde o recuo e às vezes transforma linhas de código em p|/h| (comentários
// viram título, linhas que começam com { somem). O XML do pdftohtml guarda o recuo:
este script acha no XML cada bloco "<linguagem> ... Use o código com cuidado." e troca,
na mesma ordem, os blocos do markup:
  - "p| <linguagem>" ... "p| Use o código com cuidado."  (código que virou parágrafo)
  - "code:" ... "endcode:"                                 (código já detectado)
O rótulo da linguagem é descartado, como nas outras reconstruções.
"""
import html, os, re, subprocess, sys, tempfile

LINGUAGENS = {"javascript", "typescript", "json", "python", "bash", "shell", "text", "sql",
              "html", "css", "yaml", "plaintext", "tsx", "jsx", "markdown", "sh"}
NOTA = "Use o código com cuidado."

pdf, entrada, saida = sys.argv[1:4]
tmp = tempfile.mkdtemp()
subprocess.run(["pdftohtml", "-xml", "-i", "-q", pdf, os.path.join(tmp, "x")], check=True)
xml = open(os.path.join(tmp, "x.xml"), encoding="utf-8").read()
linhas_xml = [html.unescape(re.sub(r"<[^>]+>", "", m)) for m in re.findall(r"<text [^>]*>(.*?)</text>", xml)]

blocos, i = [], 0
while i < len(linhas_xml):
    if linhas_xml[i].strip().lower() in LINGUAGENS:
        j = i + 1
        while j < len(linhas_xml) and linhas_xml[j].strip() != NOTA:
            j += 1
        if j < len(linhas_xml):
            blocos.append([l.rstrip() for l in linhas_xml[i + 1:j]])
            i = j
    i += 1

markup = open(entrada, encoding="utf-8").read().split("\n")
out, k, i = [], 0, 0
while i < len(markup):
    l = markup[i]
    eh_rotulo = l.startswith("p| ") and l[3:].strip().lower() in LINGUAGENS
    if eh_rotulo or l == "code:":
        fim = NOTA if eh_rotulo else None
        j = i + 1
        while j < len(markup) and not (markup[j] == f"p| {NOTA}" if fim else markup[j] in ("endcode:", "endnote:")):
            j += 1
        if k >= len(blocos):
            sys.exit(f"Mais blocos no markup do que no XML (linha {i + 1})")
        out.append("code:")
        out += ["c| " + c for c in blocos[k]]
        out.append("endcode:" if eh_rotulo else markup[j])
        k += 1
        i = j + 1
        continue
    out.append(l)
    i += 1

open(saida, "w", encoding="utf-8").write("\n".join(out))
print(f"{k} bloco(s) de código refeito(s) a partir do XML ({len(blocos)} no PDF)")
