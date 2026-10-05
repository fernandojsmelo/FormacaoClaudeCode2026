turma = {
    "ana": {"nota": 9.0, "faltas": 1},
    "bia": {"nota": 7.5, "faltas": 4},
}
print(turma["bia"]["nota"])
turma["caio"] = {"nota": 8.0, "faltas": 0}
print(sorted(turma))      # sorted de um dict ordena as chaves
config = {"tema": "claro", "idioma": "pt"} | {"tema": "escuro"}
print(config)             # | junta; a direita vence
