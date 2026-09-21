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

---

## Segurança e tratamento de falhas

Regras que valem para **toda** rotina deste repositório, acima de qualquer condição individual. Uma rotina que viola qualquer item abaixo está quebrada, mesmo que produza saída.

### 1. Fonte indisponível para e avisa

Se a fonte necessária não existir, não puder ser lida ou vier vazia, a rotina **para imediatamente** e retorna a expressão literal:

```
FONTE INDISPONÍVEL
```

seguida do caminho que tentou ler e do motivo (`arquivo não encontrado`, `sem permissão de leitura`, `arquivo vazio`, `cabeçalho ausente`).

**Nunca** cair em "nada a reportar" quando a fonte falhou. Silêncio por fonte quebrada e silêncio por operação saudável são indistinguíveis no log, e é assim que uma rotina morta passa semanas sem ser notada.

### 2. Proibido inventar, estimar ou completar

A rotina **não pode**:

- inventar registro que não esteja na fonte;
- estimar valor ausente a partir dos demais;
- assumir padrão para campo vazio — em particular, `status` vazio **nunca** vira `concluido`, porque o padrão errado esconderia justamente o item parado que a Regra 1 existe para achar;
- arredondar, converter ou "consertar" dado malformado em silêncio.

Campo ausente ou inválido torna o **registro** inválido. Não torna o registro um zero.

### 3. Contagem obrigatória de lidos e ignorados

Toda execução, disparando ou não, informa:

- quantos registros foram **lidos** da fonte;
- quantos foram **considerados** na condição;
- quantos foram **ignorados**;
- **o motivo de cada registro ignorado**, identificado pelo `id`.

Exemplo do formato:

```
lidos: 11 · considerados: 4 · ignorados: 2
IGNORADOS: O10 (dias_parado não numérico: "vinte") · O11 (status vazio)
```

Execução que não informa esses números é tratada como falha, não como resultado.

### 4. Dado inválido não entra no cálculo, e não passa despercebido

Registro inválido é **pulado individualmente** — uma linha ruim não derruba a execução inteira nem faz perder os registros válidos que vieram antes dela.

Mas ele também não some: aparece na lista de ignorados com o motivo. As duas coisas juntas, nunca só uma.

### 5. Limiar de fonte suspeita

Se **mais de 20%** dos registros lidos forem ignorados, a saída deixa de ser relatório e vira:

```
FONTE SUSPEITA — N de M registros ignorados
```

Muito defeito ao mesmo tempo indica extrato mal gerado, não dado ruim isolado. Nesse caso o certo é regerar `dados/amostra.csv` a partir da tabela `## 4. Prioridade` da análise mais recente em `estrategia/`, não seguir com um relatório parcial.

### Aplicação à fonte real

Conferido contra `dados/fonte.md`: a fonte canônica é `dados/amostra.csv`, com 9 registros e os campos `id`, `prioridade`, `status`, `data_origem`, `dias_parado` e `evidencia`. As regras acima se aplicam diretamente — `dias_parado` é o campo numérico a validar, `status` é o campo obrigatório que não pode ganhar padrão, e `id` é o identificador usado para reportar o que foi ignorado.

Implementação executável: [`vigia_parados.py`](vigia_parados.py).
