import re
s=open('rp57.e.txt',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
rep('p| 📍 Como posso','p| Como posso')
rep('=u@=Í','🕵️‍♀️🛍'); rep('aqui! (\n','aqui! ✨\n'); rep('Loja]. (\n','Loja]. ✨\n') if '[Nome da Loja]. (\n' in s else None
rep('vinda à [Nome da Loja]! >','vinda à [Nome da Loja]! 🤍'); rep('sua dúvida hoje? =G','sua dúvida hoje? 👇')
rep('h| 💬 Nota:','p| 💬 Nota:')
s=s.replace('li| =« ','li| 🚫 '); rep('li| =° Custo Total Estimado: ~R$ 315,00 / mês','li| 💰 Custo Total Estimado: ~R$ 315,00 / mês')
rep('Directamente na prática','Diretamente na prática')
rep('h| Teste 1:','h| 🕵️‍♀️ Teste 1:'); rep('h| Vale a pena?','h| ⚖️ Vale a pena?'); rep('p| Setor Aéreo','p| ✈️ Setor Aéreo')
rep(' 2. Operações e Análise de Dados (O cérebro do negócio)','\np| 2. Operações e Análise de Dados (O cérebro do negócio)')
rep(' 3. Marketing e Criação em Escala (A linha de produção)','\np| 3. Marketing e Criação em Escala (A linha de produção)')
rep(' 4. Configure a regra de ouro','\np| 4. Configure a regra de ouro')
L=s.split('\n'); i=[k for k,l in enumerate(L) if l.startswith('p| CenárioAtendimento')][0]
a=L[i+1][3:]; b=L[i+2][3:]; ia1=L[i+3][3:]; c=L[i+4][3:]; d=L[i+5][3:]; ia2=L[i+6][3:]
n1,c1=a.split('Cliente: ',1); robo1,c2=b.split('(Fim da interação).',1)
n2,c3=c.split('Cliente: ',1); robo2,c4=d.split('Cliente: ',1)
rows=['th| Cenário | Atendimento Tradicional / Robô Antigo | Com IA Generativa Bem Configurada',
 f'tr| {n1} | Cliente: {c1}⏎{robo1.strip()} (Fim da interação). | {c2.strip()}⏎{ia1}',
 f'tr| {n2} | Cliente: {c3}⏎{robo2.strip()} | Cliente: {c4}⏎{ia2}']
L[i:i+7]=rows; s='\n'.join(L)
open('rp57.fixed.txt','w',encoding='utf-8').write(s)
print([l[:70] for l in s.split('\n') if re.search(r'[=<>][^\s\w"\'(){}\[\].,:=<>*+|-]|\x00',l)])
