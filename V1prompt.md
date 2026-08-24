# Análise do `problema-drafted.md` — V1

Análise do documento de problema, usando `drafted-negocio.md`, `drafted-icp.md` e `About me.md` como contraprova. A maior parte dos problemas aparece justamente quando o documento é comparado com o que já está escrito nos outros arquivos.

---

## Veredito

O documento é bem escrito e argumenta o problema **errado**. Ele defende que existe um vácuo de *medição*. Mas o próprio doc de negócio diz, com todas as letras: *"Não deveria vender só medição. Medição vira commodity, ferramenta de AI visibility barata já existe e vai ficar mais barata."*

Então o `problema-drafted.md` está construindo a tese em cima do pilar classificado como o mais frágil e mais copiável do negócio. Esse é o furo central — todo o resto deriva dele.

---

## Os três problemas estruturais

### 1. A premissa "a métrica não existe" é falsa e derrubável em 30 segundos

O doc afirma cinco vezes que ninguém mede isso ("Essa pergunta não tem resposta", "A métrica não existe", "Por que Ninguém Resolveu Ainda"). Em 2026 a categoria GEO/AEO já tem dezenas de players com funding — Profound, Peec, Scrunch, Evertune, Otterly, além de Semrush e Ahrefs que já embutiram rastreamento de menção em LLM no produto core.

Qualquer mentor ou investidor que conheça o mercado abre o Google enquanto você fala. Quando o primeiro slide do problema é factualmente frágil, o resto do pitch passa a ser lido com desconfiança — e o custo não é perder aquele argumento, é perder a credibilidade da sessão inteira.

**Oportunidade:** trocar "ninguém mede" por "todo mundo já mede, e medir não resolve nada". Essa é uma tese mais difícil de atacar, mais verdadeira, e — não por acaso — é exatamente o negócio que existe hoje. A existência dos concorrentes vira munição a favor: eles provam que o mercado existe e que ele parou no lugar errado.

### 2. O documento não descreve o problema que a Drafted resolve

Pelo `drafted-negocio.md`, o problema real tem duas camadas que o `problema-drafted.md` menciona de passagem ou ignora:

- *"Ninguém dentro da empresa é dono desse assunto."* Assessoria cuida de imprensa, agência cuida de social, alguém cuida de review — e a interpretação que a IA monta a partir disso não tem responsável. Isso é um problema **organizacional**, não de dashboard. É muito mais defensável e muito menos commoditizável.
- *"A perda acontece antes do primeiro clique. A empresa nunca vê o lead que não chegou."* Essa é a melhor frase de todo o material, e ela **não está** no documento de problema.

**Oportunidade:** o problema não é "você não sabe seu score". É "você está perdendo receita numa etapa da jornada que não aparece em nenhum relatório, e não existe ninguém na sua empresa com o cargo de consertar isso". Diagnóstico é a evidência do problema, não o problema.

### 3. O documento não enfrenta o argumento mais difícil — e ele já está identificado

O doc de negócio diz: *"Provar que mover o número move receita. Esse é o gargalo do negócio inteiro."* O `problema-drafted.md` não toca nisso em nenhuma linha.

Um documento de problema que evita a própria objeção mais forte não está pronto para banca nem para investidor. Quem lê e não pensa nisso, não foi convencido — apenas ainda não testou.

**Oportunidade:** incluir uma seção de contra-argumento honesto. "Por que isso pode não ser um problema real" e a resposta. Isso inverte a dinâmica: deixa de ser alguém defendendo uma tese e passa a ser alguém que já estressou a tese.

---

## Erros factuais que precisam sair antes de qualquer apresentação

| Trecho | Problema |
|---|---|
| "ChatGPT tem 100M users" | Esse é o marco de início de 2023. A OpenAI já reportou ordem de ~800M de usuários semanais. Usar o número velho sinaliza não acompanhar o mercado que se diz liderar — pior efeito que não citar número nenhum. Conferir a fonte atual antes de usar. |
| "X API aberta" | Falso desde 2023. A API do X é paga, com tier gratuito quase inútil. E o produto v1 depende de X. |
| "Web scraping é legal para dados públicos" | Simplificação jurídica arriscada. Legalidade e Termos de Uso são coisas diferentes — Instagram e TikTok proíbem contratualmente. O uso de Apify/Tavily existe justamente por isso. Numa sala com jurídico do cliente, essa frase é um passivo. |
| "Instagram API pública (limitada mas existe)" | O negócio-doc trata essa limitação como risco material de produto. Aqui aparece como se fosse detalhe. Duas versões da mesma realidade em dois documentos. |

