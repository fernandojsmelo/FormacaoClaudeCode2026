from collections import Counter
from io import BytesIO
from pathlib import Path

import pandas as pd
import streamlit as st

from analise import (
    carregar_stopwords,
    estatisticas,
    mais_frequentes,
    nuvem_de_palavras,
    palavras,
    sem_stopwords,
)

st.set_page_config(page_title="Analisador de Texto", page_icon="📝", layout="wide")
st.title("📝 Analisador de Texto")

EXEMPLO = Path(__file__).with_name("exemplo.txt")

arquivo = st.file_uploader("Envie um arquivo .txt", type=["txt"])
if arquivo is not None:
    texto_inicial = arquivo.read().decode("utf-8", errors="replace")
else:
    texto_inicial = EXEMPLO.read_text(encoding="utf-8") if EXEMPLO.exists() else ""

texto = st.text_area("Ou cole o texto aqui", value=texto_inicial, height=180)

if not texto.strip():
    st.info("Cole um texto ou envie um arquivo para começar.")
    st.stop()

with st.sidebar:
    st.header("Stopwords")
    remover = st.toggle("Remover stopwords", value=True)
    extras = st.text_input("Outras palavras para ignorar", placeholder="separadas por vírgula")
    stopwords = carregar_stopwords() | {p.strip().lower() for p in extras.split(",") if p.strip()}
    st.caption(f"{len(stopwords)} palavras na lista (arquivo stopwords_pt.txt + as suas).")

todas = palavras(texto)
if not todas:
    st.warning("O texto não tem palavras para analisar (só números ou símbolos).")
    st.stop()
lista = sem_stopwords(todas, stopwords) if remover else todas
dados = estatisticas(texto)
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Palavras", dados["palavras"])
c2.metric("Únicas", dados["palavras_unicas"])
c3.metric("Frases", dados["frases"])
c4.metric("Caracteres", dados["caracteres"])
c5.metric("Leitura", f"{dados['minutos_leitura']} min")

if remover:
    st.caption(f"{len(todas) - len(lista)} ocorrências de stopwords ignoradas na nuvem e na frequência.")

if not lista:
    st.warning("Não sobrou nenhuma palavra depois de remover as stopwords.")
    st.stop()

aba_nuvem, aba_frequencia = st.tabs(["☁️ Nuvem de palavras", "📊 Frequência"])

with aba_nuvem:
    col_cor, col_max = st.columns(2)
    cor = col_cor.selectbox("Paleta de cores", ["viridis", "plasma", "inferno", "cividis", "Dark2", "tab10"])
    maximo = col_max.slider("Máximo de palavras na nuvem", 20, 200, 100, step=10)
    imagem = nuvem_de_palavras(Counter(lista), cor=cor, maximo=maximo)
    st.image(imagem, width="stretch")

    buffer = BytesIO()
    imagem.save(buffer, format="PNG")
    st.download_button("Baixar a nuvem (PNG)", buffer.getvalue(), "nuvem.png", "image/png")

with aba_frequencia:
    quantidade = st.slider("Quantas palavras mostrar", 5, 30, 10)
    tabela = pd.DataFrame(mais_frequentes(lista, quantidade), columns=["Palavra", "Vezes"])
    col_tabela, col_grafico = st.columns([1, 2])
    col_tabela.dataframe(tabela, hide_index=True, width="stretch")
    col_grafico.bar_chart(tabela, x="Palavra", y="Vezes", sort="-Vezes")
