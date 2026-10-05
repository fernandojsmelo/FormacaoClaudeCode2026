frutas = ["maçã", "banana", "uva"]
frutas[1] = "manga"          # listas são mutáveis
frutas.append("kiwi")        # adiciona no fim
frutas.insert(0, "pera")     # adiciona na posição 0
frutas.extend(["limão", "caju"])  # adiciona vários
print(frutas)
frutas.remove("uva")         # remove pelo valor
ultima = frutas.pop()        # remove e devolve o último
print(ultima, frutas)
del frutas[0]                # remove pela posição
print(frutas)
