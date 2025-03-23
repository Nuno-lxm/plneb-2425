# TPC6

## Descrição geral

O objetivo do presente trabalho é acrescentar uma rota de pesquisa à aplicação desenvolvida ao longo das últimas aulas. Esta rota tem uma série de funcionalidades adicionais pedidas e detalhadas de seguida.

## Implementação

**Nova Rota:** Para permitir a pesquisa de sequências de caracteres nas designações e descrições dos termos médicos guardados, foi criada a rota `/pesquisa`, que faz uso da função `pesquisa()`. Esta acede à query e aos parâmetros passados pelo formulário criado e executa a função `find(db, query, word_boundary, match_case)`, passando o seu resultado ao template `pesquisa.html`.

**Função de Pesquisa:**  
A função `find(db, query, word_boundary, match_case)` percorre a base de dados verificando a existência da query na designação ou descrição, tendo em conta os parâmetros passados de `match_case` e de `word_boundary`, acrescentando as tags HTML `<strong>` em volta da query encontrada. Devolve uma lista de tuplos com as designações e descrições modificadas para exibição e a chave original do termo para ser utilizada no URL de âncora.

**Novo Template:**  
Foi ainda criado o template HTML `pesquisa.html` para realizar pesquisas e exibir os seus resultados. Este contém o formulário de pesquisa composto por uma*search bar e caixas de seleção que permitem a definição dos parâmetros `match_case` e `word_boundary`. Para exibição de resultados, é utilizado um elemento `list-group` semelhante ao construído para a lista de conceitos, no qual as designações e descrições são escritas garantindo que as tags HTML são preservadas. Os URLs aos quais se referem são construídos utilizando as chaves não modificadas dos conceitos.