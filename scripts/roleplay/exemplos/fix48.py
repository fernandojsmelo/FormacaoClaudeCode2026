import re
from fences import fences, recuo
s=open('rp48.e.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
def tabela(primeira, ultima, novo):
    global s
    i=s.index(primeira); j=s.index('\n',s.index(ultima,i)); s=s[:i]+novo+s[j:]
s=fences('t48/x.xml',s)
rep('h| O que é o yield?','h| ⚙ O que é o yield?')
rep('p| Com yield (Vira um Gerador ()','p| Com yield (Vira um Gerador ✨)')
rep('h| O Segredo: O Frame de Execução','h| 🕵️‍♂️ O Segredo: O Frame de Execução')
rep('h| 🐬 Vendo a "Magia"','h| 🔬 Vendo a "Magia"')
rep('p| L A Abordagem Errada','p| ❌ A Abordagem Errada')
rep('GRANDES! =¨','GRANDES! 🚨')
rep('(O jeito com Gerador >à)','(O jeito com Gerador 🧠)')
rep('# O JEITO CERTO E LEVE (','# O JEITO CERTO E LEVE ✨')
rep('print("=¨\nc|  Investigando','print("🚨 Investigando')
rep('c| =¨\nc|  Investigando','c| 🚨 Investigando')
rep('Boa sorte! =»(','Boa sorte! 💻✨')
rep('destravou esse conceito! >à(','destravou esse conceito! 🧠✨')
rep('A MÁGICA ENTRA AQUI! >•','A MÁGICA ENTRA AQUI! 🪐')
rep('Parabéns! >s(','Parabéns! 🥳✨')
rep('estou por aqui! = Como você fixou','estou por aqui! 😊\np| Como você fixou')
rep('h| 🀭 As Duas Formas','h| 🎭 As Duas Formas')
rep('# L\nc|  Forma pesada','# ❌ Forma pesada')
rep('# ( Forma leve','# ✨ Forma leve')
rep('p| ó 1. Os dados são de "uso único"','h| ⏳ 1. Os dados são de "uso único"')
rep('até logo! =€=(','até logo! 🚀🐍✨')
rep('bons códigos pra você também! =','bons códigos pra você também!')
tabela('p| ConceitoO que significa?','p| GeradorUm tipo especial',
 'th| Conceito | O que significa? | Exemplo no Python\n'
 'tr| **Iterável** | Qualquer coisa que você consegue colocar dentro de um for. | Listas, Strings, Dicionários, Tuplas.\n'
 'tr| **Iterador** | O "ponteiro" por trás dos panos que sabe qual é o próximo item (usando a função next()). | O objeto que o for cria para ler a lista.\n'
 'tr| **Gerador** | Um tipo especial de iterador que fabrica os dados sob demanda em vez de guardá-los prontos. | Funções com yield ou expressões geradoras.')
tabela('p| RecursoLista []Gerador ()','p| Permite OrdenaçãoSim',
 'th| Recurso | Lista [] | Gerador ()\n'
 'tr| **Consumo de Memória** | Alto (guarda tudo de uma vez) | Mínimo (um por vez)\n'
 'tr| **Reutilização** | Sim (quantas vezes quiser) | Não (acabou, sumiu)\n'
 'tr| **Acesso por Índice ([0])** | Sim | Não\n'
 'tr| **Saber o tamanho (len())** | Sim | Não\n'
 'tr| **Permite Ordenação** | Sim (muito fácil) | Não diretamente')
rep('c|         if valor >= limite:\nc|             pass  # Tô deixando','c|         if valor >= limite:\nc|             # Aqui eu acho que deveria entrar o yield, mas não sei se tá certo...\nc|             pass  # Tô deixando')
s=recuo('t48/x.xml',s)
open('rp48.fixed.txt','w',encoding='utf-8').write(s)
print('restos:',[l[:80] for l in s.split('\n') if re.search(r'(^|[\s"#(])([=<>][^\s\w"\'(){}\[\].,:=<>*+-]|L$|=$)|¡|\x00',l)])
