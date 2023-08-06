import string
alfabeto = list(string.ascii_lowercase)

class Model:
    # Cifra de Vigenere

    # formula para codificar
    # P = caracter ascii
    # k = chave ascii

    def E(self,p, k):
        if not str(p).isalpha():
            return p
        p = alfabeto.index(str(p).lower())
        k = alfabeto.index(str(k).lower())
        return alfabeto[(p + k) % 26]

    # formula para decodificar
    # P = caracter ascii codificado
    # k = chave ascii
    def D(self,c, k):
        if str(c).lower() not in alfabeto:
            return c
        c = alfabeto.index(str(c).lower())
        k = alfabeto.index(str(k).lower())
        return alfabeto[(c - k + 26) % 26]

    def completeKey(self,key, text):
        if not str(key).isalpha():
            print('add Key [a-zA-Z].')
            exit(1)
        if not str(text).isalpha():
            print('add Text [a-zA-Z].')
            exit(2)
        tmp_chave = ""
        while len(tmp_chave) <= len(text):
            tmp_chave += key
        return tmp_chave[:len(text)]


def encode(text, key):
    tmp_chave = Model().completeKey(key=key, text=text)
    return str("".join([Model().E(p=p, k=tmp_chave[i]) for i, p in enumerate(text)])).upper()

def decode(encryptedText, key):
    tmp_chave = Model().completeKey(key=key, text=encryptedText)
    return str("".join([Model().D(c=p, k=tmp_chave[i]) for i, p in enumerate(encryptedText)]))
