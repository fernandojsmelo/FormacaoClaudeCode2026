texto = "Olá"
dados = texto.encode("utf-8")          # str -> bytes
print(dados, len(texto), len(dados))

with open("saudacao.bin", "wb") as f:   # "b": modo binário
    f.write(dados + bytes([0, 255]))

with open("saudacao.bin", "rb") as f:
    lido = f.read()
print(lido)
print(list(lido))                       # cada byte é um número
print(lido[:4].decode("utf-8"))         # bytes -> str
