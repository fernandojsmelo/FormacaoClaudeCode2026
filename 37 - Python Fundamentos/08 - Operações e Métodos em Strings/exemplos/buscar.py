frase = "banana com canela"
print(frase.find("na"))        # 2: primeira posição
print(frase.find("xyz"))       # -1: não achou
print(frase.count("a"))        # 5 ocorrências
print(frase.startswith("ban")) # True
print(frase.endswith(".txt"))  # False
print(frase.index("com"))      # 7 (find, mas com erro)
