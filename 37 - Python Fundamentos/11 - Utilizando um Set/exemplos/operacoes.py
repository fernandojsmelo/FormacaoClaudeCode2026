python = {"ana", "bia", "caio", "davi"}
dados = {"bia", "davi", "eva"}
print(sorted(python | dados))   # união: estão em algum dos dois
print(sorted(python & dados))   # interseção: estão nos dois
print(sorted(python - dados))   # diferença: só em python
print(sorted(python ^ dados))   # só em um dos dois
print({"bia"} <= dados)         # é subconjunto?
