# Análise semanal — rodada 01

**Prompt usado:** `Prompts/V3.md`
**Data:** 24/08/2026
**Rodada anterior:** `V2-analise-do-negocio.md`

## Entrada preenchida

```
OBJETO: problema-drafted.md + Contexto/ + as duas análises anteriores
OBJETIVO: [ASSUMIDO] sair de zero cliente pagante documentado para
          ao menos um contrato registrado, sabendo por qual frente entrou
ESTADO ANTERIOR: tabela O1–O8 de V2-analise-do-negocio.md
MUDOU NA SEMANA: nada no negócio; produziram-se 4 documentos de análise
DECISÃO QUE ISSO ALIMENTA: no que trabalhar esta semana
```

> O `OBJETIVO` não existe em nenhum arquivo do repositório e foi assumido para permitir a priorização. Ver oportunidade O9.

---

## 0. Delta

| ID | Item | Status | Motivo |
|---|---|---|---|
| O1 | Entrada por evidência de perda | Parado | Nenhum prospect contatado |
| O2 | Elo número→receita | Parado | Depende de cliente ativo |
| O3 | Reduzir frentes | Parado | Corretamente — dependia de O6 |
| O4 | Reputational Risk como entrada | Parado | Corretamente — dependia de O6 |
| O5 | Destravar LinkedIn | Parado | Segue "aguardando confirmação do co-founder" |
| O6 | Entrevistar quem já pagou | Parado | Nenhum registro de conversa |
| O7 | Score em banda | Parado | — |
| O8 | Corrigir erros factuais | Meio andado | Identificados no V1; `problema-drafted.md` intocado desde 06/08 |

**Ressalva de janela:** o intervalo real entre a rodada anterior e esta foi de **26 minutos**, não uma semana. "Parado" significa "não iniciado", não "estagnado". A única leitura temporal legítima é outra: o `problema-drafted.md` é de **06/08** e todo o resto do repositório é de **24/08** — 18 dias em que quatro documentos de análise foram produzidos e nenhum artefato de cliente entrou.

**Novo esta rodada:** existe agora corpo analítico e instrumento de análise. Nenhum dos dois é cliente.

---

## 1. Problema central

Na rodada anterior o problema era desalinhamento entre problema declarado, negócio e evidência. Esse diagnóstico não foi contestado e segue válido — mas já não é o gargalo operante. **O gargalo agora é que a lista de oito prioridades foi escrita sem dono e sem data de início, o que a torna uma lista de desejos e não um plano.** Só um item recebeu prazo ("uma semana", O6), nenhum recebeu responsável, e nenhum tem critério de início. Deixou de ser "não sabemos o que fazer" — sabe-se, está priorizado, e não anda.

---

## 2. Causas — máximo 5

**C1 — Nenhum item tem dono nem data de início.**
Fonte: `V2-analise-do-negocio.md`, seção 5. Dos oito próximos passos, um tem prazo e nenhum tem responsável nomeado. Item sem dono não tem quem o abandone, e por isso nunca é formalmente abandonado nem executado — fica.

**C2 — O item que destrava a fila pode ser inexecutável, e isso não foi previsto.**
O6 começa com *"listar todo mundo que já pagou"*. Se a resposta for "ninguém pagou ainda" — o que os próprios docs sugerem ao dizer que não há registro de ticket ou contrato —, O6 como escrito não tem o que executar. E como O3 e O4 foram explicitamente colocados em espera dependendo de O6, **a fila inteira trava num item que talvez não tenha entrada.**
*Hipótese: essa é a razão real da paralisia, não falta de tempo.* Custa uma pergunta verificar.

**C3 — Assimetria de retorno entre analisar e prospectar.**
Fonte: datas dos arquivos do repositório. Analisar dá retorno imediato, mensurável em páginas, e é privado — nada externo pode recusá-lo. Prospectar dá retorno incerto, demorado e público. Com capacidade escassa e perfil de fundador técnico (`Contexto/About me.md`), a atividade que se auto-recompensa desloca a que não se recompensa. É a causa 2.1 da rodada anterior, agora com evidência em vez de inferência.

**C4 — Bloqueios de decisão sobrevivem a rodadas de análise.**
"LinkedIn aguardando confirmação do co-founder" aparece em `About me.md`, em `drafted-negocio.md` e nas duas análises. Um item que atravessa três documentos sem ser resolvido não está aguardando informação — está sem dono. Mesmo mecanismo de C1, num caso concreto.

**C5 — O objetivo nunca foi escrito.**
Não existe, em nenhum dos quatro arquivos, uma meta com número e data. Foi preciso assumir uma para rodar esta análise. Sem alvo declarado, "prioridade alta" não tem referência: alta em relação a quê? E a fila não tem critério de parada, então nada nunca sai dela.

---

## 3. Oportunidades — máximo 6

**O6 — Reescrever a entrevista com ramo alternativo** *(revisado)*
*Observação:* O6 pressupõe base de clientes e nenhum documento confirma que ela existe.
*Por que acontece:* foi escrito assumindo um cenário sem verificar se ele é o caso.
*Mudança:* dividir em dois ramos e executar o que se aplicar, sem esperar decisão.
- **O6a** — se houver quem pagou ou negociou: as quatro perguntas do `drafted-icp.md`.
- **O6b** — se não houver: cinco conversas frias com empresas do ICP, sem vender, com uma pergunta só — *quando foi a última vez que você ou alguém do seu time perguntou a uma IA sobre um fornecedor da sua categoria?*

O6b não depende de ter cliente e produz o mesmo insumo.

