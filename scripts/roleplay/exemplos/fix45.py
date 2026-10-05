s=open('rp45.e.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n, ('NÃO ACHEI',a[:70]); s=s.replace(a,b)
def rep_block(first,last,new):
    global s
    i=s.index(first); j=s.index(last,i); j=s.index('\n',j); s=s[:i]+new+s[j:]
rep('primeira pedra! = Não','primeira pedra! 😅 Não')
rep('li| =Ì Exemplo mental','li| 📌 Exemplo mental',2)
rep('h| List Comprehension: Desvendando','h| 🧙‍♂️ List Comprehension: Desvendando')
rep('h| Qual escolher? Uma comparação rápida','h| ⚖ Qual escolher? Uma comparação rápida')
rep_block('p| FerramentaQuando usar?','p| confuso. Legibilidade vem sempre primeiro!',
 'th| Ferramenta | Quando usar? | Evite quando...\n'
 'tr| **for tradicional** | Para repetir ações um número fixo de vezes ou varrer listas. | A repetição depender de uma condição externa imprevisível.\n'
 'tr| **while** | Quando o encerramento depende de uma condição (ex: entrada do usuário). | Você já sabe o número exato de repetições (evita loops infinitos).\n'
 'tr| **List Comprehension** | Para transformar ou filtrar uma lista antiga em uma nova lista curta. | O código ficar muito longo ou confuso. Legibilidade vem sempre primeiro!')
for t in ['o for? >','Como eu consigo medir isso? >','juntas? =','tá bom? =','pode ser? =','combinado? =']:
    rep(t,t[:-2])
rep('sem nós na cabeça. >à(','sem nós na cabeça. 🧠✨')
rep('contador += 1  # =¨\nc|  CRUCIAL','contador += 1  # 🚨 CRUCIAL')
rep('break  # =Ñ\nc|  O break','break  # 🛑 O break')
rep('p| L NÃO use','p| ❌ NÃO use')
rep_block('li| Cenário 1: Mostrar nomes na tela (Apenas ação)python','p| Use o código com cuidado.',
 'li| Cenário 1: Mostrar nomes na tela (Apenas ação)\ncode:\n'
 'c| # 🟢 CORRETO (for tradicional):\nc| for nome in ["Ana", "Bia"]:\nc|     print(f"Olá, {nome}!")\n'
 'c| # 🔴 ERRADO (List comprehension usada só para gerar efeito colateral):\nc| [print(f"Olá, {nome}!") for nome in ["Ana", "Bia"]] # Não faça isso!\nendcode:')
rep_block('li| Cenário 2: Criar uma lista de e-mails válidos (Filtragem e criação)python','p| Use o código com cuidado.',
 'li| Cenário 2: Criar uma lista de e-mails válidos (Filtragem e criação)\ncode:\n'
 'c| # 🟢 PERFEITO para List Comprehension (Curto, direto e cria uma lista):\nc| emails_validos = [e for e in lista_emails if "@" in e]\nendcode:')
rep('print("L\nc|  Senha incorreta! Tente novamente.")','print("❌ Senha incorreta! Tente novamente.")')
rep('# =¨\nc|  O PASSO MAIS IMPORTANTE','# 🚨 O PASSO MAIS IMPORTANTE')
rep('print("=\nc|  Acesso concedido! Bem-vinda','print("🔓 Acesso concedido! Bem-vinda')
rep('print("=\nc|  Acesso concedido!")','print("🔓 Acesso concedido!")')
rep('print("L\nc|  Senha incorreta.")','print("❌ Senha incorreta.")')
rep('print("=\nc|  Conta bloqueada','print("🔒 Conta bloqueada')
rep('teste o primeiro exemplo digitando algumas\np| senhas erradas','teste o primeiro exemplo digitando algumas senhas erradas')
rep('na cabeça. =€ Essa sua regra','na cabeça. 🚀\np| Essa sua regra')
for a,b in [('🐴 O erro clássico','🔴 O erro clássico'),('📢 O jeito correto','🟢 O jeito correto'),('🐢 Usando range()','🔢 Usando range()'),('🃷 Usando enumerate()','🏷 Usando enumerate()'),
            ('🐴 O jeito demorado','🔴 O jeito demorado'),('📢 O jeito Pythônico','🟢 O jeito Pythônico')]:
    rep(a,b,1); s=s.replace(a,b)
rep('h| Bônus: List Comprehension','h| 🧙‍♂️ Bônus: List Comprehension')
rep('p| 3. As "Primas" da List Comprehension <-','p| 3. As "Primas" da List Comprehension 🎭')
rep('h| Dict Comprehension','h| 🔑 Dict Comprehension')
rep_block('o valor é o preço zerado: python','p| Use o código com cuidado.',
 'o valor é o preço zerado:\ncode:\nc| produtos = ["mouse", "teclado", "monitor"]\nc| # Usa chaves { } e define chave: valor (p: 0)\nc| estoque_inicial = {p: 0 for p in produtos}\n'
 "c| print(estoque_inicial)  # Saída: {'mouse': 0, 'teclado': 0, 'monitor': 0}\nendcode:")
rep_block('sem a estrutura de par chave-valor: python','p| Use o código com cuidado.',
 'sem a estrutura de par chave-valor:\ncode:\nc| emails_com_duplicadas = ["ana@email.com", "bia@email.com", "ana@email.com"]\nc| # Cria um conjunto que elimina e-mails repetidos na hora\n'
 "c| emails_unicos = {email for email in emails_com_duplicadas}\nc| print(emails_unicos)  # Saída: {'ana@email.com', 'bia@email.com'}\nendcode:")
rep('p| 3. Escrever um código que filtra uma lista de notas de alunos usando for e depois transformá-lo em list comprehension. Qual desses',
    'p| 3. Escrever um código que filtra uma lista de notas de alunos usando for e depois transformá-lo em list comprehension.\np| Qual desses')
open('rp45.fixed.txt','w',encoding='utf-8').write(s)
import re
sus=[l for l in s.split('\n') if re.search(r'(^|\s)[=<>][^\s\w"\'(){}\[\].,:=<>-]|\s=$|^c\|\s{1,2}\S.*\)$',l) and not l.startswith('c|     ')]
print('suspeitos:'); [print('  ',l[:100]) for l in sus]
