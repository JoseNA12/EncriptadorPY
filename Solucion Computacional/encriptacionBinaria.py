import validacion

def cifradoBinario(frase):
    if (frase=="") or isinstance(frase,int) or validacion.validacion(frase.upper(),False)==False:
        return print ("Error, operando inválido. La cadena no debe estar vacía y no debe utilizar números enteros. No es posible cifrar números ni caracteres especiales. Use únicamente el abecedario")
    else:
        return cifradoBinarioAux(frase,"")
    
def cifradoBinarioAux(frase, fraseCifrada):
    if (frase==""):
        return fraseCifrada
    else:
        frase = frase.lower()
        return cifradoBinarioAux(frase[1:],fraseCifrada+" "+comprobarLetra(frase[0]))

def comprobarLetra(frase):
    if (frase==""):
        return"Error, operando inválido."
    else:
        return comprobarLetraAux(frase,"")

def comprobarLetraAux(frase,comprobacion):
    if (frase==""):
        return comprobacion
    else:
        if (frase=="a"):
            return "00000"
        elif (frase=="b"):
            return "00001"
        elif (frase=="c"):
            return "00010"
        elif (frase=="d"):
            return "00011"
        elif (frase=="e"):
            return "00100"
        elif (frase=="f"):
            return "00101"
        elif (frase=="g"):
            return "00110"
        elif (frase=="h"):
            return "00111"
        elif (frase=="i"):
            return "01000"
        elif (frase=="j"):
            return "01001"
        elif (frase=="k"):
            return "01010"
        elif (frase=="l"):
            return "01011"
        elif (frase=="m"):
            return "01100"
        elif (frase=="n"):
            return "01101"
        elif (frase=="o"):
            return "01110"
        elif (frase=="p"):
            return "01111"
        elif (frase=="q"):
            return "10000"
        elif (frase=="r"):
            return "10001"
        elif (frase=="s"):
            return "10010"
        elif (frase=="t"):
            return "10011"
        elif (frase=="u"):
            return "10100"
        elif (frase=="v"):
            return "10101"
        elif (frase=="w"):
            return "10110"
        elif (frase=="x"):
            return "10111"
        elif (frase=="y"):
            return "11000"
        elif (frase=="z"):
            return "11001"
        elif (frase==" "):
            return "*"
        else:
            return "None"



def descifradoBinario(frase):
    frase = frase.split()
    if (frase=="") or isinstance(frase,int): #or validacion.validacionNumerica(frase,False)==False
        return ("Error, operando inválido. La cadena no debe estar vacía. No es posible descifrar letras ni caracteres especiales. Use únicamente números")
    else:
        return descifradoBinarioAux(frase,"")
    
def descifradoBinarioAux(frase, fraseDescifrada):
    contador = len(frase)
    if (contador==0):
        return fraseDescifrada
    else:
        return descifradoBinarioAux(frase[1:],fraseDescifrada+comprobarBinario(frase[0]))

def comprobarBinario(frase):
    if (frase==""):
        return "Error, operando inválido."
    else:
        return comprobarBinarioAux(frase,"")

def comprobarBinarioAux(frase,comprobacion):
    if (frase==""):
        return comprobacion
    else:
        if (frase=="00000"):
            return "a"
        elif (frase=="00001"):
            return "b"
        elif (frase=="00010"):
            return "c"
        elif (frase=="00011"):
            return "d"
        elif (frase=="00100"):
            return "e"
        elif (frase=="00101"):
            return "f"
        elif (frase=="00110"):
            return "g"
        elif (frase=="00111"):
            return "h"
        elif (frase=="01000"):
            return "i"
        elif (frase=="01001"):
            return "j"
        elif (frase=="01010"):
            return "k"
        elif (frase=="01011"):
            return "l"
        elif (frase=="01100"):
            return "m"
        elif (frase=="01101"):
            return "n"
        elif (frase=="01110"):
            return "o"
        elif (frase=="01111"):
            return "p"
        elif (frase=="10000"):
            return "q"
        elif (frase=="10001"):
            return "r"
        elif (frase=="10010"):
            return "s"
        elif (frase=="10011"):
            return "t"
        elif (frase=="10100"):
            return "u"
        elif (frase=="10101"):
            return "v"
        elif (frase=="10110"):
            return "w"
        elif (frase=="10111"):
            return "x"
        elif (frase=="11000"):
            return "y"
        elif (frase=="11001"):
            return "z"
        elif (frase=="*"):
            return " "
        else:
            return "."
   
