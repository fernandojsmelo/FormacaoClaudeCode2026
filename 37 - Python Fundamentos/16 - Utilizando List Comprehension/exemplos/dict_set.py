nomes = ["Ana", "Bruno", "Carla"]
tamanhos = {nome: len(nome) for nome in nomes}   # dict
print(tamanhos)
iniciais = {nome[0] for nome in ["ana", "alice", "bia"]}  # set
print(sorted(iniciais))
total = sum(n ** 2 for n in range(1, 4))   # gerador: sem []
print(total)
