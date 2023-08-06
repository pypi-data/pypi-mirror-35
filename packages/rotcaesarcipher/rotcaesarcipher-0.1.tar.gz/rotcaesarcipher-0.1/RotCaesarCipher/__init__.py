import model
#Crifra uma frase
#salt = 1 a 25
#frase = string ascii
def encode(salt, frase):
    e = [model.E(salt, p) for p in frase]
    return str("".join(e)).upper()
#Crifra uma frase
#salt = 1 a 25
#frase = string ascii
def decode(salt, frase):
    d = [model.D(salt, c) for c in frase]
    return "".join(d)
