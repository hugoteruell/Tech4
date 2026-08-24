# O que mudou entre V1, V2 e V3

## Em uma linha

**V1** analisa o documento. **V2** analisa o negócio. **V3** conserta o instrumento que produz a análise.

> Nota: as três versões não são o mesmo tipo de artefato. V1 e V2 são **saídas** (análises). V3 é **entrada** (o prompt semanal reescrito). A comparação abaixo trata disso explicitamente onde importa.

---

## Objeto

| | V1 | V2 | V3 |
|---|---|---|---|
| Tipo de artefato | Análise | Análise | Prompt |
| O que está sob análise | O texto do `problema-drafted.md` | A situação da Drafted | O prompt que gerou a V2 |
| Pergunta que responde | "Esse documento convence?" | "Por que o resultado atual é esse?" | "Como fazer essa pergunta toda semana sem gerar quatro documentos iguais?" |
| Leitor implícito | Quem vai reescrever o doc | Quem vai decidir a próxima semana | Quem vai rodar a análise de novo |
| Arquivo | `V1prompt.md` | `V2-analise.md` | `V3prompt.md` |

---

## Formato

| | V1 | V2 | V3 |
|---|---|---|---|
| Estrutura | Livre | Fixa — 5 seções pedidas | Fixa — 8 seções, com entrada estruturada |
| Tamanho | ~1.400 palavras | ~2.050 palavras | ~500 palavras (é instrumento, não texto) |
| Priorização | Ausente | Tabela alta/média/baixa com justificativa em prosa | Tabela com eixos nomeados: impacto, esforço, dependência |
| Limite de volume | Nenhum | Nenhum | Teto de 5 causas e 6 oportunidades |
| Próximo passo | Um só, no fim | Um por oportunidade | Um por oportunidade **alta**, com dono, prazo e critério de conclusão |
| Marcação de incerteza | Implícita | Explícita, por escolha de quem escreveu | Explícita, por regra do prompt |
| Rastreabilidade | Citações espontâneas | Citações espontâneas | Citação da fonte obrigatória |

---

## Conteúdo

**V1 — o que só ela tem**

- Correção factual linha a linha (100M users, X API, scraping legal)
- Crítica de retórica e estrutura narrativa
- Ordem sugerida dos blocos do documento reescrito
- Frases específicas a puxar dos outros docs ("atenção → interpretação")

**V2 — o que só ela tem**

- Causas-raiz, não falhas de argumento: alocação de atenção, centro de gravidade errado, janela temporal se fechando
- Dependência entre oportunidades (O6 destrava O1, O3 e O4)
- Itens operacionais sem relação com o texto: LinkedIn travado, Reputational Risk como porta de entrada, score em banda, proxy de receita
- Declaração explícita do que a análise **não pode** afirmar

**V3 — o que só ela tem**

- Campo de entrada explícito (OBJETO, OBJETIVO, DECISÃO), que elimina a ambiguidade de "o problema apresentado"
- Memória entre rodadas (ESTADO ANTERIOR + seção DELTA) — a ausência disso era o maior defeito da v2 para uso semanal
- IDs estáveis, para o mesmo item ser rastreado semana a semana
- Seção "não fazer": as versões anteriores só somavam, nunca cortavam
- Lacunas com custo de resolução, transformando hipótese em fila de pesquisa

**O que se manteve nas três**

O diagnóstico central não mudou: o documento de problema vende medição, e medição é a parte commodity do negócio. A V1 chama isso de erro de framing. A V2 mostra que é sintoma de uma inversão de validação — construir antes de vender. A V3 não repete o diagnóstico; garante que ele seja reencontrado com o mesmo rigor na próxima rodada.

---

## Grau de acionabilidade

- **V1** termina em edição de texto: sabe-se o que reescrever.
- **V2** termina em agenda: sabe-se o que fazer na segunda-feira e em que ordem.
- **V3** termina em processo: a agenda passa a ser regerada toda semana com comparabilidade entre rodadas.

---

## O salto de cada transição

**V1 → V2** — mudou o **objeto**. Saiu da crítica do texto e entrou na causa do resultado. Ganho: acionabilidade. Custo: 45% mais longo, com sobreposição entre as seções 3 e 5.

**V2 → V3** — mudou o **nível**. Parou de responder melhor e passou a perguntar melhor. Ganho: comparabilidade entre semanas, que era impossível na v2. Custo: exige preencher a entrada antes de rodar — o prompt deixa de ser copiar e colar.
