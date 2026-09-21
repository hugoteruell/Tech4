# Testes de falha

Testado em 21/09/2026.

Todos os testes abaixo foram executados contra a rotina real [`vigia_parados.py`](vigia_parados.py), que implementa a Regra 1 de [`regras.md`](regras.md), usando a fonte real `dados/amostra.csv`. Cada bloco "O que aconteceu" é saída copiada do terminal, não descrição.

**Execução de controle**, antes dos testes, com a fonte íntegra:

```
2026-09-21 08:37 · Regra 1 · DISPAROU · lidos: 9 · considerados: 4 · ignorados: 0
  O1 · Entrada por evidencia de perda · 28 dias · nenhum one-pager em estrategia/
  O5 · Destravar decisao sobre LinkedIn · 28 dias · aguardando ainda presente em contexto/drafted-negocio.md:78
  O6 · Conversas com o ICP (ramo O6b) · 28 dias · 0 arquivos em estrategia/conversas/
  O9 · Escrever objetivo.md com numero e data · 28 dias · objetivo.md nao existe no disco
```

---

## Cenário 1 · A fonte saiu do ar

**O que eu testei:**
Renomeei a fonte real do repositório, `dados/amostra.csv` → `dados/amostra_OLD.csv`, com `git mv`, e rodei a rotina como ela estava escrita em `automacoes.md` antes de existir a seção de segurança.

**O que aconteceu:**

```
Traceback (most recent call last):
  File "vigia_v1.py", line 3, in <module>
    linhas = list(csv.DictReader(open("dados/amostra.csv")))
FileNotFoundError: [Errno 2] No such file or directory: 'dados/amostra.csv'
```

A rotina **abortou com stack trace**. Não devolveu resultado vazio, não inventou nada e não mostrou `FONTE INDISPONÍVEL` — simplesmente quebrou. Num agendador sem monitoramento, isso seria uma execução que falha em silêncio.

**O que eu consertei:**
Escrevi a seção `## Segurança e tratamento de falhas` em `regras.md` e implementei a rotina em `vigia_parados.py`, com verificação de existência, permissão de leitura, arquivo vazio e cabeçalho ausente **antes** de qualquer leitura. Encerra com código de saída 1, que um agendador consegue detectar.

**Resultado após correção:**
Teste repetido com a fonte ainda renomeada:

```
FONTE INDISPONÍVEL · dados/amostra.csv · arquivo não encontrado
código de saída: 1
```

A fonte foi restaurada ao nome original com `git mv`. Conferido com `git diff --quiet dados/amostra.csv`: **idêntica byte a byte** ao arquivo versionado.

---

## Cenário 2 · Chegou dado inesperado

**O que eu testei:**
Backup da fonte, e três erros controlados introduzidos em registros reais:

| Erro | Registro | Alteração |
|---|---|---|
| Campo obrigatório vazio | O1 | `status` `nao_iniciado` → vazio |
| Valor numérico inválido | O5 | `dias_parado` `28` → `-3` (negativo) |
| Data em formato diferente | O9 | `data_origem` `2026-08-24` → `24/08/2026` |

Depois, um segundo teste com **um erro só** (O5 com `dias_parado` = `"vinte"`), para verificar se um registro ruim derruba os válidos.

**O que aconteceu:**

Com os três erros:

```
FONTE SUSPEITA — 3 de 9 registros ignorados
IGNORADOS: O1 (status vazio) · O5 (dias_parado negativo: -3) · O9 (data_origem fora do formato AAAA-MM-DD: "24/08/2026")
código de saída: 2
```

Os três foram detectados, cada um nomeado com o próprio motivo. Como 3 de 9 é 33% e o limiar é 20%, a saída virou `FONTE SUSPEITA` em vez de relatório — nenhum dado inválido entrou no cálculo.

Com um erro só:

```
2026-09-21 08:37 · Regra 1 · DISPAROU · lidos: 9 · considerados: 3 · ignorados: 1
  O1 · Entrada por evidencia de perda · 28 dias · nenhum one-pager em estrategia/
  O6 · Conversas com o ICP (ramo O6b) · 28 dias · 0 arquivos em estrategia/conversas/
  O9 · Escrever objetivo.md com numero e data · 28 dias · objetivo.md nao existe no disco
IGNORADOS: O5 (dias_parado não numérico: "vinte")
```

