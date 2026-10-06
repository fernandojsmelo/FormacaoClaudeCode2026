# Todos os numeros abaixo sao hipoteticos: troque pelos da sua empresa
atendentes = 20
tickets_por_atendente_mes = 400
minutos_por_ticket = 12
custo_hora = 35.0            # R$ por hora, com encargos
ganho_tempo = 0.20           # 20% menos tempo com um assistente de IA

horas_mes = atendentes * tickets_por_atendente_mes * minutos_por_ticket / 60
economia_mes = horas_mes * ganho_tempo * custo_hora
custo_ferramenta_mes = atendentes * 120.0   # licenca por pessoa
custo_implantacao = 30000.0                 # integracao e treinamento

ganho_liquido = economia_mes - custo_ferramenta_mes
print(f"horas de atendimento por mes: {horas_mes:,.0f}")
print(f"economia bruta por mes:       R$ {economia_mes:,.0f}")
print(f"custo da ferramenta por mes:  R$ {custo_ferramenta_mes:,.0f}")
print(f"ganho liquido por mes:        R$ {ganho_liquido:,.0f}")
print(f"payback: {custo_implantacao / ganho_liquido:.1f} meses")

print("\nSe o ganho de tempo for menor:")
for g in (0.05, 0.10, 0.20):
    liquido = horas_mes * g * custo_hora - custo_ferramenta_mes
    texto = (f"{custo_implantacao / liquido:.1f} meses"
             if liquido > 0 else "nao se paga")
    print(f"  ganho de {g:.0%}: payback {texto}")
