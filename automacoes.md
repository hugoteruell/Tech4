# Automações

Rotinas que rodam sobre o ciclo de trabalho deste repositório. As condições estão definidas em [`regras.md`](regras.md) e a fonte em [`dados/fonte.md`](dados/fonte.md).

**Estado do agendamento:** nenhum agendador está configurado. Todas as execuções registradas abaixo foram disparadas manualmente. O gatilho horário descrito é o desenho da rotina, não um cron ativo.

**Implementação executável:** [`vigia_parados.py`](vigia_parados.py). O prompt abaixo é a forma canônica da rotina; o script é a implementação que cumpre a seção `## Segurança e tratamento de falhas` de [`regras.md`](regras.md) e permite executar e reproduzir os testes de [`testes.md`](testes.md).

```bash
python3 vigia_parados.py                    # execução normal
python3 vigia_parados.py --ref 2026-08-25   # avaliação em data de referência
```

Códigos de saída: `0` normal · `1` FONTE INDISPONÍVEL · `2` FONTE SUSPEITA.

---

## Rotina com condição — NP2

### Nome da rotina

`vigia-parados` — vigia de itens de prioridade alta sem movimento.

### Objetivo

Detectar a causa **C1** diagnosticada na rodada 01 da análise: item de prioridade alta que ficou sem dono e sem data de início e, por isso, não anda. A rotina não decide o que fazer — ela torna a parada visível com número, porque item parado sem contagem de dias vira paisagem.

### Gatilho / horário

Toda segunda-feira às 9h.

### Fonte utilizada

`dados/amostra.csv` — extrato da tabela `## 4. Prioridade` da análise mais recente em `estrategia/` — cruzado com `git log` para confirmar ausência de movimento.

### Condição verificada

Existe pelo menos um item com `prioridade = Alta`, `status ≠ concluido` e `dias_parado > 7`.

### Ação quando dispara

Lista cada item que atende à condição com `id`, nome, `dias_parado` e o campo `evidencia` — isto é, o que exatamente falta no disco. Registra a execução na seção de evidências deste arquivo.

### Quem recebe

Hugo. É o único responsável nomeado em todo o repositório (`contexto/About me.md`) e o único com acesso de escrita.

### Prompt completo

```
Você é a rotina vigia-parados. Rode contra o repositório atual.

1. FONTE
   Leia dados/amostra.csv.
   Se o arquivo não existir ou vier sem linhas, NÃO diga "nada a reportar".
   Responda exatamente: "FONTE INDISPONÍVEL — dados/amostra.csv ausente ou vazio"
   e pare.

2. CONDIÇÃO
   Considere apenas linhas com prioridade = Alta.
   Dispare para as linhas em que status != concluido E dias_parado > 7.

3. SAÍDA QUANDO DISPARA
   Escreva, nesta ordem e sem comentário adicional:
   - a data e a hora da execução
   - quantos itens Alta foram verificados
   - uma linha por item que disparou, no formato:
     <id> · <item> · <dias_parado> dias · <evidencia>
   - nenhuma recomendação, nenhuma priorização, nenhuma análise.
     Priorizar é trabalho do prompt Prompts/V3.md, não desta rotina.

4. SILÊNCIO
   Se nenhum item disparar, escreva apenas uma linha:
   "AAAA-MM-DD HH:MM · Regra 1 · nada a reportar · N itens Alta verificados,
    máximo de dias parados: D"
   O N é obrigatório. Silêncio com N = 0 não é operação saudável, é fonte não lida.

5. NÃO FAÇA
   Não invente item que não esteja no CSV.
   Não estime dias_parado — use o valor do arquivo.
   Não altere nenhum arquivo do repositório.
```

### Evidências de execução

#### Execução 1 — condição DISPAROU

- **Data:** 21/09/2026
- **Hora:** 08:20:19 (execução manual; o gatilho de segunda às 9h não está agendado)
- **Status:** DISPAROU — condição verdadeira
- **Resultado:**

```
itens Alta verificados: 4 | maior dias_parado: 28
CONDIÇÃO: VERDADEIRA — dispara

  O1 · Entrada por evidencia de perda · 28 dias · nenhum one-pager em estrategia/
  O5 · Destravar decisao sobre LinkedIn · 28 dias · aguardando ainda presente em contexto/drafted-negocio.md:78
  O6 · Conversas com o ICP (ramo O6b) · 28 dias · 0 arquivos em estrategia/conversas/
  O9 · Escrever objetivo.md com numero e data · 28 dias · objetivo.md nao existe no disco
```

Os quatro itens são de prioridade Alta da rodada 01, datada de 24/08/2026. Cada campo `evidencia` foi conferido contra o disco na mesma execução: não existe one-pager em `estrategia/`, a palavra "aguardando" continua em `contexto/drafted-negocio.md:78`, a pasta `estrategia/conversas/` não existe e `objetivo.md` não existe.

#### Execução 2 — condição NÃO disparou

- **Data:** 21/09/2026
- **Hora:** 08:20:19
- **Status:** NÃO DISPAROU — nada a reportar
- **Natureza:** **execução retroativa.** A mesma rotina foi avaliada contra o estado real do repositório em **25/08/2026**, um dia após a rodada 01. Os dados são reais — as datas de origem vêm de `dados/amostra.csv` e dos commits —, mas a avaliação foi feita hoje, não naquela data.
- **Resultado:**

```
itens Alta verificados: 4 | maior dias_parado: 1
CONDIÇÃO: FALSA — nada a reportar
```

Em 25/08 os mesmos quatro itens existiam e nenhum havia passado do limite de 7 dias. A rotina fica corretamente em silêncio, com `N = 4` registrado — o que distingue "verifiquei e está tudo bem" de "não consegui ler a fonte".

#### Execução 3 — com a rotina implementada, 21/09/2026

- **Data:** 21/09/2026
- **Hora:** 08:37
- **Status:** DISPAROU
- **Comando:** `python3 vigia_parados.py --ref 2026-09-21`
- **Resultado:**

```
2026-09-21 08:37 · Regra 1 · DISPAROU · lidos: 9 · considerados: 4 · ignorados: 0
  O1 · Entrada por evidencia de perda · 28 dias · nenhum one-pager em estrategia/
  O5 · Destravar decisao sobre LinkedIn · 28 dias · aguardando ainda presente em contexto/drafted-negocio.md:78
  O6 · Conversas com o ICP (ramo O6b) · 28 dias · 0 arquivos em estrategia/conversas/
  O9 · Escrever objetivo.md com numero e data · 28 dias · objetivo.md nao existe no disco
```

Mesma condição das execuções anteriores, agora com a contagem obrigatória de lidos, considerados e ignorados exigida pela seção de segurança.

#### Execução 4 — silêncio com a rotina implementada

- **Data:** 21/09/2026 · **Hora:** 08:37
- **Status:** NÃO DISPAROU
- **Comando:** `python3 vigia_parados.py --ref 2026-08-25 --fonte <extrato recalculado para 25/08>`
- **Resultado:**

```
2026-08-25 08:37 · Regra 1 · nada a reportar · lidos: 9 · considerados: 4 · ignorados: 0, máximo de dias parados: 1
```

Os nove registros são os reais; apenas a data de referência muda. Detalhe em [`testes.md`](testes.md), Cenário 3.

**Pendência declarada:** ainda não houve uma execução ao vivo, na data corrente, que resultasse em silêncio. Ela só acontecerá quando os itens O1, O5, O6 e O9 forem concluídos ou quando uma nova rodada de análise redefinir as prioridades.
