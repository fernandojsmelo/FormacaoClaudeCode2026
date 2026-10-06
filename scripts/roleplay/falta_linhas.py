"""falta_linhas.py original.pdf markup.txt: lista as linhas do pdftotext do PDF original cujas primeiras e últimas palavras não aparecem no markup.
Encontra texto que o parser perdeu (ex.: a primeira linha de uma página, que o parse_google deixou cair). Ignore os cards de links e rodapés."""
import re,subprocess,sys,html
pdf,new=sys.argv[1:3]
txt=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout
w=lambda s: re.findall(r'\w+',html.unescape(re.sub(r'<[^>]+>','',s)).lower())
N=' '.join(w(open(new,encoding='utf-8').read()))
for l in txt.split('\n'):
    l=l.strip()
    if len(l)<30 or 'google.com/search' in l or re.match(r'^\d\d/\d\d/\d{4}',l): continue
    ws=w(l)
    if len(ws)<5: continue
    g=' '.join(ws[:4]); g2=' '.join(ws[-4:])
    if g not in N and g2 not in N: print(l[:130])
