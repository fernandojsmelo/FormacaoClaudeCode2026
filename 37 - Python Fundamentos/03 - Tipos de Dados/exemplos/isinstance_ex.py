valor = 3.14
print(isinstance(valor, float))         # True
print(isinstance(valor, int))           # False
print(isinstance(valor, (int, float)))  # True: é um dos dois
