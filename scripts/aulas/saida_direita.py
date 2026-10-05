"""saida_direita.py bNN.html eNN/arquivo.py ...: move a saída da seção para a coluna da direita."""
import re, sys
p = sys.argv[1]; s = open(p).read()
for ex in sys.argv[2:]:
    pat = re.compile(r'(<pre class="code">\{\{CODE:' + re.escape(ex) + r'\}\}</pre>)\n\s*<div class="lbl s" style="margin-top:10px">Saída</div>\n\s*(<pre class="out"[^>]*>\{\{OUT:' + re.escape(ex) + r'\}\}</pre>)\n(\s*</div>\n\s*<div[^>]*>)\n(\s*)<ul class="checklist">')
    m = pat.search(s)
    assert m, ex
    s = s[:m.start()] + m.group(1) + m.group(3) + '\n' + m.group(4) + '<div class="lbl s">Saída</div>\n' + m.group(4) + m.group(2) + '\n' + m.group(4) + '<ul class="checklist" style="margin-top:10px">' + s[m.end():]
open(p, 'w').write(s)
