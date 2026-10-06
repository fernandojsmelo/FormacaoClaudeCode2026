import re
from rpfix import Fix
P='ResumoRolePlay58.pdf' if False else __import__('glob').glob('Res*.pdf')[0]
f=Fix('res58.txt')
f.pct()
# tabela A
i=f.s.index('t| CaracterísticaWorkflow'); j=f.s.index('t| FIAP\n')+len('t| FIAP\n')
f.s=f.s[:i]+('th| Característica | Workflow (Fluxo Engessado) | Agente de IA (Autônomo)\n'
'tr| Como funciona? | Baseado na lógica estruturada de "Se acontecer X, então faça Y". | Baseado em um objetivo e na capacidade de raciocinar sobre o que fazer.\n'
'tr| Previsibilidade | 100% previsível. Segue estritamente o mapa desenhado por você. | Imprevisível. O caminho exato pode mudar a cada execução.\n'
'tr| Tomada de decisão | Você decide todas as ramificações e cenários possíveis com antecedência. | A IA avalia o contexto atual e decide qual ferramenta ou resposta usar.\n'
'tr| Tratamento de erros | Se algo sair do roteiro previsto, o fluxo quebra ou trava. | Consegue recalcular a rota, reescrever prompts ou tentar outro método.\n')+f.s[j:]
f.rep(' <strong>Etapa 2 (IA integrada):</strong>','\nli| <strong>Etapa 2 (IA integrada):</strong>')
f.rep('Zendesk n8n é uma combinação fantástica e extremamente robusta\nt| +\npara começar.','Zendesk + n8n é uma combinação fantástica e extremamente robusta para começar.') if False else None
f.rep('Fechado! Zendesk n8n é uma combinação fantástica e extremamente robusta\nt| +\np| para começar.','Fechado! Zendesk + n8n é uma combinação fantástica e extremamente robusta para começar.')
f.rep('p| Fechado! Zendesk + n8n é uma combinação fantástica e extremamente robusta para começar.','p| Fechado! Zendesk + n8n é uma combinação fantástica e extremamente robusta para começar.') if False else None
f.rep('"Minha API\nt| parou de funcionar e preciso que você investigue o log da AWS, valide o payload\np| no banco','"Minha API parou de funcionar e preciso que você investigue o log da AWS, valide o payload no banco')
f.rep('t| Origins AI\nt| Retool\nt| MindStudio\nt| | MindStudio\n','')
# tabela B
i=f.s.index('t| ⚙ Workflow Inteligente'); j=f.s.index('h| 💡 A Regra de Ouro Prática')
f.s=f.s[:i]+('th| Cenário | ⚙️ Workflow Inteligente (Trilhos) | 🧠 Agente Autônomo (Bússola)\n'
'tr| Suporte ao Cliente | Triagem automatizada: Ler o chamado do Zendesk, classificar a urgência, extrair o sentimento e encaminhar para a equipe certa no Slack. | Resolução aberta: Receber um e-mail reclamando de uma cobrança indevida, puxar o histórico de compras, cruzar os dados, tomar a decisão de estornar o valor e fazer o pix de reembolso sozinho.\n'
'tr| Desenvolvimento / TI | Pipeline de Deploy: Rodar testes automáticos após um push, verificar vulnerabilidades, compilar o código e subir para produção se tudo estiver verde. | Debugging complexo: Ler um log de erro anômalo, caçar o bug vasculhando múltiplos arquivos de um repositório, aplicar a correção no código e testar para ver se resolveu.\n'
'tr| Marketing / Conteúdo | Fábrica de Posts: Pegar um link de um vídeo, transformá-lo em um rascunho de artigo, passar por uma revisão de tom de voz automática e agendar no WordPress. | Análise de Concorrência: Investigar o que os 5 principais concorrentes lançaram de novo nesta semana, ler os comentários dos clientes deles nas redes sociais e propor uma estratégia de produto inédita.\n')+f.s[j:]
f.rep('t| "Se eu colocar um humano júnior para fazer isso, eu preciso dar\nt| um manual de instruções detalhado (passo 1, passo 2, passo\nt| 3) ou preciso dar um objetivo final e deixá-lo navegar?"',
      'p| "Se eu colocar um humano júnior para fazer isso, eu preciso dar um manual de instruções detalhado (passo 1, passo 2, passo 3) ou preciso dar um objetivo final e deixá-lo navegar?"')
f.rep('li| Vender a regra de ouro + os custos honestos: Comece pelo\nq| mais simples','q| Vender a regra de ouro + os custos honestos: Comece pelo mais simples')
f.rep('lance do \\casa iluminada','lance do "casa iluminada')
# custos
f.rep('Agente Autônomo Solitário:4x mais caro</strong>. Ele vai ler, decidir qual\nt| ~\nli| ferramenta','Agente Autônomo Solitário: ~4x mais caro</strong>. Ele vai ler, decidir qual ferramenta')
f.rep('. <strong>Agente Autônomo Solitário:','.\nli| <strong>Agente Autônomo Solitário:')
f.rep('li| <strong>Sistema Multi-Agente:15x (ou mais) mais caro</strong>. Os agentes começam a\nt| ~\nli| "conversar"','li| <strong>Sistema Multi-Agente: ~15x (ou mais) mais caro</strong>. Os agentes começam a "conversar"')
f.rep('formular a resposta.\nli| <strong>Sistema','formular a resposta.\nli| <strong>Sistema') if False else None
f.rep('"Ah, o nó de IA categorization respondeu \'Financeiro\', mas escrevi \'financeiro\'\nli| com','"Ah, o nó de IA categorization respondeu \'Financeiro\', mas escrevi \'financeiro\' com') if False else None
f.rep('t| "Ah, o nó de IA categorization respondeu \'Financeiro\', mas escrevi \'financeiro\'\nli| com \'f\' minúsculo','li| "Ah, o nó de IA categorization respondeu \'Financeiro\', mas escrevi \'financeiro\' com \'f\' minúsculo') if False else None
f.rep('Resolve 90 dos problemas de triagem, resumo\nt| %\nli| e classificação.','Resolve 90% dos problemas de triagem, resumo\nli| e classificação.') if False else None
f.rep('<strong>n8n Zendesk</strong> usando essa\nt| +\np| abordagem','<strong>n8n + Zendesk</strong> usando essa abordagem')
# rótulos de linguagem e código do JS e do Slack
f.rep('li| text\nc| Você é','c| Você é') if False else None
# Slack: t| -> c|
i=f.s.index('t| 🚨 *Novo Chamado'); j=f.s.index('h| 🚀 O Fluxo Completo')
blk=f.s[i:j].rstrip('\n').split('\n')
out=[]
for l in blk:
    c=l[3:]
    out.append('c| '+c)
    if c.startswith('🚨'): out.append('c| ')
    if c.startswith('• 📝'): out.append('c| ')
f.s=f.s[:i]+'\n'.join(out)+'\n'+f.s[j:]
f.s=f.s.replace('li| javascript\n','li| javascript\n')
f.code_xml(P)
f.code_from('rp58.fixed.txt')
f.numbered()
f.t_to_h()
f.rep('onde travou:\nh| "Ah, o nó de IA categorization respondeu \'Financeiro\', mas escrevi \'financeiro\'\nli| com','onde travou: "Ah, o nó de IA categorization respondeu \'Financeiro\', mas escrevi \'financeiro\' com')
f.rep('resumo\nli| e classificação.','resumo e classificação.')
f.save('res58.fixed.txt')
