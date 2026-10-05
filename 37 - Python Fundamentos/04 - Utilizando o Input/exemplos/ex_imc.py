# Exercício: calculadora de IMC
nome = input("Nome: ").strip()
peso = float(input("Peso (kg): ").replace(",", "."))
altura = float(input("Altura (m): ").replace(",", "."))
imc = peso / altura ** 2
print(f"{nome}, seu IMC é {imc:.1f}")
