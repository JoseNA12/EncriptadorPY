abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import validacion
def cifradoVigenere(cadena,clave):
    if cadena == '' or clave=='' or isinstance(cadena,int) or (validacion.validacion(cadena.upper(),False)==False) or (validacion.validacionNumerica(clave,False)==False):
        return 'Los datos ingresados no pueden ser procesados. Asegurese de que la cadena a cifrar no esté vacía, ni utilice números o caracteres especiales. Utilize únicamente el abecedario. La clave debe ser un numero'
    else:
        return cifrarVigenereAux(cadena.upper(),clave, clave, "")
def cifrarVigenereAux(cadena,clave,retornarClave, textoCifrado):
    if cadena == "":
        return textoCifrado
    else:
        if clave == "":
            clave = retornarClave
        if cadena[0]==" ":
            return (cifrarVigenereAux(cadena[1:], retornarClave, retornarClave, textoCifrado + " "))
        else:
      
            suma= abc.find(cadena[0]) + int(clave[0]) #Esta operación resulve la suma entre la posicion de la primera letra dentro del abecedario y el primer número de la clave. El resultado indica en que posicion se encontrará la letra correspondiente 
       
            if suma > 26:  #Si la suma se pasa del máximo de letras del abecedario se debe restar el valor de la suma menos la cantidad de letras en el abecedario y ese será la nueva posición de la letra
                posicion= suma - 26
                return (cifrarVigenereAux(cadena[1:],clave[1:],retornarClave, textoCifrado + str(abc[posicion])))
            else:
                return (cifrarVigenereAux(cadena[1:], clave[1:], retornarClave, textoCifrado + str(abc[suma])))
            
           

def descifradoVigenere(cadena,clave):
    if cadena == '' or clave=='' or isinstance(cadena,int) or (validacion.validacion(cadena.upper(),False)==False) or (validacion.validacionNumerica(clave,False)==False):
        return 'Los datos ingresados no pueden ser procesados. Asegurese de que la cadena a cifrar no esté vacía, ni utilice números o caracteres especiales. Utilize unicamente el abecedario, además la clave debe ser un numero'
    else:
        return descifrarVigenereAux(cadena.upper(),clave, clave, "")
def descifrarVigenereAux(cadena,clave,retornarClave, textodescifrado):
    if cadena == "":
        return textodescifrado
    else:
        if clave == "":
            clave = retornarClave
        if cadena[0]==" ":
            return (descifrarVigenereAux(cadena[1:], retornarClave, retornarClave, textodescifrado + " "))
        else:
      
            resta= abc.find(cadena[0]) - int(clave[0]) #Esta operación resulve la resta entre la posicion de la primera letra de la cadena dentro del abecedario y el primer número de la clave. El resultado indica en que posicion se encontrará la letra correspondiente
            
            if resta < 0: 
                posicion= 26 + resta #Si el resultado de la resta es un número negativo debe restarse al abecedario para encontrar la posicion
                return (descifrarVigenereAux(cadena[1:],clave[1:],retornarClave, textodescifrado + str(abc[posicion])))
            else:
                return (descifrarVigenereAux(cadena[1:], clave[1:], retornarClave, textodescifrado + str(abc[resta])))
            
           
  

