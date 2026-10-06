# notas de 1 a 5, atribuidas com as areas (valores ficticios)
IDEIAS = {
    "triagem de chamados":  dict(valor=5, viabilidade=4, dados=4, risco=2),
    "resumo de reunioes":   dict(valor=3, viabilidade=5, dados=5, risco=1),
    "analise de contratos": dict(valor=5, viabilidade=2, dados=3, risco=5),
    "previsao de demanda":  dict(valor=4, viabilidade=3, dados=2, risco=2),
}


def nota(i, pesos):
    pos = sum(pesos[k] * i[k] for k in ("valor", "viabilidade", "dados"))
    return pos - pesos["risco"] * i["risco"]


def ranking(pesos):
    pares = sorted(((nota(i, pesos), n) for n, i in IDEIAS.items()),
                   reverse=True)
    return [f"{n} ({s:.0f})" for s, n in pares]


base = dict(valor=3, viabilidade=2, dados=1, risco=2)
foco_valor = dict(valor=5, viabilidade=1, dados=1, risco=1)
print("pesos equilibrados:", ranking(base))
print("foco em valor:     ", ranking(foco_valor))
