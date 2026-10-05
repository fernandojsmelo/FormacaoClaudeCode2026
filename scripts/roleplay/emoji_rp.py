"""Emojis quebrados do react-pdf: acha no XML, sugere pelo resumo e aplica no markup.
Uso: emoji_rp.py tNN/x.xml resNN.txt rpNN.in.txt rpNN.out.txt [ESCOLHAS: 'trecho=emoji' ...]"""
import re,sys
from xmlq import load
HI={'=':0xD83D,'<':0xD83C,'>':0xD83E}
def cand(hi,ch):
    if not ch: return []
    lo=ch.encode('cp1252')[0]
    return [chr(0x10000+((HI[hi]-0xD800)<<10)+(b+lo-0xDC00)) for b in (0xDC00,0xDD00,0xDE00,0xDF00)]
xmlf,resf,inf,outf=sys.argv[1:5]
force=dict(a.split('=',1) for a in sys.argv[5:])
L=load(xmlf); res=open(resf,encoding='utf-8').read(); md=open(inf,encoding='utf-8').read()
achados=[]
for i,l in enumerate(L):
    t=l[4]; m=re.match(r'^([=<>])(\S?)$',t)
    if m and i+1<len(L):
        achados.append((m.group(1),m.group(2),L[i+1][4].strip()))
    m=re.match(r'^([¡])\s(.*)',t)
    if m: achados.append(('','¡',m.group(2).strip()))
for hi,lo,txt in achados:
    chave=txt[:40]
    cs=cand(hi,lo) if hi else ['⚡','➡']
    esc=None; fonte=''
    for k,v in force.items():
        if k in txt: esc=v; fonte='manual'
    if not esc:
        m=re.search(r'(\S+)\s+'+re.escape(chave[:25]),res)
        if m and (not hi or m.group(1) in cs or not lo): esc=m.group(1); fonte='resumo'
    if not esc and hi and not lo: fonte='?? byte invisível'
    elif not esc: esc=cs[0]; fonte='padrão U+1F4xx de '+''.join(cs)
    n=md.count(chave)
    if esc and n:
        md=re.sub(r'^((?:h|p|li)\| )(?=.{0,3}'+re.escape(chave)+')',lambda m:m.group(1)+esc+' ',md,count=1,flags=re.M)
    print(f'{esc or "??"}  [{fonte}] {txt[:60]}  (no markup: {n})')
open(outf,'w',encoding='utf-8').write(md)
