# TPC8

## Descrição geral  
Neste trabalho, o objetivo foi expandir o script desenvolvido nas aulas de forma a recolher também os detalhes de cada doença presente no site [Atlas da Saúde](https://www.atlasdasaude.pt).

## Implementação  

**Recolha dos Detalhes:**  
Foi criada a função `detalhes_doenca(url)`, que recebe o URL da página de uma doença e extrai a informação relevante da secção principal do conteúdo. Esta função identifica e separa os diferentes blocos de texto com base nos cabeçalhos (`<h2>`), organizando-os em categorias.

**Organização da Informação:**  
Cada secção é guardada num dicionário, onde a chave corresponde ao título da secção (ex: "Causas", "Sintomas") e os valores são listas com o conteúdo encontrado (parágrafos, listas, etc.).  
Informações adicionais, como "site" e "nota", são também recolhidas caso existam.  
O resultado final é uma estrutura organizada e facilmente navegável para cada doença.