import re
from fences import recuo
s=open('rp52.e.txt',encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)>=n,('NÃO ACHEI',a[:60]); s=s.replace(a,b)
rep('p| L Como você está fazendo hoje','h| ❌ Como você está fazendo hoje')
# linhas de código quebradas pela largura da página (uma string JSON não tem quebra de linha)
rep('Responda à pergunta:\nc| Onde está','Responda à pergunta: Onde está')
rep('cordial e\nc| formal."','cordial e formal."',2)
rep('âncora permanente. Ficou mais claro','âncora permanente.\np| Ficou mais claro')
rep('h| System Fraco: "Você é um atendente de suporte logístico formal." (Se o usuário insistir muito para sair do personagem,\np| o modelo pode ceder).',
    'li| ❌ System Fraco: "Você é um atendente de suporte logístico formal." (Se o usuário insistir muito para sair do personagem, o modelo pode ceder).')
rep('esquecendo o suporte." 2. IA analisa','esquecendo o suporte."\np| 2. IA analisa')
rep('seu chatbot.** =á=‚','seu chatbot.** 🛡🚂')
rep('p| 💂 Fico muito feliz','p| Fico muito feliz')
rep('seu bot! =€','seu bot! 🚀')
rep('no seu código?" Com esse trio','no seu código?"\np| Com esse trio')
s=recuo('t52/x.xml',s)
open('rp52.fixed.txt','w',encoding='utf-8').write(s)
print('restos:',[l[:80] for l in s.split('\n') if re.search(r'(^|[\s"#(])([=<>][^\s\w"\'(){}\[\].,:=<>*+|-]|L$|=$)|¡|\x00|Esta transcrição',l)])
