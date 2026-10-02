import streamlit as st

st.set_page_config(page_title="ToDo List", page_icon="✅")
st.title("✅ Minhas tarefas")

# Cada tarefa agora é um dicionário: id fixo, texto e se está concluída.
if "tarefas" not in st.session_state:
    st.session_state.tarefas = []
    st.session_state.proximo_id = 1

with st.form("nova_tarefa", clear_on_submit=True):
    col_texto, col_botao = st.columns([4, 1], vertical_alignment="bottom")
    texto = col_texto.text_input("Nova tarefa", placeholder="O que você precisa fazer?")
    adicionar = col_botao.form_submit_button("Adicionar", width="stretch")

if adicionar:
    texto = texto.strip()
    if not texto:
        st.warning("Digite uma tarefa antes de adicionar.")
    else:
        st.session_state.tarefas.append(
            {"id": st.session_state.proximo_id, "texto": texto, "concluida": False}
        )
        st.session_state.proximo_id += 1

tarefas = st.session_state.tarefas
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

    # As chaves usam o id da tarefa, não a posição: assim, remover uma tarefa
    # não faz a de baixo "herdar" o checkbox marcado.
    for tarefa in visiveis:
        col_check, col_remover = st.columns([5, 1], vertical_alignment="center")
        rotulo = f"~~{tarefa['texto']}~~" if tarefa["concluida"] else tarefa["texto"]
        marcada = col_check.checkbox(rotulo, value=tarefa["concluida"], key=f"feita_{tarefa['id']}")
        if marcada != tarefa["concluida"]:
            tarefa["concluida"] = marcada
            st.rerun()
        if col_remover.button("Remover", key=f"remover_{tarefa['id']}"):
            tarefas.remove(tarefa)
            st.rerun()

    if concluidas and st.button("Limpar concluídas"):
        st.session_state.tarefas = [t for t in tarefas if not t["concluida"]]
        st.rerun()
