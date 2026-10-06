import re
from rpfix import Fix
f=Fix('res59.txt')
f.pct()
f.rep('t| Abordagem "Plugar e Usar" (Alto\nt| risco de falha)Abordagem Estruturada (Sucesso na adoção)\nt| Esperar que a equipe descubra o queIdentificar os casos de uso específicos de cada\nt| fazer sozinha.área.\nt| Assumir que todos sabem interagirOferecer treinamento de engenharia de\nt| com a IA.prompt e curadoria de IA.\nt| Confiar no bom senso para segurançaCriar políticas claras de governança e\nt| de dados.segurança.\nt| Medir o sucesso pelo número deMedir o sucesso pelo tempo economizado ou\nt| contas criadas.qualidade entregue.\n',
 'th| Abordagem "Plugar e Usar" (Alto risco de falha) | Abordagem Estruturada (Sucesso na adoção)\ntr| Esperar que a equipe descubra o que fazer sozinha. | Identificar os casos de uso específicos de cada área.\ntr| Assumir que todos sabem interagir com a IA. | Oferecer treinamento de engenharia de prompt e curadoria de IA.\ntr| Confiar no bom senso para segurança de dados. | Criar políticas claras de governança e segurança.\ntr| Medir o sucesso pelo número de contas criadas. | Medir o sucesso pelo tempo economizado ou qualidade entregue.\n')
f.rep('t| Custo porCusto por\nt| UsuárioUsuárioMínimo de\nt| Ferramenta(Mensal)(Anual)PessoasDetalhe de Privacidade\nt| ChatGPTUS$ 25US$ 20A partir deDados protegidos por\nt| Business2 usuáriospadrão (não treinam a IA).\nt| Central de controle do\nt| chefe.\nt| Claude TeamUS$ 25US$ 20A partir deDados protegidos por\nt| 5 usuáriospadrão. Permite criar pastas\nt| de projetos compartilhados.\n',
 'th| Ferramenta | Custo por Usuário (Mensal) | Custo por Usuário (Anual) | Mínimo de Pessoas | Detalhe de Privacidade\ntr| ChatGPT Business | US$ 25 | US$ 20 | A partir de 2 usuários | Dados protegidos por padrão (não treinam a IA). Central de controle do chefe.\ntr| Claude Team | US$ 25 | US$ 20 | A partir de 5 usuários | Dados protegidos por padrão. Permite criar pastas de projetos compartilhados.\n')
f.rep('(Custo: US$ 50/mês)</strong>\nt| ~\n','(Custo: ~US$ 50/mês)</strong>\n')
f.rep('t| Riseup Labs\nt| claude.com\nt| & Pricing | Claude by Anthropic\nt| Coworker AI\n','')
f.rep('para gerar engajamento imediato\nt| ⚡\n','para gerar engajamento imediato ⚡\n')
f.numbered()
f.save('res59.fixed.txt')
