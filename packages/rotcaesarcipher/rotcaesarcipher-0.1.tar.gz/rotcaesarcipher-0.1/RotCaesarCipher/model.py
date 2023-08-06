import string
#lista de palavras [a-z]
alfabeto = list(string.ascii_lowercase)
#formula para codificar
def E(k,p):
    if str(p).lower() not in alfabeto:
        return p
    p = alfabeto.index(str(p).lower())
    return alfabeto[(p + k) % 26]

#formula para decodificar
def D(k,c):
    if str(c).lower() not in alfabeto:
        return c
    c = alfabeto.index(str(c).lower())
    return alfabeto[(c - k) % 26]
