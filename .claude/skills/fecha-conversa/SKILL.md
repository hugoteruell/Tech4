---
name: fecha-conversa
description: Transforma notas brutas de reunião ou conversa em ata estruturada com ações, dono e prazo; atualiza os documentos de contexto que a conversa confirmou ou contradisse; e commita. Use quando o usuário colar anotações de reunião, apontar uma transcrição, disser que acabou de falar com alguém, ou pedir para fechar/registrar uma conversa.
---

# Fechar conversa

Notas de reunião apodrecem em dois dias. Esta skill converte nota bruta em três coisas: uma ata que alguém consegue ler daqui a seis meses, uma atualização nos documentos de contexto que a conversa afetou, e um commit.

Aceita nota colada, caminho de arquivo, ou transcrição do Granola.

## Etapa 1 — a ata

Escrever em `estrategia/conversas/NN-identificador.md`, numerada em sequência.

```markdown
# Conversa NN — [Empresa ou pessoa]

**Data:** DD/MM/AAAA  ·  **Canal:** call / presencial / mensagem
**Quem:** nome e papel  ·  **Conduziu:** quem da Drafted
**Origem da nota:** transcrição / anotação durante / anotação depois

## O que foi dito
Trechos literais. Uma linha por ideia, entre aspas.

## Gatilho relatado
O evento específico que levou a pessoa a considerar o assunto.
Se não houve, escrever "não emergiu".

## Objeções
O que a pessoa levantou contra. Literal.

## Decisões
O que ficou decidido na conversa. Só o que foi acordado em voz alta.

## Ações
| Ação | Dono | Prazo | Critério de conclusão |

## Sem resposta
O que ficou em aberto e quem precisa responder.
```

**Regras da ata:**

- **Separar o que foi dito do que você concluiu.** "O que foi dito" é literal, entre aspas. Interpretação vai em seção própria, marcada `Hipótese:`. Confundir os dois é como uma conversa vira lembrança errada.
- **Nunca inventar dono nem prazo.** Se ninguém assumiu, escrever `não definido` e listar em "Sem resposta". Atribuir dono que não foi acordado gera ação que ninguém executa e ninguém cobra.
- **Critério de conclusão observável.** "Falar com o financeiro" não serve. "Resposta por escrito sobre o orçamento de 2027" serve.
- **Anotar a origem da nota.** Transcrição literal e lembrança de duas horas depois têm confiabilidade diferente, e daqui a seis meses ninguém lembra qual foi.

## Etapa 2 — atualizar o contexto

Os documentos em `Contexto/` são hipótese declarada, não retrato. Conversa real é a única coisa que os promove a fato — e é para isso que eles existem.

Para cada afirmação da conversa, verificar se algum documento fala do mesmo assunto:

- **Confirmou uma hipótese** → atualizar o trecho, trocar a marcação de hipótese por evidência, e citar a conversa: `(confirmado na conversa NN, DD/MM)`.
- **Contradisse** → não apagar a versão antiga. Registrar as duas e marcar qual tem evidência. O que estava escrito era a crença anterior, e saber que ela existiu importa.
- **Trouxe assunto novo** → acrescentar na seção certa, marcado com a conversa de origem.
- **Não tocou em nada documentado** → não mexer em nada. A maioria das conversas cai aqui.

Alvos prováveis: `Contexto/drafted-icp.md` (gatilhos, objeções, motivo de churn), `Contexto/drafted-negocio.md` (modelo comercial, ticket, estágio), e a lista de prioridade da última análise em `estrategia/`.

**Mostrar o diff antes de commitar.** Atualização de contexto muda a base de todas as análises seguintes — não passa silenciosamente.

## Etapa 3 — commit

**Antes de commitar, parar e checar quem aparece na ata.**

Este repositório é público. Ata de conversa contém pessoa de fora, e publicar o que alguém disse é diferente de publicar o que você pensa.

- Nome de pessoa física, e-mail, telefone ou cargo identificável: **perguntar antes**. Sugerir usar só o papel ("head de marketing") em vez do nome.
- Nome de empresa: perguntar se pode. Empresa que ainda não é cliente pode não querer aparecer como prospect num repositório aberto.
- Número comercial de terceiro (ticket, orçamento, contrato): **nunca commitar sem autorização explícita** de quem falou.

Se qualquer um dos três aparecer, listar o que é e perguntar antes de qualquer `git add`. A alternativa padrão é anonimizar — `estrategia/conversas/03-saas-saude.md` funciona tão bem quanto o nome real, e a informação estratégica não se perde.

Mensagem de commit: `Registra conversa NN — [assunto]`, mais uma linha por documento de contexto alterado.

## Fechamento

Reportar em três linhas: onde ficou a ata, o que mudou no contexto, e quais ações ficaram sem dono. A terceira é a que importa — ação sem dono é o que faz uma conversa não virar nada.
