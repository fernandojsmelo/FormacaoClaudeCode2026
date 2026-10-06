import re
s=open('rp58.e.txt',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
rep('"Agen- tificar"','"Agentificar"')
s=s.replace(' =€',' 🚀')
# tabela A
i=s.index('p| CaracterísticaWorkflow'); j=s.index('@turn Lucas Prado|01:03')
s=s[:i]+('th| Característica | Workflow (Fluxo Engessado) | Agente de IA (Autônomo)\n'
'tr| Como funciona? | Baseado na lógica estruturada de "Se acontecer X, então faça Y". | Baseado em um objetivo e na capacidade de raciocinar sobre o que fazer.\n'
'tr| Previsibilidade | 100% previsível. Segue estritamente o mapa desenhado por você. | Imprevisível. O caminho exato pode mudar a cada execução.\n'
'tr| Tomada de decisão | Você decide todas as ramificações e cenários possíveis com antecedência. | A IA avalia o contexto atual e decide qual ferramenta ou resposta usar.\n'
'tr| Tratamento de erros | Se algo sair do roteiro previsto, o fluxo quebra ou trava. | Consegue recalcular a rota, reescrever prompts ou tentar outro método.\n')+s[j:]
# tabela B
i=s.index('p| Cenário™'); j=s.index('h| 💡 A Regra de Ouro Prática')
blk=s[i:j]
def cells(txt,a,b):
    m=re.match(r'(.*?)'+re.escape(a)+r'(.*?)'+re.escape(b)+r'(.*)$',txt,re.S); return m.group(1),a+m.group(2),b+m.group(3)
r1=s[i:j].split('\n')
l78=r1[1][3:]; l79=r1[2][3:]
a,b=l78.split(' Desenvolvimento / TI')
t1=cells(a.strip(),'Triagem automatizada:','Resolução aberta:')
t2=cells('Desenvolvimento / TI'+b,'Pipeline de Deploy:','Debugging complexo:')
t3=cells(l79.strip(),'Fábrica de Posts:','Análise de Concorrência:')
s=s[:i]+'th| Cenário | ⚙️ Workflow Inteligente (Trilhos) | 🧠 Agente Autônomo (Bússola)\n'+''.join('tr| '+' | '.join(x.strip() for x in t)+'\n' for t in (t1,t2,t3))+s[j:]
# JS
i=s.index('p| javascript'); j=s.index('p| Use o código com cuidado.')+len('p| Use o código com cuidado.')
js='''// Captura a saída do nó anterior (IA)
let aiResponse = $json;

// Define os valores padrão de segurança (Fallback)
let resultadoFinal = {
    categoria: "nao_classificado",
    urgencia: "media",
    resumo_curto: "Falha na triagem automática da IA."
};

try {
    // Se a IA mandou uma string em vez de um objeto, tenta converter
    if (typeof aiResponse === 'string') {
        aiResponse = JSON.parse(aiResponse);
    } else if (aiResponse.output && typeof aiResponse.output === 'string') {
        // Caso o nó do n8n jogue a resposta dentro de um campo 'output'
        aiResponse = JSON.parse(aiResponse.output);
    }

    // Valida se os campos obrigatórios existem na resposta
    if (aiResponse.categoria && aiResponse.urgencia) {
        resultadoFinal.categoria = aiResponse.categoria.toLowerCase().trim();
        resultadoFinal.urgencia = aiResponse.urgencia.toLowerCase().trim();
        resultadoFinal.resumo_curto = aiResponse.resumo_curto || "Sem resumo disponível.";
    }
} catch (e) {
    // Se o JSON for totalmente inválido, o código cai aqui e mantém o fallback com segurança
    console.log("Erro ao processar JSON da IA, usando fallback.", e);
}

return resultadoFinal;'''
s=s[:i]+'code:\n'+'\n'.join('c| '+l if l else 'c| ' for l in js.split('\n'))+'\nendcode:'+s[j:]
rep('p| 2. Value 1: Clique na engrenagem e use a expressão para pegar a categoria do nó de código anterior: {{ $json.categoria\nh| [n8n.io].','p| 2. Value 1: Clique na engrenagem e use a expressão para pegar a categoria do nó de código anterior: {{ $json.categoria }} [n8n.io].')
# nota interna do Zendesk
i=s.index('li| Internal Note'); j=s.index('h| 💬 Passo 2')
s=s[:i]+('li| Internal Note (Comentário Interno): Adicione um comentário invisível para o cliente, mas visível para o seu time:\n'
 'p| > 🤖 Triagem Inteligente (IA):\np| 📌 Categoria: {{ $json.categoria }}\np| ⚠️ Urgência: {{ $json.urgencia }}\np| 📝 Resumo: {{ $json.resumo_curto }}\n')+s[j:]
# slack
i=s.index('code:\nc| *Novo Chamado'); j=s.index('endcode:',i)
s=s[:i]+('code:\nc| 🚨 *Novo Chamado Classificado via IA* 🚨\nc| \nc| • 📥 *Ticket ID:* #{{ \\$node["Zendesk Trigger"].json.ticket.id }}\n'
 'c| • 🔠 *Categoria:* `{{ $json.categoria.toUpperCase() }}`\nc| • 🔥 *Urgência:* *{{ \\$json.urgencia.toUpperCase() }}*\nc| • 📝 *Resumo:* {{ \\$json.resumo_curto }}\nc| \nc| 👉 _Abra o chamado direto no Zendesk para responder ao cliente._\n')+s[j:]
# quebras de linha das listas numeradas dentro de p| (Zendesk/Slack já separados). limpar restos
open('rp58.fixed.txt','w',encoding='utf-8').write(s)
print([l[:70] for l in s.split('\n') if re.search(r'[=<>][^\s\w"\'(){}\[\].,:=<>*+|-]|\x00|™',l)])
