type Estoque = dict[str, int]


def repor(estoque: Estoque, item: str, qtd: int = 1) -> Estoque:
    return {**estoque, item: estoque.get(item, 0) + qtd}


def em_falta(estoque: Estoque) -> list[str]:
    return [item for item, qtd in estoque.items() if qtd == 0]


atual: Estoque = {"caneta": 0, "papel": 12}
novo = repor(atual, "caneta", 5)
print(novo, em_falta(atual), em_falta(novo))
