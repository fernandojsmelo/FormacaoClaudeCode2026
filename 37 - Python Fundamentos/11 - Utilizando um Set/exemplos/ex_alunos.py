# Exercício: quem fez as duas provas?
prova1 = ["ana", "bia", "caio", "ana", "davi"]
prova2 = ["bia", "davi", "eva", "bia"]
p1, p2 = set(prova1), set(prova2)
print("Fizeram as duas:", sorted(p1 & p2))
print("Só a primeira:", sorted(p1 - p2))
print("Total de alunos:", len(p1 | p2))
