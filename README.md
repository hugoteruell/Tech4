# Drafted

**O projeto.** A Drafted é um SaaS de reputation intelligence que mede como uma marca é interpretada por sistemas de IA e opera para mudar essa interpretação.

**O problema.** O produto funciona tecnicamente, mas ainda não provou que alguém paga por ele — e a capacidade disponível vem sendo consumida produzindo análise em vez de conversa com o mercado.

**O objetivo deste repositório na disciplina.** Transformar esse ciclo de trabalho em operação verificável: uma fonte canônica declarada, regras com condição objetiva, uma rotina que roda e deixa evidência, e testes de falha executados de verdade.

## Arquivos

| Arquivo / pasta | O que é e para que serve |
|---|---|
| [`problema.md`](problema.md) | O problema que a Drafted tenta resolver, e a métrica única com alvo e prazo |
| [`regras.md`](regras.md) | As duas regras da operação, mais a seção de segurança que define o que fazer quando a fonte falha |
| [`automacoes.md`](automacoes.md) | A rotina `vigia-parados`: gatilho, condição, prompt completo e quatro execuções registradas |
| [`vigia_parados.py`](vigia_parados.py) | Implementação executável da Regra 1 — é o que roda nos testes e produz as evidências |
| [`testes.md`](testes.md) | Os três cenários de falha, executados em 21/09/2026, com a saída real de cada um |
| [`prompts.md`](prompts.md) | Índice de todos os prompts do projeto e onde cada um vive |
| [`CLAUDE.md`](CLAUDE.md) | Instruções de trabalho do repositório: estrutura, ciclo semanal, convenções e o que não fazer |
| [`dados/fonte.md`](dados/fonte.md) | A fonte canônica: qual é, onde vive, quem atualiza, com que frequência, quais campos importam e o que ela ainda não tem |
| [`dados/amostra.csv`](dados/amostra.csv) | Extrato dos nove itens de oportunidade com prioridade, status e dias parados — é o que as regras leem |
| [`contexto/`](contexto/) | Material-base: perfil do fundador, negócio, ICP, o cemitério de ideias derrubadas e a régua de decisão |
| [`radar/`](radar/) | 30 comentários públicos do Instagram da Drafted, coletados em 4 posts, classificados e lidos como sinal de negócio |
| [`Prompts/`](Prompts/) | As três versões do prompt de análise e o comparativo entre elas |
| [`estrategia/`](estrategia/) | As análises que cada versão do prompt gerou |
| [`.claude/skills/`](.claude/skills/) | Quatro skills que operam o ciclo: consistência, fecha-conversa, resumo-semanal e pesquisa de leads |

## Como o ciclo funciona

1. `Prompts/V3.md` roda quando há fato novo e produz uma análise numerada em `estrategia/`.
2. A análise define itens de oportunidade com ID estável (O1…O9) e prioridade.
3. `dados/amostra.csv` extrai esses itens em formato tabular — é a fonte canônica das regras.
4. `vigia_parados.py` lê esse extrato, aplica a Regra 1 e registra a execução em `automacoes.md`.
5. Conversas com o mercado viram atas em `estrategia/conversas/`, que é onde a métrica é contada.

## Métrica

Conversas com o ICP realizadas: **de 0 para 5 até 05/10/2026**. Conferida contando as atas em `estrategia/conversas/`. Origem do alvo e método em [`problema.md`](problema.md).

## Estado em 21/09/2026

- Última análise: **24/08/2026** — rodada 01.
- Quatro itens de prioridade alta parados há **28 dias**: O1, O5, O6 e O9.
- Conversas com o ICP registradas: **0**.
- Radar: **30 comentários** de 4 posts (10/08 a 19/08) — 60% ruído, 33,3% elogio, 6,7% intenção explícita.

O repositório documenta essa parada em vez de escondê-la. É o que a rotina `vigia-parados` detecta e o que a métrica mede.
