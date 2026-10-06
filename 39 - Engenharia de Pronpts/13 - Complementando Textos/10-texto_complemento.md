```python
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API"),  # This is the default and can be omitted
)
```

### Complemento Textual
- **Expansão de tópicos** → desenvolvimento de pontos em parágrafos
- **Expansão criativa** → narrativas envolventes
- **Expansão argumentativa** → justificativas sólidas
- **Expansão técnica** → explicações detalhadas e exemplos práticos
- **Expansão de outline** → transformação de estrutura em conteúdo completo

### Expansão de tópicos


```python
system_prompt = """
Você é um especialista em comunicação corporativa.
Expanda tópicos curtos em parágrafos claros que:
1) Desenvolvam cada ideia com exemplos reais
2) Mantenham fluidez e coerência
3) Sejam úteis para profissionais em cargos de liderança
"""

user_prompt = """
Expanda estes tópicos sobre liderança moderna:

• Comunicação transparente
• Gestão de equipes híbridas
• Incentivo à inovação
"""

response_topics = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.5
)

print("\n=== EXPANSÃO DE TÓPICOS ===")
print(response_topics.choices[0].message.content)
```

### Expansão Criativa


```python
system_prompt = """
Você é um escritor criativo. Expanda ideias simples criando:
1) Cenário vívido
2) Personagens interessantes
3) Atmosfera envolvente
"""

user_prompt = """
Expanda esta ideia em uma micro-história:
"Um barista descobre um bilhete misterioso escondido dentro de um saco de café."
"""

response_creative = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.8
)

print("\n=== EXPANSÃO CRIATIVA ===")
print(response_creative.choices[0].message.content)

```

### Expansão Argumentativa


```python
system_prompt = """
Você é um consultor estratégico.
Expanda argumentos básicos incluindo:
1) Justificativas bem fundamentadas
2) Exemplos e dados de apoio
3) Consideração de contrapontos
4) Conclusão persuasiva
"""

user_prompt = """
Expanda este argumento:
"As empresas devem adotar a semana de trabalho de 4 dias."
"""

response_argument = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.3
)

print("\n=== EXPANSÃO ARGUMENTATIVA ===")
print(response_argument.choices[0].message.content)
```

### Expansão Técnica


```python
system_prompt = """
Você é um instrutor técnico especializado em ciência de dados.
Expanda conceitos explicando:
1) Como funciona na prática
2) Exemplos de código quando útil
3) Casos de uso aplicados em empresas
4) Boas práticas de implementação
"""

user_prompt = """
Expanda este conceito técnico:
"Aplicação de modelos preditivos em análise de churn de clientes."
"""

response_technical = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.4
)

print("\n=== EXPANSÃO TÉCNICA ===")
print(response_technical.choices[0].message.content)

```

### Expansão de Outline


```python
outline_prompt = """
Expanda este outline em um artigo curto e completo:

TÍTULO: "Tendências em Educação Digital para 2026"

OUTLINE:
1. Introdução - Acelerando a transformação educacional
2. Plataformas personalizadas de aprendizagem
3. Realidade aumentada e gamificação
4. Aprendizado contínuo para profissionais
5. Desafios e riscos
6. Conclusão - O futuro da educação
"""

response_outline = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": outline_prompt}],
    temperature=0.6
)

print("\n=== EXPANSÃO DE OUTLINE ===")
print(response_outline.choices[0].message.content)
```
