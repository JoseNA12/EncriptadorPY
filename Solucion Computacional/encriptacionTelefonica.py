import validacion
def cifradoTelefonico(frase):
    if (frase==""):
        return ("Ingrese una frase.")
    elif isinstance(frase, int) or validacion.validacion(frase.upper(),False)==False:
        return ("Error, no es posible cifrar números ni caracteres especiales. Use únicamente el abecedario")
    else:
        frase=frase.lower()
        frase=list(frase)
        return cifradoTelefonicoAux(frase," ")

def cifradoTelefonicoAux(frase, cifrar):
    if (frase==[]):
        return cifrar
    else:
        return cifradoTelefonicoAux(frase[1:], cifrar + str(posicionLetra(frase[0]))+" ")
    
def posicionLetra(letra):
    teclaDos=["a","b","c"]
    teclaTres=["d","e","f"]
    teclaCuatro=["g","h","i"]
    teclaCinco=["j","k","l"]
    teclaSeis=["m","n","o"]
    teclaSiete=["p","q","r","s"]
    teclaOcho=["t","u","v"]
    teclaNueve=["w","x","y","z"]
    espacioBlanco=[" "]
    
    if encontrarLetra(letra, teclaDos) == True:
        return int("2"+ str(teclaDos.index(letra)+1))
    elif encontrarLetra(letra,teclaTres) == True:
        return int("3"+str(teclaTres.index(letra)+1))
    elif encontrarLetra(letra, teclaCuatro) == True:
        return int("4"+str(teclaCuatro.index(letra)+1))
    elif encontrarLetra(letra, teclaCinco) == True:
        return int("5"+str(teclaCinco.index(letra)+1))
    elif encontrarLetra(letra, teclaSeis) == True:
        return int("6"+str(teclaSeis.index(letra)+1))
    elif encontrarLetra(letra, teclaSiete) == True:
        return int("7"+str(teclaSiete.index(letra)+1))
    elif encontrarLetra(letra, teclaOcho) == True:
        return int("8"+str(teclaOcho.index(letra)+1))
    elif encontrarLetra(letra, teclaNueve) == True:
        return int("9"+str(teclaNueve.index(letra)+1))
    elif encontrarLetra(letra, espacioBlanco) == True:
        return ("*")
                           
def encontrarLetra(letra, frase):
    if frase == []:
        return False
    elif letra == frase[0]:
        return True
    else:
        return encontrarLetra(letra, frase[1:])



def descifradoTelefonico(frase):
    if (frase==""):
        return ("Ingrese el mensaje a descifrar.")
    if validacion.validacionNumerica(frase,False)==False:
        return "Error, la frase ingresada no debe contener letras ni caracteres."
    else:
        frase = frase.split()
        return descifradoTelefonicoAux(frase,"")

def descifradoTelefonicoAux(frase, cifrar):
    if (frase==[]):
        return cifrar
    else:
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
    
