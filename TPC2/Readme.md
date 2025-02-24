# TPC 2

## **Lista de Funções Implementadas**

A seguir apresentam-se as funções implementadas para resolver os exercícios da ficha sobre expressões regulares, acompanhadas de uma breve descrição e exemplos.

### 1. **`palavra_magica(frase)`:**  
**Descrição:**  
Verifica se a frase termina com "por favor" seguido de um sinal de pontuação válido.
**Exemplo:**  
```python
palavra_magica("Posso ir à casa de banho, por favor?")  # retorna True
palavra_magica("Preciso de um favor.")  # retorna False
```

---

### 2. **`narcissismo(linha)`:**  
**Descrição:**  
Conta quantas vezes a palavra "eu" aparece na string, independentemente de maiúsculas ou minúsculas.
**Exemplo:**  
```python
narcissismo("Eu não sei se eu quero continuar a ser eu.")  # retorna 3
```

---

### 3. **`troca_de_curso(linha, novo_curso)`:**  
**Descrição:**  
Substitui todas as ocorrências da palavra "LEI" por um novo curso especificado.
**Exemplo:**  
```python
troca_de_curso("LEI é o melhor curso!", "MEIC")  # retorna "MEIC é o melhor curso!"
```

---

### 4. **`soma_string(linha)`:**  
**Descrição:**  
Recebe uma string com números separados por vírgula e devolve a soma desses números.
**Exemplo:**  
```python
soma_string("1,2,3,4,5")  # retorna 15
```

---

### 5. **`pronomes(frase)`:**  
**Descrição:**  
Encontra e devolve todos os pronomes pessoais na frase ("eu", "tu", "ele", "ela", etc.).
**Exemplo:**  
```python
pronomes("Eu e tu fomos passear com Ele e com Ela.")  # retorna ['Eu', 'tu', 'Ele', 'Ela']
```

---

### 6. **`variavel_valida(string)`:**  
**Descrição:**  
Verifica se a string é um nome de variável válido (começa com uma letra e contém apenas letras, números ou underscores).
**Exemplo:**  
```python
variavel_valida("var_1")  # retorna True
variavel_valida("1var")  # retorna False
```

---

### 7. **`inteiros(string)`:**  
**Descrição:**  
Devolve todos os números inteiros (positivos e negativos) presentes na string.
**Exemplo:**  
```python
inteiros("um 2 4 -123 766")  # retorna ['2', '4', '-123', '766']
```

---

### 8. **`underscores(string)`:**  
**Descrição:**  
Substitui todos os espaços por underscores, garantindo que múltiplos espaços consecutivos se tornam apenas um underscore.
**Exemplo:**  
```python
underscores("e que pessoal?  tá     tudo?")  # retorna "e_que_pessoal?_tá_tudo?"
```

---

### 9. **`codigos_postais(lista)`:**  
**Descrição:**  
Divide uma lista de códigos postais no formato "xxxx-yyy" em pares.
**Exemplo:**  
```python
codigos_postais(["4700-000", "1234-567"])  # retorna [('4700', '000'), ('1234', '567')]
```

