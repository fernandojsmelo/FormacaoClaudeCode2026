saldo = 1000.0
meses = 0
while saldo < 2000:
    saldo *= 1.01        # 1% ao mês
    meses += 1
print(f"{meses} meses para dobrar: R$ {saldo:.2f}")
