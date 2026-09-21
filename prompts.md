# Prompts do projeto

Registro de todos os prompts usados na operação. Cada um tem um dono de arquivo — este índice não duplica o texto deles, para não haver duas versões divergindo.

## Prompts de análise — versionados

Vivem em [`Prompts/`](Prompts/). São o ciclo de decisão do projeto.

| Versão | Arquivo | O que faz | Resposta que gerou |
|---|---|---|---|
| v1 | `Prompts/V1.md` | Pedido livre, sem estrutura | `estrategia/V1-analise-do-documento.md` |
| v2 | `Prompts/V2.md` | Estruturado em TAREFA / FORMATO / AMOSTRA / LIMITE | `estrategia/V2-analise-do-negocio.md` |
| **v3** | **`Prompts/V3.md`** | **Corrente.** Entrada preenchida, memória entre rodadas, rubrica de prioridade, seção do que não fazer | `estrategia/V3-analise-semanal-01.md` |

[`Prompts/diff.entre.Vs.md`](Prompts/diff.entre.Vs.md) registra o que mudou entre as três versões e por quê. Ler antes de propor alteração em qualquer uma.

**Regra do ciclo:** o V3 só roda quando há fato novo. Rodado sobre estado parado, produz documento em vez de decisão — que é a causa C3 que ele mesmo diagnostica.

## Prompts de rotina — automação

| Rotina | Onde está o prompt | Regra que executa |
|---|---|---|
| `vigia-parados` | [`automacoes.md`](automacoes.md), seção "Prompt completo" | Regra 1 de `regras.md` |

## Prompts empacotados como skill

Vivem em [`.claude/skills/`](.claude/skills/) e são invocáveis por nome. Nenhuma delas edita arquivo sozinha — todas propõem e esperam decisão.

| Skill | O que faz |
|---|---|
| `consistencia` | Cruza os `.md` e aponta contradição, dado vencido, referência quebrada e pendência órfã |
| `fecha-conversa` | Nota bruta de reunião vira ata com dono e prazo, atualiza o contexto e commita |
| `resumo-semanal` | Status da semana com evidência do git; a saída preenche o campo `MUDOU NA SEMANA` do V3 |
| `lead-research-assistant` | Identifica empresas-alvo a partir do ICP. De terceiro — origem e licença em `.claude/skills/README.md` |

## Convenções que todo prompt deste repositório segue

Herdadas do [`CLAUDE.md`](CLAUDE.md):

- Toda afirmação factual citada da fonte. Sem fonte, prefixar `Hipótese:`.
- Toda análise fecha com o que ela **não** pode afirmar.
- Nunca inventar dado de cliente, ticket, contrato ou receita — não existe nenhum registrado.
- Rotina que não encontra nada fica em silêncio, mas o silêncio é registrado com os números verificados.
