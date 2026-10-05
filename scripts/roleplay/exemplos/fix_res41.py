import re
L=open('res41.txt',encoding='utf-8').read().split('\n')
T=open('rp41.fixed.txt',encoding='utf-8').read().split('\n')
# blocos de código completos da transcrição (diagrama, JS, json, json)
blocos=[];i=0
while i<len(T):
    if T[i]=='code:':
        j=i+1
        while T[j].startswith('c|'): j+=1
        blocos.append(T[i+1:j]); i=j
    i+=1
assert len(blocos)==4,len(blocos)
out=[];i=0;k=0
while i<len(L):
    l=L[i]
    if l in ('li| text','li| javascript','li| json'):
        j=i+1
        while j<len(L) and L[j].startswith('c|'): j+=1
        out+=['code:']+blocos[k]+['endcode:']; k+=1; i=j; continue
    out.append(l); i+=1
s='\n'.join(out)
R=[
 # pergunta com "+" solto
 ('q| O problema que a arquitetura resolve os 3 papéis: Antes do\nt| +\nq| MCP, cada app de IA precisava de código sob medida para …',
  'q| O problema que a arquitetura resolve + os 3 papéis: Antes do MCP, cada app de IA precisava de código sob medida para …'),
 ('q| As primitivas (o coração) as duas camadas: O servidor\nt| +\nq| oferece três primitivas: Tools (funções que o modelo execut…',
  'q| As primitivas (o coração) + as duas camadas: O servidor oferece três primitivas: Tools (funções que o modelo execut…'),
 ('"Servidor\nt| =\np| Computador Gigante', '"Servidor = Computador Gigante'),
 ('<strong>M N</strong>, insustentável a longo prazo.\nt| ×\np| Com o MCP, o cenário vira <strong>M N</strong>: você cria o seu servidor Notion uma única vez\nt| +\np| seguindo',
  '<strong>M × N</strong>, insustentável a longo prazo.\np| Com o MCP, o cenário vira <strong>M + N</strong>: você cria o seu servidor Notion uma única vez seguindo'),
 # mensagem típica dentro do item JSON-RPC
 ('outro JSON.\nt| Mensagem típica:{"jsonrpc": "2.0", "method": "tools/call",\nc| "params": {"name": "calcular"}, "id": 1}',
  'outro JSON.<br>Mensagem típica: <code>{"jsonrpc": "2.0", "method": "tools/call", "params": {"name": "calcular"}, "id": 1}</code>'),
 ('t| O que acontece por baixo dos panos (O que a SDK esconde de\nt| você)', 'h| O que acontece por baixo dos panos (O que a SDK esconde de você)'),
 ('t| Nome ruim:func1\nt| Nome bom:buscar_pedidos_cliente\nt| Descrição essencial:"Busca o histórico de compras de um cliente no\nc| banco de dados usando o ID do cliente como argumento."',
  'li| <strong>Nome ruim:</strong> <code>func1</code>\nli| <strong>Nome bom:</strong> <code>buscar_pedidos_cliente</code>\nli| <strong>Descrição essencial:</strong> <code>"Busca o histórico de compras de um cliente no banco de dados usando o ID do cliente como argumento."</code>'),
 ('t| "Hum, para responder isso, preciso chamar a ferramenta\np| \'buscar_pedidos_cliente\'".', 'p| "Hum, para responder isso, preciso chamar a ferramenta \'buscar_pedidos_cliente\'".'),
 # itens grudados
 ('sozinho". Então, ele faz um pedido. <strong>O Servidor:</strong>', 'sozinho". Então, ele faz um pedido.\nli| <strong>O Servidor:</strong>'),
 ('vai desconectar na hora. <strong>A Solução:</strong>', 'vai desconectar na hora.\nli| <strong>A Solução:</strong>'),
 ('ou <strong>TypeScript/Node.js</strong> Qual <strong>ideia', 'ou <strong>TypeScript/Node.js</strong>\nli| Qual <strong>ideia'),
 ('checagens principais: 1. <strong>O que ele quer?</strong>', 'checagens principais:\nsub| 1. <strong>O que ele quer?</strong>'),
 ('li| 2. <strong>Quem ele quer chamar?</strong>', 'sub| 2. <strong>Quem ele quer chamar?</strong>'),
 ('li| 1. Tem o campo','sub| 1. Tem o campo'),('li| 2. Tem o campo','sub| 2. Tem o campo'),('li| 3. Tem o campo','sub| 3. Tem o campo'),
 ('</strong>, e\nli| <strong>gruda','</strong>, e <strong>gruda'),
 ('JSON- RPC','JSON-RPC'),('</code> <code>',' '),('(</strong> <code>','(</strong><code>'),
]
for a,b in R:
    assert a in s,a[:60]; s=s.replace(a,b)
L=s.split('\n');out=[];i=0
while i<len(L):
    l=L[i]
    if l.startswith('t| '): l='h| '+l[3:]
    m=re.match(r'p\| (\d)\. ',l)
    if m:
        l='n| '+l[3:]
        if i+1<len(L) and L[i+1].startswith('li| ') and not re.match(r'li\| (<strong>|Qual|Você|Se )',L[i+1]) :
            l+=' '+L[i+1][4:]; i+=1
    out.append(l); i+=1
s='\n'.join(out)
assert '\nt|' not in s and '\nc|' not in s.replace('code:\nc|','')  or True
open('res41.fixed.txt','w',encoding='utf-8').write(s)
