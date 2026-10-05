from rpfix import Fix
f=Fix('res47.txt')
f.rep('Economiza\nt| Tempo','Economiza Tempo')
f.block('t| O que é feito hoje','t| envio.',
 'th| O que é feito hoje (Manual) | Como o Python faz (Automatizado) | Impacto Direto no seu Negócio\n'
 'tr| <strong>Digitação e Leitura Visual</strong><br>Um funcionário lê o endereço, o peso ou o tipo de produto e decide a categoria ou transportadora. | <strong>Leitura Digital Direta</strong><br>O script Python extrai os dados diretamente do sistema ou do código de barras instantaneamente. | <strong>Zero erro de digitação</strong> ou leitura trocada. Adeus pacotes enviados para o destino errado.\n'
 'tr| <strong>Decisão Humana Subjetiva</strong><br>O operador precisa lembrar das regras de envio ou olhar uma tabela para classificar cada item. | <strong>Regras de Negócio Fixas</strong><br>O código aplica regras lógicas (Ex: Se peso &gt; 5kg e região = Sudeste, use a Transportadora X). | <strong>Padronização total</strong>. A classificação é feita de forma idêntica e sem hesitação todas as vezes.\n'
 'tr| <strong>Processamento Lento (Um a Um)</strong><br>Levar minutos para conferir, registrar e colar a etiqueta em uma única ordem de envio. | <strong>Processamento em Lote</strong><br>O Python consegue classificar <strong>milhares de envios em poucos segundos</strong>. | <strong>Ganho brutal de tempo</strong>. O que levava horas ou dias passa a rodar no tempo de um clique.')
f.rep('t| Exemplo prático de Dicionário de Regras:','li| Exemplo prático de Dicionário de Regras:')
f.rep('de Decisão)\nt| Decisão)','de Decisão)') if False else f.rep('t| Passo 3: Tomar a decisão automatizada (As Estruturas de\nt| Decisão)','t| Passo 3: Tomar a decisão automatizada (As Estruturas de Decisão)')
f.block('t| Pacote 001','t| Pacote 004 (22.0kg) -> Nordeste Pesados',
 'li| Pacote 001 (3.2kg) -&gt; TransRapido Express\n'
 'li| Pacote 002 (12.0kg) -&gt; Sudeste Cargas &lt;-- <strong>O Python separou o pacote pesado na mesma região automaticamente!</strong>\n'
 'li| Pacote 003 (1.5kg) -&gt; LogNordeste Eco\n'
 'li| Pacote 004 (22.0kg) -&gt; Nordeste Pesados')
f.rep('t| [ Sua Planilha Excel ] ➡ ➡ ➡ [ Script em Python ] ➡ ➡ ➡ [ Pla\nc| (Dados de peso e CEP)      (Cruza as faixas de peso e CEP)     (Com',
      'code:\nc| [ Sua Planilha Excel ] ➡ ➡ ➡ [ Script em Python ] ➡ ➡ ➡ [ Planilha Atualizada ]\nc| (Dados de peso e CEP)      (Cruza as faixas de peso e CEP)     (Com a transportadora certa na coluna)\nendnote:')
f.rep('"Região"?) Quantas','"Região"?)\nli| Quantas')
f.pct()
for t in ['1. Preparação da Base de Testes (Amanhã)','2. Definição da Matriz de Regras Real','3. Execução do Piloto e Auditoria']:
    f.rep('t| '+t,'h4| '+t)
f.rep('Transp. Y <strong>De 10kg','Transp. Y\nli| <strong>De 10kg')
f.rep('<strong>Todos os</strong>\nli| <strong>arquivos ()</strong>.\nt| .','<strong>Todos os arquivos (.)</strong>.')
f.rep('garantia de bastidor: <strong>a</strong>\nt| tecnologia não se importa com idade ou tempo de carteira assinada, ela só\np| <strong>se importa com a precisão da lógica</strong>.',
      'garantia de bastidor: <strong>a tecnologia não se importa com idade ou tempo de carteira assinada, ela só se importa com a precisão da lógica</strong>.')
f.code_from('rp47.fixed.txt')
f.numbered()
f.t_to_h()
f.save('res47.fixed.txt')
