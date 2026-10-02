import re

import streamlit as st

import db
from curriculo import para_markdown, para_pdf

st.set_page_config(page_title="Gerador de Currículo", page_icon="📄", layout="wide")
st.title("📄 Gerador de Currículo")

CAMPOS = ["nome", "email", "telefone", "cidade", "resumo", "experiencias", "formacao", "habilidades"]
conexao = db.conectar()

if "id_atual" not in st.session_state:
    st.session_state.id_atual = None  # None = currículo novo, ainda não salvo


def preencher(dados, id_curriculo):
    for campo in CAMPOS:
        st.session_state[campo] = dados.get(campo, "")
    st.session_state.id_atual = id_curriculo


# Barra lateral: currículos salvos
with st.sidebar:
    st.header("Currículos salvos")
    if st.button("➕ Novo currículo", width="stretch"):
        preencher({}, None)
        st.rerun()
    salvos = db.listar(conexao)
    if not salvos:
        st.caption("Nenhum currículo salvo ainda.")
    for linha in salvos:
        atual = linha["id"] == st.session_state.id_atual
        col_nome, col_excluir = st.columns([4, 1], vertical_alignment="center")
        rotulo = f"{'▶ ' if atual else ''}{linha['nome']}"
        if col_nome.button(rotulo, key=f"abrir_{linha['id']}", help=f"Salvo em {linha['atualizado_em']}",
                           width="stretch"):
            preencher(db.carregar(conexao, linha["id"]), linha["id"])
            st.rerun()
        if col_excluir.button("🗑", key=f"excluir_{linha['id']}", help="Excluir"):
            db.excluir(conexao, linha["id"])
            if atual:
                preencher({}, None)
            st.rerun()

col_form, col_previa = st.columns(2)

with col_form:
    st.subheader("Editando: " + ("novo currículo" if st.session_state.id_atual is None else "currículo salvo"))
    st.text_input("Nome completo", key="nome")
    c1, c2 = st.columns(2)
    c1.text_input("E-mail", key="email")
    c2.text_input("Telefone", key="telefone")
    st.text_input("Cidade / estado", key="cidade")
    st.text_area("Resumo profissional", key="resumo", height=100)
    st.text_area("Experiência (uma por linha)", key="experiencias", height=110)
    st.text_area("Formação (uma por linha)", key="formacao", height=80)
    st.text_input("Habilidades (separadas por vírgula)", key="habilidades")

dados = {campo: st.session_state.get(campo, "").strip() for campo in CAMPOS}

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
        col_salvar, col_pdf = st.columns(2)
        if col_salvar.button("💾 Salvar no banco", type="primary", width="stretch"):
            st.session_state.id_atual = db.salvar(conexao, dados, st.session_state.id_atual)
            st.toast("Currículo salvo!")
            st.rerun()
        arquivo = re.sub(r"\W+", "_", dados["nome"].lower()).strip("_") or "curriculo"
        col_pdf.download_button("Baixar PDF", para_pdf(dados), f"curriculo_{arquivo}.pdf",
                                "application/pdf", width="stretch")
