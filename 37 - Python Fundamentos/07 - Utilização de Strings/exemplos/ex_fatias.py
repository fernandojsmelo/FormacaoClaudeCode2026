# Exercício: fatiando um nome
nome = input("Nome completo: ").strip()
print("Primeira letra:", nome[0])
print("Última letra:", nome[-1])
print("Três primeiras:", nome[:3])
print("Ao contrário:", nome[::-1])
print("Tamanho:", len(nome))
