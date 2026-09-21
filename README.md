# Drafted

Repositório da disciplina AI for Business, 2026-2.

## O problema

A Drafted construiu um produto de reputação em IA que funciona tecnicamente, mas ainda não provou que alguém paga por ele — e a capacidade disponível vem sendo consumida produzindo análise em vez de conversa com o mercado.

## Métrica

Conversas com o ICP realizadas: **de 0 para 5 até 05/10/2026**. Verificada contando as atas em `estrategia/conversas/`. Detalhe e origem do alvo em [`problema.md`](problema.md).

## Arquivos

| Arquivo | O que é |
|---|---|
| [`problema.md`](problema.md) | O problema que a Drafted tenta resolver, e a métrica única com alvo e prazo |
| [`regras.md`](regras.md) | As duas regras da operação: item de prioridade alta parado, e semana que produziu documento sem conversa |
| [`automacoes.md`](automacoes.md) | A rotina `vigia-parados`, com o prompt completo e duas execuções registradas |
| [`testes.md`](testes.md) | Os três cenários de falha testados em 21/09/2026, com o que cada um quebrou |
| [`prompts.md`](prompts.md) | Índice de todos os prompts do projeto e onde cada um vive |
| [`CLAUDE.md`](CLAUDE.md) | Instruções de trabalho do repositório: estrutura, ciclo semanal, convenções e o que não fazer |
| [`contexto/`](contexto/) | Material-base: perfil do fundador, negócio, ICP, o cemitério de ideias derrubadas e a régua de decisão |
| [`dados/fonte.md`](dados/fonte.md) | Qual é a fonte canônica, onde vive, quem atualiza, quais campos importam e o que os dados ainda não têm |
| [`dados/amostra.csv`](dados/amostra.csv) | Extrato dos nove itens de oportunidade com prioridade, status e dias parados — é o que as regras leem |
| [`Prompts/`](Prompts/) | As três versões do prompt de análise e o comparativo entre elas |
| [`estrategia/`](estrategia/) | As análises que cada versão do prompt gerou |
| [`radar/`](radar/) | 30 comentários públicos do Instagram da Drafted, coletados em 4 posts, classificados e lidos como sinal de negócio |
| [`.claude/skills/`](.claude/skills/) | Quatro skills que operam o ciclo: consistência, fecha-conversa, resumo-semanal e pesquisa de leads |

## Como o ciclo funciona

1. `Prompts/V3.md` roda quando há fato novo e produz uma análise numerada em `estrategia/`.
2. A análise define itens de oportunidade com ID estável (O1…O9) e prioridade.
3. `dados/amostra.csv` extrai esses itens em formato tabular.
4. As regras de `regras.md` leem esse extrato e disparam quando a condição é verdadeira.
5. Conversas com o mercado viram atas em `estrategia/conversas/`, que é onde a métrica é contada.

## Estado em 21/09/2026

- Última análise: **24/08/2026** — rodada 01.
- Quatro itens de prioridade alta parados há **28 dias**: O1, O5, O6 e O9.
- Conversas com o ICP registradas: **0**.
- Radar: **30 comentários** de 4 posts (10/08 a 19/08) — 60% ruído, 33,3% elogio, 6,7% intenção explícita.

O repositório documenta essa parada em vez de escondê-la. É o que a rotina `vigia-parados` detecta e o que a métrica mede.
