# Exercício: arrumar e analisar um nome digitado
nome = input("Nome: ").strip().title()
partes = nome.split()
print("Nome arrumado:", nome)
print("Primeiro nome:", partes[0])
print("Último nome:", partes[-1])
print("Iniciais:", partes[0][0] + partes[-1][0])
print("Quantas letras 'a':", nome.lower().count("a"))
