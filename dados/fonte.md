# Fonte de dados

## Fonte canônica

**O próprio repositório Git** — especificamente a última análise em `estrategia/V3-analise-semanal-NN.md` (tabela de prioridade) cruzada com o histórico de commits.

Não existe ERP, CRM ou banco de dados neste projeto. A operação documentada aqui é o **ciclo de trabalho estratégico da Drafted**: rodadas de análise, itens de oportunidade com ID estável (O1…O9), atas de conversa e as skills que operam esse ciclo. O dado que as regras consomem é o estado desses itens.

## Onde vive

| Dado | Caminho |
|---|---|
| Itens de oportunidade e prioridade | `estrategia/V3-analise-semanal-NN.md`, seção `## 4. Prioridade` |
| Evidência de movimento | `git log` do repositório |
| Conversas com o mercado | `estrategia/conversas/NN-*.md` — uma ata por conversa |
| Extrato tabular dos itens | `dados/amostra.csv` |
| Contexto de negócio | `contexto/` |

Remoto: `https://github.com/hugoteruell/Tech4`

## Responsável pela atualização

**Hugo.** É o único responsável nomeado em todo o repositório (`contexto/About me.md`). Não há outra pessoa com acesso de escrita.

As atas de conversa são geradas pela skill `fecha-conversa`; a tabela de prioridade, pela rodada do prompt `Prompts/V3.md`.

## Frequência

| Fonte | Atualização |
|---|---|
| Tabela de prioridade | A cada rodada de análise — **apenas quando há fato novo**, por regra do `CLAUDE.md` |
| `git log` | A cada commit |
| Atas de conversa | Quando uma conversa acontece |
| `dados/amostra.csv` | Regerado a cada nova rodada de análise |

A última rodada é de **24/08/2026**. Não houve rodada desde então.

## Campos relevantes

Campos de `dados/amostra.csv` que as regras consultam:

| Campo | Tipo | Usado por |
|---|---|---|
| `id` | texto (O1…O9) | Ambas as regras |
| `prioridade` | Alta / Média / Baixa / reservado | Regra 1 |
| `status` | nao_iniciado / concluido / bloqueado / aguardando_O6 | Regra 1 |
| `data_origem` | AAAA-MM-DD | Regra 1, para calcular dias parados |
| `dias_parado` | inteiro | Regra 1, condição dos 7 dias |
| `evidencia` | texto | Ambas, para o alerta ser acionável |

A Regra 2 consulta também o `git log` por semana ISO e a contagem de arquivos em `estrategia/conversas/`.

## Regra de prioridade

Se duas fontes divergirem:

1. **O `git log` ganha de qualquer documento.** Commit tem data e conteúdo verificáveis; texto dentro de um `.md` é afirmação.
2. **A análise mais recente ganha da anterior**, desde que declare explicitamente que substitui a posição antiga — como manda `contexto/cemiterio.md`.
3. **`dados/amostra.csv` nunca ganha**, porque é extrato derivado. Se ele divergir da análise, o CSV está desatualizado e deve ser regerado.

## Limitações atuais

Declaradas sem maquiagem:

- **Não há dado de negócio nenhum.** Nem cliente, nem ticket, nem contrato, nem receita, nem volume. `contexto/drafted-negocio.md` afirma isso textualmente, e o `CLAUDE.md` proíbe estimar esses números.
- **`contexto/drafted-icp.md` é hipótese, não retrato.** Foi construído a partir da lógica do produto, não de entrevista com comprador. O próprio arquivo declara isso no cabeçalho.
- **A pasta `estrategia/conversas/` ainda não existe.** Zero conversas registradas até 21/09/2026.
- **A fonte é de baixa frequência por desenho.** A regra do `CLAUDE.md` proíbe rodar a análise sem fato novo, então a tabela de prioridade pode ficar semanas sem mudar. Isso é intencional, não falha — e é justamente o que a Regra 1 detecta.
- **Não há agendador configurado.** As rotinas são disparadas manualmente. Nenhuma execução automática ocorreu até esta data.
