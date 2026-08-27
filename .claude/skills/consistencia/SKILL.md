---
name: consistencia
description: Cruza os documentos markdown do repositório e aponta inconsistências — contradições factuais entre arquivos, afirmações sem fonte, dados sem data, referências quebradas, IDs de oportunidade duplicados ou órfãos, e pendências que atravessam vários arquivos sem resolução. Use quando pedirem para checar os docs, antes de apresentar o material a mentor, banca, investidor ou cliente, e depois de editar qualquer arquivo em Contexto/, Prompts/ ou estrategia/.
---

# Checagem de consistência

Este repositório não tem código. O que quebra aqui não é build, é credibilidade: dois documentos afirmarem coisas diferentes sobre o mesmo fato, um número velho sobreviver a três revisões, ou um ID de oportunidade mudar de significado entre rodadas.

Nada nesta skill corrige arquivo. Ela **aponta e propõe**. A decisão é de quem escreveu.

## Procedimento

1. Listar todos os `.md` do repositório, incluindo `CLAUDE.md` e a raiz.
2. Ler todos por inteiro. Não amostrar — inconsistência mora no detalhe que o resumo descarta.
3. Montar a lista de afirmações factuais de cada arquivo: número, data, nome, status, decisão.
4. Cruzar arquivo contra arquivo, procurando as seis classes abaixo.
5. Reportar no formato da seção "Saída".

## As seis classes

### 1. Contradição factual
A mesma coisa afirmada de dois jeitos em arquivos diferentes.

> Exemplo real deste repo: `problema-drafted.md` afirma que a métrica de percepção em IA "não existe"; `Contexto/drafted-negocio.md` afirma que "ferramenta de AI visibility barata já existe e vai ficar mais barata".

Sinalizar sempre. É a classe mais cara — é a que derruba uma apresentação.

### 2. Contradição de confiança
O mesmo fato tratado como certeza num arquivo e como hipótese em outro.

> Exemplo real: a limitação da API do Instagram aparece como risco material de produto em `drafted-negocio.md` e como detalhe entre parênteses em `problema-drafted.md`.

Não é erro de fato, é erro de tom — e produz o mesmo estrago quando as duas versões chegam ao mesmo leitor.

### 3. Afirmação sem fonte
`CLAUDE.md` exige que toda afirmação factual seja citada da fonte, ou prefixada com `Hipótese:`. Apontar as que não têm nem uma coisa nem outra.

Não apontar o que o próprio documento já declara como dedução no cabeçalho — `drafted-icp.md` e `drafted-negocio.md` fazem isso e estão corretos.

### 4. Dado sem data ou vencido
Número de mercado, volume de usuário, estado de API ou preço sem data de referência. Qualquer um desses envelhece em meses.

> Exemplo real: "ChatGPT tem 100M users" — marco de 2023 mantido em documento de 2026. E "X API aberta", falso desde 2023.

Marcar também dado que tem data mas passou de doze meses.

### 5. Referência quebrada
Caminho de arquivo, nome de seção ou nome de documento citado que não existe mais. Arquivos foram renomeados e movidos neste repo; citações internas ficam para trás.

Verificar cada caminho citado contra o disco.

### 6. ID e pendência
- **IDs de oportunidade** (`O1`, `O2`, …) precisam ser estáveis entre rodadas: o mesmo ID sempre o mesmo item. Apontar ID reaproveitado para coisa diferente, ID citado que nunca foi definido, e o próximo ID livre.
- **Pendências órfãs**: "aguardando", "a validar", "a decidir", "TODO", "pendente". Se a mesma pendência aparece em mais de um arquivo sem resolução em nenhum, ela não está aguardando informação — está sem dono. Apontar com a contagem de arquivos em que aparece.

## Saída

Abrir com a contagem por severidade. Depois um bloco por achado:

```
### [Severidade] Título curto do achado
**Classe:** contradição factual
**Onde:**
- `arquivo-a.md:12` — "trecho literal"
- `arquivo-b.md:87` — "trecho literal que contradiz"
**Por que importa:** uma frase.
**Proposta:** o que fazer, e em qual dos dois arquivos.
```

Severidade:
- **Alta** — contradição factual entre documentos, ou dado comprovadamente errado. Chega ao leitor externo.
- **Média** — afirmação sem fonte, dado sem data, contradição de confiança, pendência órfã.
- **Baixa** — referência quebrada, ID fora de sequência, nomenclatura inconsistente.

## Regras

- **Nunca editar arquivo.** Propor a correção e parar. Estes documentos são posição estratégica, não configuração.
- **Sempre citar os dois lados** com arquivo, linha e trecho literal. Achado sem as duas pontas não é verificável e não deve ser reportado.
- **Distinguir contradição de evolução.** Se um documento é mais recente e declara explicitamente que substitui a posição anterior, isso é mudança de posição registrada, não inconsistência. Mencionar em nota, não como achado.
- **Não reportar o que o documento já admite.** Um arquivo que se declara hipótese no cabeçalho está cumprindo a regra, não a violando.
- **Não inventar o que deveria estar certo.** Quando os dois lados forem plausíveis e não houver como decidir pela fonte, dizer que precisa de decisão do autor em vez de escolher.
- **Fechar com o que não foi possível verificar** — dado externo que exigiria busca, afirmação sobre cliente ou receita que não tem registro em lugar nenhum.
