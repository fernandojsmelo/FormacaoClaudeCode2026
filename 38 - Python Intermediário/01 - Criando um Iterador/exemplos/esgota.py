from contagem import Contagem

c = Contagem(3)
print(list(c))   # primeira volta: consome tudo
print(list(c))   # segunda volta: o iterador já acabou
