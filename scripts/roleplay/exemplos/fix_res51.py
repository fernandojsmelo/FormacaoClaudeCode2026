from rpfix import Fix
from links_google import links
P='orig_ResumoRolePlay51.pdf'
f=Fix('res51.txt')
f.headings(P)
f.block('t| YouTube\nt| Como Automatizar','t| — Leitura e escrita de arquivos CSV',
 'q| "Oi! Eu tô automatizando umas tarefas em Python e preciso ler e gravar arquivos — uns CSV, uns relatórios em texto. …\n'
 'li| Como Automatizar Qualquer Planilha com Python [RÁPIDO] · <em>YouTube</em>\n'
 'li| Como salvar um CSV em memória utilizando Python? · <em>Stack Overflow</em>\n'
 'li| Como manipular arquivos CSV no Python · <em>pythonacademy.com.br</em>\n'
 'li| csv — Leitura e escrita de arquivos CSV — Documentação Python ... · <em>Python documentation</em>')
f.rep('(ele não fica congelado para sempre),\nt| mas ele interrompe o seu script na hora com uma mensagem de erro vermelha\np| na tela.',
      '(ele não fica congelado para sempre), mas ele interrompe o seu script na hora com uma mensagem de erro vermelha na tela.')
f.rep('rodar esse bloco\nt| aqui. Se der o erro de permissão (PermissionError), não trave o programa! Em\nt| vez disso, faça essa outra coisa (except)."',
      'rodar esse bloco aqui. Se der o erro de permissão (PermissionError), não trave o programa! Em vez disso, faça essa outra coisa (except)."')
f.rep('Só depois do arquivo estar 100 fechado e seguro é que o loop termina.\nt| %','Só depois do arquivo estar 100% fechado e seguro é que o loop termina.')
f.rep('O mistério foi 100 desvendado: o que destruiu seus dados aquela vez foi o\nt| %\np| automatismo','O mistério foi 100% desvendado: o que destruiu seus dados aquela vez foi o automatismo')
f.rep('"Formatar e recomeçar". <code>\'a\'</code> é','"Formatar e recomeçar".\nli| <code>\'a\'</code> é')
f.rep('li| Ler com inteligência + encoding + caminhos: Leitura: f.read()\nq| traz tudo','q| Ler com inteligência + encoding + caminhos: Leitura: f.read() traz tudo')
f.rep("encoding'utf-8' sempre agora, porque esses problemas co…\nt| =","encoding='utf-8' sempre agora, porque esses problemas co…")
f.block("t| O que faz se o arquivo JÁO que faz","t| (Criar)antigo!).",
 "th| Modo | Nome | O que faz se o arquivo JÁ EXISTE? | O que faz se o arquivo NÃO EXISTE?\n"
 "tr| <code>'r'</code> | Read (Leitura) | Abre para leitura a partir do início. | 🚨 Dá erro (<code>FileNotFoundError</code>).\n"
 "tr| <code>'w'</code> | Write (Escrita) | 💥 <strong>Zera tudo!</strong> Apaga o conteúdo e escreve do zero. | Cria um arquivo novinho.\n"
 "tr| <code>'a'</code> | Append (Anexar) | Preserva tudo e cola o cursor no final para adicionar. | Cria um arquivo novinho.\n"
 "tr| <code>'x'</code> | Exclusive (Criar) | 🚨 Dá erro (Protege o arquivo antigo!). | Cria um arquivo novinho.")
LK=links(P)
f.block('t| Stack Overflow\nt| Unicode (UTF-8)','t| Unicode (UTF-8) reading','\n'.join(f'li| {t} · <em>{s}</em>' for t,s in LK[-1]))
f.s=f.s.replace('</code> <code>',' ')
f.code_xml(P)
f.code_from('rp51.fixed.txt')
f.numbered()
f.t_to_h()
f.save('res51.fixed.txt')
print('\n'.join(f.tit)); print(len(LK), [len(x) for x in LK])
