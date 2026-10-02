import streamlit as st

st.set_page_config(page_title="ToDo List", page_icon="✅")
st.title("✅ Minhas tarefas")

# A lista vive na sessão do navegador: some ao recarregar a página (v1, sem banco).
if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

with st.form("nova_tarefa", clear_on_submit=True):
    col_texto, col_botao = st.columns([4, 1], vertical_alignment="bottom")
    texto = col_texto.text_input("Nova tarefa", placeholder="O que você precisa fazer?")
    adicionar = col_botao.form_submit_button("Adicionar", width="stretch")

if adicionar:
    texto = texto.strip()
    if not texto:
        st.warning("Digite uma tarefa antes de adicionar.")
    else:
        st.session_state.tarefas.append(texto)

if not st.session_state.tarefas:
    st.info("Nenhuma tarefa ainda. Adicione a primeira acima.")
else:
    st.caption(f"{len(st.session_state.tarefas)} tarefa(s)")
    for i, tarefa in enumerate(st.session_state.tarefas):
        col_tarefa, col_remover = st.columns([5, 1], vertical_alignment="center")
        col_tarefa.write(tarefa)
        if col_remover.button("Remover", key=f"remover_{i}"):
            st.session_state.tarefas.pop(i)
            st.rerun()
