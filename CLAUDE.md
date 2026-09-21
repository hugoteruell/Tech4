# CLAUDE.md

Repositório de estratégia da **Drafted** — SaaS de reputation intelligence ("next-gen PR for the AI era"). Não há código de produto aqui. São documentos de contexto, prompts de análise, as análises que eles geram e as skills que operam esse ciclo.

## Estrutura

```
README.md              Índice do repositório
problema.md            O problema e a métrica única (era problema-drafted.md até 21/09)
regras.md              As duas regras da operação
automacoes.md          A rotina vigia-parados, com prompt e evidências de execução
testes.md              Os três cenários de falha testados
prompts.md             Índice de todos os prompts e onde cada um vive
contexto/              Material-base: fundador, negócio, ICP, cemitério, régua
dados/fonte.md         Fonte canônica, responsável, frequência e limitações
dados/amostra.csv      Extrato dos itens O1–O9 — é o que as regras leem
Prompts/               Os prompts de análise, versionados (V1 → V3)
estrategia/            As respostas que cada prompt gerou
radar/                 Radar de comentários do Instagram — 30 comentários de 4 posts, classificados
.claude/skills/        Skills próprias do projeto (versionadas)
```

## A camada operacional

`regras.md` → `automacoes.md` → `testes.md` formam o ciclo executável, e todos leem `dados/amostra.csv`. Três regras de manutenção:

- **`dados/amostra.csv` é extrato, nunca fonte de verdade.** Ele deriva da tabela `## 4. Prioridade` da análise mais recente em `estrategia/`. Se divergir, o CSV está velho — regerar, não editar.
- **Condição escrita em `regras.md` e condição escrita em `automacoes.md` têm que ser idênticas, palavra por palavra.** Se uma mudar, mudar a outra na mesma edição.
- **Nunca registrar execução que não aconteceu.** Evidência sem data, hora e saída real não entra em `automacoes.md`. Execução retroativa é permitida, desde que declarada como tal.

Skills disponíveis, todas as três sem edição automática de arquivo — elas propõem, você decide:

- **`consistencia`** — cruza os `.md` e aponta contradição, dado vencido, referência quebrada e pendência órfã. Rodar antes de mostrar o material a mentor, banca ou cliente.
- **`fecha-conversa`** — nota bruta de reunião vira ata com dono e prazo, atualiza o contexto que a conversa afetou e commita. Trava antes do commit se houver terceiro identificável, porque o repositório é público.
- **`resumo-semanal`** — status da semana com evidência do git. A saída dela preenche o campo `MUDOU NA SEMANA` do V3.

As skills de terceiros em `.claude/skills/` estão no `.gitignore` — `docx` é © Anthropic com licença que proíbe redistribuição.

`Prompts/diff.entre.Vs.md` registra o que mudou entre as versões e por quê. Ler antes de propor alteração em qualquer prompt.

## O ciclo semanal

`Prompts/V3.md` é o prompt corrente. Ele exige entrada preenchida — OBJETO, OBJETIVO, ESTADO ANTERIOR, MUDOU NA SEMANA, DECISÃO. A saída vai para `estrategia/V3-analise-semanal-NN.md`, numerada em sequência.

Regras do ciclo:

- **Não rodar sem fato novo.** Rodado sobre estado parado, o prompt produz documento em vez de decisão — que é a própria causa C3 que ele diagnostica.
- **ESTADO ANTERIOR é a tabela de prioridade da rodada anterior**, colada literalmente. É o que torna as rodadas comparáveis.
- **IDs de oportunidade são estáveis** (O1, O2, …). Um item que sai da lista ativa mantém o ID reservado e volta com o mesmo número. Item novo pega o próximo ID livre — o último usado é **O9**.

## Convenções

- Português do Brasil. Copy direta, sem muleta semântica — é preferência explícita do Hugo (`contexto/About me.md`).
- Toda afirmação factual citada da fonte. Sem fonte, prefixar `Hipótese:`.
- Toda análise fecha com o que ela **não** pode afirmar.
- Documentos marcam quando são dedução e não retrato — `drafted-negocio.md` e `drafted-icp.md` já fazem isso no cabeçalho. Manter.

## O que não fazer

- **Não inventar dado de cliente, ticket, contrato ou receita.** Não existe nenhum registrado. Toda análise que precisar disso deve dizer que não sabe, não estimar.
- **Não tratar os documentos de contexto como validados.** `drafted-icp.md` é hipótese construída a partir da lógica do produto, não de entrevista. Ele mesmo declara isso.
- **Não reescrever `problema.md` por inteiro** enquanto O6 não fechar — a cena de abertura depende do que as conversas trouxerem. Correção factual pontual é liberada.

## Estado aberto

Duas pendências que bloqueiam a próxima rodada:

1. **O9** — o objetivo nunca foi escrito. A rodada 01 usou um objetivo assumido. Precisa de `objetivo.md` com número e data.
2. **O6** — existe alguém que já pagou ou negociou? A resposta decide se a rodada 02 segue por O6a (entrevistar quem pagou) ou O6b (cinco conversas frias com o ICP).

Detalhe em `estrategia/V3-analise-semanal-01.md`.

Estado verificado em 21/09/2026: quatro itens de prioridade alta parados há 28 dias (O1, O5, O6, O9) e zero conversas registradas. O radar tem 30 comentários coletados e classificados.

## Git

Repositório público. Conteúdo inclui fragilidades comerciais e ausência de base de clientes — considerar isso antes de adicionar material sensível.
