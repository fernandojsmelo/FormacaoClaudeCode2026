print(int("42") + 1)       # texto -> inteiro
print(float("3.5") * 2)    # texto -> float
print(str(10) + "0")       # inteiro -> texto
print(int(9.99))           # float -> int: corta as decimais
print(round(9.99))         # para arredondar, use round()

# bool(): vazio e zero são False; o resto é True
print(bool(0), bool(""), bool(None))
print(bool(7), bool("oi"), bool(" "))
