BANCO = [f"cliente{n}" for n in range(1, 8)]


def buscar_pagina(numero, tamanho=3):
    """Simula uma API que devolve uma página por vez."""
    print(f"  (pedindo página {numero})")
    inicio = (numero - 1) * tamanho
    return BANCO[inicio:inicio + tamanho]


def todos_os_clientes():
    numero = 1
    while pagina := buscar_pagina(numero):
        yield from pagina
        numero += 1


for cliente in todos_os_clientes():
    print(cliente)
    if cliente == "cliente4":
        break                       # nem pede a página 3
