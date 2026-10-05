import re


def validar(cadastro):
    erros = []
    if len(cadastro.get("nome", "").strip()) < 3:
        erros.append("nome: mínimo de 3 letras")
    if not re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+",
                        cadastro.get("email", "")):
        erros.append("email: formato inválido")
    if not str(cadastro.get("idade", "")).isdigit():
        erros.append("idade: use só números")
    return erros


bom = {"nome": "Ana", "email": "ana@site.com", "idade": "30"}
ruim = {"nome": " B ", "email": "b@", "idade": "trinta"}
print(validar(bom))
for erro in validar(ruim):
    print("-", erro)
