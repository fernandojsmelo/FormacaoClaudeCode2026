import streamlit as st

from jogo import OPCOES, jogada_do_computador, resultado

st.set_page_config(page_title="Pedra, Papel e Tesoura", page_icon="✊")
st.title("✊ ✋ ✌️ Pedra, Papel e Tesoura")
st.write("Escolha sua jogada. O computador escolhe ao mesmo tempo, ao acaso.")

EMOJI = {"Pedra": "✊", "Papel": "✋", "Tesoura": "✌️"}

colunas = st.columns(3)
escolha = None
for coluna, opcao in zip(colunas, OPCOES):
    if coluna.button(f"{EMOJI[opcao]} {opcao}", width="stretch"):
        escolha = opcao

if escolha:
    computador = jogada_do_computador()
    st.write(f"Você: **{EMOJI[escolha]} {escolha}** · Computador: **{EMOJI[computador]} {computador}**")
    final = resultado(escolha, computador)
    if final == "vitoria":
        st.success("Você venceu! 🎉")
    elif final == "derrota":
        st.error("O computador venceu.")
    else:
        st.info("Empate!")
