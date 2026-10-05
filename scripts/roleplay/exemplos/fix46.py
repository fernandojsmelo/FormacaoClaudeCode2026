from fences import fences
s=open('rp46.e.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n, ('NÃO ACHEI',a[:70]); s=s.replace(a,b)
def rep_block(first,last,new):
    global s
    i=s.index(first); j=s.index(last,i); j=s.index('\n',j); s=s[:i]+new+s[j:]
s=fences('t46/x.xml',s)
# blocos que viraram parágrafo (rótulo "python" grudado no fim da frase)
def para_code(intro, ultimo):
    global s
    i=s.index(intro); j=s.index('p| Use o código com cuidado.',i)
    linhas=s[i:j].split('\n'); cab=linhas[0].replace(' python','').rstrip()
    corpo=[l[3:] for l in linhas[1:] if l.startswith('p| ')]
    s=s[:i]+cab+'\ncode:\n'+'\n'.join('c| '+c for c in corpo)+'\nendcode:'+s[j+len('p| Use o código com cuidado.'):]
para_code('p| Use *args para receber uma lista','')
para_code('p| A sintaxe é sempre lambda entrada','')
para_code('p| É aí que entra o lambda.','')
rep('c| <µ\nc|  *Trilha sonora de batalha começou a tocar!* <µ\nc| ” Aragorn desferiu um golpe crítico no Dragão!\nc| <µ\nc|  *A música diminui o tom...* <µ',
    'c| 🎵 *Trilha sonora de batalha começou a tocar!* 🎵\nc| ⚔ Aragorn desferiu um golpe crítico no Dragão!\nc| 🎵 *A música diminui o tom...* 🎵')
# glifos de emoji do react-pdf dentro do código e do texto
G=[('=¥\nc|  ','💥 '),('=¥\nc| ','💥 '),('<’\nc|  ','🎒 '),('<’\nc| ','🎒 '),('=A\nc|  ','👁 '),('=A\nc| ','👁 '),('=%\nc|  ','🔥 '),('=%\nc| ','🔥 '),
   ('<µ\nc|  ','🎵 '),('<µ\nc| ")','🎵")'),('<µ\nc| ','🎵 '),('>ê\nc|  ','🧪 '),('<µ','🎵'),('=¥','💥'),('”','⚔')]
for a,b in G: s=s.replace(a,b)
rep('muito rápido! =€','muito rápido! 🚀')
rep('Desmistificando a Recursividade =','Desmistificando a Recursividade 🔄')
rep('absolutamente tudo! <Æ','absolutamente tudo! 🏆')
rep("['Maçã', 'Banana'] =.","['Maçã', 'Banana'] 😮")
rep("['Maçã', 'Banana', 'Ovo'] >/","['Maçã', 'Banana', 'Ovo'] 🤯")
rep('h| 🢄 Usando o @','h| 🪄 Usando o @')
rep('Use o código com cuidado.\np| 1. Recursividade','Use o código com cuidado.\np| 3. Recursividade') if False else None
rep('igual a 0? 3. Como você chamaria','igual a 0?\np| 3. Como você chamaria')
rep('usando **kwargs também! O que achou desse formato?','usando **kwargs também!\np| O que achou desse formato?')
from fences import recuo
s=recuo('t46/x.xml',s)
open('rp46.fixed.txt','w',encoding='utf-8').write(s)
import re
print('restos:',[l[:90] for l in s.split('\n') if re.search(r'[=<>][^\x00-\x7f]|=€|<’|”|=\.|>/|<µ',l)])
