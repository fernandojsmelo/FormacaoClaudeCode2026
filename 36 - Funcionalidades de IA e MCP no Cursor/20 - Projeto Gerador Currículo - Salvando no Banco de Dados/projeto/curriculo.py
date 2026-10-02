"""Monta o currículo em Markdown (prévia) e em PDF (download)."""
from fpdf import FPDF

SECOES = [("resumo", "Resumo"), ("experiencias", "Experiência"), ("formacao", "Formação")]


def linhas(texto):
    """Uma entrada por linha, sem linhas vazias."""
    return [l.strip() for l in texto.splitlines() if l.strip()]


def habilidades(texto):
    return [h.strip() for h in texto.split(",") if h.strip()]


def para_markdown(dados):
    partes = [f"# {dados['nome']}"]
    contato = " · ".join(v for v in (dados["email"], dados["telefone"], dados["cidade"]) if v)
    if contato:
        partes.append(contato)
    if dados["resumo"].strip():
        partes.append("## Resumo\n" + dados["resumo"].strip())
    for chave, titulo in SECOES[1:]:
        itens = linhas(dados[chave])
        if itens:
            partes.append(f"## {titulo}\n" + "\n".join(f"- {i}" for i in itens))
    lista = habilidades(dados["habilidades"])
    if lista:
        partes.append("## Habilidades\n" + ", ".join(lista))
    return "\n\n".join(partes)


def _latin1(texto):
    # As fontes padrão do PDF só têm caracteres latinos (acentos do português incluídos).
    return texto.replace("•", "-").replace("–", "-").replace("—", "-").encode("latin-1", "replace").decode("latin-1")


def para_pdf(dados):
    pdf = FPDF(format="A4")
    pdf.set_margins(18, 18, 18)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 11, _latin1(dados["nome"]), new_x="LMARGIN", new_y="NEXT")
    contato = " | ".join(v for v in (dados["email"], dados["telefone"], dados["cidade"]) if v)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(0, 6, _latin1(contato), new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)

    def titulo(texto):
        pdf.ln(4)
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(200, 90, 50)
        pdf.cell(0, 7, _latin1(texto.upper()), new_x="LMARGIN", new_y="NEXT")
        pdf.set_draw_color(220, 200, 190)
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(2)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "", 10.5)

    if dados["resumo"].strip():
        titulo("Resumo")
        pdf.multi_cell(0, 5.5, _latin1(dados["resumo"].strip()), new_x="LMARGIN", new_y="NEXT")
    for chave, nome in SECOES[1:]:
        itens = linhas(dados[chave])
        if itens:
            titulo(nome)
            for item in itens:
                pdf.multi_cell(0, 5.5, _latin1(f"- {item}"), new_x="LMARGIN", new_y="NEXT")
    lista = habilidades(dados["habilidades"])
    if lista:
        titulo("Habilidades")
        pdf.multi_cell(0, 5.5, _latin1(", ".join(lista)), new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output())
