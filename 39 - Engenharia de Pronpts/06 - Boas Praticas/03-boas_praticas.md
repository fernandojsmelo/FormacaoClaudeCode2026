### Boas Práticas em Promtps

- Use Prompts específicos
- Instruções Precisas e Detalhadas
- Controle o formato da resposta
- Use separadores para organizar informações


```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

### Use Prompts Específicos


```python
# Prompt vago
prompt_vago = "Fale sobre café"

response_vago = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Você é um especialista em gastronomia."},
        {"role": "user", "content": prompt_vago}
    ],
    temperature=0.7,
    max_completion_tokens=400
)
print("Prompt vago:")
print(f"Resposta: {response_vago.choices[0].message.content}\n")
```


```python
# Prompt específico
prompt_especifico = "Liste e explique 3 métodos de preparo de café que realçam diferentes sabores."

response_especifico = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Você é um especialista em gastronomia."},
        {"role": "user", "content": prompt_especifico}
    ],
    temperature=0.7,
    max_completion_tokens=400
)
print("Prompt com verbo específico:")
print(f"Resposta: {response_especifico.choices[0].message.content}\n")
```

### Instruções Precisas e Detalhadas


```python
# Instrução genérica
prompt_generico = "Escreva sobre viagens na Europa"

response_generico = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Você é um guia de viagens."},
        {"role": "user", "content": prompt_generico}
    ],
    temperature=0.7,
    max_completion_tokens=400
)
print("Instrução genérica:")
print(f"Resposta: {response_generico.choices[0].message.content}\n")
```


```python
# Instrução detalhada
prompt_detalhado = """Monte um roteiro de 5 dias para Paris.
Cada dia deve conter: (1) ponto turístico principal, 
(2) atividade gastronômica e (3) sugestão de transporte."""

response_detalhado = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Você é um guia de viagens especializado em roteiros práticos."},
        {"role": "user", "content": prompt_detalhado}
    ],
    temperature=0.7,
    max_completion_tokens=400
)
print("Instrução detalhada:")
print(f"Resposta: {response_detalhado.choices[0].message.content}\n")

```

### Controlando o Formato da Resposta


```python
# Sem limite de formato
prompt_sem_limite = "Quais são frutas tropicais famosas?"

response_sem_limite = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Você é um nutricionista que fala sobre alimentos."},
        {"role": "user", "content": prompt_sem_limite}
    ],
    temperature=0.7,
    max_completion_tokens=400
)
print("Sem limite de formato:")
print(f"Resposta: {response_sem_limite.choices[0].message.content}\n")

```


```python
# Com limite de formato
prompt_com_limite = """Liste exatamente 4 frutas tropicais.
Use o formato:
- [Nome]: [1 benefício nutricional em uma frase]"""

response_com_limite = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Você é um nutricionista e deve seguir o formato solicitado."},
        {"role": "user", "content": prompt_com_limite}
    ],
    temperature=0.7,
    max_completion_tokens=400
)
print("Com limite de formato:")
print(f"Resposta: {response_com_limite.choices[0].message.content}\n")
```

### Usando Separadores


```python
# Sem delimitadores
prompt_sem_delimitadores = """
Analise o desempenho de uma startup: 
Receita 2022: R$ 2M, Receita 2023: R$ 3.5M, Receita 2024: R$ 5M.
Faça observações e dê sugestões.
"""

response_sem_delimitadores = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Você é um consultor de negócios."},
        {"role": "user", "content": prompt_sem_delimitadores}
    ],
    temperature=0.7,
    max_completion_tokens=800
)
print("Sem delimitadores:")
print(f"Resposta: {response_sem_delimitadores.choices[0].message.content}\n")
```


```python
# Com delimitadores
prompt_com_delimitadores = """
Analise os seguintes dados de receita anual:

--- DADOS ---
2022: R$ 2M
2023: R$ 3.5M
2024: R$ 5M
--- FIM DADOS ---

TAREFA: Identifique o ritmo de crescimento e sugira 2 estratégias de expansão.
"""

response_com_delimitadores = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Você é um consultor de negócios e deve considerar apenas os dados entre os delimitadores."},
        {"role": "user", "content": prompt_com_delimitadores}
    ],
    temperature=0.7,
    max_completion_tokens=800
)
print("Com delimitadores:")
print(f"Resposta: {response_com_delimitadores.choices[0].message.content}\n")

```

### Juntando Tudo


```python
print("## Exemplo 5: Combinação de Princípios\n")

system_prompt = """
Você é um estrategista de marketing criativo.
Sempre siga o formato solicitado e use linguagem clara e objetiva.
"""

user_prompt = """
TAREFA: Criar um mini plano de marketing para lançamento de um aplicativo fitness.

--- INFORMAÇÕES ---
Público: jovens de 18-30 anos
Orçamento: R$ 50.000
Objetivo: 10.000 downloads no primeiro mês
--- FIM ---

FORMATO DA RESPOSTA:
1. POSICIONAMENTO (2 frases)
2. CANAIS DE MARKETING (3 itens numerados)
3. AÇÃO CRIATIVA PRINCIPAL (1 frase)
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.6,
    max_completion_tokens=800
)

print("Resposta final:")
print(response.choices[0].message.content)
```
