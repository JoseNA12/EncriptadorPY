def invertirMensaje(frase):
    if isinstance(frase,str):
        return invertirMensajeAux(frase,"")
    else:
        return "Error, operando inválido"

def invertirMensajeAux(frase, mensajeInvertido):

    longitudFrase = len(frase)

    if (longitudFrase==0):
        return mensajeInvertido
    else:
        return invertirMensajeAux(frase[1:], frase[0]+mensajeInvertido)
