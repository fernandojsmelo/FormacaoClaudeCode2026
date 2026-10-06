from rpfix import Fix
from links_google import links
P='orig_ResumoRolePlay50.pdf'
f=Fix('res50.txt')
f.headings(P)
f.block('t| Reddit','t| : domine os loops',
 'q| "Opa! Eu tô aprendendo Python pra mexer com dados e meus loops tão um horror. Quando eu quero o número de ca…\n'
 'li| Como você começa um loop "for" em 1 em vez de 0? : r/learnpython · <em>Reddit</em>\n'
 'li| Python: domine os loops (for, while) de forma simples - Rocketseat · <em>Rocketseat</em>')
f.rep('</strong> <strong>O que ele te entrega:</strong>','</strong>\nli| <strong>O que ele te entrega:</strong>') if '</strong> <strong>O que ele te entrega:</strong>' in f.s else f.rep('automático. <strong>O que ele te entrega:</strong>','automático.\nli| <strong>O que ele te entrega:</strong>')
f.block('t| O que você\nt| FunçãoO que','t| lista2)lista2[i] para cruzar dados.',
 'th| Função | O que ela resolve? | O que você recebe no for?\n'
 'tr| <code>enumerate(lista)</code> | Evita que você use <code>range(len())</code> para pegar o índice. | <code>índice, item</code>\n'
 'tr| <code>zip(lista1, lista2)</code> | Evita que você use <code>lista1[i]</code> e <code>lista2[i]</code> para cruzar dados. | <code>item1, item2</code>')
f.rep('melhorar sua lógica em Python!\nt| 🚀','melhorar sua lógica em Python! 🚀')
f.rep('q| Explicar enumerate (índice item, sem contador na mão): O\nt| +\nq| problema','q| Explicar enumerate (índice + item, sem contador na mão): O problema')
f.rep('q| Combinar os dois a natureza "preguiçosa": Dá para usar\nt| +\nq| juntos:','q| Combinar os dois + a natureza "preguiçosa": Dá para usar juntos:')
f.block('t| YouTube\nt| zip() - Python em 1 minuto','t| zip Explained - PythonAlchemist','\n'.join(f'li| {t} · <em>{s}</em>' for t,s in links(P)[0]))
f.rep('h| 🦥 2. A Natureza "Preguiçosa" (y)\nt| Laz Evaluation','h| 🦥 2. A Natureza "Preguiçosa" (Lazy Evaluation)')
f.s=f.s.replace('</code> <code>',' ')
f.code_xml(P)
f.code_from('rp50.fixed.txt')
f.numbered()
f.t_to_h()
f.save('res50.fixed.txt')
print('\n'.join(f.tit))
