def ler_idade(texto):
    try:
        idade = int(texto)
    except ValueError:
        return None, f"'{texto}' não é um número inteiro"
    if not 0 <= idade <= 120:
        return None, f"{idade} está fora da faixa 0-120"
    return idade, "ok"


for entrada in ["34", "trinta", "-3", "150", " 42 "]:
    print(repr(entrada), "->", ler_idade(entrada))
