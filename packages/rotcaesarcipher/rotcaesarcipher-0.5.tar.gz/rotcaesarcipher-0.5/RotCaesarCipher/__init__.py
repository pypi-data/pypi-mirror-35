import string
import argparse

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


"""if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-s', '--salt', help='Description for foo argument', required=False,type=int)
    parser.add_argument('-e', '--encode', help='Description for foo argument', required=False)
    parser.add_argument('-d', '--decode', help='Description for bar argument', required=False)
    parser.add_argument('-c', '--crack', help='Description for bar argument', required=False)
    parser.add_argument('-v','--verbose', nargs='?',const=1, help='Description for bar argument',type=int)
    args = vars(parser.parse_args())
    if args['encode'] and args['salt']:
        print encode(int(args['salt']), args['encode'])
    if args['decode'] and args['salt']:
        print decode(int(args['salt']), args['decode'])
    if args['crack']:
        cracked = ""
        for n in range(1, 26):
            d = decode(n, args['crack'])
            c = "{} => {}".format(("0{}".format(n) if n < 10 else n), d)
            if args['verbose']:
                print c
            else:
                cracked += "{}\n".format(c)
        if not args['verbose']:
            print cracked
"""