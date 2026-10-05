# Exercício: segundos em horas, minutos e segundos
total = int(input("Segundos: "))
horas = total // 3600
minutos = total % 3600 // 60
segundos = total % 60
print(f"{horas}h {minutos}min {segundos}s")
