abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    
def cifradoCesar(cadena):
    if (cadena == '') or (isinstance(cadena,int)):
        return 'Los datos ingresados no pueden ser procesados. Asegurese de que la cadena a cifrar no esté vacía ni utilice números o caracteres especiales. Utilize unicamente el abecedario'
    else:
        return cifrarCesarAux(cadena.upper(),"")
def cifrarCesarAux(cadena,textoCifrado):
    if cadena == "":
        return textoCifrado
    else:
        if cadena[0]==" ":
            return (cifrarCesarAux(cadena[1:], textoCifrado + " "))
        else:
            #La operación de suma,busca la letra del texto a cifrar en el abecedario y devuelve la pocisión numérica en la que se encuentra y a esa posición le suma 3.
            suma= abecedario.find(cadena[0]) + 3
            #La operación de módulo, saca el mod del resultado de suma entre el tamaño total del abecesario, eso permite saber la posición de la letra nueva.
            modulo = int(suma)  % len(abecedario)
            return (cifrarCesarAux(cadena[1:], textoCifrado+str(abecedario[modulo])))
                

def descifradoCesar(cadena):
    if cadena == '' or isinstance(cadena,int):
        return 'Los datos ingresados no pueden ser procesados. Asegurese de que la cadena a descifrar no esté vacía ni utilice números o caracteres especiales. Utilize unicamente el abecedario'
    else:
        return descifrarCesarAux(cadena.upper(),"")
def descifrarCesarAux(cadena,textoDescifrado):
    if cadena == "":
        return textoDescifrado
    else:
        if cadena[0]==" ":
            return (descifrarCesarAux(cadena[1:], textoDescifrado + " "))
        else:
            #La operación de resta, busca en el abecedario la primera letra de la cadena y le resta 3 posicione
            resta= abecedario.find(cadena[0]) - 3
            #Se utiliza el módulo para averiguar la posición de le letra nueva.
            modulo = int(resta)  % len(abecedario)
            return (descifrarCesarAux(cadena[1:], textoDescifrado+str(abecedario[modulo])))
