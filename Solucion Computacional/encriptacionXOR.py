abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import validacion

def cifradoXOR(cadena,clave):
    if cadena == '' or isinstance(cadena,int) or (validacion.validacion(cadena.upper(),False)==False) or (validacion.validacion(clave.upper(),False)==False):
        return 'Estos valores no pueden ser descifrados. Asegurece que la cadena y la clave no estén vacías, la clave no utiliza números, y que la cadena y la clave sean strings'
    else:
        return cifrarXORAux(cadena.upper(),clave, clave, "")
def cifrarXORAux(cadena,clave,retornarClave, textoCifrado):
    if cadena == "":
        return SecuenciaEscape(textoCifrado)
    else:
        if clave == "":
            clave = retornarClave
        if cadena[0]==" ":
            return (cifrarXORAux(cadena[1:], retornarClave, retornarClave, textoCifrado + " "))
        else:
      
            XOR= ord(str(cadena[0])) ^ ord(str(clave[0])) #Devuelve el resultado de efectuar el XOR entre esos dos caracteres
            Caracter= chr(XOR) #El número obtenido se reemplaza por su respectivo caracter en la tabla ASCII
            return (cifrarXORAux(cadena[1:], clave[1:], retornarClave, textoCifrado + str(Caracter)))
            
def descifradoXOR(cadena,clave):
    if cadena == '' or isinstance(cadena,int) or clave== '':
        return 'Estos valores no pueden ser descifrados. Asegurece que la cadena y clave no estén vacías'
    else:
        return descifrarXORAux(cadena,clave, clave, "")
def descifrarXORAux(cadena,clave,retornarClave, textodescifrado):
    if cadena == "":
        return SecuenciaEscape(textodescifrado)
    else:
        if clave == "":
            clave = retornarClave
        if cadena[0]==" ":
            return (descifrarXORAux(cadena[1:], retornarClave, retornarClave, textodescifrado + " "))
        else:
      
            valorCaracter= ord(str(cadena[0]))  #El caracter de la tabla ASCII se reemplaza por su valor numérico
            XOR= valorCaracter ^ ord(str(clave[0])) #Se realiza el XOR entre la clave y el valor númerico del caracter dado por el usuario
            Caracter= chr(XOR) #Se resultado del XOR se convierte a su respectivo alfanumerico
            return (descifrarXORAux(cadena[1:], clave[1:], retornarClave, textodescifrado + str(Caracter)))
            
def SecuenciaEscape(codigo):
    temporal= "%r" % codigo
    nuevaSalida = temporal[1:-1]
    return print (nuevaSalida)
