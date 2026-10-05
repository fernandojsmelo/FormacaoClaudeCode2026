import re
exec(open('code43.py').read().split("if __name__")[0])
from links43 import LINKS
s=open('res43.txt',encoding='utf-8').read().split('\n#cards')[0]
# 1) código: texto completo da transcrição, linhas em branco do resumo
L=s.split('\n'); out=[]; i=0; nb=0
while i<len(L):
    if L[i].startswith('c|'):
        j=i
        while j<len(L) and L[j].startswith('c|'): j+=1
        tb=[x for x in TB[nb][2] if x.strip()]; k=0; blk=[]
        for x in L[i:j]:
            if x[2:].strip()=='' : blk.append('c| ')
            else: blk.append('c| '+tb[k]); k+=1
        assert k==len(tb),(i,k,len(tb))
        if out and out[-1] in ('t| python','t| bash','t| text'): out.pop()
        out+=['code:']+blk+['endcode:']; nb+=1; i=j; continue
    out.append(L[i]); i+=1
s='\n'.join(out)
def rep(a,b):
    global s
    assert a in s, a[:70]; s=s.replace(a,b)
def rep_block(first,last,new):
    global s
    i=s.index(first); j=s.index(last,i); j=s.index('\n',j)
    s=s[:i]+new+s[j:]
rep('t| Depois (f-string):','li| <strong>Depois (f-string):</strong>')
rep_block('t| O que você quer\n','t| termina com algo',
 'th| O que você quer fazer? | Método ideal | Exemplo prático\n'
 'tr| <strong>Limpar espaços inúteis</strong> nas pontas (comum em planilhas) | <code>.strip()</code> | <code>" joao@email.com ".strip()</code><br>↳ <code>"joao@email.com"</code>\n'
 'tr| <strong>Dividir um texto</strong> em uma lista de pedaços | <code>.split()</code> | <code>"Ana,Maria,Pedro".split(",")</code><br>↳ <code>[\'Ana\', \'Maria\', \'Pedro\']</code>\n'
 'tr| <strong>Juntar uma lista</strong> de textos usando um separador | <code>.join()</code> | <code>"-".join([\'2026\', \'10\', \'05\'])</code><br>↳ <code>"2026-10-05"</code>\n'
 'tr| <strong>Trocar uma palavra/caractere</strong> por outro | <code>.replace()</code> | <code>"R$ 1.500,00".replace(".", "")</code><br>↳ <code>"R$ 1500,00"</code>\n'
 'tr| Saber se o texto <strong>começa ou termina</strong> com algo | <code>.startswith()</code><br><code>.endswith()</code> | <code>"relatorio_final.pdf".endswith(".pdf")</code><br>↳ <code>True</code>')
rep('<code>" MArIa sILVA</code> <code>"</code>','<code>" MArIa sILVA "</code>')
rep('\\guia prático"','"guia prático"'); rep('\\da"','"da"')
rep('f- strings','f-strings'); rep('e- mails','e-mails'); rep('pop- up','pop-up'); rep('sexta- feira','sexta-feira')
rep('<strong>Proteção contra erros (</strong> <code>pd.isna</code>','<strong>Proteção contra erros (</strong><code>pd.isna</code>')
rep('<strong>O poder do</strong> <code>.apply()</code>','<strong>O poder do</strong> <code>.apply()</code>')
rep('100 pronto para rodar, me conta:\nt| %','100% pronto para rodar, me conta:')
rep('100 pronta para rodar no seu computador, me\nt| %\np| conta:','100% pronta para rodar no seu computador, me conta:')
rep('100 pronto e automatizado! Se você\nt| %\np| quiser','100% pronto e automatizado! Se você quiser')
rep_block('t| Nota: Adicionamos','t| puro.','p| <em>Nota: Adicionamos o <code>.astype(str)</code> antes para garantir que o Pandas trate a coluna como texto, evitando erros caso algum CPF tenha vindo como número puro.</em>')
rep('<code>012345...</code>) ou eles podem sumir?','<code>012345...</code>) ou eles podem sumir?')
rep('<strong>hifens, barras e anos com 2 ou 4 dígitos</strong>? Além disso,','<strong>hifens, barras e anos com 2 ou 4 dígitos</strong>?\nli| Além disso,')
rep('direto na exibição.','direto na exibição.')
rep('textos livres). Como formatar','textos livres).\nli| Como formatar')
rep('h| 🪟 Se você usa Windows: Agendador de Tarefas (Task\nt| Scheduler)','h| 🪟 Se você usa Windows: Agendador de Tarefas (Task Scheduler)')
rep('próxima rodada! 🚀\nt| 🤖','próxima rodada! 🚀🤖')
rep('li| Operações básicas + a regra que muda tudo (imutabilidade):\nq| O conceito','q| Operações básicas + a regra que muda tudo (imutabilidade): O conceito')
rep('q| Construir texto do jeito moderno (f-strings) cuidados: Para\nt| +\nq| montar','q| Construir texto do jeito moderno (f-strings) + cuidados: Para montar')
# lista de links (3 seções)
partes=s.split('p| Confira os principais resultados da Web para saber mais sobre esse tema:\n')
assert len(partes)==4
novo=partes[0]
for n in range(3):
    resto=partes[n+1].split('\n'); k=0
    while k<len(resto) and resto[k].startswith('t| '): k+=1
    novo+='p| Confira os principais resultados da Web para saber mais sobre esse tema:\n'
    novo+='\n'.join(f'li| {t} · <em>{f}</em>' for t,f in LINKS[n])+'\n'+'\n'.join(resto[k:])
s=novo
# itens numerados
L=s.split('\n'); out=[]; i=0; crontab=False
while i<len(L):
    l=L[i]
    if l.startswith('h| 🍏'): crontab=True
    if l.startswith('h| 💡'): crontab=False
    m=re.match(r'p\| \d\. ',l)
    if m:
        if i+1<len(L) and L[i+1].startswith('li| ') and re.match(r'li\| ([a-zà-ú"]|um editor)',L[i+1]):
            l+=' '+L[i+1][4:]; i+=1
        if not crontab: l='n| '+l[3:]
    elif l.startswith('li| ') and out and out[-1].startswith('n| 6. <strong>Configurar o Python'):
        pass
    out.append(l); i+=1
s='\n'.join(out)
# subitens do passo 6 (Windows)
s=re.sub(r'(n\| 6\. <strong>Configurar o Python:</strong>)\n((?:li\| .*\n)+)', lambda m: m.group(1)+'\n'+m.group(2).replace('li| ','subli| '), s)
s='\n'.join('h| '+l[3:] if l.startswith('t| ') else l for l in s.split('\n'))
open('res43.fixed.txt','w',encoding='utf-8').write(s)
print(s.count('\nq|')+1,'perguntas')
