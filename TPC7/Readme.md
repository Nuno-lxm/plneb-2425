# TPC6

## Descrição geral  
O objetivo do presente trabalho é integrar uma tabela da framework DataTables na aplicação desenvolvida durante a aula.

## Implementação  

**Nav Bar:**  
Para facilitar o acesso à nova rota, esta foi adicionada à Nav Bar existente, incluindo `<a class="nav-link" href="/conceitos/tabela">Tabela</a>` no ficheiro `layout.html`, de forma que se mantenha constante em todas as rotas.

**Pesquisa com Regex:**  
Para otimizar a pesquisa na tabela, a funcionalidade de regex foi ativada definindo o parâmetro `regex` como `true` na inicialização da tabela no ficheiro `conceitos.js`.

**Estilo:**  
Para garantir consistência visual com o restante da aplicação, a classe da tabela foi definida no template `tabela.html` como `class="table table-striped table-bordered table-hover"`.

**Extra:**  
Foi adicionada uma âncora `<a href="/conceitos/{{ designacao }}" class="text-decoration-none text-dark">{{ designacao }}</a>` em cada entrada da tabela, permitindo que um clique redirecione para a página de detalhes do conceito e possibilite sua eliminação.