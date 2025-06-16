# TPC10

## Descrição geral

O presente trabalho tem como objetivo a extração e organização de informações de artigos científicos da Revista da Sociedade Portuguesa de Medicina Interna através de técnicas de web scraping. O programa desenvolvido permite a coleta automatizada de dados de artigos publicados, incluindo títulos, resumos, autores, DOIs, palavras-chave e datas de publicação.

O scraper navega recursivamente pelo arquivo de edições da revista, identificando e extraindo metadados de artigos científicos de forma estruturada, armazenando-os em formato JSON para análise posterior. O trabalho demonstra a aplicação prática de técnicas de web scraping para a construção de um corpus de dados textuais científicos na área médica.

## Implementação

A implementação foi realizada em Python, utilizando principalmente as bibliotecas BeautifulSoup para parsing HTML e requests para requisições HTTP. O código organiza-se em funções modulares que realizam tarefas específicas:

- Recuperação e parsing de páginas HTML
- Extração de URLs de edições da revista
- Extração de URLs de artigos de cada edição (com filtro seletivo de seções)
- Extração de metadados detalhados de cada artigo, incluindo:
  - Título
  - Resumo
  - DOI
  - Palavras-chave
  - Data de publicação
  - Informações de autores (nome, afiliação, ORCID)

Os dados extraídos são estruturados em um dicionário Python e persistidos em um arquivo JSON, facilitando o uso posterior para análise textual, mineração de dados ou aplicações de processamento de linguagem natural no domínio médico.