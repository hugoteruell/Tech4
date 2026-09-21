# Regras da operação

Duas regras que rodam sobre o ciclo de trabalho documentado neste repositório. A fonte de ambas é a declarada em [`dados/fonte.md`](dados/fonte.md).

Contexto que torna estas regras necessárias: a rodada 01 da análise (`estrategia/V3-analise-semanal-01.md`) diagnosticou duas causas concretas — **C1**, itens de prioridade sem dono nem data de início, e **C3**, capacidade sendo consumida por produção de documento em vez de contato com o mercado. Cada regra abaixo detecta uma delas.

---

## Regra 1 · Item de prioridade alta parado há mais de 7 dias

- **Gatilho:** toda segunda-feira às 9h.
- **Fonte:** `dados/amostra.csv` — extrato da tabela `## 4. Prioridade` da análise mais recente em `estrategia/` — cruzado com `git log` para confirmar ausência de movimento.
- **Condição:** existe pelo menos um item com `prioridade = Alta`, `status ≠ concluido` e `dias_parado > 7`.
- **Ação:** lista cada item que atende à condição, com `id`, nome, `dias_parado` e o campo `evidencia` (o que exatamente está faltando no disco). Registra a execução na seção de evidências de [`automacoes.md`](automacoes.md).
- **Quem recebe:** Hugo — único responsável com acesso de escrita, conforme `contexto/About me.md`. Não há outra pessoa a notificar.
- **Se não disparar:** registra a linha `AAAA-MM-DD HH:MM · Regra 1 · nada a reportar · N itens Alta verificados, máximo de dias parados: D`. O número de itens verificados é obrigatório: silêncio com `N = 0` significa que a fonte não foi lida, e isso é rotina quebrada, não operação saudável.

---

## Regra 2 · Semana que produziu documento e nenhuma conversa

- **Gatilho:** toda sexta-feira às 18h, fechando a semana ISO corrente.
- **Fonte:** `git log` da semana ISO corrente, filtrado pelos caminhos `estrategia/` e `contexto/`, cruzado com a contagem de arquivos em `estrategia/conversas/`.
- **Condição:** a semana teve **≥ 1 commit** tocando `estrategia/` ou `contexto/` **e** **0 ata nova** em `estrategia/conversas/`.
- **Ação:** emite alerta nomeando os commits da semana e a contagem de atas, com a frase de referência da régua: *"esta semana terminou em arquivo, não em conversa"*. Aponta o item O6 como o desbloqueio.
- **Quem recebe:** Hugo.
- **Se não disparar:** registra a linha de silêncio **dizendo qual dos dois motivos** o causou, porque eles são opostos:
  - `nada a reportar · houve N ata(s) na semana` — operação saudável, a semana terminou em conversa.
  - `nada a reportar · 0 commit em estrategia/ e contexto/` — **não é saudável**: a semana não produziu nada, nem documento nem conversa. A regra fica silenciosa por ausência de matéria-prima, não por sucesso.

  Sem essa distinção, uma semana morta e uma semana boa produzem exatamente o mesmo registro.

---

## Por que o critério é "dias parados" e não "está atrasado"

Não existe prazo contratado em nenhum item deste repositório — a rodada 01 registrou que, das oito prioridades, apenas uma tinha prazo e nenhuma tinha dono. "Atrasado" seria inverificável. "Dias sem evidência de movimento no git" é verificável a qualquer momento por qualquer pessoa com acesso ao repositório, inclusive por quem não participou da decisão.
