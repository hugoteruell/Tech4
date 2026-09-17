# Cemitério

O que já se acreditou neste projeto e se descobriu estar errado.

Existe por um motivo prático: sem isso, a mesma ideia morta volta a cada rodada com roupa nova, e ninguém lembra por que ela foi enterrada. Aqui nada é apagado — a crença antiga fica escrita ao lado do que a derrubou.

**Como usar:** antes de propor qualquer coisa, ler. Se a ideia já está aqui, ou você tem evidência nova que não existia quando ela morreu, ou ela continua morta.

---

## 1. "Ninguém mede como você é visto por IA"

**Acreditava-se:** o vácuo era de medição, e a métrica não existia.
**O que derrubou:** o próprio `drafted-negocio.md` já dizia que ferramenta de AI visibility barata existe e vai ficar mais barata. A categoria GEO/AEO tem dezenas de players com funding.
**Quando:** 24/08/2026 · corrigido no commit `2ce4701`
**O que mudou:** o problema deixou de ser medir e passou a ser quem, dentro da empresa, responde pela interpretação e opera para mudá-la. Medição virou a parte fácil da tese, não a tese.

## 2. Os números que provavam o "por que agora"

**Acreditava-se:** "ChatGPT tem 100M users", "X API aberta", "web scraping é legal para dados públicos".
**O que derrubou:** o primeiro é marco de 2023 num documento de 2026. O segundo é falso desde 2023 — e o produto v1 depende de X. O terceiro confunde legalidade com Termos de Uso, que Instagram e TikTok proíbem.
**Quando:** 24/08/2026 · seção "Dados Existem" removida em `2ce4701`
**O que mudou:** o documento de problema parou de tentar provar viabilidade técnica. Viabilidade é assunto de outro documento, e era ali que estavam os três erros.

## 3. "Entrevistar quem já pagou" era um passo executável

**Acreditava-se:** O6 começava com "listar todo mundo que já pagou". O3 e O4 foram postos em espera dependendo dele.
**O que derrubou:** se ninguém pagou ainda — o que os próprios documentos sugerem —, O6 não tem entrada, e a fila inteira trava num item sem o que executar.
**Quando:** rodada 01 do V3, 24/08/2026
**O que mudou:** nasceu o **O6b** — cinco conversas frias com o ICP, uma pergunta só, sem depender de ter cliente. Produz o mesmo insumo.

## 4. Uma lista priorizada é um plano

**Acreditava-se:** a análise V2 entregou oito oportunidades ordenadas por prioridade, com próximo passo para cada.
**O que derrubou:** nenhuma tinha dono. Só uma tinha prazo. Nenhuma tinha data de início. Vinte e quatro dias depois, nenhuma havia começado.
**Quando:** rodada 01 do V3
**O que mudou:** o V3 passou a exigir dono, prazo e critério de conclusão observável — e só para as prioridades altas, porque item sem dono é trava, não próximo passo.

## 5. O prompt estruturado servia para uso semanal

**Acreditava-se:** o prompt V2, com TAREFA/FORMATO/AMOSTRA/LIMITE, bastava para rodar toda semana.
**O que derrubou:** ele não tinha estado anterior. Rodado quatro vezes, produziria quatro documentos quase idênticos e nenhuma leitura de progresso.
**Quando:** revisão que gerou o V3
**O que mudou:** V3 ganhou `ESTADO ANTERIOR`, `MUDOU NA SEMANA` e a seção de delta. Custo: deixou de ser copiar e colar.

## 6. Saúde é o primeiro setor do ICP

**Status: contestado, não enterrado.**

**Acredita-se:** `drafted-icp.md` lista saúde e clínicas em primeiro, tecnologia B2B em quinto.
**O que contesta:** ao consultar categorias reais, o grupo que já demonstra por comportamento acreditar no problema é o SaaS de saúde brasileiro — Feegow, Amplimed, ByDoctor, ClinicWeb, IterClinic, GestãoDS. Cada um publica o próprio comparativo de categoria, ou seja, já gasta dinheiro para controlar a resposta "qual é o melhor".
**Quando:** pesquisa de leads, 24/08/2026
**Por que não está enterrado:** quatro consultas de busca não são amostra. `Hipótese:` derrubada ou confirmada pelas conversas do O6b.