Sugestão dura: **cortar a seção "Dados Existem" inteira**. Ela tenta provar viabilidade técnica dentro de um documento de problema, o que é fora de escopo, e é justamente onde estão os três erros factuais. Viabilidade é assunto de outro doc.

---

## Oportunidades de melhora, em ordem de impacto

**1. Abrir com uma cena, não com uma tese**
O documento é 100% abstrato — "marcas", "analistas", "clientes". Não tem ninguém dentro dele. Enquanto isso, o `drafted-icp.md` tem os gatilhos prontos e muito melhores: *"alguém do time pergunta ao ChatGPT e ele recomenda o concorrente"*. Isso é uma cena, dói, e cabe em uma linha. Começar por aí.

**2. Aterrissar no Brasil e no ICP**
O cliente é empresa brasileira de 50 a 500 funcionários, em saúde, educação, imobiliário. O documento não menciona o Brasil uma vez. Uma clínica que perde paciente porque o ChatGPT recomendou a concorrente é infinitamente mais concreto que "marcas não são mais avaliadas apenas pelo que controlam".

**3. Puxar a melhor frase já escrita para dentro do doc**
*"Marketing passou vinte anos disputando atenção. Agora disputa interpretação."* Está no `drafted-negocio.md` e não está no documento de problema. Essa frase é a tese inteira em nove palavras — deveria ser a primeira linha.

**4. Subir "O Problema em Uma Frase" para o topo**
Hoje está no rodapé, depois de 1.500 palavras. Ninguém em banca ou reunião lê até o fim antes de formar opinião. Tese primeiro, evidência depois.

**5. Cortar a seção "Para LLMs e Sistemas de Recomendação"**
LLM não é cliente, não paga, e a Drafted não faz nada por ele. A seção dilui o foco e não é retomada em nenhum momento.

**6. Reescrever "Por que Ninguém Resolveu Ainda"**
É a seção mais fraca. "É complexo, é problema de engenharia" **enfraquece** o argumento — se é só engenharia, qualquer time com scraper e API de LLM replica em um trimestre. Não há defensibilidade técnica e não é preciso fingir que há. A defensibilidade que os próprios docs apontam é outra: **operação contínua + custo de troca**. Cliente com calendário de conteúdo, produção e creators rodando não troca de fornecedor. É isso que precisa ser argumentado.

**7. Fechar com hipóteses falsificáveis, não com manifesto**
O doc termina em retórica. Deveria terminar em três afirmações testáveis — o que precisa ser verdade para esse problema ser real e caro:

- empresas do ICP aparecem pior que concorrentes em consulta de IA na sua categoria;
- existe volume relevante de jornada de compra passando por LLM nesses setores;
- alguém dentro dessas empresas já sentiu essa perda e não teve a quem recorrer.

Isso conecta com o `drafted-icp.md`, que já pede a mesma coisa: *"Três conversas honestas substituem este arquivo inteiro."*

---

## Estrutura proposta para a reescrita

1. A cena (o lead que não chegou)
2. A tese em uma frase (atenção → interpretação)
3. O que mudou e por que agora (com dado atual e datado)
4. Por que as métricas atuais não respondem — e por que as ferramentas novas de AI visibility também não
5. O problema de dono: ninguém na empresa responde por isso
6. O contra-argumento honesto e a resposta
7. Hipóteses que precisam ser verdade

Do ~1.500 palavras atuais para algo em torno de 700. O documento hoje perde força por acumulação, não por falta de material.

---

## O ponto cego mais caro

Os três documentos são internamente coerentes entre si, e nenhum deles tem **um cliente dentro**. O ICP admite isso explicitamente ("hipótese de trabalho, não retrato de base"), o negócio admite ("não existe registro de ticket, contrato ou base de clientes"). Mas o `problema-drafted.md` não admite nada — ele afirma com a confiança de quem tem evidência.

Esse descompasso de tom é o maior risco do material: um documento de problema escrito como certeza, apoiado em dois documentos escritos como hipótese.
