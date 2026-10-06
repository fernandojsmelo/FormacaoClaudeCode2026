```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

### Análise Textual 1 - Cores e Ambientes


```python
system_prompt = """
Você é um especialista em análise visual. Dada uma descrição de imagem, identifique:
1. Paleta de cores dominante
2. Clima ou atmosfera sugerida
3. Elementos de cenário
"""

user_prompt = """
Descrição:

"Uma praia ao entardecer, com o céu em tons de laranja e roxo,
ondas suaves batendo na areia clara e algumas gaivotas voando no horizonte."
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.3
)

print("=== RESULTADO (Cores e Ambientes) ===")
print(response.choices[0].message.content)
```

### Análise Textual 2 - Objetos e Elementos


```python
system_prompt = """
Você é um analista de imagens em texto. Identifique:
1. Objetos principais
2. Relações entre eles
3. Elementos secundários
"""

user_prompt = """
Descrição:

"Um escritório moderno com uma mesa de madeira, um laptop aberto,
uma xícara de café fumegante e uma estante cheia de livros ao fundo."
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.4
)

print("=== RESULTADO (Objetos e Elementos) ===")
print(response.choices[0].message.content)
```

### Análise Textual 3 - Análise Simbólica


```python
system_prompt = """
Você é um especialista em semiótica visual. Interprete:
1. Significados simbólicos dos elementos
2. Possíveis metáforas
3. Impacto emocional no observador
"""

user_prompt = """
Descrição:

"Uma vela acesa em meio a uma sala escura,
iluminando apenas um diário aberto e uma fotografia antiga."
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.5
)

print("=== RESULTADO (Análise Simbólica) ===")
print(response.choices[0].message.content)
```

### Análise Comparativa


```python
descricao_a = "Um campo de trigo dourado sob um céu azul claro, com uma árvore solitária no horizonte."
descricao_b = "Uma metrópole movimentada à noite, cheia de arranha-céus iluminados e ruas lotadas."

comparison_prompt = f"""
Compare estas duas descrições de imagens:
1. Diferenças de cores e atmosfera
2. Elementos principais
3. Estilos possíveis
4. Emoções transmitidas

DESCRIÇÃO A: {descricao_a}

DESCRIÇÃO B: {descricao_b}
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": comparison_prompt}
    ],
    temperature=0.4
)

print("=== RESULTADO (Análise Comparativa) ===")
print(response.choices[0].message.content)
```
