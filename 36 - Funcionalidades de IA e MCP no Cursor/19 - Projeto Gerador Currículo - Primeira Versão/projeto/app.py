import re

import streamlit as st

from curriculo import para_markdown, para_pdf

st.set_page_config(page_title="Gerador de Currículo", page_icon="📄", layout="wide")
st.title("📄 Gerador de Currículo")

col_form, col_previa = st.columns(2)

with col_form:
    st.subheader("Seus dados")
    nome = st.text_input("Nome completo")
    c1, c2 = st.columns(2)
    email = c1.text_input("E-mail")
    telefone = c2.text_input("Telefone")
    cidade = st.text_input("Cidade / estado")
    resumo = st.text_area("Resumo profissional", height=100,
                          placeholder="Duas ou três frases sobre você e o que procura.")
    experiencias = st.text_area("Experiência (uma por linha)", height=110,
                                placeholder="Empresa X · Desenvolvedor · 2024–atual")
    formacao = st.text_area("Formação (uma por linha)", height=80,
                            placeholder="Universidade Y · Análise de Sistemas · 2023")
    habilidades = st.text_input("Habilidades (separadas por vírgula)",
                                placeholder="Python, SQL, Git, Streamlit")

dados = {"nome": nome.strip(), "email": email.strip(), "telefone": telefone.strip(),
         "cidade": cidade.strip(), "resumo": resumo, "experiencias": experiencias,
         "formacao": formacao, "habilidades": habilidades}

with col_previa:
    st.subheader("Prévia")
    problemas = []
    if not dados["nome"]:
        problemas.append("Preencha o nome.")
    if dados["email"] and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", dados["email"]):
        problemas.append("O e-mail parece inválido.")

    if problemas:
        for p in problemas:
            st.warning(p)
    else:
        with st.container(border=True):
            st.markdown(para_markdown(dados))
        arquivo = re.sub(r"\W+", "_", dados["nome"].lower()).strip("_") or "curriculo"
        st.download_button("Baixar PDF", para_pdf(dados), f"curriculo_{arquivo}.pdf",
                           "application/pdf", type="primary")
