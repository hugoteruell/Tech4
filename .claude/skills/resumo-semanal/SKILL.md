---
name: resumo-semanal
description: Lê o repositório e escreve o status da semana — o que andou, o que travou e quais são os próximos passos, sempre com evidência. Use quando pedirem o resumo da semana, o status do projeto, "como estamos", ou antes de rodar a análise semanal, já que a saída daqui alimenta o campo MUDOU NA SEMANA do prompt V3.
---

# Resumo semanal

Relatório de status, não análise. Ele descreve o que aconteceu; quem decide o que fazer a respeito é `Prompts/V3.md`. Não repriorizar, não recomendar estratégia, não criar oportunidade nova — isso é trabalho da análise, e duplicar as duas coisas faz as duas piorarem.

A saída daqui é a entrada de lá: o bloco final preenche o campo `MUDOU NA SEMANA` do V3.

## A distinção que faz esta skill funcionar

**Documento produzido não é progresso.**

Escrever cinco análises e não falar com ninguém é atividade, não avanço — e é exatamente o padrão que a rodada 01 diagnosticou como causa C3. Um relatório que soma documento à coluna de progresso mente para quem o lê.

Por isso o resumo tem duas seções separadas, sempre, e nunca misturadas:

- **Fatos do mundo** — conversa realizada, resposta recebida, decisão tomada com alguém, contato enviado, contrato movido, dado obtido de fora.
- **Movimento no repositório** — arquivo criado, editado, reorganizado.

Se a primeira estiver vazia, ela aparece vazia. Não preencher com a segunda.

## Procedimento

1. **Ler o git.** `git log` do período com datas e arquivos tocados. É a única fonte confiável do que mudou e quando — não confiar em memória de conversa.
2. **Ler a última análise** em `estrategia/`, a mais recente por número. Extrair a tabela de prioridade e os IDs.
3. **Para cada ID, procurar evidência de movimento.** Arquivo novo que o item pedia, edição no arquivo que ele mirava, ata de conversa, decisão registrada. Sem evidência localizável, o item não andou — independentemente do que se lembre.
4. **Contar dias de cada trava.** Para cada item parado, achar a data em que ele apareceu pela primeira vez e calcular há quantos dias está aberto. Trava sem número vira paisagem; trava com "aberta há 34 dias" incomoda, que é o ponto.
5. **Escrever.**

## Saída

```markdown
# Status — semana de DD/MM a DD/MM

## Fatos do mundo
[conversas, respostas, decisões com terceiros, contatos enviados]
[se não houver: "Nenhum registrado no período." e nada mais]

## Movimento no repositório
[arquivos criados e editados, com o commit]

## Por item de prioridade
| ID | Item | Status | Evidência |
Status: andou / travado há N dias / não iniciado

## Travas
[cada uma com há quantos dias, e o que precisa acontecer para destravar]

## Próximos passos
[só os que já têm dono e prazo definidos em algum documento]
[item sem dono não entra aqui — entra em Travas]

## Para o campo MUDOU NA SEMANA do V3
[duas ou três linhas, colável direto na entrada do prompt]
```

## Regras

- **Toda afirmação de movimento precisa de evidência citável** — commit, arquivo, data. Sem isso, o item não andou.
- **Nunca listar documento na seção de fatos do mundo.** Nem "produzimos a análise X". Documento vai para a segunda seção, sempre.
- **Se nada aconteceu, dizer que nada aconteceu.** Um resumo honesto de semana parada é mais útil que um cheio de atividade — é o sinal de que o V3 não deve rodar ainda.
- **Não repriorizar nem sugerir estratégia.** Se algo parece obviamente errado na prioridade, registrar em uma linha como observação e seguir. A decisão é da análise.
- **Próximos passos só com dono e prazo.** Item sem dono não é próximo passo, é trava — e vai para a seção de travas com a contagem de dias.
- **Fechar com o que não foi possível verificar** — o que aconteceu fora do repositório e não deixou registro.
