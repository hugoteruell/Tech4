# Análise — Drafted

**Objeto:** o problema apresentado em `problema-drafted.md`, lido junto de `drafted-negocio.md`, `drafted-icp.md` e `About me.md`.

**Base de evidência:** os quatro arquivos do repositório. Não há dado de cliente, receita, contrato ou uso. Tudo que depende disso está marcado como **Hipótese**.

---

## 1. Problema central

Não é um problema de produto nem de mercado. É um **desalinhamento entre três camadas que deveriam se sustentar mutuamente e hoje se contradizem**:

| Camada | O que ela afirma |
|---|---|
| Problema declarado | "Ninguém mede como você é visto por IA" — o vácuo é de **medição** |
| Negócio que sustenta a empresa | "Não deveria vender só medição... o que segura cliente é operação rodando" — o valor está na **execução** |
| Evidência disponível | "Não existe registro de ticket, contrato ou base de clientes" — nenhuma das duas afirmações foi **testada com comprador** |

O documento de problema vende o componente que o documento de negócio classifica como commodity. E nenhum dos dois se apoia em cliente pagante.

O resultado atual: uma empresa com produto rodando, metodologia documentada, site no ar e posicionamento definido — que ainda não sabe se alguém paga por isso, e cujo argumento de entrada está ancorado na parte mais barata e mais copiável da oferta.

---

## 2. Principais causas

### 2.1 — Inversão da ordem de validação

O próprio material diagnostica: *"resolveu a parte difícil de construir antes de resolver a parte difícil de vender"*. A causa não é preguiça comercial — é que o problema técnico (scraping, normalização, ponderação, não-determinismo) é intelectualmente mais interessante e dá retorno imediato de progresso. Conversa com comprador não dá. O gargalo é de **alocação de atenção**, e ele se auto-reforça.

### 2.2 — O centro de gravidade da empresa está no componente mais atacável

*"O que amarra as quatro frentes: o scorecard."* Toda a arquitetura pende de um número que os próprios docs descrevem como: não-determinístico ("não entrega o mesmo resultado duas vezes"), metodologicamente discutível ("peso é decisão, não medida") e substituível ("uma ferramenta de AI visibility barata resolve 70% do valor percebido").

Se o eixo estrutural é o item mais frágil, cada aumento de sofisticação do scorecard aumenta o custo de construção sem aumentar a defensibilidade.

### 2.3 — O elo entre o número e o dinheiro nunca foi construído

*"Provar que mover o número move receita. Esse é o gargalo do negócio inteiro."* Isso está corretamente identificado no doc de negócio e **ausente** no doc de problema. Enquanto o elo não existir, o contrato vive no pedaço cortável do orçamento — e é exatamente o que o próprio ICP descreve como churn de renovação: *"o CFO pergunta o que voltou e o CMO não tem resposta em número de negócio"*.

### 2.4 — Quatro frentes antes do primeiro cliente documentado

Intelligence, Execution, House e Circle exigem quatro capacidades operacionais distintas: engenharia de dados, PR/conteúdo, produção audiovisual e relacionamento com creators. Para uma operação sem base de clientes registrada, isso dispersa capacidade escassa e cria o risco já antecipado no próprio doc: *"quatro fornecedores dentro de uma fatura só"*.

### 2.5 — As lacunas de produto estão exatamente nos pontos de maior pressão de venda

Não é coincidência ruim, é sintoma de priorização por facilidade técnica:

- **Reputational Risk** é o pilar pendente — e é *"justamente o pilar que um cliente em crise vai perguntar primeiro"*.
- **LinkedIn está fora**, bloqueado por *"confirmação do co-founder"*. Para os setores B2B e serviços financeiros do ICP, isso é um buraco na demo. E o bloqueio é **decisório, não técnico** — o tipo de gargalo mais barato de remover e mais fácil de esquecer.

### 2.6 — O ICP é dedução a partir do produto, não observação de comprador

O documento admite: *"hipótese de trabalho, não retrato de base"*. A consequência é uma inversão de causalidade — o produto está definindo quem é o cliente, em vez do cliente definir o produto. Porte, faixa de receita e ranking de setores foram inferidos da lógica das quatro frentes.

### 2.7 — A vantagem competitiva é temporal e está sendo gasta em construção

