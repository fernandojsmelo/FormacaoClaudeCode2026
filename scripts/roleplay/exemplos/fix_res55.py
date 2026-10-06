import re,glob
ARQ=['┌────────────────────────┐                    ┌────────────────────────┐',
     '│     FRONTEND (UI)      │                    │    BACKEND (Python)    │',
     '│  Componentes Material  │ ─── Requisição ──> │   Busca no Postgres    │',
     '│   Renderizador Markdown│ <── Streaming (SSE)│  Dispara API do Llama  │',
     '└────────────────────────┘                    └────────────────────────┘']
PAINEL='''┌─────────────────────────────────────────────────────────────────────────┐
│   Dashboard Geral > [ Painel do Assistente IA ]                         │
├──────────────────────┬──────────────────────────────────────────────────┤
│ Histórico de Chats   │ 🤖 Assistente Virtual                            │
│                      │                                                  │
│ 💬 Dúvida sobre...   │ [Usuário]: Como funciona o reembolso?            │
│ 💬 Atualização de... │                                                  │
│ 💬 Erro no boleto    │ [Assistente]: Com base no seu histórico de       │
│                      │  compras no nosso sistema, você tem direito a... │
│                      │  • Opção 1: Estorno direto no cartão             │
│                      │  • Opção 2: Crédito na loja                      │
│                      │                                                  │
│                      ├──────────────────────────────────────────────────┤
│                      │ ✉️ Digite sua mensagem aqui...          [Enviar] │
└──────────────────────┴──────────────────────────────────────────────────┘'''.split('\n')

from rpfix import Fix
P=glob.glob('Res*.pdf')[0]
f=Fix('res55.txt')
f.pct()
f.rep('t| winningdata.io\n','')
f.rep('li| <strong>Modelos de Fronteira','li| <strong>Modelos de Fronteira')
f.rep('t| Modelos de Peso Aberto / Open Source (Download/Local): Llama 3.1 / 3.2\nli| (Meta)','li| <strong>Modelos de Peso Aberto / Open Source (Download/Local): Llama 3.1 / 3.2</strong> (Meta)')
# tabela
i=f.s.index('t| 🚀 Modelos de Fronteira🔓'); j=f.s.index('h| ⚖ Se os abertos')
f.s=f.s[:i]+('th| Característica | 🚀 Modelos de Fronteira (Fechados) | 🔓 Modelos de Peso Aberto (Open Source)\n'
'tr| Exemplos | GPT-4o (OpenAI), Claude 3.5 Sonnet (Anthropic), Gemini 1.5 Pro (Google) | Llama 3.3 (Meta), DeepSeek-V3/R1, Qwen 2.5 (Alibaba)\n'
'tr| Como funciona | Você acessa via API ou aplicativo. Eles controlam o código e a infraestrutura. | Você baixa os "pesos" (o cérebro do modelo) e roda onde quiser.\n'
'tr| Onde roda | Nos servidores da OpenAI, Google ou Anthropic. | No seu computador, no servidor da sua empresa ou em nuvens privadas.\n'
'tr| Custo | Pago por uso (pay-per-token). Quanto mais usa, mais paga. | Grátis para baixar. Você paga apenas o custo da máquina/nuvem que o hospeda.\n')+f.s[j:]
f.rep('por que alguém paga os\nt| fechados?','por que alguém paga os fechados?')
f.rep('1. A Rota Mais Barata e Rápida (Open Source via API)','1. A Rota Mais Barata e Rápida (Open Source via API)')
f.rep('t| 2. O Desenvolvedor Generalista vai se bater?\nt| Não, ele vai achar extremamente fácil.','t| 2. O Desenvolvedor Generalista vai se bater?\np| <strong>Não, ele vai achar extremamente fácil.</strong>') if False else None
f.rep('t| 3. O chatbot precisa buscar o Histórico do Cliente. Isso muda o\nt| plano?','t| 3. O chatbot precisa buscar o Histórico do Cliente. Isso muda o plano?')
f.rep('t| 2. E se o provedor falhar? Dá para mudar sem reescrever o\nt| código?\nt| Sim! Você pode mudar de provedor em menos de 1 minuto trocando apenas\nt| duas linhas de código.','t| 2. E se o provedor falhar? Dá para mudar sem reescrever o código?\np| Sim! Você pode mudar de provedor em menos de 1 minuto trocando apenas duas linhas de código.')
f.rep('p| Here is your file:\nt| Chatbot Postgres Llama','p| Here is your file: Chatbot Postgres Llama')
f.rep('t| Não, ele vai achar extremamente fácil.','p| Não, ele vai achar extremamente fácil.')
f.rep('<strong>Python PostgreSQL</strong>, você está na melhor combinação\nt| +\np| técnica possível','<strong>Python + PostgreSQL</strong>, você está na melhor combinação técnica possível')
f.rep('<strong>Python PostgreSQL</strong> no banco, <strong>Llama 3.3</strong>\nt| +\np| <strong>via API','<strong>Python + PostgreSQL</strong> no banco, <strong>Llama 3.3 via API')
f.rep('Quase 90% das ferramentas, bibliotecas e tutoriais do mercado são desenhados\np| exatamente','Quase 90% das ferramentas, bibliotecas e tutoriais do mercado são desenhados exatamente')
f.rep('têm 100% do\np| escopo','têm 100% do escopo') if False else None
f.rep('<strong>permanece 100% idêntico</strong>. Você tem\np| total independência','<strong>permanece 100% idêntico</strong>. Você tem total independência')
f.rep('Together\nli| AI.','Together AI.')
f.rep('Llama\nli| 3.3 responder.','Llama 3.3 responder.')
f.rep('o modelo\nli| <strong>Llama 3.3 (70B)</strong> via API','o modelo <strong>Llama 3.3 (70B)</strong> via API')
f.rep('</strong>\nli| <strong>mesmo descobre','</strong> <strong>mesmo descobre')
f.rep('<strong>React com</strong>\nli| <strong>Material UI</strong>','<strong>React com Material UI</strong>')
f.rep('(<code>pip install</code>\nli| <code>openai</code>)','(<code>pip install openai</code>)') if False else None
f.rep('t| (DESC), o seu desenvolvedor precisa inverter a lista no Python antes de mandar\nt| para a IA, garantindo que o chat fique na ordem cronológica correta (a mensagem\nt| mais antiga primeiro, a mais nova por último).\nt| Abordagem 2:','p| (DESC), o seu desenvolvedor precisa inverter a lista no Python antes de mandar para a IA, garantindo que o chat fique na ordem cronológica correta (a mensagem mais antiga primeiro, a mais nova por último).\nt| Abordagem 2:') if False else None
f.rep('h| 🛡 O Próximo Passo: Segurança de Rotas (Evitando Vazamento\nt| de Dados)','h| 🛡 O Próximo Passo: Segurança de Rotas (Evitando Vazamento de Dados)')
f.rep('trás para frente\nt| (DESC)','trás para frente (DESC)')
f.rep('(DESC), o seu desenvolvedor precisa inverter a lista no Python antes de mandar\nt| para a IA, garantindo que o chat fique na ordem cronológica correta (a mensagem\nt| mais antiga primeiro, a mais nova por último).','(DESC), o seu desenvolvedor precisa inverter a lista no Python antes de mandar para a IA, garantindo que o chat fique na ordem cronológica correta (a mensagem mais antiga primeiro, a mais nova por último).')
f.rep('nunca\nt| confie no que o frontend envia no corpo ou nos parâmetros da URL (como ?\np| <code>cliente_id=123</code><strong>)</strong>.','nunca confie no que o frontend envia no corpo ou nos parâmetros da URL (como <code>?cliente_id=123</code>).')
f.rep('t| 🤖 Assistente Inteligente\n','')
f.rep('t| 🔄 Como o Python','h| 🔄 Como o Python')
f.code_xml(P)
f.code_from('rp55.fixed.txt')

