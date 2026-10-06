import random
from collections import Counter, defaultdict

texto = """o gato dorme no sofa . o gato come o peixe .
o cachorro dorme no tapete . o cachorro come a carne .
a menina le o livro no sofa . a menina come o bolo ."""
palavras = texto.split()

# TREINO: percorre o texto uma vez e conta quem vem depois de quem
modelo = defaultdict(Counter)
for atual, proxima in zip(palavras, palavras[1:]):
    modelo[atual][proxima] += 1
print("palavras no vocabulario:", len(set(palavras)))
print("depois de 'o':", dict(modelo["o"]))


# INFERENCIA: usa o que foi aprendido, sem mudar nada no modelo
def gerar(inicio, tamanho, semente):
    rnd = random.Random(semente)
    saida = [inicio]
    for _ in range(tamanho):
        opcoes = modelo[saida[-1]]
        if not opcoes:
            break
        saida.append(rnd.choices(list(opcoes), list(opcoes.values()))[0])
    return " ".join(saida)


for s in (1, 2, 3):
    print(f"geracao {s}:", gerar("o", 6, s))
