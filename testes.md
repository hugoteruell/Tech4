# Testes de falha da operação

Testes aplicados à rotina `vigia-parados` ([`automacoes.md`](automacoes.md)) e às regras de [`regras.md`](regras.md), contra a fonte declarada em [`dados/fonte.md`](dados/fonte.md).

**Executados em 21/09/2026, 08:21.** Rodaram sobre cópias do `dados/amostra.csv` em diretório temporário — o arquivo do repositório não foi alterado. Os três acharam falha real; nenhum resultado abaixo é hipotético.

---

## 1. Fonte saiu do ar

**O que foi testado.** O comportamento da rotina quando `dados/amostra.csv` — a fonte canônica — não pode ser lido.

**Como a falha foi simulada.** Dois cenários, executados separadamente:
1. Caminho inexistente passado ao leitor de CSV.
2. Arquivo presente mas **vazio** (zero bytes).

**O que aconteceu.**

| Cenário | Resultado real |
|---|---|
| Arquivo ausente | `FileNotFoundError: [Errno 2] No such file or directory` — a rotina **aborta** com stack trace |
| Arquivo vazio | Lê **0 linhas sem erro nenhum** e sairia como `nada a reportar · N = 0` |

**Falha encontrada.** As duas são problema, e a segunda é a pior. O prompt em `automacoes.md` manda responder `FONTE INDISPONÍVEL` e parar — **isso não está implementado**. No caso do arquivo vazio, a rotina produziria um silêncio indistinguível de operação saudável. É exatamente o risco que a cláusula "se não disparar" da Regra 1 antecipa, e o teste confirma que a proteção está escrita mas não existe no código.

**Como detectamos que houve problema.** Hoje, só olhando o terminal. O `FileNotFoundError` é visível; o arquivo vazio **não é** — ele passa silenciosamente.

**Plano B / correção.**
1. Antes de qualquer leitura, checar se o arquivo existe **e** tem mais de uma linha. Se falhar, emitir `FONTE INDISPONÍVEL` e parar, sem nunca cair em "nada a reportar".
2. Tratar `N = 0` como erro, não como silêncio: a fonte tem 9 linhas e 4 itens Alta; `N = 0` só é possível se a leitura falhou.
3. Fonte de reserva: regerar `amostra.csv` a partir da tabela `## 4. Prioridade` da análise mais recente em `estrategia/`, que é a origem do extrato.

---

## 2. Chegou dado inesperado

**O que foi testado.** Como a rotina reage a linhas malformadas no CSV.

**Qual dado inesperado entrou.** Duas linhas acrescentadas a uma cópia:

```
O10,Item com dado sujo,Alta,nao_iniciado,2026-09-01,vinte,campo dias_parado veio como texto
O11,Item sem status,Alta,,2026-09-01,10,status vazio
```

A primeira tem **texto onde deveria haver número** (`dias_parado = "vinte"`). A segunda tem **campo obrigatório vazio** (`status`).

**O que aconteceu.**

```
ValueError: invalid literal for int() with base 10: 'vinte'
```

A rotina **aborta na linha suja e não reporta os itens válidos que vinham antes dela**. O1, O5, O6 e O9 — que disparariam normalmente — são perdidos porque uma linha posterior estava quebrada. Uma linha ruim derruba o relatório inteiro.

**Como a rotina deveria reagir.** Processar linha a linha, isolando o erro:

1. Linha com campo inválido é **pulada**, não derruba a execução.
2. As linhas puladas aparecem no fim da saída, em bloco próprio: `LINHAS IGNORADAS: O10 (dias_parado não numérico), O11 (status vazio)`.
3. Se mais de 20% das linhas forem ignoradas, a saída vira `FONTE SUSPEITA` em vez de relatório — muitos defeitos indicam extrato mal gerado, não dado ruim isolado.

**Correção / plano B.** Envolver a conversão de cada linha em tratamento de erro individual e acumular os defeitos numa lista, em vez de deixar a primeira exceção interromper tudo. `status` vazio deve ser tratado como `desconhecido` e reportado, nunca como `concluido` — o padrão errado esconderia um item parado.

`TESTE PENDENTE DE EXECUÇÃO` — a correção acima ainda não foi implementada. O teste acima documenta o comportamento atual, que é o defeituoso.

---

## 3. A condição nunca dispara

**Regra testada:** Regra 2 · semana que produziu documento e nenhuma conversa.

**Como percebemos que a regra não dispara.** Executada contra a semana ISO **W37 (07 a 13/09/2026)**, com dados reais do `git log`:

```
commits em estrategia/ ou contexto/ na W37: 0 | atas: 0
CONDIÇÃO FALSA — silêncio
```

A regra ficou calada. Mas o motivo **não** foi que a semana terminou em conversa — foi que **não houve commit nenhum**. A semana não produziu nem documento nem conversa.

**Como distinguir operação saudável de rotina quebrada.** São três silêncios diferentes, e sem o motivo registrado eles são idênticos no log:

| Registro | Leitura |
|---|---|
| `nada a reportar · houve 2 ata(s) na semana` | Saudável — a semana terminou em conversa |
| `nada a reportar · 0 commit em estrategia/ e contexto/` | **Não é saudável** — semana morta, nada aconteceu |
| Ausência total de linha no log | **Rotina quebrada** — ninguém rodou, ou a execução falhou |

A cláusula "se não disparar" da Regra 2 já exige esse motivo por escrito. Este teste é a razão de ela existir.

**Depois de quanto tempo investigar.** Duas execuções seguidas com o motivo `0 commit` — isto é, **duas semanas sem nenhum movimento**. Uma semana parada é normal e está prevista: o `CLAUDE.md` proíbe rodar a análise sem fato novo. Duas seguidas significam que o ciclo parou, não que ele está descansando.

Para a Regra 1 o critério é o inverso: ela está disparando há 28 dias com os mesmos quatro itens. Regra que dispara sempre com o mesmo conteúdo também perde função — vira ruído que se aprende a ignorar. Se a rodada 02 mantiver os mesmos quatro itens em Alta, o problema não é a regra, é a fila.

**Como testar propositalmente a condição.** Procedimento pronto, ainda não executado:

1. Criar `estrategia/conversas/01-teste.md` com conteúdo mínimo e commitar.
2. Rodar a Regra 2 na mesma semana.
3. **Esperado:** silêncio com o motivo `houve 1 ata na semana` — o silêncio saudável.
4. Remover o arquivo de teste e commitar a remoção.
5. Rodar de novo. **Esperado:** volta a disparar.

Se o passo 3 produzir silêncio com o motivo errado, ou nenhum registro, a regra está quebrada.

`TESTE PENDENTE DE EXECUÇÃO` — depende de criar e remover um arquivo de teste no repositório, que é uma alteração no histórico e precisa da sua autorização.

**O que fica registrado quando não há alerta.** Uma linha por execução, sempre, com data, hora, regra, motivo do silêncio e os números verificados. Execução que não deixa linha nenhuma é tratada como falha, não como ausência de alerta.
