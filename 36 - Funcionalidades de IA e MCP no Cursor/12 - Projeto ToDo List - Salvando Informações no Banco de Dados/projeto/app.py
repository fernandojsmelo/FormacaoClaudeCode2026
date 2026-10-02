import streamlit as st

import db

st.set_page_config(page_title="ToDo List", page_icon="✅")
st.title("✅ Minhas tarefas")

# As tarefas agora ficam no arquivo tarefas.db: sobrevivem a recarregar a página
# e a reiniciar o app.
conexao = db.conectar()
db.criar_tabela(conexao)

with st.form("nova_tarefa", clear_on_submit=True):
    col_texto, col_botao = st.columns([4, 1], vertical_alignment="bottom")
    texto = col_texto.text_input("Nova tarefa", placeholder="O que você precisa fazer?")
    adicionar = col_botao.form_submit_button("Adicionar", width="stretch")

if adicionar:
    texto = texto.strip()
    if not texto:
        st.warning("Digite uma tarefa antes de adicionar.")
    else:
        db.adicionar(conexao, texto)

tarefas = db.listar(conexao)
if not tarefas:
    st.info("Nenhuma tarefa ainda. Adicione a primeira acima.")
else:
    concluidas = sum(t["concluida"] for t in tarefas)
    st.progress(concluidas / len(tarefas), text=f"{concluidas} de {len(tarefas)} concluída(s)")

    filtro = st.radio("Mostrar", ["Todas", "Pendentes", "Concluídas"], horizontal=True)
    visiveis = [
        t for t in tarefas
        if filtro == "Todas"
        or (filtro == "Pendentes" and not t["concluida"])
        or (filtro == "Concluídas" and t["concluida"])
    ]
    if not visiveis:
        st.caption("Nenhuma tarefa neste filtro.")

    for tarefa in visiveis:
        col_check, col_remover = st.columns([5, 1], vertical_alignment="center")
        rotulo = f"~~{tarefa['texto']}~~" if tarefa["concluida"] else tarefa["texto"]
        marcada = col_check.checkbox(rotulo, value=tarefa["concluida"], key=f"feita_{tarefa['id']}")
        if marcada != tarefa["concluida"]:
            db.marcar(conexao, tarefa["id"], marcada)
            st.rerun()
        if col_remover.button("Remover", key=f"remover_{tarefa['id']}"):
            db.remover(conexao, tarefa["id"])
            st.rerun()

    if concluidas and st.button("Limpar concluídas"):
        db.remover_concluidas(conexao)
        st.rerun()
