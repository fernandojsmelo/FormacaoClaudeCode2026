import re
s=open('rp56.e.txt',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
s=s.replace(' =€',' 🚀')
L=s.split('\n'); i=[k for k,l in enumerate(L) if l.startswith('p| CaracterísticaTreinamento')][0]
cut=lambda t,b: t.split(b,1)
rows=[]
for k,(nome,b) in enumerate([('O que é?','O processo de conversar'),('Frequência','Feito toda vez'),('Custo','Baixíssimo'),('Atualização','Não altera')],1):
    t=L[i+k][3:]; assert t.startswith(nome),(t[:30]); t=t[len(nome):]
    a,c=t.split(b,1); rows.append(f'tr| {nome} | {a.strip()} | {b}{c}')
L[i:i+5]=['th| Característica | Treinamento do Modelo (Training) | Uso do Modelo (Inferência / Prompting)']+rows
s='\n'.join(L)
rep(' 4. A IA lê aquilo','\np| 4. A IA lê aquilo'); rep(' 6. "Passando mal','\np| 6. "Passando mal'); rep(' 7. "A empresa reembolsa','\np| 7. "A empresa reembolsa')
open('rp56.fixed.txt','w',encoding='utf-8').write(s)
print([l[:70] for l in s.split('\n') if re.search(r'[=<>][^\s\w"\'(){}\[\].,:=<>*+|-]|\x00',l)])
