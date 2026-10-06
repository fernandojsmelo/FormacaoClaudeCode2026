import math
import re
from collections import Counter

DOCS = {
    "reembolso": "Reembolsos podem ser pedidos em ate 30 dias apos a compra. "
                 "O valor volta pelo mesmo meio de pagamento em 7 dias uteis.",
    "troca": "Trocas de produtos sao gratuitas em ate 15 dias, "
             "desde que o produto esteja na embalagem original.",
    "garantia": "A garantia dos eletronicos e de 12 meses contra defeitos "
                "de fabricacao, com apresentacao da nota fiscal.",
    "frete": "O frete e gratuito para compras acima de 200 reais "
             "em todo o territorio nacional.",
}
PARADAS = {"a", "o", "os", "as", "e", "de", "da", "do", "dos", "em", "no",
           "na", "para", "com", "por", "que", "qual", "ate", "apos", "um"}


def tokens(texto, limpar):
    palavras = re.findall(r"[a-z0-9]+", texto.lower())
    if not limpar:
        return palavras
    # sem palavras vazias e com plural removido (reembolsos -> reembolso)
    return [p.rstrip("s") if len(p) > 3 else p
            for p in palavras if p not in PARADAS]


def vetor(texto, idf, limpar):
    c = Counter(tokens(texto, limpar))
    return {t: n * idf.get(t, 0) for t, n in c.items()}


def cosseno(a, b):
    prod = sum(a[t] * b.get(t, 0) for t in a)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return prod / (na * nb) if na and nb else 0.0


def montar_indice(limpar):
    freq = Counter(t for d in DOCS.values() for t in set(tokens(d, limpar)))
    idf = {t: math.log(len(DOCS) / f) + 1 for t, f in freq.items()}
    return idf, {n: vetor(d, idf, limpar) for n, d in DOCS.items()}


def buscar(pergunta, limpar, minimo=0.2):
    idf, indice = montar_indice(limpar)
    q = vetor(pergunta, idf, limpar)
    pontos = sorted(((cosseno(q, v), n) for n, v in indice.items()),
                    reverse=True)
    s, nome = pontos[0]
    return (nome, round(s, 2)) if s >= minimo else (None, round(s, 2))


perguntas = ["Qual o prazo para pedir reembolso?",
             "Quanto tempo dura a garantia do celular?",
             "Qual a capital da Franca?"]
for p in perguntas:
    print("PERGUNTA:", p)
    print("  busca ingenua:", buscar(p, limpar=False))
    print("  busca limpa:  ", buscar(p, limpar=True))
