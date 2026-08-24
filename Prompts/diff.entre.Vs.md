# O que mudou entre V1, V2 e V3

Comparativo das três versões do prompt de análise e das respostas que cada uma gerou.

- **Prompts:** `Prompts/V1.md`, `V2.md`, `V3.md`
- **Respostas:** `estrategia/V1-analise-do-documento.md`, `V2-analise-do-negocio.md`, `V3-analise-semanal-01.md`

## Em uma linha

**V1** pergunta de forma aberta e recebe uma crítica de texto. **V2** estrutura a pergunta e recebe uma análise de negócio. **V3** dá memória e critério à pergunta e recebe um plano com dono e data.

---

## O prompt

| | V1 | V2 | V3 |
|---|---|---|---|
| Forma | Uma frase livre | TAREFA / FORMATO / AMOSTRA / LIMITE | ENTRADA / TAREFA / FORMATO / REGRAS |
| Define o objeto? | Não | Não — "o problema apresentado" | Sim — campo OBJETO |
| Define o alvo? | Não | Não — "resultado atual" sem dizer qual | Sim — campo OBJETIVO |
| Tem estado anterior? | Não | Não | Sim — ESTADO ANTERIOR + MUDOU NA SEMANA |
| Rubrica de prioridade | — | Ausente: pede classificar sem dizer por qual eixo | Impacto, esforço, dependência |
| Teto de volume | Nenhum | Nenhum | 5 causas, 6 oportunidades |
| Exige rastreabilidade | Não | "não invente", sem mecanismo | Citação da fonte obrigatória |
| Pede corte | Não | Não | Sim — seção "não fazer" |
| Serve para rodar semanalmente | Não | Não — sem memória, repetiria a mesma lista | Sim |

---

## A resposta

| | V1 | V2 | V3 |
|---|---|---|---|
| O que analisou | O texto do `problema-drafted.md` | A situação da Drafted | Por que a lista da rodada anterior não andou |
| Tamanho | ~1.400 palavras | ~2.050 palavras | ~1.700 palavras, com teto |
| Priorização | Ausente | Alta/média/baixa, justificada em prosa | Tabela com eixos nomeados |
| Próximo passo | Um, no fim | Um por oportunidade | Um por prioridade alta, com dono, prazo e critério observável |
| Incerteza | Implícita | Explícita por escolha de quem escreveu | Explícita por regra, com custo de resolução |
| Diz o que não fazer | Não | Não | Sim |

---

## Conteúdo — o que só cada uma tem

**V1**
Correção factual linha a linha (100M users, X API, scraping legal). Crítica de retórica e estrutura narrativa. Ordem sugerida dos blocos numa reescrita. Frases a puxar dos outros docs ("atenção → interpretação").

**V2**
Causas-raiz em vez de falhas de argumento: alocação de atenção, centro de gravidade errado, janela temporal se fechando. Dependência entre oportunidades (O6 destrava O3 e O4). Itens operacionais sem relação com o texto: LinkedIn travado, Reputational Risk como porta de entrada, score em banda, proxy de receita.

**V3**
Delta explícito contra a rodada anterior. Identificação de que O6 podia ser inexecutável e travaria a fila inteira — defeito da própria rodada anterior, invisível sem comparação. Ramo alternativo O6b, que remove a dependência. Dono, prazo e critério de conclusão por item. Lista do que **não** fazer. O9: registrar o objetivo, que nenhum documento continha.

**O que se manteve nas três**
O diagnóstico central de que o documento de problema vende medição, e medição é a parte commodity do negócio. V1 chama de erro de framing. V2 mostra que é sintoma de inversão de validação — construir antes de vender. V3 não repete: mostra que o diagnóstico correto não produziu movimento, e que o gargalo migrou de "não sabemos o que fazer" para "a lista não tem dono".

---

## O salto de cada transição

**V1 → V2 — mudou o objeto.**
Saiu da crítica do texto e entrou na causa do resultado.
*Ganho:* acionabilidade. *Custo:* 45% mais longo, com sobreposição entre as seções 3 e 5.

**V2 → V3 — mudou o nível.**
Parou de responder melhor e passou a perguntar melhor.
*Ganho:* comparabilidade entre rodadas e itens executáveis em vez de recomendações. *Custo:* exige preencher a entrada antes de rodar — deixa de ser copiar e colar.

---

## Limite observado na rodada 01 do V3

O V3 foi rodado 26 minutos depois do V2, sem que nada tivesse mudado no negócio. O formato funcionou — produziu delta, achou um defeito real da rodada anterior e gerou plano com dono —, mas a coluna de status ficou inteira em "parado" por ausência de intervalo, não por estagnação.

Consequência prática: **o V3 só deve rodar quando houver fato novo.** Rodado sobre estado parado, ele produz documento em vez de decisão — que é exatamente a causa C3 que ele mesmo diagnostica.
