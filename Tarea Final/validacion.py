abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '123456789*'

def validacion(cadena,resultado):
    
    if cadena == "":
        return resultado
    
    else:
        if cadena[0]== " ":
            return validacion(cadena[1:],resultado)
        
        if abc.find(cadena[0])== -1:
            return False
    
        else:
            return validacion(cadena[1:],True)

def validacionNumerica(cadena,resultado):
    if cadena == "":
        return resultado
    
    else:
        if cadena[0]==" ":
            return validacionNumerica(cadena[1:],True)
        
        if numeros.find(cadena[0])== -1:
            return False
    
        else:
            return validacionNumerica(cadena[1:],True)
