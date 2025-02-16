# TPC1

## **Lista de Funções Implementadas**

A seguir apresentam-se as funções implementadas no projeto, acompanhadas de uma breve descrição e exemplos.

### 1. **`reverse(s)`:**  
**Descrição:**  
Inverte uma string usando **slicing** (`[::-1]`).  
**Exemplo:**  
```python
reverse("String exemplo")  # retorna "olpmexe gnirtS"
```

---

### 2. **`count(s)`:**  
**Descrição:**  
Conta quantas vezes a letra `"a"` (maiúscula ou minúscula) aparece na string `s`.  
**Exemplo:**  
```python
count("BanAna e lAranjA")  # retorna 5
```

---

### 3. **`vowels(s)`:**  
**Descrição:**  
Conta o número total de vogais (`a, e, i, o, u` maiúsculas ou minúsculas) presentes na string `s`.  
**Exemplo:**  
```python
vowels("cOnta as vogAis de uma frase")  # retorna 11
```

---

### 4. **`lower(s)`:**  
**Descrição:**  
Converte a string `s` para **minúsculas**, utilizando o método `.lower()`.  
**Exemplo:**  
```python
lower("FRASE em lEtRA MinuSCUla")  # retorna "frase em letra minuscula"
```

---

### 5. **`upper(s)`:**  
**Descrição:**  
Converte a string `s` para **maiúsculas**, utilizando o método `.upper()`.  
**Exemplo:**  
```python
upper("FRASE em lEtRA MaiuSCUla")  # retorna "FRASE EM LETRA MAIUSCULA"
```

---

### 6. **`capicua(s)`:**  
**Descrição:**  
Verifica se a string `s`, ao ser invertida, mantém o mesmo valor.  
**Exemplo:**  
```python
capicua("capicua")    # retorna True
capicua("aibofobia")  # retorna True
capicua("exemplo")    # retorna False
```

---

### 7. **`balanced(s1, s2)`:**  
**Descrição:**  
Verifica se todos os caracteres de `s1` estão presentes em `s2`.  
**Exemplo:**  
```python
balanced("bola", "luisa e o seu bitoque")  # retorna True
balanced("exemplo", "falso")               # retorna False
```

---

### 8. **`ocurrences(s1, s2)`:**  
**Descrição:**  
Conta quantas vezes a substring `s1` aparece na string `s2`.  
**Exemplo:**  
```python
ocurrences("ai", "ai ai que isto doi, dai-me anestesia")  # retorna 3
```

---

### 9. **`anagram(s1, s2)`:**  
**Descrição:**
Utiliza a função `characterDict(s)` que percorre uma string e cria um dicionário com a  contagem de caracteres. Verifica se duas strings são **anagramas** comparando as contagens de cada uma.  
Considerei utilizar o método aplicado no exercício 10, mas a criação do dicionário apenas percorria cada string uma vez mantendo a complexidade linear **O(n)**.  
**Exemplo:**  
```python
anagram("listen", "silent")  # retorna True
anagram("hello", "world")    # retorna False
```

---

### 10. **`anagramClasses(lista)`:**  
**Descrição:**  
Agrupa palavras que são anagramas umas das outras, utilizando um dicionário onde a **chave** é a versão ordenada das letras da palavra.
A função charecterDict foi orginalmente pensada para ser utilizada tanto no exercício 9 como no 10. No entanto, para criar as chaves do dicionário, decidi utilizar o sorted acabando por comparar as strings ordenadas de forma a realizar também a verificação de anagrama.
**Exemplo:**  
```python
anagramClasses(['amor', 'saco', 'roma', 'caso', 'ponte', 'ramo'])
# Retorna:
# {
#   "amor": ["amor", "roma", "ramo"],
#   "acos": ["saco", "caso"],
#   "eopnt": ["ponte"]
# }