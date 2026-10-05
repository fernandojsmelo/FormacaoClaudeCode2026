# Exercício: limpar uma lista de e-mails
brutos = [" Ana@Ex.com", "bia@ex.com ", "", "CAIO@EX.COM", "x"]
emails = [e.strip().lower() for e in brutos if "@" in e]
print(emails)
dominios = {e.split("@")[1] for e in emails}
print(dominios)
