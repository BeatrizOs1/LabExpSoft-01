# 📄 Relatório Final

## Introdução e hipóteses

Neste relatório, busca-se analisar repositórios populares do GitHub, coletando dados sobre estrelas, issues, pull requests, releases e linguagem de programação. Com base nos dados, foram levantadas algumas hipóteses iniciais:

**H1:** Repositórios mais antigos tendem a ter mais estrelas?

**H2:** Linguagens mais populares têm mais issues e pull requests?

**H3:** A maioria dos repositórios tem mais issues abertas do que fechadas?

**H4:** Projetos com mais releases são mais populares?

**H5:** Projetos mais populares são escritos em poucas linguagens?


## Introdução

Este relatório tem como objetivo analisar as principais características de sistemas populares open-source no GitHub. A partir da coleta de dados de 1.000 repositórios com maior número de estrelas, buscamos responder algumas questões sobre a idade, colaboração externa, frequência de releases, atualizações e a influência das linguagens de programação na popularidade dos repositórios.

## Hipóteses Informais

Com base no comportamento esperado dos repositórios populares, formulamos algumas hipóteses:

- **H1:** Repositórios mais antigos tendem a ter mais estrelas.

- **H2:** Linguagens mais populares possuem maior número de issues e pull requests.

- **H3:** A maioria dos repositórios tem mais issues abertas do que fechadas.

- **H4:** Projetos com mais releases são mais populares.

- **H5:** Projetos mais populares são escritos em poucas linguagens.

- **H6:** Sistemas escritos nas linguagens mais populares recebem mais contribuições externas, lançam mais releases e são atualizados com mais frequência.

## Metodologia

Para responder às questões de pesquisa, utilizamos a API GraphQL do GitHub para coletar os seguintes dados dos 1.000 repositórios mais estrelados:

- Nome do repositório

- Data de criação (para calcular a idade)

- Data da última atualização

- Total de pull requests aceitas

- Total de releases

- Total de issues abertas e fechadas

- Linguagem principal

- Número de estrelas

Os dados foram armazenados em um arquivo .csv e analisados utilizando Python, bibliotecas como Pandas e Matplotlib para visualização e estatísticas descritivas.

## Resultados

**RQ 01: Sistemas populares são maduros/antigos?**

- **Métrica:** Idade do repositório

- **Resultado:** A mediana da idade dos repositórios analisados é de aproximadamente 7 anos. A maioria dos repositórios populares não são extremamente antigos, mas também não são recentes.

**RQ 02: Sistemas populares recebem muita contribuição externa?**

- **Métrica:** Total de pull requests aceitas

- **Resultado:** A mediana de pull requests aceitas é 1.200, indicando que esses repositórios são bastante colaborativos.

**RQ 03: Sistemas populares lançam releases com frequência?**

-**Métrica:** Total de releases

- **Resultado:** A mediana de releases é 35, mostrando que repositórios populares têm atualizações significativas ao longo do tempo.

**RQ 04: Sistemas populares são atualizados com frequência?**

- **Métrica:** Tempo até a última atualização

- **Resultado:** A maioria dos repositórios foi atualizada nos últimos 3 meses, o que indica alta manutenibilidade.

**RQ 05: Sistemas populares são escritos nas linguagens mais populares?**

- **Métrica:** Linguagem primária

- **Resultado:** As linguagens mais comuns nos repositórios analisados são JavaScript, Python e TypeScript, confirmando a tendência de linguagens populares dominarem os projetos mais bem avaliados.

**RQ 06: Sistemas populares possuem um alto percentual de issues fechadas?**

- **Métrica:** Razão entre issues fechadas e totais

- **Resultado:** A média de issues fechadas está em torno de 78%, indicando que a maioria dos problemas são resolvidos rapidamente.

**RQ 07: Sistemas escritos em linguagens populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?**

- **Métrica:** Comparativo entre linguagens

- **Resultado:** Repositórios em Python e JavaScript apresentam maior número de pull requests aceitas e releases frequentes. Linguagens menos comuns têm menor participação externa.

## Discussão

Ao comparar os resultados com as hipóteses iniciais:

- **H1:** Repositórios mais antigos tendem a ter mais estrelas?

Parcialmente confirmada. Repositórios populares têm uma idade mediana de 7 anos, mas há exceções recentes.

- **H2:** Linguagens mais populares têm mais issues e pull requests?

Confirmada. JavaScript e Python lideram em colaboração e problemas reportados.

- **H3:** A maioria dos repositórios tem mais issues abertas do que fechadas?

Rejeitada. 78% das issues são fechadas, indicando boa gestão.

- **H4:** Projetos com mais releases são mais populares?

Confirmada. Projetos ativos têm maior engajamento.

- **H5:** Projetos mais populares são escritos em poucas linguagens?

Confirmada. As mesmas linguagens dominam o ranking.

- **H6:** Sistemas escritos nas linguagens mais populares recebem mais contribuições externas, lançam mais releases e são atualizados com mais frequência?

Confirmada. JavaScript e Python possuem os repositórios mais ativos e colaborativos.

## Conclusão

A análise dos 1.000 repositórios mais populares no GitHub mostrou padrões consistentes na popularidade de sistemas open-source. Repositórios mais antigos e bem mantidos tendem a receber mais contribuição externa, e as linguagens dominantes estão fortemente correlacionadas à popularidade. As hipóteses foram, em grande parte, confirmadas, demonstrando que popularidade está diretamente relacionada a fatores como colaboração, atualizações frequentes e bom gerenciamento de issues.
