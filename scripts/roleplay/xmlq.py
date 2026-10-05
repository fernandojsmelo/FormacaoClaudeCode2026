"""xmlq.py: lê o XML do pdftohtml (load) e mostra trechos (python3 xmlq.py x.xml "texto" ...)."""
import re,html,sys
def load(path):
    x=open(path,encoding='utf-8').read()
    fonts=dict(re.findall(r'<fontspec id="(\d+)" size="[^"]*" family="([^"]*)"',x))
    L=[]
    for pg in re.finditer(r'<page number="(\d+)"(.*?)</page>',x,re.S):
        for m in re.finditer(r'<text top="(\d+)" left="(\d+)" width="\d+" height="\d+" font="(\d+)">(.*?)</text>',pg.group(2)):
            t=html.unescape(re.sub(r'<a [^>]*>|</a>','',m.group(4))).replace('<b>','<strong>').replace('</b>','</strong>')
            L.append((int(pg.group(1)),int(m.group(1)),int(m.group(2)),fonts[m.group(3)],t))
    return L
def show(L,key,b=2,a=10):
    for i,l in enumerate(L):
        if key in l[4]:
            for j in range(max(0,i-b),min(len(L),i+a)): print(L[j][:3],L[j][3][:14],repr(L[j][4][:110]))
            print('--'); return
    print('NÃO ACHEI',key)
if __name__=='__main__':
    L=load(sys.argv[1])
    for k in sys.argv[2:]: show(L,k)
