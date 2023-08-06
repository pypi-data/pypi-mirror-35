import string

alfabeto = list(string.ascii_lowercase)

class Model:
    # formula para codificar
    def E(self,k, p):
        if str(p).lower() not in alfabeto:
            return p
        p = alfabeto.index(str(p).lower())
        return alfabeto[(p + k) % 26]

    # formula para decodificar
    def D(self,k, c):
        if str(c).lower() not in alfabeto:
            return c
        c = alfabeto.index(str(c).lower())
        return alfabeto[(c - k) % 26]

#Crifra uma frase
#salt = 1 a 25
#frase = string ascii
def encode(salt, frase):
    e = [Model().E(salt, p) for p in frase]
    return str("".join(e)).upper()
#Crifra uma frase
#salt = 1 a 25
#frase = string ascii
def decode(salt, frase):
    d = [Model().D(salt, c) for c in frase]
    return "".join(d)
