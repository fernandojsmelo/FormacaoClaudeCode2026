import re
s=open('res42.txt',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s, a[:70]; s=s.replace(a,b)
def rep_block(first,last,new):
    """troca do início de `first` até o fim da linha de `last`"""
    global s
    i=s.index(first); j=s.index(last,i); j=s.index('\n',j)
    s=s[:i]+new+s[j:]
rep('atualizada no\nt| documento interno?"','atualizada no documento interno?"')
rep_block('t| BenefícioComo','t| prontos para uso.',
 'th| Benefício | Como o MCP resolve\n'
 'tr| <strong>Fim das Alucinações</strong> | O chatbot passa a responder com base em <strong>fatos e documentos reais</strong>, e não no que ele "acha" que é o certo.\n'
 'tr| <strong>Segurança de Dados</strong> | Você escolhe exatamente quais pastas ou arquivos o Servidor MCP pode acessar. Os dados confidenciais <strong>permanecem no seu ambiente seguro</strong>.\n'
 'tr| <strong>Flexibilidade (Sem "Lock-in")</strong> | Se amanhã você quiser trocar o modelo de IA (mudar do OpenAI para o Anthropic ou Google, por exemplo), você não perde o trabalho. O plugue MCP continua sendo o mesmo.\n'
 'tr| <strong>Desenvolvimento Rápido</strong> | Sua equipe de tecnologia não precisa criar código do zero para ler PDFs ou planilhas. Já existem dezenas de conectores MCP prontos para uso.')
rep_block('t| "Imagine que a inteligência do chatbot','t| segurança à IA usando a mesma entrada."',
 'p| <em>"Imagine que a inteligência do chatbot é uma tomada na parede e os dados da sua empresa são os diferentes aparelhos eletrônicos (uma TV, um liquidificador, um carregador). No passado, cada aparelho tinha um plugue de formato bizarro e você precisava comprar um adaptador caro e sob medida para cada um deles. <strong>O MCP é o padrão USB-C</strong>: um plugue universal. Agora, qualquer sistema da sua empresa se conecta instantaneamente e com segurança à IA usando a mesma entrada."</em>')
rep('USB- C','USB-C'); rep('alterá- lo','alterá-lo')
rep_block('t| Resource (Fonte de Dados)\nt| Característica📘Tool','t| Segurançamal configurado)',
 'th| Característica | Resource (Fonte de Dados) 📘 | Tool (Ferramenta) 🛠\n'
 'tr| <strong>O que é?</strong> | Um dado estático ou dinâmico para <strong>leitura</strong>. | Uma função de código para <strong>execução</strong>.\n'
 'tr| <strong>Intenção</strong> | Conhecer e entender um contexto. | Alterar o estado do mundo ou agir.\n'
 'tr| <strong>Exemplo de Chatbot</strong> | "Deixe-me ler o manual de integração..." [1] | "Deixe-me criar este novo usuário no sistema..." [1]\n'
 'tr| <strong>Risco de Segurança</strong> | Baixo (vazamento de info se mal configurado). | Alto (ações indesejadas se não houver aprovação).')
rep('como:\nc| empresa://documentos/departamento/{nome_departamento}/politica_atua\nli| <code>lizada</code>.',
    'como: <code>empresa://documentos/departamento/{nome_departamento}/politica_atualizada</code>.')
rep('Mudanças ()\nc| Resource Changed','Mudanças (<code>Resource Changed</code>)')
rep('c|  sharepoint://{tenant}://{site_name}/lists/{library_name}/files/{fil\nc| e_path}','c| sharepoint://{tenant}://{site_name}/lists/{library_name}/files/{file_path}')
rep('c|  sharepoint://sites/{site_id}/drives/{drive_id}/root:/{file_path}:/c\nc| ontent','c| sharepoint://sites/{site_id}/drives/{drive_id}/root:/{file_path}:/content')
rep('c|  gdrive://{drive_id}/folders/{department_folder_id}/files/{document_\nc| name}','c| gdrive://{drive_id}/folders/{department_folder_id}/files/{document_name}')
rep('c|  gdrive://shared-drive-\nc| corporativo/','c| gdrive://shared-drive-corporativo/')
rep('c|  sharepoint://{tenant}://{site_name}/libraries/{library_name}/docume\nc| nts/{file_path}','c| sharepoint://{tenant}://{site_name}/libraries/{library_name}/documents/{file_path}')
rep('100 interno facilita imensamente\nt| %\np| a arquitetura','100% interno facilita imensamente a arquitetura')
rep_block('t| "Servidor MCP, o usuário','t| reembolso_2026.docx no SharePoint."',
 'p| <em>"Servidor MCP, o usuário <strong>João (Token XYZ)</strong> quer ler o documento <code>reembolso_2026.docx</code> no SharePoint."</em>')
rep('On- Behalf-Of','On-Behalf-Of')
rep('de texto comuns. <strong>Segurança Embutida:</strong>','de texto comuns.\nli| <strong>Segurança Embutida:</strong>')
rep('t| Google Codelabs\nt| Microsoft Developer\nt| Microsoft Community Hub\n','')
rep('t| O objetivo aqui é fazer a equipe "brincar" com o MCP antes de programar o bot\nt| do Teams.',
    'p| <em>O objetivo aqui é fazer a equipe "brincar" com o MCP antes de programar o bot do Teams.</em>')
for t in ['Garantir que a IA só leia o que o usuário logado no Teams pode ver.','Conectar o cérebro da IA ao plugue universal.','Colocar o produto para rodar na interface oficial.']:
    rep('t| '+t,'p| <em>'+t+'</em>')
rep('baseadas no usuário). <strong>Fluxo On-Behalf-Of (OBO):</strong>','baseadas no usuário).\nli| <strong>Fluxo On-Behalf-Of (OBO):</strong>')
rep('li| Implementar a lógica: Pergunta do Usuário → Detecção de Intenção de\nt| Leitura → Chamada de Resource via MCP → Injeção de Contexto no LLM →\nli| Resposta.',
    'li| Implementar a lógica: Pergunta do Usuário ➔ Detecção de Intenção de Leitura ➔ Chamada de Resource via MCP ➔ Injeção de Contexto no LLM ➔ Resposta.')
rep('<strong>Protocolo Oficial:</strong>modelcontextprotocol.io','<strong>Protocolo Oficial:</strong> modelcontextprotocol.io')
rep('100 das respostas</strong> sobre documentos\nt| %\nli| internos','100% das respostas</strong> sobre documentos internos')
rep('100 de sucesso nos testes de isolamento</strong>.\nt| %\nli| Se um','100% de sucesso nos testes de isolamento</strong>. Se um')
rep('<strong>90 das</strong>\nt| %\nli| <strong>variações','<strong>90% das</strong> <strong>variações')
rep_block('t| "Os riscos existem','t| onde a IA pisa',
 'p| <em>"Os riscos existem, mas todos são mitigáveis porque o MCP nos dá controle total sobre o fluxo do dado. Nós escolhemos exatamente onde a IA pisa, o que ela lê e o quanto ela gasta."</em>')
rep('100 das premissas de TI:\nt| %\n','100% das premissas de TI:\n')
rep('p| 1. <strong>Governança Delegada:</strong> O ecossistema usa autenticação nativa (SSO com\nli| Microsoft','p| 1. <strong>Governança Delegada:</strong> O ecossistema usa autenticação nativa (SSO com\nli| microsoft_')
rep('<strong>[Seu Nome] [Seu Cargo/Produto]</strong>','<strong>[Seu Nome]</strong><br><strong>[Seu Cargo/Produto]</strong>')
rep('até a próxima! 🚀✨ Quando o MVP','até a próxima! 🚀✨\np| Quando o MVP')
rep_block('t| "Imagine que a inteligência da Inteligência','t| complicação e sem gambiarras."',
 'p| <em>"Imagine que a inteligência da Inteligência Artificial é uma tomada na parede e os dados da sua empresa são os diferentes aparelhos eletrônicos (como uma TV, uma geladeira ou um carregador de celular). No passado, cada aparelho tinha um plugue de formato bizarro e diferente. Você precisava contratar um eletricista para criar um adaptador caro e sob medida para cada um deles conseguir se conectar à tomada.</em>\n'
 'p| <em>O <strong>MCP (Model Context Protocol)</strong> chegou para ser o <strong>padrão USB-C</strong>: um plugue único e universal. Agora, qualquer sistema de arquivos ou banco de dados da sua empresa se conecta instantaneamente à IA usando exatamente a mesma entrada, sem complicação e sem gambiarras."</em>')
rep('imediatamente. <strong>Segurança e Controle:</strong>','imediatamente.\nli| <strong>Segurança e Controle:</strong>')
rep('"Onde...". <strong>Exemplos práticos:</strong>','"Onde...".\nli| <strong>Exemplos práticos:</strong>')
rep_block('t| Resource (Fonte de Dados)\nt| Característica📘Tool','t| Segurançaarquivo estiver',
 'th| Característica | Resource (Fonte de Dados) 📘 | Tool (Ferramenta) 🛠\n'
 'tr| <strong>Objetivo Principal</strong> | Conhecer e entender um contexto. | Alterar o estado do mundo ou agir.\n'
 'tr| <strong>Operação Computacional</strong> | Apenas Leitura (Read-Only). | Execução e Escrita (Read/Write/Execute).\n'
 'tr| <strong>Exemplo no Chatbot</strong> | "Deixe-me ler o manual de integração..." | "Deixe-me criar este novo usuário no sistema..."\n'
 'tr| <strong>Impacto de Segurança</strong> | Baixo (vazamento se o arquivo estiver exposto). | Alto (ações indesejadas se não houver travas).')
rep_block('t| "Aha! Se o usuário','t| padrão do MCP."',
 'p| <em>"Aha! Se o usuário me pedir um documento do Financeiro, eu não preciso caçar no Drive inteiro. Eu só preciso descobrir o <code>{file_path}</code> ou o <code>{document_name}</code> e encaixar nesse endereço padrão do MCP."</em>')
rep('viagens da\nt| empresa?"','viagens da empresa?"')
rep_block('t| CaracterísticaResource (Recurso)','t| configurado).',
 'th| Característica | Resource (Recurso) 📘 | Tool (Ferramenta) 🛠\n'
 'tr| <strong>O que ele representa?</strong> | Um <strong>dado</strong> ou documento para consulta. | Uma <strong>função</strong> de código para execução.\n'
 'tr| <strong>Permissão padrão</strong> | Apenas Leitura (Read-Only). | Escrita e Execução (Read/Write/Execute).\n'
 'tr| <strong>Exemplo de fala do bot</strong> | "Deixe-me dar uma olhada no contrato..." | "Deixe-me atualizar o status no sistema..."\n'
 'tr| <strong>Nível de Risco</strong> | Baixo (risco de ler dado confidencial se mal configurado). | Alto (risco de fazer alterações indesejadas sem aprovação).')
# passes genéricos
L=s.split('\n'); out=[]; i=0
while i<len(L):
    l=L[i]
    m=re.match(r'p\| \d\. ',l)
    if m:
        l='n| '+l[3:]
        if i+1<len(L) and L[i+1].startswith('li| ') and re.match(r'li\| (microsoft_|[a-zà-ú])',L[i+1]):
            l+=' '+L[i+1][4:].replace('microsoft_','Microsoft'); i+=1
    if l.startswith('c|'):
        blk=[]
        while i<len(L) and L[i].startswith('c|'): blk.append(L[i]); i+=1
        out+=['code:']+blk+['endnote:']; continue
    out.append(l); i+=1
s='\n'.join(out)
left=[l for l in s.split('\n#cards')[0].split('\n') if l.startswith('t|')]
assert not left, left
open('res42.fixed.txt','w',encoding='utf-8').write(s)
print(s.count('\nq|')+1,'perguntas')
# recuo exato dos diagramas a partir do XML (left 166 = 1 espaço a mais que 156)
exec(open('lines42.py').read().split('# linhas')[0])
D=[(re.sub(r'\s+',' ',l[4]).strip(), (' ' if l[2]==166 else '')+l[4].rstrip()) for l in L if l[3]=='D' and l[2] in (156,166)]
out=[];p=0
for ln in s.split('\n'):
    if ln.startswith('c|'):
        k=re.sub(r'\s+',' ',ln[2:]).strip()
        for q in range(p,len(D)):
            if D[q][0]==k: ln='c| '+D[q][1]; p=q+1; break
    out.append(ln)
s='\n'.join(out)
open('res42.fixed.txt','w',encoding='utf-8').write(s)
