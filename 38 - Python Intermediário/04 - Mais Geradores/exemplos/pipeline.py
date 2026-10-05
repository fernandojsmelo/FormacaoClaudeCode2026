linhas = ["10", "", "7", "x", "3", "25"]


def nao_vazias(itens):
    for item in itens:
        if item.strip():
            yield item


def numeros(itens):
    for item in itens:
        if item.isdigit():
            yield int(item)


def acima_de(limite, nums):
    for n in nums:
        if n > limite:
            yield n


etapas = acima_de(5, numeros(nao_vazias(linhas)))
print(list(etapas))
