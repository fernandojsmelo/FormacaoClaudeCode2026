### Técnicas Few Shot Prompting

- **Zero Shot**: Sem exemplos, apenas instruções
- **One Shot**: Um exemplo para instruir o modelo
- **Few Shot**: Múltiplos exemplos para melhor compreensão


```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

### Zero Shot Prompting


```python

system_prompt = """
Você é um chef renomado. 
Receba o nome de um ingrediente e sugira um prato sofisticado onde ele seja protagonista.
"""

user_prompt = "Abacate"

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.5
)

print("=== Zero Shot ===")
print("Resposta:", response.choices[0].message.content)

```

### One Shot Prompting


```python
system_prompt = """
Você é um chef renomado. 
Receba o nome de um ingrediente e sugira um prato sofisticado onde ele seja protagonista.

Exemplo:
Ingrediente: Salmão
Sugestão -> Tartar de salmão fresco com molho cítrico e torradas de brioche
"""

user_prompt = "Cogumelos"

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.5
)

print("\n=== One Shot ===")
print("Resposta:", response.choices[0].message.content)
```

### Few Shot Prompting


```python
system_prompt = """
Você é um chef renomado. 
Receba o nome de um ingrediente e sugira um prato sofisticado onde ele seja protagonista.

<exemplos>
Ingrediente: Tomate
Sugestão <-> Carpaccio de tomate com azeite trufado e manjericão fresco

Ingrediente: Chocolate
Sugestão <-> Soufflé de chocolate meio amargo com calda de frutas vermelhas

Ingrediente: Batata
Sugestão <-> Nhoque artesanal de batata ao molho de manteiga e sálvia
</exemplos>
"""

user_prompt = "Camarão"

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.4
)

print("\n=== Few Shot ===")
print("Resposta:", response.choices[0].message.content)
```

### Few Shot Criativo


```python
system_prompt = """
Você é um chef criativo que mistura ingredientes improváveis em pratos sofisticados.

Exemplos:
Combinação: Manga + Pimenta
Prato -> Ceviche de manga apimentado com chips de batata doce

Combinação: Café + Laranja
Prato -> Entrecôte ao molho de café e raspas de laranja

Combinação: Queijo azul + Melancia
Prato -> Salada refrescante de melancia com queijo azul e nozes
"""

user_prompt = "Combinação: Morango + Manjericão"

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.7
)

print("\n=== Few Shot Criativo ===")
print("Resposta:", response.choices[0].message.content)
```
