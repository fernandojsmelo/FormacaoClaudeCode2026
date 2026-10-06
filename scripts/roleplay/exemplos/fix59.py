import re
s=open('rp59.e.txt',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
rep('=4 Vermelho','🔴 Vermelho'); rep('=á Amarelo','🟡 Amarelo')
# tabela 1
rep('p| Abordagem "Plugar e Usar" (Alto risco de falha)Abordagem Estruturada (Sucesso na adoção)\n'
 'p| Esperar que a equipe descubra o que fazer sozinha.Identificar os casos de uso específicos de cada área.\n'
 'p| Assumir que todos sabem interagir com a IA.Oferecer treinamento de engenharia de prompt e curadoria de IA.\n'
 'p| Confiar no bom senso para segurança de dados.Criar políticas claras de governança e segurança.\n'
 'p| Medir o sucesso pelo número de contas criadas.Medir o sucesso pelo tempo economizado ou qualidade entregue.\n',
 'th| Abordagem "Plugar e Usar" (Alto risco de falha) | Abordagem Estruturada (Sucesso na adoção)\n'
 'tr| Esperar que a equipe descubra o que fazer sozinha. | Identificar os casos de uso específicos de cada área.\n'
 'tr| Assumir que todos sabem interagir com a IA. | Oferecer treinamento de engenharia de prompt e curadoria de IA.\n'
 'tr| Confiar no bom senso para segurança de dados. | Criar políticas claras de governança e segurança.\n'
 'tr| Medir o sucesso pelo número de contas criadas. | Medir o sucesso pelo tempo economizado ou qualidade entregue.\n')
# tabela 2
i=s.index('p| FerramentaCusto por Usuário'); j=s.index('p| Como o seu projeto pode')
s=s[:i]+('th| Ferramenta | Custo por Usuário (Mensal) | Custo por Usuário (Anual) | Mínimo de Pessoas | Detalhe de Privacidade\n'
 'tr| ChatGPT Business | US$ 25 | US$ 20 | A partir de 2 usuários | Dados protegidos por padrão (não treinam a IA). Central de controle do chefe.\n'
 'tr| Claude Team | US$ 25 | US$ 20 | A partir de 5 usuários | Dados protegidos por padrão. Permite criar pastas de projetos compartilhados.\n')+s[j:]
# itens numerados que grudaram
rep('"Pessoal, a ferramenta','"Pessoal, a ferramenta')
s=re.sub(r'(passar vergonha com dados errados\.") 3\. ',r'\1\np| 3. ',s)
s=re.sub(r'(faça essa amarração no processo:) 1\. ',r'\1\np| 1. ',s)
open('rp59.fixed.txt','w',encoding='utf-8').write(s)
print([l[:70] for l in s.split('\n') if re.search(r'[=<>][^\s\w"\'(){}\[\].,:=<>*+|-]|\x00',l)])
