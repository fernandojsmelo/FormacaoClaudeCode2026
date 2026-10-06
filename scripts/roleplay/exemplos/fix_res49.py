from rpfix import Fix
from links_google import links
P='orig_ResumoRolePlay49.pdf'
f=Fix('res49.txt')
f.headings(P)
LK=links(P)[0]
LK=[('5. Estruturas de dados — Documentação Python 3.14.8',s) if s=='Python documentation' else (t,s) for t,s in LK]
f.block('t| pythonacademy.com.br','t| Manipulando Listas em Python: Dicas e Truques Essenciais - DIO',
 '\n'.join(f'li| {t} · <em>{s}</em>' for t,s in LK))
f.block('t| MétodoQuando usar?','t| mais legível.',
 'th| Método | Quando usar? | O que ele faz?\n'
 'tr| <code>map()</code> | Quando precisa modificar todos os itens (ex: converter moedas, formatar strings). | Aplica uma função em cada elemento.\n'
 'tr| <code>filter()</code> | Quando você precisa reduzir a lista (ex: remover nulos, filtrar idades &gt; 18). | Testa cada elemento usando uma condição.\n'
 'tr| <strong>List Comprehension</strong> | Quase sempre. É o padrão mais amado pela comunidade Python. | Faz o papel do <code>map</code> e do <code>filter</code> de forma ainda mais legível.')
f.rep('<code>map</code>\nt| em vez de uma compreensão','<code>map</code> em vez de uma compreensão')
f.rep('t| (Nota: Você também pode fazer isso com compreensões usando parênteses (x *\nt| 2 for x in ...), que viram "generator expressions").',
      'p| (Nota: Você também pode fazer isso com compreensões usando parênteses <code>(x * 2 for x in ...)</code>, que viram "generator expressions").')
f.pct()
f.rep('padrão visual do\nli| Python, aceita','padrão visual do Python, aceita')
f.rep('"Se for diferente de\nt| \'NULO\', vou limpar e converter para inteiro. Caso contrário (else), vou\nli| transformar em 0".',
      '"Se for diferente de \'NULO\', vou limpar e converter para inteiro. Caso contrário (else), vou transformar em 0".')
f.rep('t| (Dica de amigo: se o seu código começar a ficar complexo assim em uma linha só,\nt| geralmente vale mais a pena voltar para o for tradicional ou usar funções para\nt| não quebrar a cabeça tentando ler o código depois!).',
      'p| (Dica de amigo: se o seu código começar a ficar complexo assim em uma linha só, geralmente vale mais a pena voltar para o <code>for</code> tradicional ou usar funções para não quebrar a cabeça tentando ler o código depois!).')
f.rep('para Nome). Partir direto','para Nome).\nli| Partir direto')
f.rep('t| Repare que temos espaços extras','p| Repare que temos espaços extras')
for n in ('17500','0','1200'):
    f.rep(f'({n} 0)\nt| >',f'({n} &gt; 0)')
f.rep('"Gere o arquivo\nt| CSV apenas com as minhas colunas reais (produto, quantidade, preco_unitario,\nli| faturamento)',
      '"Gere o arquivo CSV apenas com as minhas colunas reais (produto, quantidade, preco_unitario, faturamento)')
f.rep('t| (Repare que o Corolla e o Compass sumiram porque o faturamento deles deu zero,\nt| e os nomes do Onix e do HB20 agora estão sem espaços nas pontas).',
      'p| (Repare que o Corolla e o Compass sumiram porque o faturamento deles deu zero, e os nomes do Onix e do HB20 agora estão sem espaços nas pontas).')
f.rep('esperadas? Quer que eu mostre','esperadas?\nli| Quer que eu mostre')
f.rep('q| Cuidados (iterador preguiçoso) a alternativa pythônica: No\nt| +\nq| Python 3,','q| Cuidados (iterador preguiçoso) + a alternativa pythônica: No Python 3,')
f.code_xml(P)
f.code_from('rp49.fixed.txt',langs=('python','text','csv'))
f.numbered()
f.t_to_h()
f.save('res49.fixed.txt')
print('\n'.join(f.tit)); print(f.s.count('\nq| ')+f.s.startswith('q| '),'perguntas')