**O1 — Usar a evidência de perda como pretexto de contato** *(revisado)*
*Observação:* na rodada anterior O1 era abordagem comercial e ficou parado junto com todo o resto.
*Por que acontece:* estava enquadrado como venda, o que tem custo psicológico alto sem cliente nenhum na base.
*Mudança:* reenquadrar como insumo de O6b. O one-pager mostrando o que a IA responde sobre a categoria do prospect deixa de ser pitch e vira motivo legítimo de conversa. Mesmo trabalho, barreira de execução muito menor.

**O9 — Escrever o objetivo com número e data** *(novo)*
*Observação:* nenhum arquivo contém meta. Foi preciso assumir uma para poder priorizar.
*Por que acontece:* os documentos foram escritos para explicar o negócio, não para operá-lo.
*Mudança:* um arquivo curto com a meta do trimestre em número e data, virando campo fixo `OBJETIVO` do prompt semanal. Sem isso, cada rodada renegocia silenciosamente o critério de prioridade e as rodadas deixam de ser comparáveis.

**O5 — Converter LinkedIn de escopo em pendência com data**
*Observação:* aberto em três documentos sem resolução.
*Por que acontece:* está catalogado como decisão de produto, e decisão de produto não tem prazo.
*Mudança:* tratar como item com dono e data-limite. A resposta pode ser não — o custo está em ficar aberto.

**O8 — Corrigir o `problema-drafted.md`**
*Observação:* três erros factuais identificados no V1; o arquivo não é editado desde 06/08.
*Por que acontece:* a correção foi documentada em outro arquivo, o que dá sensação de resolvido sem resolver.
*Mudança:* editar o arquivo-fonte. Só a correção factual e a remoção da seção "Dados Existem" — não a reescrita completa, que depende de O6b.

**O2 — Elo número→receita**
Mantido sem alteração em relação à rodada anterior. Rebaixado: só é executável com cliente ativo.

*O3, O4 e O7 saem da lista ativa nesta rodada por dependerem de O6. IDs reservados, retornam quando O6 fechar.*

---

## 4. Prioridade

| ID | Impacto no objetivo | Esforço | Depende de | Prioridade |
|---|---|---|---|---|
| **O6** | Alto — única fonte de evidência de mercado; destrava O3, O4 e o pitch | Médio — 5 conversas | Nada (com o ramo O6b) | **Alta** |
| **O9** | Alto — sem alvo, nenhuma priorização é verificável, inclusive esta | Baixo — 30 min | Nada | **Alta** |
| **O1** | Médio direto, alto como viabilizador de O6b | Baixo — 5 one-pagers | Nada | **Alta** |
| **O5** | Médio — credibilidade da demo em 2 setores do ICP | Muito baixo — uma conversa | Co-founder | **Alta** |
| **O8** | Baixo comercial, alto em risco evitado | Muito baixo | Nada | **Média** |
| **O2** | Alto quando aplicável | Baixo | Existir cliente | **Baixa agora** |

Critério aplicado: alta exige impacto direto no objetivo **e** nenhuma dependência aberta. O9 sobe apesar do impacto indireto porque é pré-condição de todas as rodadas seguintes.

---

## 5. Próximo passo — só prioridades altas

**O6** — Dono: Hugo. Até sexta. Responder por escrito se existe alguém que já pagou ou negociou. Se sim, agendar duas conversas O6a. Se não, listar 10 empresas do ICP e enviar 5 contatos O6b.
*Critério de conclusão: cinco conversas agendadas ou realizadas, com anotação do gatilho relatado.*

**O9** — Dono: Hugo. Hoje, 30 minutos. Escrever `objetivo.md` com uma frase: qual número, até quando.
*Critério: o campo OBJETIVO da próxima rodada é copiado desse arquivo, não assumido.*

**O1** — Dono: Hugo. Até quarta. Cinco one-pagers, um por empresa da lista de O6b, com o print do que os modelos respondem sobre a categoria.
*Critério: cinco PDFs prontos, anexáveis ao contato.*

**O5** — Dono: co-founder, agendado por Hugo. Esta semana. Sair da conversa com decisão registrada em `drafted-negocio.md`: dentro, fora com justificativa, ou adiado com data.
*Critério: a palavra "aguardando" some do arquivo.*

---

## 6. Não fazer esta semana

- **Não reescrever o `problema-drafted.md` por inteiro.** A cena de abertura correta depende do que O6b trouxer. Reescrever agora é escrever duas vezes.
- **Não construir Reputational Risk.** Depende de O6 confirmar que crise é gatilho dominante.
- **Não mexer em pesos ou normalização do scorecard.** É o trabalho de maior retorno percebido e menor retorno real nesta fase — precisamente o mecanismo de C3.
- **Não rodar esta análise de novo sem fato novo.** O prompt semanal só gera valor sobre delta. Rodado sobre estado parado, produz mais um documento e reforça a causa que ele mesmo diagnostica.

---

## 7. Lacunas

| Hipótese | O que resolveria | Custo |
|---|---|---|
| Não existe cliente pagante hoje | Uma frase de resposta do Hugo | Zero |
| A paralisia vem de O6 ser inexecutável, não de falta de tempo | Verificar a hipótese acima | Zero |
| Empresas do ICP nunca notaram perda por IA | As cinco conversas de O6b | Uma semana |
| Crise é o gatilho de venda mais rápido | Frequência do gatilho nas conversas de O6 | Incluído em O6 |
| O objetivo real é receita, não validação | Conversa com o co-founder, junto de O5 | Zero |

---

## O que esta análise não pode afirmar

Se existe cliente pagante, ticket, duração de contrato ou mix de receita. O `OBJETIVO` usado foi assumido, não declarado — se estiver errado, a tabela de prioridade inteira muda. E a janela de delta foi de 26 minutos: a rodada 01 estabelece a linha de base, não mede progresso. A primeira leitura de progresso real só existe na rodada 02.
