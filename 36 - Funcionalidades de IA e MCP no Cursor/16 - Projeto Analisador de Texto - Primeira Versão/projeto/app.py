from pathlib import Path

import pandas as pd
import streamlit as st

from analise import estatisticas, mais_frequentes, palavras

st.set_page_config(page_title="Analisador de Texto", page_icon="📝")
st.title("📝 Analisador de Texto")

EXEMPLO = Path(__file__).with_name("exemplo.txt")

arquivo = st.file_uploader("Envie um arquivo .txt", type=["txt"])
if arquivo is not None:
    texto_inicial = arquivo.read().decode("utf-8", errors="replace")
else:
    texto_inicial = EXEMPLO.read_text(encoding="utf-8") if EXEMPLO.exists() else ""

texto = st.text_area("Ou cole o texto aqui", value=texto_inicial, height=220)

if not texto.strip():
    st.info("Cole um texto ou envie um arquivo para começar.")
    st.stop()

dados = estatisticas(texto)
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Palavras", dados["palavras"])
c2.metric("Únicas", dados["palavras_unicas"])
c3.metric("Frases", dados["frases"])
c4.metric("Caracteres", dados["caracteres"])
c5.metric("Leitura", f"{dados['minutos_leitura']} min")

quantidade = st.slider("Quantas palavras mostrar", 5, 30, 10)
top = mais_frequentes(palavras(texto), quantidade)
tabela = pd.DataFrame(top, columns=["Palavra", "Vezes"])

st.subheader("Palavras mais frequentes")
col_tabela, col_grafico = st.columns([1, 2])
col_tabela.dataframe(tabela, hide_index=True, width="stretch")
col_grafico.bar_chart(tabela, x="Palavra", y="Vezes", sort="-Vezes")
