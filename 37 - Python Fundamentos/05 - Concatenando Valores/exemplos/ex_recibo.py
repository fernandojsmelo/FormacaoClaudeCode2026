# Exercício: recibo com f-strings
cliente = "Ana Souza"
produto = "Curso de Python"
valor = 197
parcelas = 3
print("=" * 32)
print(f"{'RECIBO':^32}")
print("=" * 32)
print(f"Cliente: {cliente}")
print(f"Produto: {produto}")
print(f"Total:   R$ {valor:.2f}")
print(f"{parcelas}x de R$ {valor / parcelas:.2f}")
