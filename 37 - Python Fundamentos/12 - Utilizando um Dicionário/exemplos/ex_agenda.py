# Exercício: agenda de telefones
agenda = {"Ana": "81 99999-0001", "Bia": "11 98888-0002"}
agenda["Caio"] = "21 97777-0003"
nome = input("Buscar: ").strip().title()
print(agenda.get(nome, "Não encontrado"))
print(len(agenda), "contatos:", ", ".join(sorted(agenda)))
