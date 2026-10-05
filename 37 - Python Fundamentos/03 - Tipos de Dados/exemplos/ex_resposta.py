# Exercício: descubra o tipo e converta
valores = ["42", 3.7, True, "2.5"]
print(type(valores[0]), type(valores[1]), type(valores[2]))
print(int(valores[0]) * 2)       # "42" -> 42
print(int(valores[1]))           # 3.7 -> 3
print(float(valores[3]) + 1)     # "2.5" -> 3.5
print(int(valores[2]) + 1)       # True vale 1
