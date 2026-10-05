"""Listas "Confira os principais resultados da Web..." de um resumo do Modo IA do Google.
Uso: links_google.py ResumoRolePlayNN.pdf  -> imprime cada seção como linhas 'li| Título · <em>Fonte</em>'.
Como módulo: links(pdf) -> [[(titulo, fonte), ...], ...] na ordem das seções."""
import os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xmlq import load
TABS = {'Tudo', 'Imagens', 'Vídeos', 'Notícias', 'Mais', 'Modo IA', 'Shopping', 'Vídeos curtos'}
def links(pdf):
    t = tempfile.mkdtemp(); subprocess.run(['pdftohtml', '-xml', '-i', '-q', pdf, t + '/x'], check=True)
    L = load(t + '/x.xml'); secs = []; cur = None
    for i, l in enumerate(L):
        if l[4].startswith('Confira os principais'): cur = []; secs.append(cur); continue
        if cur is None: continue
        # nome da fonte: linha seguida, na mesma altura, por "· https://..."
        viz = [m for m in L if m[0] == l[0] and m[1] == l[1] and m[4].startswith('· http')]
        if viz and l[2] < viz[0][2] and not l[4].startswith('·'):
            nxt = [m for m in L if m[0] == l[0] and abs(m[1] - (l[1] + 33)) <= 3 and m[2] >= 140 and not (m[1] in (88, 89) and m[4].strip() in TABS)]
            if not nxt: nxt = [m for m in L if m[0] == l[0] + 1 and 40 <= m[1] <= 48 and m[2] >= 140 and m[4].strip() not in TABS]
            title = ''.join(m[4] for m in sorted(nxt, key=lambda m: m[2])).strip()
            cur.append((title, l[4].strip()))
    return secs
if __name__ == '__main__':
    for n, s in enumerate(links(sys.argv[1])):
        print(f'# seção {n + 1}: {len(s)} links')
        for t, f in s: print(f'li| {t} · <em>{f}</em>')
