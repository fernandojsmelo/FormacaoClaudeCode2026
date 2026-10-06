import re
s=open('rp55.codigo.txt',encoding='utf-8').read()
res=open('res55.txt',encoding='utf-8').read().split('\n')
def rep(a,b):
    global s
    assert a in s,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
L=s.split('\n')
# tabela de modelos
i=[k for k,l in enumerate(L) if l.startswith('p| Característica=€')][0]
rows=[('Exemplos','Llama 3.3'),('Como funciona','Você baixa os "pesos"'),('Onde roda','No seu computador'),('Custo','Grátis para baixar')]
out=['th| Característica | 🚀 Modelos de Fronteira (Fechados) | 🔓 Modelos de Peso Aberto (Open Source)']
nome_pref={'Exemplos':'Exemplos','Como funciona':'Como funciona','Onde roda':'Onde roda','Custo':'Custo'}
for k,(nome,b) in enumerate(rows,1):
    t=L[i+k][3:]; assert t.startswith(nome),t[:30]; t=t[len(nome):]
    a,c=t.split(b,1); out.append(f'tr| {nome} | {a.strip()} | {b}{c}')
L[i:i+5]=out; s='\n'.join(L)
rep(' 2. Capacidade Máxima no Limite','\np| 2. Capacidade Máxima no Limite')
rep(' 1. A Rota Mais Barata e Rápida','\np| 1. A Rota Mais Barata e Rápida')
rep(' 4. Conforme o Llama responde','\np| 4. Conforme o Llama responde')
rep(' 3. Memória Inteligente','\np| 3. Memória Inteligente')
rep('banco com remetente\nh| \'assistant\'.','banco com remetente = \'assistant\'.')
# truque do dev
m=re.search(r'^h\| (💡 O Truque do Dev:.*)\np\| (.*)$',s,flags=re.M); s=s[:m.start()]+'p| '+m.group(1)+' '+m.group(2)+s[m.end():]
# diagramas
def bloco(ini,fim,linhas,nota=False):
    global s
    i=s.index(ini); j=s.index(fim,i); j=s.index('\n',j)
    s=s[:i]+'code:\n'+'\n'.join('c| '+x for x in linhas)+'\n'+('endcode:' if nota else 'endnote:')+s[j:]
k=[n for n,l in enumerate(res) if l.startswith('c| [Cliente digita')][0]
dg=[l[3:] for l in res[k:k+23]]
bloco('p| [Cliente digita','p| Azul, entregue ontem',dg)
arq=['┌────────────────────────┐                    ┌────────────────────────┐',
     '│     FRONTEND (UI)      │                    │    BACKEND (Python)    │',
     '│  Componentes Material  │ ─── Requisição ──> │   Busca no Postgres    │',
     '│   Renderizador Markdown│ <── Streaming (SSE)│  Dispara API do Llama  │',
     '└────────────────────────┘                    └────────────────────────┘']
i=s.index('p| \np| FRONTEND (UI)'); j=s.index('p| 1. No Backend')
s=s[:i]+'code:\n'+'\n'.join('c| '+x for x in arq)+'\nendnote:\n'+s[j:]
painel='''┌─────────────────────────────────────────────────────────────────────────┐
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
i=s.index('p| Dashboard Geral >'); j=s.index('h| 🚀 Resumo do Próximo Passo')
s=s[:i]+'code:\n'+'\n'.join('c| '+x for x in painel)+'\nendnote:\n'+s[j:]
rep('encodeURIComponent(mensagemAtu-\nc|       al)}','encodeURIComponent(mensagemAtual)}') if 'mensagemAtu-\nc|       al)}' in s else rep('mensagemAtu-\nc| al)}','mensagemAtual)}')
open('rp55.fixed.txt','w',encoding='utf-8').write(s)
print([l[:70] for l in s.split('\n') if re.search(r'[=<>][^\s\w"\'(){}\[\].,:=<>*+|-]|\x00',l) and not l.startswith('c|')])
print([l[:70] for l in s.split('\n') if l.startswith('c|') and re.search(r'[=<>][^\s\w"\'(){}\[\].,:=<>*+|/-]|\x00',l)][:10])
