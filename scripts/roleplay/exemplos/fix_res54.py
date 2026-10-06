import re
from rpfix import Fix
P='orig_ResumoRolePlay54.pdf'
f=Fix('res54.txt')
f.headings(P)
f.rep('Correção ramatical\nt| G\n','Correção Gramatical\n')
f.rep('t| Few-shot promptingé uma técnica de engenharia de prompt onde você\nt| ensina a inteligência artificial a realizar uma tarefa fornecendo alguns exemplos\np| de respostas certas',
      'p| <strong>Few-shot prompting</strong> é uma técnica de engenharia de prompt onde você ensina a inteligência artificial a realizar uma tarefa fornecendo alguns exemplos de respostas certas')
# chips/cards de fontes da interface
f.rep('t| 4ED Escola de Design\nt| | Engenharia de Prompt\n','')
br=lambda t: re.sub(r' (Sentimento:|Gíria de TI:)', r'<br>\1', t)
f.rep('li| Frase: "Simplesmente incrível, superou minhas expectativas." Sentimento: [POSITIVO] Frase:',
      'li| Frase: "Simplesmente incrível, superou minhas expectativas." Sentimento: [POSITIVO]\nli| Frase:')
f.rep('Código: BR Japão','Código: BR\nli| Japão'); f.rep('Código: JP França','Código: JP\nli| França')
f.s='\n'.join(br(l) if l.startswith('li| Frase: "') or l.startswith('li| Termo:') else l for l in f.s.split('\n'))
f.rep('t| Resposta da IA:Capital: Roma | Código: IT','li| <strong>Resposta da IA:</strong> <code>Capital: Roma | Código: IT</code>')
f.rep('e- mail"','e-mail"')
f.rep('t| Resposta da IA:"Dar shutdown no sistema para manutenção\nc| preventiva"','li| <strong>Resposta da IA:</strong> "Dar shutdown no sistema para manutenção preventiva"')
f.s=f.s.replace(' <strong>Frase corrigida:</strong>','<br><strong>Frase corrigida:</strong>').replace(' <strong>Explicação:</strong>','<br><strong>Explicação:</strong>')
f.s=re.sub(r'^(li|p)\|<br>', r'\1| ', f.s, flags=re.M)
f.rep('(eu). <strong>Frase original:</strong> "Aonde você comprou esse livro novo?"\nt| Frase corrigida:',
      '(eu).\nli| <strong>Frase original:</strong> "Aonde você comprou esse livro novo?"<br><strong>Frase corrigida:</strong>')
f.rep('t| Resposta da IA:\nli|','p| <strong>Resposta da IA:</strong>\nli|')
f.code_xml(P)
f.code_from('rp54.fixed.txt')
f.numbered()
f.t_to_h()
f.save('res54.fixed.txt')
print(f.s.count('\nq| ')+f.s.startswith('q| '),'perguntas')
