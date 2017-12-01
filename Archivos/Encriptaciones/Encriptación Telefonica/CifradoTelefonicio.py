def cifradoTelefonico(frase):
    frase=frase.lower()
    frase=list(frase)
    if (frase==""):
        return ("Ingrese una frase.")
    else:
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

    
