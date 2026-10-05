from collections import Counter
from ler_arquivo import linhas


def so_erros(itens):
    return (l for l in itens if " ERROR " in l)


def codigos(itens):
    for linha in itens:
        yield linha.split()[3]       # data hora NIVEL CODIGO


contagem = Counter(codigos(so_erros(linhas("servidor.log"))))
print(contagem)
print(contagem.most_common(1))
