# CLAUDE.md

Repositório de estratégia da **Drafted** — SaaS de reputation intelligence ("next-gen PR for the AI era"). Não há código aqui. São documentos de contexto, prompts de análise e as análises que eles geram.

## Estrutura

```
problema-drafted.md    Documento de problema (fonte, de 06/08/2026)
Contexto/              Material-base: perfil do fundador, negócio, ICP
Prompts/               Os prompts de análise, versionados (V1 → V3)
estrategia/            As respostas que cada prompt gerou
```

`Prompts/diff.entre.Vs.md` registra o que mudou entre as versões e por quê. Ler antes de propor alteração em qualquer prompt.

## O ciclo semanal

`Prompts/V3.md` é o prompt corrente. Ele exige entrada preenchida — OBJETO, OBJETIVO, ESTADO ANTERIOR, MUDOU NA SEMANA, DECISÃO. A saída vai para `estrategia/V3-analise-semanal-NN.md`, numerada em sequência.

Regras do ciclo:

- **Não rodar sem fato novo.** Rodado sobre estado parado, o prompt produz documento em vez de decisão — que é a própria causa C3 que ele diagnostica.
- **ESTADO ANTERIOR é a tabela de prioridade da rodada anterior**, colada literalmente. É o que torna as rodadas comparáveis.
- **IDs de oportunidade são estáveis** (O1, O2, …). Um item que sai da lista ativa mantém o ID reservado e volta com o mesmo número. Item novo pega o próximo ID livre — o último usado é **O9**.

## Convenções

- Português do Brasil. Copy direta, sem muleta semântica — é preferência explícita do Hugo (`Contexto/About me.md`).
- Toda afirmação factual citada da fonte. Sem fonte, prefixar `Hipótese:`.
- Toda análise fecha com o que ela **não** pode afirmar.
- Documentos marcam quando são dedução e não retrato — `drafted-negocio.md` e `drafted-icp.md` já fazem isso no cabeçalho. Manter.

## O que não fazer

- **Não inventar dado de cliente, ticket, contrato ou receita.** Não existe nenhum registrado. Toda análise que precisar disso deve dizer que não sabe, não estimar.
- **Não tratar os documentos de contexto como validados.** `drafted-icp.md` é hipótese construída a partir da lógica do produto, não de entrevista. Ele mesmo declara isso.
- **Não reescrever `problema-drafted.md` por inteiro** enquanto O6 não fechar — a cena de abertura depende do que as conversas trouxerem. Correção factual pontual é liberada.

## Estado aberto

Duas pendências que bloqueiam a próxima rodada:

1. **O9** — o objetivo nunca foi escrito. A rodada 01 usou um objetivo assumido. Precisa de `objetivo.md` com número e data.
2. **O6** — existe alguém que já pagou ou negociou? A resposta decide se a rodada 02 segue por O6a (entrevistar quem pagou) ou O6b (cinco conversas frias com o ICP).

Detalhe em `estrategia/V3-analise-semanal-01.md`.

## Git

Repositório público. Conteúdo inclui fragilidades comerciais e ausência de base de clientes — considerar isso antes de adicionar material sensível.
