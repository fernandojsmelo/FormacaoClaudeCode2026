from rpfix import Fix
from links_google import links
f=Fix('res45.txt')
f.rep('primeira pedra!\nt| 😅','primeira pedra! 😅')
H=[('h| 💻 vs. : Quando usar cada um?\nc| forwhile','h| 💻 <code>for</code> vs. <code>while</code>: Quando usar cada um?'),
   ('h| 1. Como garantir que o vai parar mesmo?\nc| while','h| 1. Como garantir que o <code>while</code> vai parar mesmo?'),
   ('h| 2. A List Comprehension sempre substitui o ?\nc| for','h| 2. A List Comprehension sempre substitui o <code>for</code>?'),
   ('h| 1. Quando o NÃO dá conta e você REALMENTE precisa do\nc| for\nh| ?\nc| while','h| 1. Quando o <code>for</code> NÃO dá conta e você REALMENTE precisa do <code>while</code>?'),
   ('h| 2. A List Comprehension é mesmo mais rápida que o ?\nc| for','h| 2. A List Comprehension é mesmo mais rápida que o <code>for</code>?'),
   ('h| 1. O perigo do (Loop Infinito vs. Caminhar para a saída)\nc| while','h| 1. O perigo do <code>while</code> (Loop Infinito vs. Caminhar para a saída)'),
   ('h| 2. Ferramentas poderosas do\nc| for','h| 2. Ferramentas poderosas do <code>for</code>'),
   ('h| 🧙‍♂️ Bônus: List Comprehension com Filtragem ()\nc| if','h| 🧙‍♂️ Bônus: List Comprehension com Filtragem (<code>if</code>)'),
   ('h| 2. Adicionando um filtro ()\nc| if','h| 2. Adicionando um filtro (<code>if</code>)')]
for a,b in H: f.rep(a,b)
f.rep('quando depende de uma CONDIÇÃO</strong> O <code>while</code>','quando depende de uma CONDIÇÃO</strong>\np| O <code>while</code>')
f.rep('<code>while x</code> <code>&lt; 5:</code>','<code>while x &lt; 5:</code>')
f.block('t| FerramentaQuando usar?','t| curta.sempre primeiro!',
 'th| Ferramenta | Quando usar? | Evite quando...\n'
 'tr| <strong><code>for</code> tradicional</strong> | Para repetir ações um número fixo de vezes ou varrer listas. | A repetição depender de uma condição externa imprevisível.\n'
 'tr| <strong><code>while</code></strong> | Quando o encerramento depende de uma condição (ex: entrada do usuário). | Você já sabe o número exato de repetições (evita loops infinitos).\n'
 'tr| <strong>List Comprehension</strong> | Para transformar ou filtrar uma lista antiga em uma nova lista curta. | O código ficar muito longo ou confuso. Legibilidade vem sempre primeiro!')
f.rep('(</strong> <code>break</code><strong>)</strong>','(</strong><code>break</code><strong>)</strong>')
f.rep('<strong>de 10 a 30 mais rápida</strong> do que um <code>for</code> com <code>.append()</code>.\nt| %%','<strong>de 10% a 30% mais rápida</strong> do que um <code>for</code> com <code>.append()</code>.')
f.s=f.s.replace('</code><strong>','</code> <strong>')
f.rep('q| for vs while — a escolha por "definido indefinido": Os dois\nt| ×\nq| repetem','q| for vs while — a escolha por "definido × indefinido": Os dois repetem')
f.rep('q| O perigo do while as ferramentas dos laços: O risco clássico\nt| +\nq| do while','q| O perigo do while + as ferramentas dos laços: O risco clássico do while')
f.rep('q| exemplos?','q| … exemplos?'); f.rep('q| exemplos de códigos','q| … exemplos de códigos')
f.rep('para pegar o Índice Item:</strong>\nt| +','para pegar o Índice + Item:</strong>')
f.rep('t| Saída no console:\nli| 1º Lugar: Ana 2º Lugar: Bia 3º Lugar: Carlos','p| <em>Saída no console:</em>\nli| 1º Lugar: Ana\nli| 2º Lugar: Bia\nli| 3º Lugar: Carlos')
LK=links('orig_ResumoRolePlay45.pdf')
f.block('t| W3Schools','t| Towards Data Science','\n'.join(f'li| {t} · <em>{s}</em>' for t,s in LK[0]))
f.rep('(3 linhas com</strong> <code>for</code> <strong> </strong> <code>append</code> <strong>):</strong>\nt| +','(3 linhas com</strong> <code>for</code> <strong>+</strong> <code>append</code><strong>):</strong>')
f.rep('Bons testes! 🏃‍♀️🔋 Quando terminar de testar, me conta:','Bons testes! 🏃‍♀️🔋\np| Quando terminar de testar, me conta:')
f.rep('<strong>3 mensagens</strong> certinhas? O que acontece','<strong>3 mensagens</strong> certinhas?\nli| O que acontece')
f.s=f.s.replace('</code> <code>',' ')
f.code_from('rp45.fixed.txt')
f.numbered()
f.save('res45.fixed.txt')
