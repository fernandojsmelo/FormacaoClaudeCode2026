import re
from fences import recuo
s=open('rp49.e.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
# emojis dos comentários de código (fonte: resumo 49)
rep('# L\nc|  Como você faz hoje','# ❌ Como você faz hoje',2)
rep('# =¡\nc|  Com map e lambda','# 💡 Com map e lambda')
rep('# =¡\nc|  Com filter e lambda','# 💡 Com filter e lambda')
rep('# =\nc|  O jeito mais recomendado','# 🐍 O jeito mais recomendado',2)
rep('# =¡\nc|  Com map: Você passa','# 💡 Com map: Você passa')
rep('# =\nc|  Com list comprehension','# 🐍 Com list comprehension')
rep('# =¨\nc|  A List Comprehension processa','# 🚨 A List Comprehension processa')
rep('# ¡ O map faz isso','# ⚡ O map faz isso')
rep('# =¡\nc|  O map puxa','# 💡 O map puxa')
rep('# =\nc|  Na compreensão de lista','# 🐍 Na compreensão de lista')
rep('# =¡\nc|  A estrutura lê-se','# 💡 A estrutura lê-se')
rep('# <¯\nc|  A MAGIA DO FILTRO','# 🎯 A MAGIA DO FILTRO')
rep('# <¯\nc|  A MAGIA DA EXPORTAÇÃO','# 🎯 A MAGIA DA EXPORTAÇÃO')
rep('li| =Ë Objetivo','li| 📋 Objetivo',2)
rep('li| =» A diferença','li| 💻 A diferença')
rep('junto! =€','junto! 🚀'); rep('Boa sorte no desafio! =€','Boa sorte no desafio! 🚀')
rep('p| L O jeito nativo','h| ❌ O jeito nativo')
rep('p| O detalhe mais importante','h| ⚠ O detalhe mais importante')
rep('p| amos nessa!','p| Vamos nessa!')
# "!=" e "/ else" confundidos com título
rep("if venda\nh| 'NULO']. Ficou certo?","if venda != 'NULO']. Ficou certo?")
rep('fazer um if\nh| else dentro da List Comprehension (por exemplo, para transformar o "NULO" em 0 em vez de deletar ele), ou prefere\np| fechar',
    'fazer um if / else dentro da List Comprehension (por exemplo, para transformar o "NULO" em 0 em vez de deletar ele), ou prefere fechar')
rep('o seu VS Code. Para eu preparar o próximo passo ideal, me conta:','o seu VS Code.\np| Para eu preparar o próximo passo ideal, me conta:')
# tabela
i=s.index('p| MétodoQuando usar?'); j=s.index('\n',s.index('p| filter()When'))
s=s[:i]+('th| Método | Quando usar? | O que ele faz?\n'
 'tr| **map()** | Quando precisa modificar todos os itens (ex: converter moedas, formatar strings). | Aplica uma função em cada elemento.\n'
 'tr| **filter()** | Quando você precisa reduzir a lista (ex: remover nulos, filtrar idades > 18). | Testa cada elemento usando uma condição.\n'
 'tr| **List Comprehension** | Quase sempre. É o padrão mais amado pela comunidade Python. | Faz o papel do map e do filter de forma ainda mais legível.')+s[j:]
def para_code(intro,tirar=None):
    global s
    i=s.index(intro); j=s.index('p| Use o código com cuidado.',i)
    linhas=s[i:j].split('\n'); cab=re.sub(r' python$','',linhas[0].rstrip())
    corpo=[l[3:] if l.startswith('p| ') else '' for l in linhas[1:] if l.startswith('p|')]
    if tirar and corpo and corpo[0]==tirar: corpo=corpo[1:]
    s=s[:i]+cab+'\ncode:\n'+'\n'.join('c| '+c for c in corpo)+'\nendcode:'+s[j+len('p| Use o código com cuidado.'):]
para_code('p| Você precisa abrir o arquivo, pular o cabeçalho')
for intro in ['p| O arquivo está assim por dentro:','p| Assim que você executar esse script',
              'p| Imagine que você recebeu um arquivo chamado frotas.csv','p| Se o seu código estiver correto, o arquivo final']:
    para_code(intro,'csv')
s=recuo('t49/x.xml',s)
open('rp49.fixed.txt','w',encoding='utf-8').write(s)
print('restos:',[l[:80] for l in s.split('\n') if re.search(r'(^|[\s"#(])([=<>][^\s\w"\'(){}\[\].,:=<>*+-]|L$|=$)|¡|\x00|Esta transcrição|^p\| csv$',l)])
