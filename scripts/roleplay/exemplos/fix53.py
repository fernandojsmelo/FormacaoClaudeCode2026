import re, html
from fences import recuo
s=open('rp53.e.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
# 1) linhas de prompt quebradas pela largura da página: no XML elas chegam à margem (largura >= 740)
x=open('t53/x.xml',encoding='utf-8').read()
larg={}
for m in re.finditer(r'<text top="\d+" left="\d+" width="(\d+)"[^>]*>(.*?)</text>',x):
    t=html.unescape(re.sub('<[^>]+>','',m.group(2))).strip()
    larg[t]=max(larg.get(t,0),int(m.group(1)))
out=[]; dentro=False; juntar=False
for l in s.split('\n'):
    if l=='code:': dentro=True
    elif l=='endcode:': dentro=False
    prox=l[3:].strip()
    if dentro and l.startswith('c| ') and juntar and not re.match(r'(\d+\. |[-*#] |---|Passo |Dados|Pedido|Resposta|Anotações)', prox) \
       and (not (re.search(r'[.:]$', out[-1]) and re.match(r'[A-ZÁÉÍÓÚÂÊÔÀ]', prox)) or prox.startswith('Siga RIGOROSAMENTE')):
        out[-1]+=' '+l[3:].strip(); juntar=larg.get(l[3:].strip(),0)>=740; continue
    out.append(l)
    juntar = dentro and l.startswith('c| ') and larg.get(l[3:].strip(),0)>=740
s='\n'.join(out)
# 2) emojis (fonte: resumo 53); 📈 vira 🚀 (renderiza quebrado neste ambiente)
rep('[=¨ CRÍTICO]','[🚨 CRÍTICO]',2); rep('[( POSITIVO]','[✨ POSITIVO]',2)
E={'=Å':'📅','=e':'👥','=¡':'💡','=€':'🚀','>à':'🧠','=Ë':'📋','=È':'🚀','=°':'💰','<æ':'🏦','=à':'🛠','<':'🌐'}
def emo(m): return m.group(1)+E[m.group(2)]+' '
s=re.sub(r'^(c\| (?:\* )?)(=Å|=e|=¡|=€|>à|=Ë|=È|=°|<æ|=à|<)\nc\|  ', emo, s, flags=re.M)
rep('* Status: [  PARCIALMENTE APROVADO]','* Status: [⚠ PARCIALMENTE APROVADO]')
rep('* Meta Atingida:  SIM','* Meta Atingida: ✅ SIM')
rep('(=à, =È, <æ)','(🛠, 🚀, 🏦)')
rep('Na seção =° PROPOSTA','Na seção 💰 PROPOSTA'); rep('custo de gente (=e)','custo de gente (👥)'); rep('infraestrutura (<).','infraestrutura (🌐).')
rep('Bom trabalho! =€','Bom trabalho! 🚀'); rep('Obrigado por tudo! =€','Obrigado por tudo! 🚀')
# 3) tabela
i=s.index('p| TécnicaO que ela resolve?'); j=s.index('\n',s.index('p| Chain-of-ThoughtErros'))
s=s[:i]+('th| Técnica | O que ela resolve? | Como você aplica?\n'
 'tr| **Few-Shot** | Formato bagunçado e falta de padrão. | Colando 2 ou 3 exemplos de "Pergunta/Resposta" ideais no prompt.\n'
 'tr| **Chain-of-Thought** | Erros de lógica, matemática e pressa da IA. | Escrevendo "Pense passo a passo" ou criando um exemplo onde a IA resolve o problema em etapas.')+s[j:]
s=recuo('t53/x.xml',s)
open('rp53.fixed.txt','w',encoding='utf-8').write(s)
print('restos:',[l[:90] for l in s.split('\n') if re.search(r'(^|[\s"#(\[*])([=<>][^\s\w"\'(){}\[\].,:=<>*+|/-]|L$|=$|<$)|¡|\x00|Esta transcrição',l)])