*"Antecipação — comprar antes do concorrente. Esse é o argumento mais forte hoje e o que menos dura."* O ativo que hoje mais vende é o que mais se deprecia. Cada semana investida em refinamento de metodologia consome janela sem convertê-la em cliente.

---

## 3. Pontos de oportunidade

**O1 — Trocar o produto de entrada de "relatório" para "evidência de perda"**
Hoje a venda entra pelo diagnóstico *"porque é concreto e mensurável"*. Isso ancora a conversa em medição — exatamente o que o cliente poderá comprar mais barato de outro fornecedor. A oportunidade é entrar pela cena que já está escrita no ICP: rodar, **antes da reunião**, a consulta real da categoria do prospect nos modelos e chegar com o print do concorrente sendo recomendado. O score deixa de ser a oferta e passa a ser a explicação do porquê. Muda o que está sendo comprado: de "um relatório" para "uma perda que você não sabia que tinha".

**O2 — Fechar o elo número→receita com um proxy rastreável, não com metodologia**
*(Hipótese: nunca foi tentado — não há menção a isso em nenhum dos docs.)* O elo provavelmente não precisa de prova estatística de causalidade, precisa de um instrumento barato que tire o contrato da zona "não mede nada": pergunta de origem no primeiro contato do lead ("como você chegou até nós?"), somada ao tráfego de referral vindo de domínios de IA. Não prova causalidade — resolve o problema real, que é o CMO não ter o que responder ao CFO na renovação.

**O3 — Reduzir de quatro frentes para uma frente vendida e três capacidades acessíveis**
*(Hipótese, depende da estrutura de custo, que não está documentada.)* House e Circle podem ser entregues via parceiro ou freela sem serem posicionadas publicamente como frentes próprias até existir base de clientes. Ganho duplo: libera capacidade e elimina o risco dos quatro interlocutores, que o próprio doc já marca como causa de churn.

**O4 — Converter Reputational Risk de pendência em porta de entrada**
Dos cinco gatilhos de compra listados no ICP, quatro são de melhoria (querer aparecer melhor) e apenas um é de urgência: *"uma avaliação ruim ou crise aparece no topo do Google"*. Melhoria não tem prazo; crise tem prazo e frequentemente tem orçamento fora do budget de marketing. **Hipótese:** Reputational Risk pode ter ciclo de venda mais curto que os outros quatro pilares somados — e hoje é o único que não existe.

**O5 — Destravar a decisão sobre LinkedIn**
É um item de decisão pendente há tempo suficiente para aparecer em dois documentos diferentes como "aguardando confirmação". Não é escopo, é uma conversa de quinze minutos com o co-founder. É a oportunidade de melhor relação impacto/esforço da lista inteira.

**O6 — Substituir o ICP deduzido por 3 a 5 conversas**
O roteiro já está escrito no fim do `drafted-icp.md` (quatro perguntas). O próprio documento conclui: *"Três conversas honestas substituem este arquivo inteiro."* A oportunidade não é fazer pesquisa — é **executar o plano que já existe e está parado**.

**O7 — Tratar o não-determinismo como cláusula, não como defeito a esconder**
Hoje a variação entre execuções é um passivo que *"precisa ser explicada ao cliente antes, nunca depois"*. A oportunidade é publicar o score como **banda** (intervalo observado nas cinco execuções) em vez de ponto. **Hipótese:** isso converte a objeção "rodei ontem e deu diferente" em demonstração de rigor metodológico, e diferencia de ferramenta barata que entrega número único e falsamente preciso.

**O8 — Corrigir os erros factuais do `problema-drafted.md`**
"ChatGPT tem 100M users" (marco de 2023), "X API aberta" (falso desde 2023) e "web scraping é legal para dados públicos" (confunde legalidade com Termos de Uso). Custo de correção próximo de zero; custo de não corrigir é a credibilidade da apresentação inteira.

---

## 4. Prioridade

