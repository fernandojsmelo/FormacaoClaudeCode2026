from rpfix import Fix
P='orig_ResumoRolePlay48.pdf'
f=Fix('res48.txt')
f.headings(P)
f.rep('t| Oi!','p| Oi!')
f.rep('destrói a função. O <code>yield</code> é um','destrói a função.\np| O <code>yield</code> é um')
f.rep('p| Veja a diferença na prática: <strong>Com</strong>','p| Veja a diferença na prática:\np| <strong>Com</strong>')
f.block('t| Conceito O que significa?','t| prontos.',
 'th| Conceito | O que significa? | Exemplo no Python\n'
 'tr| <strong>Iterável</strong> | Qualquer coisa que você consegue colocar dentro de um <code>for</code>. | Listas, Strings, Dicionários, Tuplas.\n'
 'tr| <strong>Iterador</strong> | O "ponteiro" por trás dos panos que sabe qual é o próximo item (usando a função <code>next()</code>). | O objeto que o <code>for</code> cria para ler a lista.\n'
 'tr| <strong>Gerador</strong> | Um tipo especial de iterador que fabrica os dados sob demanda em vez de guardá-los prontos. | Funções com <code>yield</code> ou expressões geradoras.')
f.rep('\\preguiçoso"','"preguiçoso"')
f.rep('de uma vez só! Ficou mais claro como','de uma vez só!\np| Ficou mais claro como')
f.rep('pede a próxima linha. 6. A função','pede a próxima linha.\np| 6. A função')
f.rep('t| 🚨 Investigando transações suspeitas:\nc|','c| 🚨 Investigando transações suspeitas:\nc|')
f.rep('Boa prática! 💻\nt| 🔥','Boa prática! 💻🔥')
f.rep('li| Organizar os três conceitos (iterável → iterador → gerador):\nq| Iterável','q| Organizar os três conceitos (iterável → iterador → gerador): Iterável')
f.rep('<strong>99 lá!</strong> O seu caminho está absolutamente correto e a sua intuição foi\nt| %\np| perfeita','<strong>99% lá!</strong> O seu caminho está absolutamente correto e a sua intuição foi perfeita')
f.rep('quebra- cabeça','quebra-cabeça'); f.rep('reutilizá- lo','reutilizá-lo')
f.rep('q| Explicar o gerador na prática (o yield que pausa) as duas\nt| +\nq| formas:','q| Explicar o gerador na prática (o yield que pausa) + as duas formas:')
f.block('t| RecursoLista []Gerador ()','t| Permite OrdenaçãoSim',
 'th| Recurso | Lista <code>[]</code> | Gerador <code>()</code>\n'
 'tr| <strong>Consumo de Memória</strong> | Alto (guarda tudo de uma vez) | Mínimo (um por vez)\n'
 'tr| <strong>Reutilização</strong> | Sim (quantas vezes quiser) | Não (acabou, sumiu)\n'
 'tr| <strong>Acesso por Índice ([0])</strong> | Sim | Não\n'
 'tr| <strong>Saber o tamanho (len())</strong> | Sim | Não\n'
 'tr| <strong>Permite Ordenação</strong> | Sim (muito fácil) | Não diretamente')
f.rep('até logo! 🚀🐍✨ Sempre que quiser','até logo! 🚀🐍✨\np| Sempre que quiser')
f.s=f.s.replace('</code> <code>',' ')
f.code_xml(P)
f.code_from('rp48.fixed.txt')
f.numbered()
f.t_to_h()
f.save('res48.fixed.txt')
print('\n'.join(f.tit))
