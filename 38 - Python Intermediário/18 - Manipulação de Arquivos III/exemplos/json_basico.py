import json

config = {"tema": "escuro", "fonte": 14, "atalhos": ["ctrl+s"],
          "beta": True, "proxy": None}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

with open("config.json", encoding="utf-8") as f:
    lido = json.load(f)

print(lido == config, type(lido["atalhos"]).__name__)
print(open("config.json", encoding="utf-8").read())
