"""Funções de análise de texto (sem dependências além da biblioteca padrão)."""
import math
import re
from collections import Counter

PALAVRA = re.compile(r"[^\W\d_]+(?:-[^\W\d_]+)*")  # letras, com acentos e hífen interno


def palavras(texto):
    """Lista de palavras em minúsculas, sem números nem pontuação."""
    return [p.lower() for p in PALAVRA.findall(texto)]


def estatisticas(texto):
    lista = palavras(texto)
    frases = [f for f in re.split(r"[.!?]+", texto) if f.strip()]
    paragrafos = [p for p in re.split(r"\n\s*\n", texto) if p.strip()]
    return {
        "caracteres": len(texto),
        "palavras": len(lista),
        "palavras_unicas": len(set(lista)),
        "frases": len(frases),
        "paragrafos": len(paragrafos),
        # cerca de 200 palavras por minuto de leitura silenciosa
        "minutos_leitura": max(1, math.ceil(len(lista) / 200)) if lista else 0,
    }


def mais_frequentes(lista, quantidade=10):
    return Counter(lista).most_common(quantidade)


def nuvem_de_palavras(frequencias, largura=900, altura=450, cor="viridis", maximo=100):
    """Gera a nuvem (imagem PIL) a partir de um dicionário {palavra: vezes}."""
    from wordcloud import WordCloud

    nuvem = WordCloud(
        width=largura,
        height=altura,
        background_color="white",
        colormap=cor,
        max_words=maximo,
        stopwords=set(),  # a v2 ainda não remove palavras: isso vem na próxima aula
        collocations=False,
    )
    return nuvem.generate_from_frequencies(frequencias).to_image()
