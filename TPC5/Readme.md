# TPC5

## Descrição geral

O presente trabalho foi realizado com base na atividade desenvolvida na aula e com o objetivo de acrescentar a funcionalidade de visualizar os detalhes de cada conceito médico e chegar a esta página de detalhes clicnado em cada um.

## Implementação

**Nova Rota:** Para permitir a visualização dos detalhes de cada conceito, foi criada a rota `conceitos/<designacao>` que faz uso da função `conceito_detalhes(designacao)`.
Esta recupera a descrição do conceito a partir da base de dados carregada em memória e passa a `designacao` e a `descricao` a um novo template HTML.

**Novo Template:** Foi também criado um novo template HTML para exibir as informações de cada conceito, este apenas contém a designacao como título e a descrição como conteúdo, com uma `hr` para separação e organização.

**Âncora:** De forma a permitir aceder diretamente aos detalhes dos conceitos clicando nestes, foi tb adicionado um elemento `<a>` no template da lista de conceitos que associa a designação de cada conceito ao url dos seus detalhes.