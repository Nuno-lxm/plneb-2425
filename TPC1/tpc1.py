#Exercício 1
def reverse(s):
    return s[::-1]

#Exercício 2
def count(s):
    res = 0
    for c in s:
        if c  == "a" or c == "A":
            res += 1
    
    return res

#Exercício 3
def vowels(s):
    res = 0
    for c in s:
        if c in "aAeEiIoOuU":
            res += 1
    
    return res

#Exercício 4
def lower(s):
    return s.lower()

#Exercício 5
def upper(s):
    return s.upper()

#Exercício 6
def capicua(s):
    return s == reverse(s.lower())

#Exercício 7
def balanced(s1, s2):
    for c in s1:
        if c not in s2:
            return False
    return True

#Exercício 8
def ocurrences(s1, s2):
    if len(s2) < len(s1):
        return 0
    res = 0

    for i in range(len(s2) - len(s1) + 1):
        if s1 == s2[i: i + len(s1)]:
            res += 1
    return res

#Exercício 9
def characterDict(s):
    res = {}
    for c in s:
        if c in res.keys():
            res[c] += 1
        else:
            res[c] = 0
    return res

def anagram(s1, s2):
    return characterDict(s1) == characterDict(s2)


#Exercício 10
def anagramClasses(lista):
    res = {}
    for s in lista:
        key = ''.join(sorted(s.lower()))
        if key in res:
            res[key].append(s)
        else:
            res[key] = [s]
    return res


print("Exercício 1: " + reverse("String exemplo"))
print("Exercício 2: " + str(count("BanAna e lAranjA")))
print("Exercício 3: " + str(vowels("cOnta as vogAis de uma frase")))
print("Exercício 4: " + lower("FRASE em lEtRA MinuSCUla"))
print("Exercício 5: " + upper("FRASE em lEtRA MaiuSCUla"))
print("Exercício 6 " + "capicua - " + str(capicua("capicua")) + ", aibofobia - " + str(capicua("aibofobia")))
print("Exercício 7: " + str(balanced("bola", "luisa e o seu bitoque")) + ", " + str(balanced("exemplo", "falso")))
print("Exercício 8: " + str(ocurrences("ai", "ai ai que isto doi, dai-me anestesia")))
print("Exercício 9: " + str(anagram("listen", "silent")) + ", " + str(anagram("hello", "world")))
print("Exercício 10: " + str(anagramClasses(['amor', 'saco', 'roma', 'caso', 'ponte', 'ramo'])))