O registro ruim foi pulado, os três válidos continuaram sendo reportados, e o que foi ignorado aparece com o motivo. `considerados` caiu de 4 para 3, tornando a perda visível no próprio número.

**O que eu consertei:**
A validação passou a ser por registro, não pela execução inteira: cada linha é checada isoladamente e o erro vai para uma lista de ignorados em vez de interromper o laço. `status` vazio **nunca** recebe padrão — um padrão `concluido` esconderia justamente o item parado que a regra existe para achar.

A fonte foi restaurada do backup. Conferido: **idêntica byte a byte** ao arquivo versionado, 9 registros.

---

## Cenário 3 · A condição nunca dispara

**O que eu testei:**
Regra 1 — item de prioridade alta parado há mais de 7 dias. Rodei a rotina real numa situação em que a condição **não** é verdadeira: extrato recalculado para **25/08/2026**, um dia após a rodada 01, quando nenhum item havia passado de 7 dias. Os dados são os mesmos nove registros reais; só a data de referência muda.

**O que aconteceu:**

```
2026-08-25 08:37 · Regra 1 · nada a reportar · lidos: 9 · considerados: 4 · ignorados: 0, máximo de dias parados: 1
código de saída: 0
```

A condição não disparou, corretamente. E o silêncio veio acompanhado de números.

**Como sei que a rotina está funcionando:**

O silêncio nunca é uma linha em branco. Ele carrega `lidos`, `considerados`, `ignorados` e `máximo de dias parados` — e é isso que separa os três estados possíveis:

| Registro | Leitura |
|---|---|
| `nada a reportar · lidos: 9 · considerados: 4 · … máximo: 1` | **Tudo bem.** Leu a fonte inteira, avaliou os 4 itens Alta, nenhum passou do limite |
| `nada a reportar · lidos: 0` ou `considerados: 0` | **Quebrada.** A fonte tem 9 registros e 4 itens Alta; esses números só são possíveis se a leitura falhou |
| `FONTE INDISPONÍVEL` | **Quebrada**, e diz o motivo |
| Nenhuma linha registrada | **Quebrada** — ninguém rodou, ou a execução morreu antes de escrever |

O `máximo de dias parados` é o indicador mais útil do silêncio: ele mostra o quanto falta para disparar. Um silêncio com máximo de 1 dia é folgado; com 7 dias, está na borda.

**O que eu consertei / plano B:**

**Depois de quanto tempo investigar.** Duas execuções seguidas com `lidos: 0` ou sem linha nenhuma — ou seja, **duas semanas** sem registro legível. Uma semana silenciosa é normal e prevista: o `CLAUDE.md` proíbe rodar a análise sem fato novo, então a tabela de prioridade pode ficar parada de propósito.

**O problema oposto, que é o real hoje.** A Regra 1 vem disparando com os **mesmos quatro itens há 28 dias**. Regra que dispara sempre com o mesmo conteúdo deixa de ser alerta e vira paisagem. Se a rodada 02 mantiver O1, O5, O6 e O9 em Alta, o defeito não está na regra — está na fila.

**Como forçar a condição para confirmar que o alerta ainda funciona.** Foi exatamente o que o teste acima faz, e o procedimento é reproduzível por qualquer pessoa:

```bash
python3 vigia_parados.py --ref 2026-08-25 --fonte <extrato recalculado>
```

Rodar com uma data de referência anterior ao limite dos 7 dias deve produzir `nada a reportar` com `considerados: 4`. Rodar com a data de hoje deve disparar quatro itens. Se os dois derem o mesmo resultado, a condição parou de ser avaliada.

`TESTE PENDENTE DE EXECUÇÃO` — o caminho inverso, criar uma ata em `estrategia/conversas/` para silenciar a Regra 2 e depois removê-la, não foi executado. Ele altera o histórico do repositório e depende de autorização. O procedimento está escrito e pode ser rodado a qualquer momento.
