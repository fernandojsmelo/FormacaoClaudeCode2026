idade = 20
tem_ingresso = True
if idade >= 18 and tem_ingresso:
    print("Pode entrar")
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Fim de semana")
if dia in ("sábado", "domingo"):   # o mesmo, mais curto
    print("Fim de semana (com in)")
