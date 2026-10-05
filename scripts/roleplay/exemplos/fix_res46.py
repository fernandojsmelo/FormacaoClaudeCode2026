from rpfix import Fix
from links_google import links
P='orig_ResumoRolePlay46.pdf'
f=Fix('res46.txt')
f.headings(P)
LK=links(P)
f.block('t| pythonacademy.com.br','t| Funções Python! - YouTube','\n'.join(f'li| {t} · <em>{s}</em>' for t,s in LK[0]))
f.block('t| 1 / 5','t| Think about an immutable',
 'p| 1 / 5\np| 1. What data type does *args represent inside a function?\nli| A. List\nli| B. Dictionary\nli| C. Tuple\nli| D. Set\np| Ocultar dica\np| <em>Think about an immutable, ordered sequence in Python that uses parentheses ().</em>')
for t in ['O que vai acontecer aqui?','O que acabou de acontecer aqui?','Como corrigir isso do jeito profissional?','O que acontece se o arquivo do banco for corrompido ou apagado?']:
    f.rep('t| '+t,'h4| '+t)
f.rep('t| O que acontece na memória do Python quando você roda\nt| somar_ate_um(4)?','h4| O que acontece na memória do Python quando você roda <code>somar_ate_um(4)</code>?')
f.rep('e chama\nc| somar_ate_um(3)','e chama <code>somar_ate_um(3)</code>')
f.rep('para podermos passar algo como\nc| fazer_pedido("Mariana", "Hambúrguer", "Batata Frita", bebida="Suco de\np| <code>Laranja", ponto_da_carne="Bem passada")</code>.',
      'para podermos passar algo como <code>fazer_pedido("Mariana", "Hambúrguer", "Batata Frita", bebida="Suco de Laranja", ponto_da_carne="Bem passada")</code>.')
f.rep('para o <code>sorted</code>:\nt| "Olhe para esta informação aqui!"','para o <code>sorted</code>: <em>"Olhe para esta informação aqui!"</em>')
f.rep('t| Como ler isso em voz alta:\nt| "Python, ordene o ranking. Para cada jogador (entrada), use o\nt| jogador[\'pontos\'] (saída) como critério de ordenação."',
      'h4| Como ler isso em voz alta:\np| <em>"Python, ordene o ranking. Para cada jogador (entrada), use o jogador[\'pontos\'] (saída) como critério de ordenação."</em>')
f.rep('jogador[\\nome"]','jogador["nome"]')
f.rep('seria if n 1:. Então','seria if n == 1:. Então'); f.rep('assim:\\…\nt| ==','assim:\\…')
f.s=f.s.replace(':\\…',': …').replace(':\\ …',': …')
f.rep('em funções. Olhe para esta função','em funções.\np| Olhe para esta função')
f.rep('<code>lambda</code> <strong> </strong> <code>sorted()</code>: Vamos criar uma arena onde os monstros são\nt| +\nli| ordenados','<code>lambda</code> <strong>+</strong> <code>sorted()</code>: Vamos criar uma arena onde os monstros são\nli| ordenados')
f.rep('tudo! 🏆 O seu código','tudo! 🏆\np| O seu código')
T=open('rp46.fixed.txt',encoding='utf-8').read()
def bloco_rp(inicio):
    i=T.index(inicio); j=T.index('code:\n',i)+6; k=T.index('\nendcode:',j)
    return 'code:\n'+T[j:k]+'\nendcode:'
f.block('t| text\nt| ⚔ Herói Aragorn criado com sucesso!','t| 💥 O combo terminou! O herói cansou.',bloco_rp('h| 📺 O que aparece na tela quando rodamos'))
f.rep('<code>print("</code>🎵 <code>*Trilha sonora épica tocando*</code>🎵 <code>")</code>','<code>print("🎵 *Trilha sonora épica tocando* 🎵")</code>')
f.block('t| 📺 O que vai aparecer na tela:','t| 🎵 *A música diminui o tom...* 🎵','p| 📺 <strong>O que vai aparecer na tela:</strong>\n'+bloco_rp('h| 📺 O que vai aparecer na tela:'))
f.block('t| text\nt| ⚔ Herói Aragorn criado com sucesso!','t| ✨ FIM DE TURNO',
 'code:\nc| ⚔ Herói Aragorn criado com sucesso!\nc| 🎒 Equipamentos: (\'Espada\', \'Escudo\')\nc| - Forca: 18\nc| - Vida: 100\nc| 🔥 Aragorn entra na caverna escura e avista um DRAGAO!\nc| 🧪 *Aragorn bebe uma Poção de Força! Os ataques brilham em vermelho\nc| ⚔ Ataque Consecutivo! Energia restante: 3\nc| ⚔ Ataque Consecutivo! Energia restante: 2\nc| ⚔ Ataque Consecutivo! Energia restante: 1\nc| 💥 O combo terminou! O herói cansou.\nc| ✨ FIM DE TURNO: Aragorn causou um total de 60 de dano!\nendcode:')
f.rep('Define- se','Define-se')
f.rep('podemos ver\nt| como capturar erros de páginas que não existem (Erro 404) usando\np| <code>try/except</code>','podemos ver como capturar erros de páginas que não existem (Erro 404) usando <code>try/except</code>')
f.rep('de forma direta\nt| (escrevendo comandos SQL na mão) ou através de ORMs (ferramentas\nt| mágicas que transformam tabelas do banco de dados em classes e objetos\np| Python).',
      'de forma direta (escrevendo comandos SQL na mão) ou através de ORMs (ferramentas mágicas que transformam tabelas do banco de dados em classes e objetos Python).')
f.rep('blocos de linhas). A ausência','blocos de linhas).\nli| A ausência')
f.s=f.s.replace('</code> <code>',' ')
f.code_xml(P)
f.code_from('rp46.fixed.txt')
f.numbered()
f.save('res46.fixed.txt')
