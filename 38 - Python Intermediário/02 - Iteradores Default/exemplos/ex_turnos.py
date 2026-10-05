from itertools import cycle

pessoas = ["Ana", "Bia", "Caio"]
dias = ["seg", "ter", "qua", "qui", "sex"]

for dia, pessoa in zip(dias, cycle(pessoas)):
    print(f"{dia}: {pessoa}")
