from rpfix import Fix
from links_google import links
P='orig_ResumoRolePlay44.pdf'
f=Fix('res44.txt')
f.headings(P)
f.rep('h| 🛠 Passo 1: Adicione este método dentro da classe\nc| GerenciadorEstoque','h| 🛠 Passo 1: Adicione este método dentro da classe <code>GerenciadorEstoque</code>')
f.block('t| Pode\nt| ÉAceita','t| produto -> Preço).',
 'th| Estrutura | Símbolo | É Ordenada? | Aceita Duplicados? | Pode Alterar? (Mutável) | Superpoder / Quando usar?\n'
 'tr| <strong>Lista</strong> | <code>[ ]</code> | Sim | Sim | Sim | <strong>Acessar por posição (índice).</strong> Use quando a ordem importa e você vai mexer nos dados toda hora.\n'
 'tr| <strong>Tupla</strong> | <code>( )</code> | Sim | Sim | ❌ Não | <strong>Garantia de segurança.</strong> Use para dados que nunca devem mudar (ex: coordenadas X e Y, meses do ano).\n'
 'tr| <strong>Set (Conjunto)</strong> | <code>{ }</code> | ❌ Não | ❌ Não | Sim | <strong>Busca instantânea e remoção de duplicados.</strong> Use para testar se algo existe ali dentro num piscar de olhos.\n'
 'tr| <strong>Dicionário</strong> | <code>{k: v}</code> | Sim* | ❌ Chaves não | Sim | <strong>Buscar "pelo nome" (Chave).</strong> Perfeito para associar uma informação a outra (ex: Nome do produto -&gt; Preço).')
f.rep('t| *Nota: Os dicionários','p| <em>*Nota: Os dicionários'); f.rep('a partir do Python 3.7.','a partir do Python 3.7.</em>')
# gráfico do original recriado em SVG (Lista cresce linearmente; Set fica constante)
xs=''.join(f'<text x="{60+i*40}" y="232" text-anchor="middle">{"0M" if i==0 else ("1M" if i==10 else f"0.{i}M")}</text>' for i in range(11))
ys=''.join(f'<text x="52" y="{214-i*19}" text-anchor="end">{i*10}</text><line x1="60" x2="460" y1="{210-i*19}" y2="{210-i*19}" stroke="#3A2F24" stroke-width="0.6"/>' for i in range(11))
svg=('<svg viewBox="0 0 480 268" width="100%" style="max-width:520px;display:block;margin:6px auto 10px;background:#100D0A;border:1px solid #3A2F24;border-radius:6px" '
 'font-family="Inter,sans-serif" font-size="9" fill="#AE9F8C">'
 '<text x="240" y="14" text-anchor="middle" font-size="11" fill="#F3ECE2">Tempo de Busca: Lista vs Set</text>'+ys+xs+
 '<line x1="60" y1="210" x2="460" y2="20" stroke="#6FA8F2" stroke-width="2"/>'
 '<line x1="60" y1="210" x2="460" y2="210" stroke="#DE8B62" stroke-width="2.4"/>'
 '<text x="260" y="250" text-anchor="middle">Número de Elementos (N)</text>'
 '<text x="16" y="115" text-anchor="middle" transform="rotate(-90 16 115)">Tempo de Busca (Tempo Relativo)</text>'
 '<rect x="80" y="26" width="10" height="3" fill="#6FA8F2"/><text x="94" y="30">Lista (Busca Linear)</text>'
 '<rect x="200" y="26" width="10" height="3" fill="#DE8B62"/><text x="214" y="30">Set (Busca Instantânea)</text></svg>')
f.rep('t| Tempo de Busca: Lista vs Set','p| '+svg)
for t in ['1. Procurar dados "pelo nome" (Dicionário)','2. Checagem ultra rápida sem lentidão (Set)','Exemplo 1: Coordenadas de um mapa (Dicionário)','Exemplo 2: Histórico de combinações de jogos (Set)',
          '1. Criando o Estoque e Evitando Duplicatas (O jeito ideal)','2. Buscando Dados "Pelo Código" Instantaneamente','3. E onde o Set entraria se você quisesse usá-lo?',
          'Do jeito antigo (com risco de esquecer o contador):','Do jeito Pythonico (com enumerate):']:
    f.rep('t| '+t,'h4| '+t)
f.rep('<strong>sim, isso dá um erro clássico no</strong>\nt| Python!','<strong>sim, isso dá um erro clássico no Python!</strong>')
f.rep('\\unhashable"','"unhashable"')
LK=links(P)
for n,(a,b) in enumerate([('t| Stack Overflow\nt| use a Dictionary','t| Data Structure For Storing Non Duplicate Items In Python'),('t| Stack Overflow\nt| function to reduce','t| function to reduce the quantity in the stock. The ...'),('t| YouTube\nt| Inventory System','t| DEV Community\nt| Inventory Management System with Python')]):
    f.block(a,b,'\n'.join(f'li| {t} · <em>{s}</em>' for t,s in LK[n]))
f.rep('Dicionário Set ficou perfeito?\nt| +','Dicionário + Set ficou perfeito?')
f.rep('(quantidade preço de cada item).\nt| ×','(quantidade × preço de cada item).')
f.rep('facilitando a leitura rápida. <strong>Visão de Negócio:</strong>','facilitando a leitura rápida.\nli| <strong>Visão de Negócio:</strong>')
f.rep('h| 💻 O Código Completo (com Salvamento e Carregamento\nt| Automático)','h| 💻 O Código Completo (com Salvamento e Carregamento Automático)')
f.rep('criássemos esse sistema usando\nt| Orientação a Objetos','criássemos esse sistema usando <strong>Orientação a Objetos</strong>')
f.rep('duas classes: 1. <code>Produto</code>:','duas classes:\np| 1. <code>Produto</code>:')
f.rep('<strong>Para iniciar o</strong>\nt| programa, você executará este arquivo.','<strong>Para iniciar o programa, você executará este arquivo.</strong>')
f.rep('(esquecendo o terminal de vez!) Criar uma opção','(esquecendo o terminal de vez!)\nli| Criar uma opção')
f.rep('li| for vs while — a escolha por "definido × indefinido": Os dois\nq| repetem','q| for vs while — a escolha por "definido × indefinido": Os dois repetem')
f.rep('resolve 99 das\nt| %\np| dúvidas sobre loops.','resolve 99% das dúvidas sobre loops.')
f.rep('q| O perigo do while as ferramentas dos laços: O risco clássico\nt| +\nq| do while','q| O perigo do while + as ferramentas dos laços: O risco clássico do while')
f.rep('h| 🦥 A Prima "Preguiçosa": enerator Expression\nt| G','h| 🦥 A Prima "Preguiçosa": Generator Expression')
f.rep('t| Reparou que na função sum() você nem precisa de parênteses duplos? O Python\nt| já entende que é um Generator!','p| <em>Reparou que na função <code>sum()</code> você nem precisa de parênteses duplos? O Python já entende que é um Generator!</em>')
f.s=f.s.replace('</code> <code>',' ')
f.code_xml(P)
f.code_from('rp44.fixed.txt')
f.numbered()
f.save('res44.fixed.txt')
print('\n'.join(f.tit))
