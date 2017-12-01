def invertirPalabra(frase):
    if isinstance(frase, str):
        return invertirPalabraAux(frase,"")
    else:
        return ("Error, algún operando es inválido")

def invertirPalabraAux(frase, palabraInversa):

    longitudFrase = len(frase)
    palabraOrdenada = (palabraInversa).split()[::-1]

    if (longitudFrase==0):
        return " ".join(palabraOrdenada)
    else:
        return invertirPalabraAux(frase[1:], frase[0]+palabraInversa)

