import json
import os
from pathlib import Path


def salvar_json_seguro(dados, caminho):
    caminho = Path(caminho)
    temporario = caminho.with_suffix(".tmp")
    with open(temporario, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False)
    os.replace(temporario, caminho)    # troca de uma vez só


salvar_json_seguro({"saldo": 150}, "conta.json")
salvar_json_seguro({"saldo": 90}, "conta.json")
print(Path("conta.json").read_text(encoding="utf-8"))
print(Path("conta.tmp").exists())
