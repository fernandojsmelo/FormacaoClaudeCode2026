s = open("rp41.c.txt", encoding="utf-8").read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:60])
    s = s.replace(a, b)
rep("segurança para a IA seguir. 3. A Engrenagem: JSON-RPC e Stdio",
    "segurança para a IA seguir.\np| 3. A Engrenagem: JSON-RPC e Stdio")
rep("Elas já vêm formatadas ou eu mesma\n@turn tenho que criar essas mensagens do zero?\x00Você|02:29",
    "Elas já vêm formatadas ou eu mesma tenho que criar essas mensagens do zero?\n@turn Você|02:29")
rep("faz um JSON.parse(). 4. O Reconhecimento Automático:",
    "faz um JSON.parse().\np| 4. O Reconhecimento Automático:")
open("rp41.fixed.txt", "w", encoding="utf-8").write(s)
print("ok")
