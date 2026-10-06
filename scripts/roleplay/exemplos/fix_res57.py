import re,glob
from rpfix import Fix
P=glob.glob('Res*.pdf')[0]
f=Fix('res57.txt')
f.pct()
# títulos quebrados em duas linhas
f.s=re.sub(r'^(h\| .*)\nt\| (.*)$',lambda m:m.group(1)+' '+m.group(2),f.s,flags=re.M)
# tabela
i=f.s.index('t| Atendimento\nt| Tradicional /'); j=f.s.index('p| <strong>O impacto real nas vendas')
f.s=f.s[:i]+('th| Cenário | Atendimento Tradicional / Robô Antigo | Com IA Generativa Bem Configurada\n'
'tr| Dúvida de Tamanho | Cliente: "Tem essa calça no P?"<br>Robô: "Sim, temos." (Fim da interação). | Cliente: "Tem essa calça no P? Tenho medo de ficar apertada."<br>IA: "Temos sim! Ótima escolha. Essa calça tem a modelagem um pouco menor na cintura. Me diz, quanto você tem de quadril ou qual tamanho costuma usar na marca X? Posso conferir na nossa tabela para você."\n'
'tr| Indisponibilidade | Cliente: "Tem o vestido vermelho M?"<br>Robô: "Produto esgotado." | Cliente: "Tem o vestido vermelho M?"<br>IA: "Poxa, o vermelho M acabou bem rápido! Mas olha, eu tenho ele disponível no tamanho M na cor terracota, que está super em alta, ou tenho este outro modelo [Envia foto/link] que tem o caimento bem parecido. Quer dar uma olhadinha?"\n')+f.s[j:]
f.rep('li| <strong>Z-API /</strong> Evolution API: Sistemas','li| <strong>Z-API / Evolution API:</strong> Sistemas')
f.rep(' <strong>ManyChat</strong>: Muito famoso',  '\nli| <strong>ManyChat:</strong> Muito famoso')
f.rep('li| Chatbase <strong>ou</strong> Botsonic: Plataformas','li| <strong>Chatbase ou Botsonic:</strong> Plataformas')
f.rep('30 a 40 no tempo de entrega</strong> de novos\nt| %%\nli| sistemas','30% a 40% no tempo de entrega</strong> de novos sistemas')
f.rep('<strong>RD (Pesquisa e Desenvolvimento):</strong> Aceleração na descoberta de novos\nt| &\nli| materiais','<strong>R&D (Pesquisa e Desenvolvimento):</strong> Aceleração na descoberta de novos materiais')
f.rep('<strong>ManyChat Pro (IA inclusa):</strong> R$ 215,00\nt| ~\n','<strong>ManyChat Pro (IA inclusa):</strong> ~R$ 215,00\n')
f.rep('Custo Total Estimado:R$ 315,00 / mês</strong>\nt| ~\n','Custo Total Estimado: ~R$ 315,00 / mês</strong>\n')
f.rep('t| Duotach\nt| Medium ·\nt| www.omago.ai\n','')
f.rep('exclusivo da <code>[Nome da Loja]</code>.\nt| ✨\n','exclusivo da <code>[Nome da Loja]</code>. ✨\n')
f.rep('avisa o passageiro: 1. Ela identifica','avisa o passageiro:\np| 1. Ela identifica')
f.numbered()
f.code_xml(P)
f.code_from('rp57.fixed.txt')
f.rep('<strong>bagagem seja</strong>\nli| <strong>reencaminhada</strong>','<strong>bagagem seja reencaminhada</strong>')
f.rep('celular do cliente.\nli| Tudo isso','celular do cliente. Tudo isso')
f.rep('c| [Isolado]  Cliente pergunta no WhatsApp ➔ IA responde se tem estoqu\n','c| [Isolado]  Cliente pergunta no WhatsApp ➔ IA responde se tem estoque ➔ Fim do processo.\n')
f.rep('c| [Escalado] Cliente pergunta no WhatsApp ➔ IA responde se tem estoqu\n','c| [Escalado] Cliente pergunta no WhatsApp ➔ IA responde se tem estoque ➔ IA atualiza o CRM com o interesse do cliente ➔ IA gera um cupom de desconto personalizado ➔ IA avisa o marketing para criar anúncios parecidos com o produto mais buscado.\n')
f.rep('esse papo de \\funcionário','esse papo de "funcionário')
f.rep('A maioria das empresas\nli| (~71%)','A maioria das empresas (~71%)')
f.t_to_h()
f.save('res57.fixed.txt')
