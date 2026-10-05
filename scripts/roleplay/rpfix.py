"""Ajudantes comuns para corrigir o markup dos resumos (parse_google)."""
import re
norm=lambda x: re.sub(r'\s+',' ',x).strip()
class Fix:
    def __init__(s,path): s.s=open(path,encoding='utf-8').read().split('\n#cards')[0]
    def rep(s,a,b,n=1):
        assert s.s.count(a)>=n and a, ('NÃO ACHEI', a[:80]); s.s=s.s.replace(a,b)
    def block(s,first,last,new):
        i=s.s.index(first); j=s.s.index(last,i)+len(last); j=s.s.find('\n',j-1) if not last.endswith('\n') else j-1
        if j<0: j=len(s.s)
        s.s=s.s[:i]+new+s.s[j:]
    def pct(s):
        # "... 100 das ...\nt| %" -> "... 100% das ..." (último número da linha; não junta a linha seguinte)
        s.s=re.sub(r'^(.*\d)(\D*)\nt\| %$', lambda m: m.group(1)+'%'+m.group(2), s.s, flags=re.M)
    def code_from(s,rpfile,langs=('python','bash','text','json','javascript','sh','shell','plaintext','typescript','html','css','sql','yaml')):
        """troca cada sequência de c| pelo bloco da transcrição que casa (linhas completas e recuo)."""
        T=open(rpfile,encoding='utf-8').read().split('\n'); TB=[];i=0
        while i<len(T):
            if T[i]=='code:':
                j=i+1
                while j<len(T) and T[j].startswith('c|'): j+=1
                TB.append([x[3:] if x.startswith('c| ') else x[2:] for x in T[i+1:j]]); i=j
            i+=1
        L=s.s.split('\n'); out=[]; i=0; s.sem=[]
        while i<len(L):
            if L[i].startswith('c|') and out and out[-1]=='code:':
                out.append(L[i]); i+=1; continue
            if L[i].startswith('c|') and out and out[-1].startswith('c|'):
                out.append(L[i]); i+=1; continue
            if L[i].startswith('c|'):
                j=i
                while j<len(L) and L[j].startswith('c|'): j+=1
                rb=[x[3:] if x.startswith('c| ') else x[2:] for x in L[i:j]]
                rn=[norm(x) for x in rb if norm(x)]
                achou=None
                for tb in TB:
                    tn=[x for x in tb if x.strip()]
                    if len(tn)==len(rn) and all(norm(t).startswith(r) or norm(re.sub(r'\W','',t)).startswith(norm(re.sub(r'\W','',r))) for r,t in zip(rn,tn)):
                        achou=tn; break
                if out and out[-1][3:].strip() in langs and out[-1].startswith(('t|','li|','p|')): out.pop(); nota=True
                else: nota=False
                if achou:
                    k=0; blk=[]
                    for x in rb:
                        if not x.strip(): blk.append('c| ')
                        else: blk.append('c| '+achou[k]); k+=1
                else:
                    blk=['c| '+x for x in rb]; s.sem.append(rb[0][:60])
                out+=['code:']+blk+['endcode:' if nota else 'endnote:']; i=j; continue
            out.append(L[i]); i+=1
        s.s='\n'.join(out)
    def numbered(s, keep_p=()):
        L=s.s.split('\n'); out=[]; i=0
        while i<len(L):
            l=L[i]
            if re.match(r'p\| \d+\.\s',l):
                if i+1<len(L) and re.match(r'li\| ([a-zà-ú"(]|<code>)',L[i+1]): l+=' '+L[i+1][4:]; i+=1
                if not any(k in l for k in keep_p): l='n| '+re.sub(r'^p\| (\d+)\.\s+',r'\1. ',l)
            out.append(l); i+=1
        s.s='\n'.join(out)
    def t_to_h(s):
        s.s='\n'.join('h| '+l[3:] if l.startswith('t| ') else l for l in s.s.split('\n'))
    def save(s,path):
        left=[l for l in s.s.split('\n') if l.startswith('t|')]
        open(path,'w',encoding='utf-8').write(s.s)
        print(s.s.count('\nq|')+(1 if s.s.startswith('q|') else 0),'perguntas | t| restantes:',len(left),'| código sem par:',getattr(s,'sem',[]))
        for l in left: print('   ',l[:100])

