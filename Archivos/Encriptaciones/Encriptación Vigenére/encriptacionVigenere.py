abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifradoVigenere(cadena,clave):
    if cadena == '' or isinstance(cadena,int):
        return 'Estos valores no pueden ser cifrados'
    else:
        return cifrarVigenereAux(cadena.upper(),clave, clave, "")
def cifrarVigenereAux(cadena, clave, retornarClave, textoCifrado):
    if cadena == "":
        return textoCifrado
    else:
        if clave == "":
            clave = retornarClave
        if cadena[0]==" ":
            return (cifrarVigenereAux(cadena[1:], retornarClave, retornarClave, textoCifrado + " "))
        else:
      
            suma= abc.find(cadena[0]) + int(clave[0]) 
       
            if suma > 26:
                posicion= suma - 26
                return (cifrarVigenereAux(cadena[1:],clave[1:],retornarClave, textoCifrado + str(abc[posicion])))
            else:
                return (cifrarVigenereAux(cadena[1:], clave[1:], retornarClave, textoCifrado + str(abc[suma])))
            
           

def descifradoVigenere(cadena,clave):
    if cadena == '' or isinstance(cadena,int):
        return 'Estos valores no pueden ser descifrados'
    else:
        return descifrarVigenereAux(cadena.upper(),clave, clave, "")
def descifrarVigenereAux(cadena, clave, retornarClave, textodescifrado):
    if cadena == "":
        return textodescifrado
    else:
        if clave == "":
            clave = retornarClave
        if cadena[0]==" ":
            return (descifrarVigenereAux(cadena[1:], retornarClave, retornarClave, textodescifrado + " "))
        else:
      
            resta= abc.find(cadena[0]) - int(clave[0]) 
            
            if resta < 0:
                posicion= 26 + resta
                return (descifrarVigenereAux(cadena[1:],clave[1:],retornarClave, textodescifrado + str(abc[posicion])))
            else:
                return (descifrarVigenereAux(cadena[1:], clave[1:], retornarClave, textodescifrado + str(abc[resta])))
            
           
  

