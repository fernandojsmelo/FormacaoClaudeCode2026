original = [1, 2, 3]
mesmo = original  # NÃO copia: mesma lista, dois nomes
copia = original.copy()  # cópia de verdade (ou original[:])
mesmo.append(4)
print(original)   # [1, 2, 3, 4]: mudou junto!
print(copia)      # [1, 2, 3]
