"""Trechos ```...``` digitados na conversa (transcrição react-pdf): recupera o recuo pelo XML
e troca, na ordem, as regiões 'p| ```lang' ... 'p| ```' do markup por um bloco code:/endnote:."""
import re
from xmlq import load
def fences(xml, md):
    L=[l[4] for l in load(xml)]
    blocos=[];i=0
    while i<len(L):
        if L[i].strip().startswith('```') and len(L[i].strip())>3 or L[i].strip()=='```' and False:
            j=i+1; b=[L[i].rstrip()]
            while j<len(L) and not L[j].rstrip().endswith('```'): b.append(L[j].rstrip()); j+=1
            b.append(L[j].rstrip()); blocos.append(b); i=j
        i+=1
    out=[];M=md.split('\n');i=0;k=0
    while i<len(M):
        if M[i].startswith('p| ```') and len(M[i].strip())>6:
            j=i
            while not (j>i and M[j].rstrip().endswith('```')): j+=1
            out+=['code:']+['c| '+x for x in blocos[k]]+['endnote:']; k+=1; i=j+1; continue
        out.append(M[i]); i+=1
    assert k==len(blocos),(k,len(blocos))
    return '\n'.join(out)

def recuo(xml, md):
    """Devolve o recuo do XML às linhas c| (casamento sequencial pelo texto sem espaços)."""
    L=[l[4] for l in load(xml)]
    norm=lambda x: re.sub(r'\s+',' ',x).strip()
    N=[norm(x) for x in L]; p=0; out=[]
    for ln in md.split('\n'):
        if ln.startswith('c|') and norm(ln[2:]):
            k=norm(ln[2:])
            for q in range(p,min(len(N),p+400)):
                if N[q]==k:
                    ln='c| '+L[q].rstrip(); p=q+1; break
        out.append(ln)
    return '\n'.join(out)

def nulos(md):
    """Cabeçalhos de turno partidos pelo parse_rp ('\\x00Nome|00:00'): devolve o texto ao turno anterior."""
    md=re.sub(r'\n@turn ([^\n]*?)\x00([^\n|]+\|\d\d:\d\d)', lambda m: ' '+m.group(1)+'\n@turn '+m.group(2), md)
    md=re.sub(r'\x00([^\n|]+\|\d\d:\d\d)', r'\n@turn \1', md)
    return md
