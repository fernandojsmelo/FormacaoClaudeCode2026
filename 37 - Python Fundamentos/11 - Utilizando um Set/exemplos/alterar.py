tags = {"python"}
tags.add("cursor")             # adiciona um
tags.update(["ia", "mcp"])     # adiciona vários
tags.add("python")             # já existe: nada muda
print(sorted(tags))
tags.discard("java")           # remove se existir (sem erro)
tags.remove("mcp")             # remove (dá erro se não existir)
print(sorted(tags))
