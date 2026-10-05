entrada = "10, x, 25, , 7, 40"

partes = map(str.strip, entrada.split(","))
validos = filter(str.isdigit, partes)
numeros = map(int, validos)
print(sum(numeros))

# O mesmo com uma comprehension:
print(sum(int(p) for p in entrada.split(",")
          if p.strip().isdigit()))
