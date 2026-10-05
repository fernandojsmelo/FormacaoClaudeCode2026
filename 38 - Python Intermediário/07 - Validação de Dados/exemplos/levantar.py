def definir_desconto(percentual):
    if not 0 <= percentual <= 50:
        raise ValueError(f"desconto deve ficar entre 0 e 50, "
                         f"veio {percentual}")
    return percentual / 100


print(definir_desconto(15))
try:
    definir_desconto(80)
except ValueError as erro:
    print("Erro:", erro)
