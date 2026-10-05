import re

REGRAS = [
    (r".{8,}", "pelo menos 8 caracteres"),
    (r"[A-Z]", "uma letra maiúscula"),
    (r"[a-z]", "uma letra minúscula"),
    (r"\d", "um número"),
]


def problemas_da_senha(senha):
    return [msg for padrao, msg in REGRAS
            if not re.search(padrao, senha)]


for s in ["abc", "Senha2026", "senhafraca1"]:
    faltam = problemas_da_senha(s)
    print(s, "->", "forte" if not faltam else "falta:")
    for item in faltam:
        print("   -", item)
