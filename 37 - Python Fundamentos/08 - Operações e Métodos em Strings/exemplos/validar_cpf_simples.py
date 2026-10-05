cpf = input("CPF: ").strip().replace(".", "").replace("-", "")
if cpf.isdigit() and len(cpf) == 11:
    formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    print("Formato válido:", formatado)
else:
    print("Formato inválido")