def troca_bloco(f,ini):
    tr=open('rp55.fixed.txt',encoding='utf-8').read().split('\n')
    a=[k for k,l in enumerate(tr) if l.startswith('c|') and ini in l][0]
    b=a
    while tr[b].startswith('c|'): b+=1
    novo=tr[a:b]
    L=f.s.split('\n'); a2=[k for k,l in enumerate(L) if l.startswith('c|') and ini in l][0]
    s0=a2
    while not L[s0].startswith('code:'): s0-=1
    e0=a2
    while not L[e0].startswith(('endcode:','endnote:')): e0+=1
    L[s0+1:e0]=novo
    f.s='\n'.join(L)
f.rep('<code>SELECT</code>\ncode:\nc|  historico_compras FROM clientes WHERE id = 123;\nendnote:','<code>SELECT historico_compras FROM clientes WHERE id = 123;</code>')
f.rep("<code>SELECT conteudo,</code>\ncode:\nc|  remetente FROM mensagens_chat WHERE sessao_id = '...' ORDER BY\nc|  criado_em ASC LIMIT 10;\nendnote:","<code>SELECT conteudo, remetente FROM mensagens_chat WHERE sessao_id = '...' ORDER BY criado_em ASC LIMIT 10;</code>")
troca_bloco(f,"import React, { useState")
troca_bloco(f,"from fastapi import FastAPI, Depends")
# diagrama do roteador
i=f.s.index('c| [Mensagem do Usuário]'); j=f.s.index('t| Exemplo real em um E-commerce:')
roteador='''[Mensagem do Usuário]
         │
         ▼
┌────────────────────────────────────────────────────────┐
│ Roteador de IA (Triagem Inicial)                       │
└───────────────────────┬────────────────────────────────┘
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
【 Tarefa Simples / Barata 】    【 Lógica Complexa / Crítica 】
Ex: Classificar e-mail,         Ex: Planejamento financeiro,
resumir chat, extrair data      refatoração de código antigo
         │                             │
         ▼                             ▼
┌───────────────┐             ┌───────────────┐
│ Modelo Aberto │             │   Fronteira   │
│ (Llama/Qwen)  │             │ (GPT-4o/Claude)│
└───────────────┘             └───────────────┘
(4x a 10x mais barato)        (Custo maior, erro menor)'''.split('\n')
f.s=f.s[:i]+'\n'.join('c| '+x for x in roteador)+'\n'+f.s[j:]
arq=open('rp55.fixed.txt',encoding='utf-8').read()
i=f.s.index('c| ┌────────────────────────┐'); j=f.s.index('t| 1. No Backend')
f.s=f.s[:i]+'\n'.join('c| '+x for x in ARQ)+'\n'+f.s[j:]
i=f.s.index('c| ┌───────────────────────────────────────────────────────────────────\n'); j=f.s.index('h| 🚀 Resumo do Próximo Passo')
f.s=f.s[:i]+'\n'.join('c| '+x for x in PAINEL)+'\n'+f.s[j:]
f.numbered()
f.t_to_h()
f.save('res55.fixed.txt')
