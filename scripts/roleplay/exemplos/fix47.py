s=open('rp47.e.txt',encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s, a[:70]; s=s.replace(a,b)
def rep_block(first,last,new):
    global s
    i=s.index(first); j=s.index(last,i); j=s.index('\n',j); s=s[:i]+new+s[j:]
rep_block('p| O que é feito hoje (Manual)','p| Levar minutos para conferir',
 'th| O que é feito hoje (Manual) | Como o Python faz (Automatizado) | Impacto Direto no seu Negócio\n'
 'tr| **Digitação e Leitura Visual** ⏎ Um funcionário lê o endereço, o peso ou o tipo de produto e decide a categoria ou transportadora. | **Leitura Digital Direta** ⏎ O script Python extrai os dados diretamente do sistema ou do código de barras instantaneamente. | **Zero erro de digitação** ou leitura trocada. Adeus pacotes enviados para o destino errado.\n'
 'tr| **Decisão Humana Subjetiva** ⏎ O operador precisa lembrar das regras de envio ou olhar uma tabela para classificar cada item. | **Regras de Negócio Fixas** ⏎ O código aplica regras lógicas (Ex: Se peso > 5kg e região = Sudeste, use a Transportadora X). | **Padronização total**. A classificação é feita de forma idêntica e sem hesitação todas as vezes.\n'
 'tr| **Processamento Lento (Um a Um)** ⏎ Levar minutos para conferir, registrar e colar a etiqueta em uma única ordem de envio. | **Processamento em Lote** ⏎ O Python consegue classificar milhares de envios em poucos segundos. | **Ganho brutal de tempo**. O que levava horas ou dias passa a rodar no tempo de um clique.')
rep('falhas na triagem. Para que eu possa','falhas na triagem.\np| Para que eu possa')
rep_block('li| Exemplo prático de Dicionário de Regras:python','p| Use o código com cuidado.',
 'li| Exemplo prático de Dicionário de Regras:\ncode:\n'
 'c| # O Python sabe exatamente para onde vai cada região sem precisar "adivinhar"\n'
 'c| regras_transportadora = {\nc|     "Sudeste": "TransRapido",\nc|     "Nordeste": "LogNordeste",\nc|     "Sul": "SulCargas"\nc| }\nendcode:')
rep('print(f"=æ\nc|  Pacote','print(f"📦 Pacote')
rep('h| Sua Planilha Excel ] ¡ ¡ ¡ [ Script em Python ] ¡ ¡ ¡ [ Planilha Atualizada ]\np| (Dados de peso e CEP)      (Cruza as faixas de peso e CEP)     (Com a transportadora certa na coluna)',
    'code:\nc| [ Sua Planilha Excel ] ➡ ➡ ➡ [ Script em Python ] ➡ ➡ ➡ [ Planilha Atualizada ]\nc| (Dados de peso e CEP)      (Cruza as faixas de peso e CEP)     (Com a transportadora certa na coluna)\nendnote:')
rep('economizadas na hora. Para que eu possa','economizadas na hora.\np| Para que eu possa')
rep('p| xcelente, Felipe!','p| Excelente, Felipe!')
for cmd in ['pip install pandas openpyxl','cd Desktop\\Piloto_Logistica','python classificador.py']:
    rep(':bash\np| '+cmd+'\np| Use o código com cuidado.', ':\ncode:\nc| '+cmd+'\nendcode:')
rep('perfeitamente. Me avise assim que rodar!','perfeitamente.\np| Me avise assim que rodar!')
open('rp47.fixed.txt','w',encoding='utf-8').write(s)
