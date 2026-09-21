# O Problema: Reputação Invisível em Sistemas de IA

## A Realidade Mudou

Marcas não são mais avaliadas apenas pelo que controlam. Um **sistema de IA vê você antes que seus clientes veem**.

Quando um cliente potencial faz uma pergunta a ChatGPT, Claude, Perplexity — ou quando uma corporação faz RAG interno sobre seu setor — quem decide se você existe é um modelo generativo. Você é percebido através de dados: sociais, web, reviews, menções. Os LLMs indexam tudo isso e sintetizam você em uma narrativa.

**Você não sabe como essa narrativa fica.**

---

## O Vácuo

Hoje, marcas medem:
- **Marketing tradicional:** cliques, impressões, CTR
- **Performance marketing:** conversões, CPA, ROAS
- **Social media:** seguidores, engagement rate, alcance
- **PR:** menções, share of voice, earned media

Nenhuma dessas métricas responde uma pergunta básica:

> **Como você é visto por inteligência artificial?**

Já existe quem tente responder: uma categoria inteira de ferramentas de AI visibility surgiu para medir menção de marca em LLM. O problema é outro. Medir virou a parte fácil e está ficando barata. O que ninguém resolve é o passo seguinte — quem, dentro da empresa, responde por essa interpretação e opera para mudá-la.

---

## Por que Isso Importa

### Para Marcas

Um cliente ganha 50% de seguidores no Instagram. Ótimo. Mas:
- Como isso se traduz em percepção dentro de um LLM?
- Você aparece quando alguém pede recomendação?
- Você aparece com qual contexto? Comparado a quem?
- Seus dados estão sendo consumidos por IA de forma consistente, ou desaparece em comparação com concorrentes?

Ninguém sabe responder isso.

### Para Analistas (agências, consultores)

Um cliente paga por relatório mensal. O que você entrega?
- Dashboard com 50 métricas de diferentes plataformas
- "Engagement subiu 3%"
- Recomendações genéricas

Ninguém sabe qual desses números *importa realmente*. Qual ação vai impactar como você é percebido por IA?

### Para LLMs e Sistemas de Recomendação

Eles consomem dados públicos que estão desorganizados. Instagram stories desaparecem. TikTok vídeos somem. Dados de web desatualizam. A percepção resultante é:
- Incompleta
- Temporal (muda conforme crawler atualiza)
- Sem contexto claro

---

## Por que Ninguém Resolveu Ainda

### É Complexo

Medir reputação em IA não é como medir cliques (binário, fácil). Envolve:
- Raspar dados de múltiplas plataformas (Instagram, TikTok, X, web, reviews)
- Normalizar métricas diferentes entre plataformas
- Entender pesos relativos (o que importa mais?)
- Treinar ou usar modelos que indexem o que LLMs veem
- Medir consistência temporal

É um problema de engenharia, não de dashboard pronto.

### Não é Óbvio que é um Problema

Marcas ainda acreditam em "mais seguidores = melhor". Agências tradicionais vendem números. Ferramentas de social media agregam métricas velhas de novo jeito.

Ninguém disse: "não, o problema é outro — você não sabe como você é visto por IA."

### Não tinha dados públicos suficientes até recentemente

Alguns anos atrás: LLMs não eram universais o suficiente pra justificar medição específica.

Agora: assistentes de IA entraram na rotina de decisão de compra, e o hábito de perguntar antes de escolher deixou de ser de nicho. Perplexity cresce, Claude é usado em RAG corporativo, e sistemas de recomendação passaram a se alimentar de LLMs.

> `Hipótese:` este parágrafo precisa de **um número com fonte e data** — volume de uso do ChatGPT ou share de jornada de compra que passa por IA. Sem isso, ele é asserção sem lastro, e é exatamente onde a leitura de um investidor para.

A reputação em IA deixou de ser futurista e virou hoje.

---

## O Padrão Atual Não Funciona

**Métrica Social Vazia:**
- "Temos 50k seguidores, 5% engagement"
- Por quê? Porque não temos ferramenta melhor
- O que muda? Nada, era apenas número

**Métrica que Importaria:**
- "Quando buscam nossa categoria em um LLM, aparecemos? Em qual posição entre concorrentes?"
- "Nossos dados aparecem de forma consistente ou desatualizado?"
- "O contexto em que aparecemos é favorável?"
- "Como podemos melhorar a percepção, dado como LLMs consomem dados?"

Uma ferramenta responde a primeira. Nenhuma responde a última — e a última é a única que muda o que a empresa faz na segunda-feira.

---

## O Momento é Agora

### Modelos Existem

Você pode treinar ou usar modelos existentes que indexem o que LLMs veem. Não é ficção, é construível.

### Urgência Existe

Mais dinheiro se move pra IA. Mais decisões são tomadas por LLMs. Marcas começam a perceber que desaparecem em sistemas de IA sem saber por quê.

---

## O Problema em Uma Frase

**Medir como a IA te interpreta já é possível e está ficando barato. O que ninguém faz é responder por essa interpretação e operar para mudá-la — e é aí que a receita se perde, antes do primeiro clique.**

---

## Métrica

| Métrica | Alvo | Como confiro |
|---|---|---|
| Conversas com o ICP realizadas (contagem acumulada) | De **0** para **5** até **05/10/2026** | **Onde:** contar os arquivos `.md` em `estrategia/conversas/` — uma ata por conversa, gerada pela skill `fecha-conversa`. **Cálculo:** contagem simples de arquivos; não conta e-mail enviado sem resposta, só conversa realizada. **Frequência:** toda segunda às 9h, junto da execução da Regra 1. **Quem atualiza:** Hugo, ao fechar cada conversa. |

**Por que esta métrica e não outra.** O repositório não tem cliente, receita, ticket nem contrato — `contexto/drafted-negocio.md` declara isso, e o `CLAUDE.md` proíbe estimar esses números. Conversa realizada é a única coisa hoje verificável no disco que muda o estado do problema: sem ela, `contexto/drafted-icp.md` continua sendo hipótese construída a partir da lógica do produto, e não retrato de comprador.

**Origem do alvo.** O número 5 vem do item **O6b** da rodada 01 (`estrategia/V3-analise-semanal-01.md`), que já especifica cinco conversas frias com empresas do ICP. Não é alvo novo — é o alvo que já estava escrito, agora com prazo.

**Estado atual verificado em 21/09/2026:** a pasta `estrategia/conversas/` não existe. Zero conversas registradas, 28 dias após a rodada que definiu o item.
