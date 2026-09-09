# Agendamento com `/loop`

O `/loop` roda um prompt ou slash command repetidamente dentro de uma
mesma sessão do Claude Code, em intervalo fixo ou autoajustado pelo
próprio modelo.

## Sintaxe

```
/loop [intervalo] <prompt ou slash command>
```

- **Com intervalo** — ex.: `/loop 20m /verificar-novos-materiais` — roda no
  cronograma fixo indicado (minutos/horas).
- **Sem intervalo** — ex.: `/loop /checar-padrao-pastas` — modo dinâmico:
  a cada rodada o próprio modelo decide quando agendar a próxima, com base
  no que encontrou (nada mudou → espera mais; algo relevante aconteceu →
  reagenda mais cedo).

## Limitações importantes

- Só existe enquanto a sessão do terminal está aberta — não é um cron do
  sistema operacional. Fechou o terminal, o loop para.
- Para algo que precise sobreviver ao fechamento da sessão (rodar mesmo
  com o terminal desligado), o caminho é a skill `schedule` (agentes com
  cron real na nuvem), não o `/loop`.

## Os 3 exemplos deste diretório

Cada um é um **slash command** (arquivo `.md` que viveria em
`.claude/commands/`) pensado para ser executado repetidamente pelo
`/loop`, mais o README com a explicação e o teste real que rodei:

1. [exemplo-1-commit-automatico-de-materiais](exemplo-1-commit-automatico-de-materiais/)
   — detecta arquivos novos não versionados e cria um commit local
   descritivo (nunca dá push).
2. [exemplo-2-atualizar-indice-readme](exemplo-2-atualizar-indice-readme/)
   — mantém a lista de pastas de tema sempre atualizada dentro do
   `README.md`, editando só um trecho delimitado.
3. [exemplo-3-checagem-padrao-pastas](exemplo-3-checagem-padrao-pastas/)
   — comando somente leitura que confere se as pastas de exemplo seguem o
   padrão de nomenclatura do curso e relata divergências, sem corrigir
   nada sozinho.

Juntos, eles cobrem os três "temperamentos" de automação recorrente que
fazem sentido com `/loop`: **agir com efeito reversível** (commit local),
**agir com efeito restrito/cirúrgico** (editar só um trecho do README) e
**só observar e avisar** (relatório sem tocar em nada).

## Como cada um foi testado

Nenhum dos três foi instalado em `.claude/commands/` **deste** projeto, e
nenhum `/loop` ficou rodando de verdade contra este repositório — por
pedido explícito de manter isso só como exemplo, não em produção.

Cada comando foi:

1. Colocado em `.claude/commands/` de um **repositório git temporário**,
   criado à parte (fora deste projeto) e descartado depois do teste.
2. Executado com `claude -p "/comando" --allowedTools "..."` (modo
   headless, não-interativo) contra esse repositório de teste, com cenários
   criados de propósito (arquivo novo, pasta nova, pasta fora do padrão).
3. Rodado uma segunda vez sem mudanças, para confirmar que é **idempotente**
   — pré-requisito para algo que o `/loop` vai chamar repetidamente sem
   supervisão constante.

Os resultados reais de cada execução (não simulados) estão documentados no
README de cada exemplo.

## Como ativar de verdade (se um dia quiser usar em produção)

1. Copiar o `.md` do exemplo desejado para `.claude/commands/` deste
   projeto.
2. Abrir uma sessão nova do Claude Code (comandos custom só carregam no
   início da sessão).
3. Rodar `/loop <intervalo> /<nome-do-comando>` para agendar, ou chamar o
   comando manualmente quando quiser.
