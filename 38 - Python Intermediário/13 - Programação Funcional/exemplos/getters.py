from operator import itemgetter, attrgetter
from collections import namedtuple

vendas = [("ana", 300), ("bia", 950), ("caio", 120)]
print(sorted(vendas, key=itemgetter(1), reverse=True))

Livro = namedtuple("Livro", "titulo ano")
livros = [Livro("Duna", 1965), Livro("1984", 1949)]
por_ano = sorted(livros, key=attrgetter("ano"))
print([livro.titulo for livro in por_ano])
