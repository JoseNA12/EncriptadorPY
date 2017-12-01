abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def cifradoLlave(cadena,clave):
    if cadena == '' or isinstance(cadena,int):
        return 'Estos valores no pueden ser cifrados'
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
      
            suma= abc.find(cadena[0]) + abc.find(clave[0]) +1
           
            if suma > 26:
                posicion= suma - 26
                return (cifrarLlaveAux(cadena[1:],clave[1:],retornarClave, textoCifrado + str(abc[posicion])))
            else:
                return (cifrarLlaveAux(cadena[1:], clave[1:], retornarClave, textoCifrado + str(abc[suma])))
            
           
def descifradoLlave(cadena,clave):
    if cadena == '' or isinstance(cadena,int):
        return 'Estos valores no pueden ser descifrados'
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
      
            resta= abc.find(cadena[0]) - abc.find(clave[0]) -1
           
            if resta < 0:
                posicion= 26 + resta
                
                return (descifrarLlaveAux(cadena[1:],clave[1:],retornarClave, textodescifrado + str(abc[posicion])))
            else:
                return (descifrarLlaveAux(cadena[1:], clave[1:], retornarClave, textodescifrado + str(abc[resta])))
            
           
  
