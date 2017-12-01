def descifradoBinario(frase):
    frase = frase.split()
    if (frase=="") or isinstance(frase,int):
        return print ("Error, operando inválido.")
    else:
        return descifradoBinarioAux(frase," ")
    
def descifradoBinarioAux(frase, fraseDescifrada):
    contador = len(frase)
    if (contador==0):
        return fraseDescifrada
    else:
        print ("FRASE:",frase,"DESCIFRADO:",fraseDescifrada)
        return descifradoBinarioAux(frase[1:],fraseDescifrada+comprobarLetra(frase[0]))

def comprobarLetra(frase):
    if (frase==""):
        return "Error, operando inválido."
    else:
        return comprobarLetraAux(frase,"")

def comprobarLetraAux(frase,comprobacion):
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
