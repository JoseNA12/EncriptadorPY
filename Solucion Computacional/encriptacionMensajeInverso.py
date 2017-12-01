import validacion

def invertirMensaje(frase):
    if isinstance(frase,str) and (validacion.validacion(frase.upper(),False)==True) and frase != '':
        return invertirMensajeAux(frase,"")
    else:
        return "El mensaje no puede ser procesado. Asegurece que no tenga números o caracteres especiales ni que el mensaje esté vacío. Utilize únicamente el abecedario. "

def invertirMensajeAux(frase, mensajeInvertido):
    
    longitudFrase = len(frase)

    if (longitudFrase==0):
        return mensajeInvertido
    else:
        return invertirMensajeAux(frase[1:], frase[0]+mensajeInvertido)
