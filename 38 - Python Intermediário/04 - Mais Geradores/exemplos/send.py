def media_movel():
    total = quantidade = 0
    media = None
    while True:
        valor = yield media      # recebe o que vier no send()
        total += valor
        quantidade += 1
        media = total / quantidade


m = media_movel()
next(m)                  # avança até o primeiro yield
print(m.send(10))
print(m.send(20))
print(m.send(60))
