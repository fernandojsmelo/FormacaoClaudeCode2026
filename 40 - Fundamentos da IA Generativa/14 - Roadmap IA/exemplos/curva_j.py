# Todos os numeros sao hipoteticos
investimento_inicial = 60000.0   # integracao, dados, treinamento
custo_mensal = 4000.0            # licencas, tokens, manutencao
ganho_pleno_mensal = 18000.0     # quando todos usam
meses_ate_adocao_plena = 6

acumulado = -investimento_inicial
virada = None
print("mes | adocao | resultado do mes | acumulado")
for mes in range(1, 13):
    adocao = min(mes / meses_ate_adocao_plena, 1.0)
    resultado = ganho_pleno_mensal * adocao - custo_mensal
    acumulado += resultado
    if virada is None and acumulado >= 0:
        virada = mes
    print(f"{mes:>3} | {adocao:>6.0%} | R$ {resultado:>11,.0f} | R$ {acumulado:>9,.0f}")
print("acumulado positivo a partir do mes:", virada)
