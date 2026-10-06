"""faltando.py rpNN.txt rpNN.fixed.txt: linhas do pdftotext que não aparecem no markup final."""
import re, sys
norm = lambda x: re.sub(r'[\W_]+', '', x).lower()
bruto = [l.split('| ', 1)[1] for l in open(sys.argv[1], encoding='utf-8').read().split('\n') if '| ' in l and l[:3] in ('p| ', 'c| ', 'li|', 'h| ')]
final = norm(open(sys.argv[2], encoding='utf-8').read())
falt = [b for b in bruto if len(norm(b)) > 15 and norm(b)[:40] not in final]
print(len(falt), 'linha(s) ausente(s)')
for f in falt[:15]: print('  ', f[:100])
