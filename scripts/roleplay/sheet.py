"""sheet.py arquivo.pdf saida.png: folha de contato (todas as páginas em miniatura) para a checagem visual."""
import sys,glob,subprocess,tempfile,os
from PIL import Image
pdf,out=sys.argv[1:3]
t=tempfile.mkdtemp()
subprocess.run(['pdftoppm','-png','-r','22',pdf,t+'/sh'],check=True)
fs=sorted(glob.glob(t+'/sh-*.png')); ims=[Image.open(f) for f in fs]; w,h=ims[0].size; c=9
S=Image.new('RGB',(c*(w+4),((len(ims)+c-1)//c)*(h+4)),'#666')
for k,i in enumerate(ims): S.paste(i,((k%c)*(w+4),(k//c)*(h+4)))
S.save(out); [__import__('os').remove(f) for f in fs]
