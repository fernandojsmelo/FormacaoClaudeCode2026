# Exercício: classificação do IMC
imc = float(input("IMC: ").replace(",", "."))
if imc < 18.5:
    faixa = "abaixo do peso"
elif imc < 25:
    faixa = "peso normal"
elif imc < 30:
    faixa = "sobrepeso"
else:
    faixa = "obesidade"
print(f"IMC {imc:.1f}: {faixa}")
