abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import validacion
        
def cifradoLlave(cadena,clave):
    if cadena == '' or isinstance(cadena,int) or (validacion.validacion(cadena.upper(),False)==False) or (validacion.validacion(clave.upper(),False)==False):
        return 'Los datos ingresados no pueden ser procesados. Asegurese de que la cadena a cifrar y la clave secreta no están vacías ni utilicen números o caracteres especiales. Unicamente el abecedario'
    else:
        return cifrarLlaveAux(cadena.upper(),clave.upper(), clave.upper(), "")
def cifrarLlaveAux(cadena,clave,retornarClave, textoCifrado):
    if cadena == "":
        return textoCifrado
    else:
        if clave == "":
            clave = retornarClave
        if cadena[0]==" ":
            return (cifrarLlaveAux(cadena[1:], retornarClave, retornarClave, textoCifrado + " "))
        else:
      #Suma el valor del primer caracter de la cadena y el primer caracter de la clave.
            suma= abc.find(cadena[0]) + abc.find(clave[0]) +1
           
            if suma > 26:
                posicion= suma - 26
                return (cifrarLlaveAux(cadena[1:],clave[1:],retornarClave, textoCifrado + str(abc[posicion])))
            else:
                return (cifrarLlaveAux(cadena[1:], clave[1:], retornarClave, textoCifrado + str(abc[suma])))
            
           
  

def descifradoLlave(cadena,clave):
    if cadena == '' or isinstance(cadena,int)or (validacion.validacion(cadena.upper(),False)==False) or (validacion.validacion(clave.upper(),False)==False):
        return 'Los datos ingresados no pueden ser procesados. Asegurese de que la cadena a cifrar o la clave secreta no están vacías ni utilicen números o caracteres especiales. Unicamente el abecedario'
    else:
        return descifrarLlaveAux(cadena.upper(),clave.upper(), clave.upper(), "")
def descifrarLlaveAux(cadena,clave,retornarClave, textodescifrado):
    if cadena == "":
        return textodescifrado
    else:
        if clave == "":
            clave = retornarClave
        if cadena[0]==" ":
            return (descifrarLlaveAux(cadena[1:], retornarClave, retornarClave, textodescifrado + " "))
        else:
      #Resta el valor del primer caracter de la cadena y el primer caracter de la clave
            resta= abc.find(cadena[0]) - abc.find(clave[0]) -1
           
            if resta < 0:
                posicion= 26 + resta
                
                return (descifrarLlaveAux(cadena[1:],clave[1:],retornarClave, textodescifrado + str(abc[posicion])))
            else:
                return (descifrarLlaveAux(cadena[1:], clave[1:], retornarClave, textodescifrado + str(abc[resta])))
            
           
  
