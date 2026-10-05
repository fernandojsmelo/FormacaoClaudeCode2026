import re

post = "Lançou! #python #regex custa R$ 49,90 ou 3x de 18,00"

print(re.findall(r"#\w+", post))               # hashtags
print(re.findall(r"\d+,\d{2}", post))          # preços
print(re.findall(r"\b\d+x\b", post))           # parcelas
