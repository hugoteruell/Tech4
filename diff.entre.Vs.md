# O que mudou da V1 para a V2

## Em uma linha

A V1 analisa **o documento**. A V2 analisa **o negócio**.

---

## Objeto

| | V1 | V2 |
|---|---|---|
| O que está sob análise | O texto do `problema-drafted.md` | A situação da Drafted |
| Pergunta que responde | "Esse documento convence?" | "Por que o resultado atual é esse?" |
| Quem é o leitor implícito | Quem vai reescrever o doc | Quem vai decidir a próxima semana |

---

## Formato

| | V1 | V2 |
|---|---|---|
| Estrutura | Livre — veredito, problemas, erros, oportunidades | Fixa — 5 seções pedidas no prompt |
| Tamanho | ~1.400 palavras | ~2.050 palavras |
| Priorização | Ausente (lista ordenada por impacto, sem classificação) | Tabela explícita alta/média/baixa com justificativa |
| Próximo passo | Um só, no fim ("quer que eu reescreva?") | Um por oportunidade, com prazo e critério de saída |
| Marcação de incerteza | Implícita | Explícita — cada dedução marcada como **Hipótese** |

---

## Conteúdo

**O que a V1 tem e a V2 não**

- Correção factual linha a linha (100M users, X API, scraping legal)
- Crítica de retórica e estrutura narrativa do texto
- Sugestão de ordem dos blocos do documento reescrito
- Frases específicas a puxar dos outros docs ("atenção → interpretação")

**O que a V2 tem e a V1 não**

- Causas-raiz, não só falhas de argumento — alocação de atenção, centro de gravidade errado, janela temporal se fechando
- Priorização com dependência entre itens (O6 desbloqueia O1, O3 e O4)
- Oportunidades operacionais que não têm nada a ver com o texto: LinkedIn travado, Reputational Risk como porta de entrada, score em banda, proxy de receita
- Declaração explícita do que a análise **não pode** afirmar

**O que se manteve**

O diagnóstico central é o mesmo nas duas: o documento de problema vende medição, e medição é a parte commodity do negócio. A V1 chama isso de erro de framing; a V2 mostra que é sintoma de uma inversão de validação — construir antes de vender.

---

## Grau de acionabilidade

- **V1** termina em edição de texto: sabe-se o que reescrever.
- **V2** termina em agenda: sabe-se o que fazer na segunda-feira e em que ordem.
