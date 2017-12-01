import validacion

def invertirPalabra(frase):
    if isinstance(frase, str) and (validacion.validacion(frase.upper(),False)==True) and frase != '':
        return invertirPalabraAux(frase,"")
    else:
        return ("El mensaje no puede ser procesado. Asegurece que no tenga números o caracteres especiales ni que el mensaje esté vacío. Utilize únicamente el abecedario.")

def invertirPalabraAux(frase, palabraInversa):

    longitudFrase = len(frase)
    # Se asigna a palabraOrdenada la separacion de la frase(palabra por palabra) y a la vez invirtiendo su orden
    palabraOrdenada = (palabraInversa).split()[::-1]

    if (longitudFrase==0):
        return " ".join(palabraOrdenada)
    else:
        return invertirPalabraAux(frase[1:], frase[0]+palabraInversa)

