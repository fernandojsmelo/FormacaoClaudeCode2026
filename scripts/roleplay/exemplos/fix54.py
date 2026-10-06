import re
from fences import recuo
s=open('rp54.e.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
rep('Resposta da IA:Frase corrigida','Resposta da IA: Frase corrigida')
rep('p| Muito sucesso nos seus testes e até a próxima!','p| Muito sucesso nos seus testes e até a próxima! 🚀🎓')
# o template final veio quebrado pela largura da página: junta as continuações
i=s.index('code:\nc| Você é um assistente'); j=s.index('endcode:',i)
linhas=s[i:j].split('\n')[1:-1]; out=[]
for l in linhas:
    t=l[3:]
    if out and not re.match(r'(Frase |Explicação:|Você é)',t): out[-1]+=' '+t
    else: out.append(t)
s=s[:i]+'code:\n'+'\n'.join('c| '+t for t in out)+'\n'+s[j:]
s=recuo('t54/x.xml',s)
open('rp54.fixed.txt','w',encoding='utf-8').write(s)
print('restos:',[l[:80] for l in s.split('\n') if re.search(r'(^|[\s"#(])([=<>][^\s\w"\'(){}\[\].,:=<>*+|-]|L$|=$)|¡|\x00|Esta transcrição',l)])
