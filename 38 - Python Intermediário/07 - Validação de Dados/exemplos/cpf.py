import re


def cpf_valido(cpf):
    numeros = re.sub(r"\D", "", cpf)      # só os dígitos
    repetido = numeros == numeros[0] * 11
    if len(numeros) != 11 or repetido:
        return False
    for tamanho in (9, 10):           # os 2 dígitos finais
        soma = sum(int(d) * (tamanho + 1 - i)
                   for i, d in enumerate(numeros[:tamanho]))
        digito = soma * 10 % 11 % 10
        if digito != int(numeros[tamanho]):
            return False
    return True


for cpf in ["529.982.247-25", "529.982.247-26",
            "111.111.111-11"]:
    print(cpf, cpf_valido(cpf))
