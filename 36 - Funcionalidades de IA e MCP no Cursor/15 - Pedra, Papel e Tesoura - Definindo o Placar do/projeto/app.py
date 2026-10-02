from pathlib import Path

import streamlit as st

from jogo import OPCOES, jogada_do_computador, resultado

st.set_page_config(page_title="Pedra, Papel e Tesoura", page_icon="✊")
st.title("Pedra, Papel e Tesoura")

PASTA_IMAGENS = Path(__file__).with_name("assets")
IMAGEM = {opcao: PASTA_IMAGENS / f"{opcao.lower()}.png" for opcao in OPCOES}
MENSAGEM = {"vitoria": "Você venceu! 🎉", "derrota": "O computador venceu.", "empate": "Empate!"}

if "placar" not in st.session_state:
    st.session_state.placar = {"vitoria": 0, "derrota": 0, "empate": 0}
    st.session_state.historico = []  # rodadas mais recentes primeiro

placar = st.session_state.placar

# Placar no topo
c1, c2, c3, c4 = st.columns(4)
c1.metric("Você", placar["vitoria"])
c2.metric("Computador", placar["derrota"])
c3.metric("Empates", placar["empate"])
c4.metric("Rodadas", sum(placar.values()))

colunas = st.columns(3)
for coluna, opcao in zip(colunas, OPCOES):
    coluna.image(str(IMAGEM[opcao]), width="stretch")
    if coluna.button(opcao, key=f"jogar_{opcao}", width="stretch"):
        computador = jogada_do_computador()
        final = resultado(opcao, computador)
        placar[final] += 1
        st.session_state.historico.insert(0, (opcao, computador, final))
        st.rerun()

historico = st.session_state.historico
if historico:
    jogador, computador, final = historico[0]
    st.divider()
    lado_a, meio, lado_b = st.columns([2, 1, 2], vertical_alignment="center")
    lado_a.image(str(IMAGEM[jogador]), caption=f"Você: {jogador}", width=160)
    meio.markdown("<h2 style='text-align:center'>×</h2>", unsafe_allow_html=True)
    lado_b.image(str(IMAGEM[computador]), caption=f"Computador: {computador}", width=160)
    {"vitoria": st.success, "derrota": st.error, "empate": st.info}[final](MENSAGEM[final])

    with st.expander("Últimas rodadas"):
        for jogador, computador, final in historico[:5]:
            st.write(f"{jogador} × {computador} → {MENSAGEM[final]}")

    if st.button("Zerar placar"):
        del st.session_state.placar
        del st.session_state.historico
        st.rerun()