def linhas_codigo_xml(pdf):
    """Remonta as linhas de código (fonte mono) do XML do resumo, com recuo pela coluna e emojis."""
    import subprocess, tempfile, html as H
    from xmlq import load
    t=tempfile.mkdtemp(); subprocess.run(['pdftohtml','-xml','-i','-q',pdf,t+'/x'],check=True)
    L=load(t+'/x.xml')
    grupos={}
    for l in L:
        if 'Mono' in l[3] or 'Noto' in l[3]:
            grupos.setdefault((l[0],l[1]),[]).append(l)
    # junta itens com top até 6 px de diferença (emojis ficam um pouco acima)
    chaves=sorted(grupos); linhas=[]
    for k in chaves:
        if linhas and linhas[-1][0][0]==k[0] and abs(linhas[-1][0][1]-k[1])<=6:
            linhas[-1][1].extend(grupos[k])
        else: linhas.append([k,list(grupos[k])])
    out=[]
    for (pg,top),itens in linhas:
        itens.sort(key=lambda x:x[2])
        if not any('Mono' in i[3] for i in itens): continue
        base=156; cw=9.55; s=''; desloc=0
        for i in itens:
            txt=re.sub(r'</?[ib]>|</?strong>','',i[4])
            col=round((i[2]-base)/cw)-desloc
            if col>len(s): s+=' '*(col-len(s))
            s+=txt
            if 'Noto' in i[3]: desloc+=1   # o emoji ocupa duas colunas no PDF

        out.append(s.rstrip())
    return out

def _code_xml(self,pdf):
    X=linhas_codigo_xml(pdf)
    key=lambda x: ''.join(ch for ch in x if not ch.isspace() and ord(ch)<0x2190 and ch!='\u200d')
    KX=[key(x) for x in X]; p=0; out=[]
    for ln in self.s.split('\n'):
        if ln.startswith('c|') and key(ln[2:]):
            k=key(ln[2:])
            for q in range(p,min(len(X),p+60)):
                if KX[q]==k or (len(k)>8 and KX[q].startswith(k)):
                    ln='c| '+X[q]; p=q+1; break
        out.append(ln)
    self.s='\n'.join(out)
Fix.code_xml=_code_xml

def _headings(self,pdf):
    """Títulos (h|) que perderam palavras em fonte de código: remonta pelo XML e remove as linhas c| soltas."""
    import subprocess, tempfile
    from xmlq import load
    t=tempfile.mkdtemp(); subprocess.run(['pdftohtml','-xml','-i','-q',pdf,t+'/x'],check=True)
    L=load(t+'/x.xml'); grupos=[]
    for l in sorted(L,key=lambda x:(x[0],x[1])):
        if grupos and grupos[-1][0]==l[0] and abs(l[1]-grupos[-1][1])<=12: grupos[-1][2].append(l)
        else: grupos.append([l[0],l[1],[l]])
    # linhas com algum pedaço mono
    cand=[]
    for _,_,it in grupos:
        it=sorted(it,key=lambda x:x[2])
        if any('Mono' in i[3] for i in it) and any('Mono' not in i[3] for i in it):
            txt=''; sem=''
            for i in it:
                c=re.sub(r'</?[ib]>|</?strong>','',i[4])
                if 'Mono' in i[3]: txt+='<code>'+c.strip()+'</code>' if c.strip() else c
                else: txt+=c; sem+=c
            cand.append((re.sub(r'\W','',sem),re.sub(r'\s+',' ',txt).strip()))
    L2=self.s.split('\n'); out=[]; i=0; self.tit=[]
    while i<len(L2):
        l=L2[i]
        if l.startswith('h| ') and i+1<len(L2) and L2[i+1].startswith('c|'):
            j=i+1; extra=[]
            while j<len(L2) and (L2[j].startswith('c|') or L2[j].strip()=='h| ?'):
                extra.append(L2[j]); j+=1
            sem=re.sub(r'\W','',l[3:]+''.join(x[3:] for x in extra if x.startswith('h|')))
            achou=[c for s,c in cand if s==sem]
            if achou:
                out.append('h| '+achou[0].replace('</code> <code>',' ').replace('</code><code>','')); self.tit.append(achou[0]); i=j; continue
        out.append(l); i+=1
    self.s='\n'.join(out)
Fix.headings=_headings
