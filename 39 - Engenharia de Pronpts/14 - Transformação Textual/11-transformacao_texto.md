```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

- **Transformação de formato** → mudança de estrutura
- **Transformação de tom** → ajuste de estilo
- **Transformação de perspectiva** → mudança de ponto de vista
- **Adaptação para público** → linguagem adequada ao leitor

### Transformação de Formato


```python
system_prompt = """
Você é um especialista em formatação de conteúdo.
Transforme textos entre diferentes estruturas garantindo:
1) Clareza
2) Preservação das informações originais
3) Boa organização
"""

user_prompt = """
Transforme este parágrafo em uma receita passo a passo:

"Para preparar um bom café gelado, você deve moer grãos de café fresco, preparar um café forte,
deixar esfriar, adicionar gelo em um copo alto e completar com leite ou creme a gosto.
Finalize com um toque de açúcar ou xarope de baunilha."
"""

response_format = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.3
)

print("=== RESULTADO (Formato) ===")
print(response_format.choices[0].message.content)
```

### Transformação de Tom


```python
system_prompt = """
Você é um especialista em adaptação de estilo.
Transforme textos mudando o tom sem perder o sentido.
"""

user_prompt = """
Transforme este texto jornalístico em um post leve para redes sociais:

"A cidade de Lisboa recebeu mais de 4 milhões de turistas em 2024,
consolidando-se como um dos destinos mais procurados da Europa."
"""

response_tone = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.6
)

print("\n=== RESULTADO (Tom) ===")
print(response_tone.choices[0].message.content)
```

### Transformação de Ponto de Vista


```python
system_prompt = """
Você é um especialista em narrativa.
Reescreva o texto mudando o ponto de vista.
"""

user_prompt = """
Transforme de primeira para terceira pessoa:

"Eu viajei para o Japão pela primeira vez em 2023 e fiquei impressionado
com a mistura de tradição e tecnologia em Tóquio."
"""

response_perspective = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.4
)

print("\n=== RESULTADO (Perspectiva) ===")
print(response_perspective.choices[0].message.content)
```

### Múltiplas Transformações


```python
texto_original = """
"O restaurante Verde Sabor lançou um cardápio 100% sustentável,
com ingredientes locais, redução de plástico e incentivo a fornecedores regionais.
A proposta busca unir gastronomia, saúde e responsabilidade ambiental."
"""

print("=== TEXTO ORIGINAL ===")
print(texto_original)

# %%
# Versão para negócios
business_prompt = f"""
Reescreva este texto para empresários do setor de alimentação, 
focando em inovação e competitividade:\n\n{texto_original}"""

response_business = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": business_prompt}],
    temperature=0.5
)

print("\n=== VERSÃO PARA NEGÓCIOS ===")
print(response_business.choices[0].message.content)
```
