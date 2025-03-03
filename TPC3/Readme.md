# TPC3 

## Descrição geral

O presente trabalho foi realizado com base na atividade desenvolvida na aula e com o objetivo de melhorar a captura de informação do dicionário disponibilizado lidando com caracteres indesejados de forma adequada para a geração de um ficheiro html de agregação e visualização dos dados.

Tendo isto em conta, o programa segue a estrutura desenvolvida na aula, mantendo as etapas de leitura, marcação dos conceitos, extração dos mesmos, limpeza das descrições e geração do ficheiro html. A alteração realizada como trabalho de casa incide na etapa de limpeza do ficheiro txt lido.

## Implementação

De forma a remover os caracteres de quebra de página **\f**, foram aplicadas as duas expressões regulares apresentadas de seguida.

```python
texto = re.sub(r"\f(?=[a-zØ-öø-ÿ])", "", texto)
```
A primeira expressão aplicada identifica os caracteres **\f** localizados antes de letras minúsculas, incluindo caracteres acentuados, ou seja, identifica os caracteres **\f** que precedem conceitos ou linhas intermédias da descrição. Neste caso, a única operação a realizar é remover o caracter para a marcação proceder normalmente.

```python
texto = re.sub(r"\n\f", "", texto)
```

A segunda expressão originalmente definida como **\n\f(?=[A-ZÀ-Ö0-9])**, tem como objetivo identificar os caracteres **\f** que precedem as frases iniciais das descrições. Neste caso, é necessário remover o caracter e o **\n** que o precede de forma a manter a coesão entre conceito e descrição para a marcação. No entanto, todos os **\f** restantes são os que se encontram nesta posição ou os dois caracteres finais que podem ser ignorados. Desta forma, a expressão foi simplificada para a versão apresentada acima.

Sendo assim, todos os caracteres indesejados foram removidos de forma apropriada e a marcação desenvolvida na aula pode decorrer normalmente e sem erros. Todos os passos seguintes seguem a ordem e lógica da aula, culminando na organização e exibição dos dados de forma simples e facilmente interpretável no formato html pretendido.

Os ficheiros de dados pdf e txt estão incluídos, assim como o html gerado para verificação de resultados.