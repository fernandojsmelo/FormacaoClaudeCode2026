import psycopg2
from openai import OpenAI

# 1. Configuração do cliente de IA (Exemplo utilizando a Groq)
# Mudar de provedor aqui é tão simples quanto alterar o base_url e a api_key
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="SUA_CHAVE_DE_API_AQUI" # Substituir pela chave real obtida no painel do provedor
)

def buscar_historico_cliente(cliente_id):
    """
    Simula a busca de informações do cliente diretamente no banco PostgreSQL.
    """
    try:
        # Configuração da conexão com o seu banco PostgreSQL
        conn = psycopg2.connect(
            host="seu_host.postgres.database.azure.com",
            database="seu_banco",
            user="seu_usuario",
            password="sua_senha"
        )
        cursor = conn.cursor()
        
        # Query simples para trazer os dados relevantes do cliente
        query = """
            SELECT nome, ultimas_compras, status_suporte 
            FROM clientes 
            WHERE id = %s;
        """
        cursor.execute(query, (cliente_id,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if resultado:
            nome, compras, suporte = resultado
            return f"Nome do Cliente: {nome}\nÚltimos Pedidos: {compras}\nStatus de Suporte Atual: {suporte}"
        return "Nenhum histórico encontrado para este cliente."
        
    except Exception as e:
        print(f"Erro ao conectar no PostgreSQL: {e}")
        # Fallback seguro para o caso do banco falhar durante o teste
        return "Erro temporário ao acessar o histórico do cliente."

def responder_cliente(cliente_id, pergunta_usuario):
    """
    Recupera o contexto do banco de dados e gera a resposta utilizando o modelo open source Llama 3.3.
    """
    # Passo 1: Busca o contexto real no PostgreSQL
    contexto_cliente = buscar_historico_cliente(cliente_id)
    
    # Passo 2: Monta a estrutura de mensagens injetando o contexto no 'system prompt'
    mensagens = [
        {
            "role": "system",
            "content": (
                "Você é um assistente de suporte inteligente e cordial integrado ao nosso sistema.\n"
                "Use estritamente as informações fornecidas no contexto abaixo para responder ao cliente de forma personalizada.\n\n"
                f"--- CONTEXTO DO CLIENTE ---\n{contexto_cliente}\n---------------------------"
            )
        },
        {
            "role": "user",
            "content": pergunta_usuario
        }
    ]
    
    # Passo 3: Envia a requisição para a API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # Modelo aberto, rápido, inteligente e barato
        messages=mensagens,
        temperature=0.3 # Baixa temperatura para manter a resposta factual e precisa
    )
    
    return response.choices[0].message.content

# --- Exemplo de Execução ---
if __name__ == "__main__":
    # Exemplo simulando o cliente João (ID 42) perguntando sobre seu pedido
    id_do_usuario_logado = 42
    pergunta = "Quero saber o status do meu último pedido e se ele já foi enviado."
    
    # O sistema processa tudo em background de forma transparente
    resposta_da_ia = responder_cliente(id_do_usuario_logado, pergunta)
    
    print("=== Resposta Gerada pelo Chatbot ===")
    print(resposta_da_ia)
