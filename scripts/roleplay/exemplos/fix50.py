s=open('rp50.e.txt',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
rep('h| 🣩 1. enumerate()','h| 🧩 1. enumerate()')
rep('h| 2. zip()','h| 🤐 2. zip()')
rep('p| 3. Alerta de Perigo: O Truncamento Silencioso','p| 3. Alerta de Perigo: O Truncamento Silencioso ⚠')
i=s.index('p| FunçãoO que ela resolve?'); j=s.index('\n',s.index('p| zip(lista1, lista2)Evita'))
s=s[:i]+('th| Função | O que ela resolve? | O que você recebe no for?\n'
 'tr| **enumerate(lista)** | Evita que você use range(len()) para pegar o índice. | índice, item\n'
 'tr| **zip(lista1, lista2)** | Evita que você use lista1[i] e lista2[i] para cruzar dados. | item1, item2')+s[j:]
rep('enumerate(a). Deixe a preguiça do Python trabalhar a favor da sua memória RAM. 2. Para inspecionar','enumerate(a). Deixe a preguiça do Python trabalhar a favor da sua memória RAM.\np| 2. Para inspecionar')
open('rp50.fixed.txt','w',encoding='utf-8').write(s)
