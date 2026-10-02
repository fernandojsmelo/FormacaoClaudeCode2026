from pathlib import Path

import streamlit as st

from jogo import OPCOES, jogada_do_computador, resultado

st.set_page_config(page_title="Pedra, Papel e Tesoura", page_icon="✊")
st.title("Pedra, Papel e Tesoura")
st.write("Clique na sua jogada. O computador escolhe ao mesmo tempo, ao acaso.")

PASTA_IMAGENS = Path(__file__).with_name("assets")
IMAGEM = {opcao: PASTA_IMAGENS / f"{opcao.lower()}.png" for opcao in OPCOES}

colunas = st.columns(3)
for coluna, opcao in zip(colunas, OPCOES):
    coluna.image(str(IMAGEM[opcao]), width="stretch")
    if coluna.button(opcao, key=f"jogar_{opcao}", width="stretch"):
        st.session_state.rodada = (opcao, jogada_do_computador())

if "rodada" in st.session_state:
    jogador, computador = st.session_state.rodada
    st.divider()
    lado_a, meio, lado_b = st.columns([2, 1, 2], vertical_alignment="center")
    lado_a.image(str(IMAGEM[jogador]), caption=f"Você: {jogador}", width=160)
    meio.markdown("<h2 style='text-align:center'>×</h2>", unsafe_allow_html=True)
    lado_b.image(str(IMAGEM[computador]), caption=f"Computador: {computador}", width=160)

    final = resultado(jogador, computador)
    if final == "vitoria":
        st.success("Você venceu! 🎉")
    elif final == "derrota":
        st.error("O computador venceu.")
    else:
        st.info("Empate!")
