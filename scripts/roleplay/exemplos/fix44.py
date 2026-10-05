import re
from fences import recuo
s=open('rp44.n.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n, ('NÃO ACHEI',a[:70]); s=s.replace(a,b)
# rodapé/cabeçalho de página que vazou para dentro de um bloco de código
s=re.sub(r'\nc\| Esta transcrição inclui conteúdo gerado por IA[^\n]*\nc\| \d+/\d+\nc\| Formação Claude Code 2026: IA com Claude e Cowork\nc\| O Especialista em Python e o Iniciante que "Usa Lista pra\nc\| Tudo"','',s)
# tabela
i=s.index('p| EstruturaSímbolo'); j=s.index('\n',s.index('p| Dicionário{k: v}'))
s=s[:i]+('th| Estrutura | Símbolo | É Ordenada? | Aceita Duplicados? | Pode Alterar? (Mutável) | Superpoder / Quando usar?\n'
 'tr| **Lista** | [ ] | Sim | Sim | Sim | **Acessar por posição (índice).** Use quando a ordem importa e você vai mexer nos dados toda hora.\n'
 'tr| **Tupla** | ( ) | Sim | Sim | ❌ Não | **Garantia de segurança.** Use para dados que nunca devem mudar (ex: coordenadas X e Y, meses do ano).\n'
 'tr| **Set (Conjunto)** | { } | ❌ Não | ❌ Não | Sim | **Busca instantânea e remoção de duplicados.** Use para testar se algo existe ali dentro num piscar de olhos.\n'
 'tr| **Dicionário** | {k: v} | Sim* | ❌ Chaves não | Sim | **Buscar "pelo nome" (Chave).** Perfeito para associar uma informação a outra (ex: Nome do produto -> Preço).')+s[j:]
s=s.replace('? ¡ ','? ➡ ')
# blocos que viraram parágrafo (rótulo "python" grudado no fim da frase)
def para_code(intro):
    global s
    i=s.index(intro); j=s.index('p| Use o código com cuidado.',i)
    linhas=s[i:j].split('\n'); cab=re.sub(r':? ?python$',':',linhas[0].rstrip()) if linhas[0].rstrip().endswith('python') else linhas[0]
    corpo=[l[3:] if l.startswith('p| ') else '' for l in linhas[1:] if l.startswith('p|')]
    s=s[:i]+cab+'\ncode:\n'+'\n'.join('c| '+c for c in corpo)+'\nendcode:'+s[j+len('p| Use o código com cuidado.'):]
para_code('p| Imagine que você quer registrar as combinações')
para_code('p| Procure a classe GerenciadorEstoque no seu código')
# emojis do react-pdf quebrados no código: glifo + quebra de linha
G={'=æ':'📦','=¨':'🚨','=Í':'🛍','=Ò':'🛒','=Ë':'📋','=°':'💰','=K':'👋','=¾':'💾','=á':'🛡','=È':'🚀','=4':'🔴','=Ñ':'🗑'}
for g,e in G.items():
    s=s.replace(g+'\nc|  ',e+' ').replace(g+' ',e+' ')
s=re.sub(r'(f"(?:\\n)?)=\nc\|  ',r'\1🔄 ',s)
s=re.sub(r'(["#n] ?)L\nc\|  ',r'\1❌ ',s)
s=s.replace('\\nL Erro','\\n❌ Erro')
s=s.replace('"( ','"✨ ').replace('\\n( ','\\n✨ ')
for a,b in [('"  Estoque insuficiente','"⚠ Estoque insuficiente'),('\\n  Estoque insuficiente','\\n⚠ Estoque insuficiente'),('"  BAIXO"','"⚠ BAIXO"'),('" OK"','"✅ OK"'),
            ('"  Erro ao ler','"⚠ Erro ao ler'),('"  Alerta de compras','"⚠ Alerta de compras'),('#  CORRETO','# ✅ CORRETO'),('#  IMPORTANTE','# ⬅ IMPORTANTE'),
            ('#  Criando o objeto','# ⬅ Criando o objeto'),('Catálogo   NOVO','Catálogo  ⬅ NOVO'),('Vendas      NOVO','Vendas     ⬅ NOVO'),
            ('status   BAIXO ou 🚨 ESGOTADO','status ⚠ BAIXO ou 🚨 ESGOTADO'),('h| 📠 Como funciona o try/except','h| 🛠 Como funciona o try/except')]:
    rep(a,b,1); s=s.replace(a,b)
# junções e separações de parágrafos
rep('sem ter que caçar item por\np| item dentro','sem ter que caçar item por item dentro')
rep('Para avançar no\np| aprendizado de Python','Para avançar no aprendizado de Python')
rep('gerar relatórios. Substitua todo o código','gerar relatórios.\np| Substitua todo o código')
rep('organizar a pasta do projeto Me diz qual','organizar a pasta do projeto\np| Me diz qual')
rep('em um único arquivo. Crie uma pasta','em um único arquivo.\np| Crie uma pasta')
s=recuo('t44/x.xml',s)
open('rp44.fixed.txt','w',encoding='utf-8').write(s)
print('restos:',[l[:80] for l in s.split('\n') if re.search(r'(^|[\s"#(n])([=<>][^\s\w"\'(){}\[\].,:=<>*+-]|L$|=$)|¡|\x00|\(\s|"  [A-Z]',l)])
