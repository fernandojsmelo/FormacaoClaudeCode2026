"""emo_res.py x.xml: lista os emojis (fonte NotoColorEmoji) do XML do resumo, com o contexto, para recuperar os da transcrição."""
import sys
from xmlq import load
L=load(sys.argv[1])
for i,l in enumerate(L):
    if 'NotoCol' in l[3]:
        prev=''.join(x[4] for x in L[max(0,i-1):i] if x[0]==l[0])[-30:]
        nxt=L[i+1][4][:45] if i+1<len(L) else ''
        print(l[0],repr(l[4]),'|',repr(prev),'>>',repr(nxt))
