s = open("rp43.c.txt", encoding="utf-8").read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70])
    s = s.replace(a, b)
# código que ficou fora dos blocos (rótulo grudado no texto)
rep('h| O jeito que não funciona:python\np| nome = "carlos"\np| nome.upper()  # O Python cria "CARLOS", mas ninguém guarda\np| print(nome)  # Continua mostrando "carlos"\np| Use o código com cuidado.',
    'li| ❌ O jeito que não funciona:\ncode:\nc| nome = "carlos"\nc| nome.upper()  # O Python cria "CARLOS", mas ninguém guarda\nc| print(nome)  # Continua mostrando "carlos"\nendcode:')
rep('h| Antes (Frankenstein):python\np| mensagem = "Olá, " + nome + "! Seu saldo no plano " + plano + " é de R$ " + str(saldo) + "."\np| Use o código com cuidado.',
    'li| ❌ Antes (Frankenstein):\ncode:\nc| mensagem = "Olá, " + nome + "! Seu saldo no plano " + plano + " é de R$ " + str(saldo) + "."\nendcode:')
rep('p| 2. Digite o comando para editar os seus agendamentos:bash\np| crontab -e\np| Use o código com cuidado.',
    'p| 2. Digite o comando para editar os seus agendamentos:\ncode:\nc| crontab -e\nendcode:')
rep('aperte Ctrl+O para salvar e Ctrl+X para sair):text\np| 0 17 * * 5 /usr/bin/python3 /Users/seu_usuario/projeto/meu_script.py\np| Use o código com cuidado.',
    'aperte Ctrl+O para salvar e Ctrl+X para sair):\ncode:\nc| 0 17 * * 5 /usr/bin/python3 /Users/seu_usuario/projeto/meu_script.py\nendcode:')
# tabela de métodos
rep('''p| O que você quer fazer?Método idealExemplo prático
p| Limpar espaços inúteis nas pontas (comum em planilhas).strip()"  joao@email.com  ".strip()
p| ³ "joao@email.com"
p| Dividir um texto em uma lista de pedaços.split()"Ana,Maria,Pedro".split(",")
p| ³ ['Ana', 'Maria', 'Pedro']
p| Juntar uma lista de textos usando um separador.join()"-".join(['2026', '10', '05'])
p| ³ "2026-10-05"
p| Trocar uma palavra/caractere por outro.replace()"R$ 1.500,00".replace(".", "")
p| ³ "R$ 1500,00"
p| Saber se o texto começa ou termina com algo.startswith()
p| .endswith()"relatorio_final.pdf".endswith(".pdf")
p| ³ True''',
'''th| O que você quer fazer? | Método ideal | Exemplo prático
tr| Limpar espaços inúteis nas pontas (comum em planilhas) | .strip() | "  joao@email.com  ".strip() ↳ "joao@email.com"
tr| Dividir um texto em uma lista de pedaços | .split() | "Ana,Maria,Pedro".split(",") ↳ ['Ana', 'Maria', 'Pedro']
tr| Juntar uma lista de textos usando um separador | .join() | "-".join(['2026', '10', '05']) ↳ "2026-10-05"
tr| Trocar uma palavra/caractere por outro | .replace() | "R$ 1.500,00".replace(".", "") ↳ "R$ 1500,00"
tr| Saber se o texto começa ou termina com algo | .startswith() .endswith() | "relatorio_final.pdf".endswith(".pdf") ↳ True''')
# emojis que o react-pdf grava em dois pedaços (alta/baixa de surrogate)
rep("Use f-strings >„", "Use f-strings 🪄")
rep("Combinando tudo na prática =€", "Combinando tudo na prática 🚀")
rep("Pronto para o Trabalho =€", "Pronto para o Trabalho 🚀")
rep('sucesso! <‰\nc| ")', 'sucesso! 🎉")')
rep('print("=%\nc|  Sucesso total!', 'print("🔥 Sucesso total!', 2)
rep('na pasta! L\nc| ")', 'na pasta! ❌")')
rep('{pasta_downloads} L\nc| ")', '{pasta_downloads} ❌")')
rep('print(f"=Á\nc|  Arquivo', 'print(f"📁 Arquivo', 2)
rep('print(f"<‰\nc|  Arquivo salvo', 'print(f"🎉 Arquivo salvo')
rep('print(f"=%\nc|  Sucesso! Arquivo limpo', 'print(f"🔥 Sucesso! Arquivo limpo')
rep("h| Se você usa Windows:", "h| 🪟 Se você usa Windows:")
rep("p| <O Se você usa Mac ou =' Linux: O poderoso Crontab", "h| 🍏 Se você usa Mac ou 🐧 Linux: O poderoso Crontab")
# itens grudados e hifenização de quebra de linha
rep("(ex: 17:00). 5. Ação: Escolha Iniciar um programa.", "(ex: 17:00).\np| 5. Ação: Escolha Iniciar um programa.")
rep("C:\\Users\\Seu- Usuario\\Projetos", "C:\\Users\\SeuUsuario\\Projetos")
open("rp43.fixed.txt", "w", encoding="utf-8").write(s)
restos = [c for c in "€„‰³Á" if c in s] + [l for l in s.split("\n") if l.strip() in ("c| L", "c| \")")]
print("ok; restos:", restos)
