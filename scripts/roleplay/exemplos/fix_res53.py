import re
from rpfix import Fix
from links_google import links
P='orig_ResumoRolePlay53.pdf'
f=Fix('res53.txt')
f.headings(P)
# linhas com emoji dentro dos blocos de prompt saíram como t|: devolve ao bloco (c|)
L=f.s.split('\n')
for _ in range(3):
    for k in range(1,len(L)-1):
        if L[k].startswith('t| ') and L[k-1].startswith('c| ') and (L[k+1].startswith('c| ') or L[k+1].startswith('t| ')):
            L[k]='c| '+L[k][3:]
f.s='\n'.join(L)
# exemplos de few-shot
f.rep(' Saída: [🚨',"<br>Saída: [🚨"); f.rep(' Saída: [✨',"<br>Saída: [✨"); f.rep('configurações." Saída:','configurações."<br>Saída:')
f.rep('<code>[</code>🚨 <code>CRÍTICO]</code>','<code>[🚨 CRÍTICO]</code>'); f.rep('<code>[</code>✨ <code>POSITIVO]</code>','<code>[✨ POSITIVO]</code>')
f.rep('<strong>Pense passo a</strong>\nt| passo, mostrando o cálculo de cada etapa antes de dar o\nli| <strong>resultado final.</strong>"',
      '<strong>Pense passo a passo, mostrando o cálculo de cada etapa antes de dar o resultado final.</strong>"')
f.block('t| TécnicaO que ela resolve?','t| da IA.etapas.',
 'th| Técnica | O que ela resolve? | Como você aplica?\n'
 'tr| <strong>Few-Shot</strong> | Formato bagunçado e falta de padrão. | Colando 2 ou 3 exemplos de "Pergunta/Resposta" ideais no prompt.\n'
 'tr| <strong>Chain-of-Thought</strong> | Erros de lógica, matemática e pressa da IA. | Escrevendo "Pense passo a passo" ou criando um exemplo onde a IA resolve o problema em etapas.')
# links da busca da 3ª pergunta
LK=links(P)
f.block('t| Medium\nt| Prompting and Chain','t| Chain of Thought (CoT) Prompting Helps LLMs Reason More ...','\n'.join(f'li| {t} · <em>{s}</em>' for t,s in LK[0]))
f.rep('t| Misturar Few-Shot (exemplos) com Chain-of-Thought (passo a passo) é a\np| <strong>estratégia',
      'p| Misturar Few-Shot (exemplos) com Chain-of-Thought (passo a passo) é a <strong>estratégia')
f.rep('t| Copie e cole este prompt para testar:','p| Copie e cole este prompt para testar:',2)
f.rep('(Few-Shot Chain-of-Thought)</strong> customizado\nt| +\np| e pronto','(Few-Shot + Chain-of-Thought)</strong> customizado e pronto')
f.pct()
f.rep('(1.200 600)','(1.200 + 600)'); f.rep('<code>0.75</code>\nt| +\nli| (margem','<code>0.75</code> (margem')
f.rep('pagando a\nli| infraestrutura','pagando a infraestrutura')
f.rep('ficar 100% automático\np| para você','ficar 100% automático para você') if 'ficar 100% automático\np| para você' in f.s else None
f.rep('q| Dar o critério de uso cuidados honestos: Use few-shot\nt| +\nq| quando','q| Dar o critério de uso + cuidados honestos: Use few-shot quando')
f.rep('(Garbage In, Garbage Out). <strong>A Ilusão','(Garbage In, Garbage Out).\nli| <strong>A Ilusão')
f.rep('até a próxima! 🚀👊 Quando você terminar','até a próxima! 🚀👊\np| Quando você terminar')
f.rep('(Sem\nt| Errar Logística)','(Sem Errar Logística)')
f.rep('(Lógica\nt| +\nt| Formato)','(Lógica + Formato)'); f.rep('(Métricas\nt| +\nt| Relatório)','(Métricas + Relatório)')
f.s=f.s.replace('📈','🚀')
f.rep('Few-Shot  Chain-of-Thought','Few-Shot &amp; Chain-of-Thought')
f.code_xml(P)
f.code_from('rp53.fixed.txt')
f.s=f.s.replace('📈','🚀')
f.numbered()
f.t_to_h()
f.save('res53.fixed.txt')
print(f.s.count('\nq| ')+f.s.startswith('q| '),'perguntas'); print([len(x) for x in LK])
