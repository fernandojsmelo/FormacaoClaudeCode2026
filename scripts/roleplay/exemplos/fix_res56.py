import re,glob
from rpfix import Fix
P=glob.glob('Res*.pdf')[0]
f=Fix('res56.txt')
f.pct()
f.rep('t| O modelo de inteligência artificial não aprende em tempo real durante as\np| conversas cotidianas.','p| O modelo de inteligência artificial não aprende em tempo real durante as conversas cotidianas.')
i=f.s.index('t| Uso do Modelo (Inferência'); j=f.s.index('t| chat atual.\n')+len('t| chat atual.\n')
f.s=f.s[:i]+('th| Característica | Treinamento do Modelo (Training) | Uso do Modelo (Inferência / Prompting)\n'
'tr| O que é? | O processo de construção da IA. É quando ela analisa bilhões de textos para aprender padrões de linguagem, gramática e fatos do mundo. | O processo de conversar com a IA. Você faz uma pergunta e ela gera uma resposta com base no que já sabe.\n'
'tr| Frequência | Feito raramente (leva meses para planejar e executar). | Feito toda vez que você envia uma mensagem.\n'
'tr| Custo | Altíssimo. Exige supercomputadores rodando por semanas e milhões de dólares em energia e infraestrutura. | Baixíssimo ou gratuito.\n'
'tr| Atualização | Cria uma "foto" congelada do conhecimento do mundo até aquela data (data de corte). | Não altera o cérebro do modelo; apenas consome as informações enviadas no chat atual.\n')+f.s[j:]
f.rep('página 4 do\nt| nosso manual','página 4 do nosso manual')
f.rep('t| O Microsoft 365 é o cenário perfeito para vocês, e esse tamanho de grupo (50\np| pessoas) é o ideal','p| O Microsoft 365 é o cenário perfeito para vocês, e esse tamanho de grupo (50 pessoas) é o ideal')
f.rep('t| "Nós queremos usar a função de respostas generativas fazendo o\nt| upload manual de arquivos (manuais em PDF do RH). Precisamos\nt| que a política do locatário (Tenant) permita o envio desses\nt| documentos internos para o Copilot."','p| "Nós queremos usar a função de respostas generativas fazendo o upload manual de arquivos (manuais em PDF do RH). Precisamos que a política do locatário (Tenant) permita o envio desses documentos internos para o Copilot."')
f.rep('t| [Seu Nome]','p| [Seu Nome]')
f.rep('q| O que é cada um: Treinamento ensinar o modelo,\nt| =\nq| processando','q| O que é cada um: Treinamento = ensinar o modelo, processando')
f.rep('como a Inteligência\nt| %\np| Artificial funciona:','como a Inteligência Artificial funciona:') if False else None
f.rep('<strong>Treinamento Ajustar Parâmetros (Pesos):</strong> É a fase de criação.\nt| =\n','<strong>Treinamento = Ajustar Parâmetros (Pesos):</strong> É a fase de criação.\n')
f.rep('<strong>Inferência Pesos Congelados:</strong> É o uso diário. O cérebro dele está "travado".\nt| =\nli| Quando','<strong>Inferência = Pesos Congelados:</strong> É o uso diário. O cérebro dele está "travado". Quando')
f.rep('t| DigitalOcean\nt| | DigitalOcean\nt| Domo\nt| paths.grasp.study\nt| | Grasp\n','')
f.rep('t| dokumen.pub\nt| Medium\nt| | by Sai\nt| | GenAI-LLMs | Medium\n','')
k=f.s.index('li| <strong>Na consequência (b):</strong>'); k2=f.s.index('\n',k)
f.s=f.s[:k2]+'\nli| <strong>Na consequência (c):</strong> O custo da inferência (por uso/tokens) significa que disponibilizar esse chat para 50 pessoas vai custar centavos ou valores muito baixos por mês, ao contrário dos milhões que custaria um treinamento.'+f.s[k2:]
f.rep('t| Essas perguntas servem para ver se ele localiza dados óbvios no texto.','p| Essas perguntas servem para ver se ele localiza dados óbvios no texto.')
f.rep('t| Os funcionários não falam igual ao manual técnico. Vamos ver se a IA entende\nt| gírias e variações.','p| Os funcionários não falam igual ao manual técnico. Vamos ver se a IA entende gírias e variações.')
f.rep('semana passada?"\nt| (Testando se ela associa \'reaver o dinheiro\' com \'reembolso\' e \'Uber\' com\nt| \'transporte\')','semana passada?" (Testando se ela associa \'reaver o dinheiro\' com \'reembolso\' e \'Uber\' com \'transporte\')')
f.rep('o\nt| termo popular para \'abono pecuniário\')','o termo popular para \'abono pecuniário\')')
f.rep('localiza as\nt| regras sobre \'atestado médico\')','localiza as regras sobre \'atestado médico\')')
f.rep('t| Essas são as mais importantes! Elas garantem que a IA não vai inventar respostas\nt| se a informação não estiver no papel.\np| 7.','p| Essas são as mais importantes! Elas garantem que a IA não vai inventar respostas se a informação não estiver no papel.\np| 7.')
f.rep('(Uma pergunta aleatória para garantir que o robô diga educadamente que não sabe e que seu foco é\nt| apenas o RH).','(Uma pergunta aleatória para garantir que o robô diga educadamente que não sabe e que seu foco é apenas o RH).') if False else None
f.rep('foco é\nt| apenas o RH).','foco é apenas o RH).') if False else None
f.s=f.s.replace('seu foco é\nt| apenas o RH).','seu foco é apenas o RH).').replace('educadamente que não sabe e que seu foco é\nt| apenas','educadamente que não sabe e que seu foco é apenas')
f.s=f.s.replace('educadamente que não sabe e que seu foco é apenas o RH).','educadamente que não sabe e que seu foco é apenas o RH).')
f.s=f.s.replace('t| para garantir que o robô diga educadamente que não sabe e que seu foco é\nt| apenas o RH).','(garantir)')
import re
m=re.search(r'^p\| 7\. .*$',f.s,flags=re.M)
line=m.group(0)
rest=f.s[m.end():]
assert rest.startswith('\nt| para garantir')
rest=rest.split('\n',3)  # ['', t1, t2, resto]
new=line+' '+rest[1][3:]+' '+rest[2][3:]
new=re.sub(r' (8|9|10)\. "',lambda mm:'\np| '+mm.group(1)+'. "',new)
f.s=f.s[:m.start()]+new+'\n'+rest[3]
f.rep('como a Inteligência\np| Artificial funciona:','como a Inteligência Artificial funciona:')
f.numbered()
f.t_to_h()
f.save('res56.fixed.txt')
