def descifradoTelefonico(frase):
    frase = frase.split()
    if (frase==""):
        return ("Ingrese el mensaje a descifrar.")
    else:
        return descifradoTelefonicoAux(frase,"")

def descifradoTelefonicoAux(frase, cifrar):
    if (frase==[]):
        return cifrar
    else:
        print ("FRASE:",frase,"CIFRAR:",cifrar)
        return descifradoTelefonicoAux(frase[1:], cifrar + str(posicionNumeral(frase[0])))
    
def posicionNumeral(numero):
    if numero == "21":
        return "a"
    elif numero == "22":
        return "b"
    elif numero == "23":
        return "c"
    elif numero == "31":
        return "d"
    elif numero == "32":
        return "e"
    elif numero == "33":
        return "f"
    elif numero == "41":
        return "g"
    elif numero == "42":
        return "h"
    elif numero == "43":
        return "i"
    elif numero == "51":
        return "j"
    elif numero == "52":
        return "k"
    elif numero == "53":
        return "l"
    elif numero == "61":
        return "m"
    elif numero == "62":
        return "n"
    elif numero == "63":
        return "o"
    elif numero == "71":
        return "p"
    elif numero == "72":
        return "q"
    elif numero == "73":
        return "r"
    elif numero == "74":
        return "s"
    elif numero == "81":
        return "t"
    elif numero == "82":
        return "u"
    elif numero == "83":
        return "v"
    elif numero == "91":
        return "w"
    elif numero == "92":
        return "x"
    elif numero == "93":
        return "y"
    elif numero == "94":
        return "z"
    elif numero == "*":
        return " "
    else:
        return " None"
    

    

    

    
    
