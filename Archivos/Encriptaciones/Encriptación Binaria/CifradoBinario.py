def cifradoBinario(frase):
    if (frase=="") or isinstance(frase,int):
        return print ("Error, operando inválido.")
    else:
        return cifradoBinarioAux(frase,"")
    
def cifradoBinarioAux(frase, fraseCifrada):
    frase = frase.lower()
    if (frase==""):
        return fraseCifrada
    else:
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

