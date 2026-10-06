import re
from fences import recuo
s=open('rp51.e.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
# rodapé/cabeçalho de página vazado no bloco de código
s=re.sub(r'\nc\| Esta transcrição inclui conteúdo gerado por IA[^\n]*\nc\| \d+/\d+\nc\| Formação Claude Code 2026: IA com Claude e Cowork\nc\| O Especialista em Python e a Programadora que "Apagou os\nc\| Próprios Dados"','',s)
rep('# L\nc|  ERRO','# ❌ ERRO',3); s=s.replace('# L\nc|  ERRO','# ❌ ERRO')
rep('# =\nc|  Verifica','# 🔍 Verifica',2); s=s.replace('# =\nc|  Verifica','# 🔍 Verifica')
rep('# =\nc|  Se a pasta','# 🔍 Se a pasta')
rep('print("\\n=¨\nc|  ATENÇÃO','print("\\n🚨 ATENÇÃO')
rep('# =Â\nc|  LEITURA','# 📂 LEITURA')
rep('#  ESCRITA PRECISA','# ✍ ESCRITA PRECISA')
def para_code(intro):
    global s
    i=s.index(intro); j=s.index('p| Use o código com cuidado.',i)
    linhas=s[i:j].split('\n'); cab=re.sub(r' python$','',linhas[0].rstrip())
    corpo=[l[3:] if l.startswith('p| ') else '' for l in linhas[1:] if l.startswith('p|')]
    s=s[:i]+cab+'\ncode:\n'+'\n'.join('c| '+c for c in corpo)+'\nendcode:'+s[j+len('p| Use o código com cuidado.'):]
para_code('p| Às vezes, mesmo verificando se o arquivo existe')
para_code('p| Dá para ser ainda mais inteligente!')
i=s.index('p| ModoNomeO que faz'); j=s.index('\n',s.index("p| 'x'Exclusive (Criar)"))
s=s[:i]+("th| Modo | Nome | O que faz se o arquivo JÁ EXISTE? | O que faz se o arquivo NÃO EXISTE?\n"
 "tr| **'r'** | Read (Leitura) | Abre para leitura a partir do início. | 🚨 Dá erro (FileNotFoundError).\n"
 "tr| **'w'** | Write (Escrita) | 💥 Zera tudo! Apaga o conteúdo e escreve do zero. | Cria um arquivo novinho.\n"
 "tr| **'a'** | Append (Anexar) | Preserva tudo e cola o cursor no final para adicionar. | Cria um arquivo novinho.\n"
 "tr| **'x'** | Exclusive (Criar) | 🚨 Dá erro (Protege o arquivo antigo!). | Cria um arquivo novinho.")+s[j:]
rep('(De um site, de outro sistema, ou você está digitando na hora?) Com isso','(De um site, de outro sistema, ou você está digitando na hora?)\np| Com isso')
s=recuo('t51/x.xml',s)
open('rp51.fixed.txt','w',encoding='utf-8').write(s)
print('restos:',[l[:80] for l in s.split('\n') if re.search(r'(^|[\s"#(])([=<>][^\s\w"\'(){}\[\].,:=<>*+-]|L$|=$)|¡|\x00|Esta transcrição',l)])