| # | Oportunidade | Prioridade | Motivo |
|---|---|---|---|
| **O6** | Entrevistar quem já pagou | **Alta** | É a única que **desbloqueia as outras sete**. Sem ela, O1, O3 e O4 são palpite informado. Custa uma semana e o roteiro já existe. |
| **O2** | Elo número→receita | **Alta** | Ataca o gargalo declarado do negócio inteiro. Sem isso, todo contrato é cortável e o churn de renovação é estrutural, não corrigível por atendimento. |
| **O1** | Entrada por evidência de perda | **Alta** | Ataca a causa 2.2 diretamente: tira o peso do scorecard e coloca na constatação, que é o que gera urgência. Também é o que menos depende de novo desenvolvimento. |
| **O5** | Destravar LinkedIn | **Alta** | Bloqueio decisório, não técnico. Impacto direto na credibilidade da demo para dois setores do ICP. Melhor relação impacto/esforço da lista. |
| **O4** | Reputational Risk como entrada | **Média** | Impacto potencialmente alto, mas exige construir o pilar que falta. Sobe para alta **se** O6 confirmar que crise é o gatilho dominante. |
| **O3** | Reduzir frentes | **Média** | Ganho real de foco, mas é decisão estrutural com implicação de receita. Não deve ser tomada antes de O6 mostrar por qual frente o cliente entra. |
| **O7** | Score em banda | **Média** | Resolve uma objeção certa e é barato de implementar, mas não gera venda sozinha. Vale fazer junto do próximo ciclo de produto. |
| **O8** | Corrigir erros factuais | **Média** | Não muda resultado comercial e por isso não é alta. É média e não baixa porque o custo é quase zero e o risco de manter é desproporcional — um dado errado na abertura contamina tudo que vem depois. |

---

## 5. Recomendação — próximo passo por oportunidade

**O6 — Entrevistas.** Listar todo mundo que já pagou ou chegou perto de pagar, incluindo quem disse não. Rodar as quatro perguntas que já estão no `drafted-icp.md`, sem apresentar o produto. Ouvir especialmente o **evento específico** que motivou a busca. Prazo: uma semana. Saída: uma lista dos gatilhos reais, ordenada por frequência.

**O2 — Elo com receita.** Não construir metodologia. Definir, para o próximo cliente que entrar, **duas** métricas de negócio acordadas na assinatura (ex.: origem declarada do lead + referral de domínios de IA), com leitura mensal. O objetivo do próximo passo não é provar causalidade — é garantir que exista uma resposta em número de negócio quando o CFO perguntar.

**O1 — Entrada por evidência.** Escolher cinco prospects do ICP, rodar as consultas de categoria nos modelos e montar um one-pager de uma página por empresa mostrando o que a IA responde hoje. Usar como abordagem fria. Métrica de teste: taxa de resposta comparada à abordagem atual.

**O5 — LinkedIn.** Marcar a conversa com o co-founder esta semana e sair dela com uma decisão registrada — dentro do escopo, fora dele com justificativa, ou adiado com data. O problema não é a resposta, é a pendência aberta.

**O4 — Reputational Risk.** Não desenvolver ainda. Aguardar O6. Se crise aparecer como gatilho recorrente nas entrevistas, ele vira a próxima entrega de produto e provavelmente o novo produto de entrada. Se não aparecer, desce de prioridade e o esforço vai para O1.

**O3 — Frentes.** Aguardar O6. A decisão ("Intelligence é isca ou produto autônomo?" e "House e Circle são escopo ou upsell?" — as duas perguntas que o próprio doc de negócio deixa em aberto) precisa ser tomada com dado de por onde o cliente realmente entrou, não com lógica de arquitetura.

**O7 — Banda.** Incluir o intervalo observado das cinco execuções no próximo relatório gerado, com uma linha de explicação na página do pilar de AI Perception. Mudança pequena de apresentação, sem alterar o cálculo.

**O8 — Correções.** Aplicar direto no `problema-drafted.md` junto da reescrita já mapeada em `estrategia/V1-analise-do-documento.md`, ou remover a seção "Dados Existem", que concentra os três erros e é fora de escopo para um documento de problema.

---

**O que essa análise não pode afirmar:** se existe cliente pagando hoje, qual é o ticket, quanto dura um contrato, qual frente traz mais receita e qual foi o motivo real de saída de quem saiu. Os quatro documentos são consistentes entre si e nenhum deles contém um cliente. Enquanto isso não mudar, toda priorização acima — inclusive esta — é dedução sofisticada.
