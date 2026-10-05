def buscar_email(nome: str) -> str | None:     # pode faltar
    cadastro = {"ana": "ana@site.com"}
    return cadastro.get(nome)


email = buscar_email("bia")
if email is None:
    print("sem e-mail cadastrado")
else:
    print(email.upper())     # aqui o verificador sabe que é str
