import encriptacionCesar
import encriptacionLlave
import encriptacionVigenere
import encriptacionXOR
import encriptacionPalabraInversa
import encriptacionMensajeInverso
import encriptacionTelefonica
import encriptacionBinaria

def solicitarSeguirEncriptando():
    print ("¿Desea seguir utilizando los algoritmos de encriptación?. | Si / No |")
    opcion = input()
    opcion = opcion.lower()
    if (opcion == "si") or (opcion == "sí"):
        return menu()
    elif (opcion == "no"):
        return "Gracias por utilizar nuestro programa, hasta la proxima!."
    else:
        return solicitarSeguirEncriptando()
def menu():
    print ("*** Bienvenido al menú de criptografía ***")
    print ("Digíte el número para ingresar a la encriptación deseada.")
    print ("[ 1 ] -> Encriptación Cesar")
    print ("[ 2 ] -> Encriptación por llave")
    print ("[ 3 ] -> Encriptación Vigenére")
    print ("[ 4 ] -> Encriptación mediante XOR y llave")
    print ("[ 5 ] -> Encriptación de palabra inversa")
    print ("[ 6 ] -> Encriptación de mensaje inverso")
    print ("[ 7 ] -> Encriptación telefónica")
    print ("[ 8 ] -> Encriptación binaria")

    opcionDeseada = input()
    
    if (opcionDeseada == "1"):
        print ("** Ha ingresado a: Encriptación Cesar **")
        print ("¿Desea codificar o descodificar el mensaje?")
        print ("[ 1 ] -> Codificar")
        print ("[ 2 ] -> Descodificar")
        opcionDeseada = input()
        if (opcionDeseada == "1"):
            print ("Por favor, inserte la frase que desea cifrar:")
            cadena = input()
            print (">> El resultado es: <<")
            print (encriptacionCesar.cifradoCesar(cadena))
            return solicitarSeguirEncriptando()
        elif (opcionDeseada == "2"):
            print ("Por favor, inserte el mensaje que desea descifrar:")
            cadena = input()
            print (">> El resultado es: <<")
            print (encriptacionCesar.descifradoCesar(cadena))
            return solicitarSeguirEncriptando()
        else:
            return menu()
            
    elif (opcionDeseada == "2"):
        print ("** Ha ingresado a: Encriptación por llave **")
        print ("¿Desea codificar o descodificar el mensaje?")
        print ("[ 1 ] -> Codificar")
        print ("[ 2 ] -> Descodificar")
        opcionDeseada = input()
        if (opcionDeseada == "1"):
            print ("Por favor, inserte la frase que desea cifrar:")
            cadena = input()
            print ("Ahora, digite una clave:")
            clave = input()
            print (">> El resultado es: <<")
            print (encriptacionLlave.cifradoLlave(cadena, clave))
            return solicitarSeguirEncriptando()
        elif (opcionDeseada == "2"):
            print ("Por favor, inserte el mensaje que desea descifrar:")
            cadena = input()
            print ("Ahora, ingrese la clave que utilizó en el proceso de cifrado:")
            print ("* Asegúrese de digitar la clave correcta! *")
            clave = input()
            print (">> El resultado es: <<")
            print (encriptacionLlave.descifradoLlave(cadena, clave))
            return solicitarSeguirEncriptando()
        else:
            return menu()
    
    elif (opcionDeseada == "3"):
        print ("** Ha ingresado a: Encriptación Vigenére **")
        print ("¿Desea codificar o descodificar el mensaje?")
        print ("[ 1 ] -> Codificar")
        print ("[ 2 ] -> Descodificar")
        opcionDeseada = input()
        if (opcionDeseada == "1"):
            print ("Por favor, inserte la frase que desea cifrar:")
            cadena = input()
            print ("Ahora, digite una clave:")
            print ("* Recuerde que la clave deben ser dos digítos! *")
            clave = input()
            print (">> El resultado es: <<")
            print (encriptacionVigenere.cifradoVigenere(cadena, clave))
            return solicitarSeguirEncriptando()
        elif (opcionDeseada == "2"):
            print ("Por favor, inserte el mensaje que desea descifrar:")
            cadena = input()
            print ("Ahora, ingrese la clave que utilizó en el proceso de cifrado:")
            print ("* Asegúrese de digitar la clave correcta! *")
            clave = input()
            print (">> El resultado es: <<")
            print (encriptacionVigenere.descifradoVigenere(cadena, clave))
            return solicitarSeguirEncriptando()
        else:
            return menu()
    
    elif (opcionDeseada == "4"):
        print ("** Ha ingresado a: Encriptación XOR y Llave **")
        print ("¿Desea codificar o descodificar el mensaje?")
        print ("[ 1 ] -> Codificar")
        print ("[ 2 ] -> Descodificar")
        opcionDeseada = input()
        if (opcionDeseada == "1"):
            print ("Por favor, inserte la frase que desea cifrar:")
            cadena = input()
            print ("Ahora, digite una clave:")
            clave = input()
            print (">> El resultado es: <<")
            print (encriptacionXOR.cifradoXOR(cadena,clave))
            return solicitarSeguirEncriptando()
        elif (opcionDeseada == "2"):
            print ("Por favor, inserte el mensaje que desea descifrar:")
            cadena = input()
            print ("Ahora, digite una clave:")
            clave = input()
            print (">> El resultado es: <<")
            print (encriptacionXOR.descifradoXOR(cadena,clave))
            return solicitarSeguirEncriptando()
        else:
            return menu()
    
    elif (opcionDeseada == "5"):
        print ("** Ha ingresado a: Encriptación de palabra inversa **")
        print ("¿Desea codificar o descodificar el mensaje?")
        print ("[ 1 ] -> Codificar")
        print ("[ 2 ] -> Descodificar")
        opcionDeseada = input()
        if (opcionDeseada == "1") or (opcionDeseada == "2"):
            print ("Por favor, inserte la frase:")
            frase = input()
            print (">> El resultado es: <<")
            print (encriptacionPalabraInversa.invertirPalabra(frase))
            return solicitarSeguirEncriptando()
        else:
            return menu()
        
    elif (opcionDeseada == "6"):
        print ("** Ha ingresado a: Encriptación de mensaje inverso **")
        print ("¿Desea codificar o descodificar el mensaje?")
        print ("[ 1 ] -> Codificar")
        print ("[ 2 ] -> Descodificar")
        opcionDeseada = input()
        if (opcionDeseada == "1") or (opcionDeseada == "2"):
            print ("Por favor, inserte la frase:")
            frase = input()
            print (">> El resultado es: <<")
            print (encriptacionMensajeInverso.invertirMensaje(frase))
            return solicitarSeguirEncriptando()
        else:
            return menu()
        
    elif (opcionDeseada == "7"):
        print ("** Ha ingresado a: Encriptación telefónica **")
        print ("¿Desea codificar o descodificar el mensaje?")
        print ("[ 1 ] -> Codificar")
        print ("[ 2 ] -> Descodificar")
        opcionDeseada = input()
        if (opcionDeseada == "1"):
            print ("Por favor, inserte la frase que desea cifrar:")
            frase = input()
            print (">> El resultado es: <<")
            print (encriptacionTelefonica.cifradoTelefonico(frase))
            return solicitarSeguirEncriptando()
        elif (opcionDeseada == "2"):
            print ("Por favor, inserte el mensaje que desea descifrar:")
            frase = input()
            print (">> El resultado es: <<")
            print (encriptacionTelefonica.descifradoTelefonico(frase))
            return solicitarSeguirEncriptando()
        else:
            return menu()
        
    elif (opcionDeseada == "8"):
        print ("** Ha ingresado a: Encriptación binaria **")
        print ("¿Desea codificar o descodificar el mensaje?")
        print ("[ 1 ] -> Codificar")
        print ("[ 2 ] -> Descodificar")
        opcionDeseada = input()
        if (opcionDeseada == "1"):
            print ("Por favor, inserte la frase que desea cifrar:")
            frase = input()
            print (">> El resultado es: <<")
            print (encriptacionBinaria.cifradoBinario(frase))
            return solicitarSeguirEncriptando()
        elif (opcionDeseada == "2"):
            print ("Por favor, inserte el mensaje que desea descifrar:")
            frase = input()
            print (">> El resultado es: <<")
            print (encriptacionBinaria.descifradoBinario(frase))
            return solicitarSeguirEncriptando()
        else:
            return menu()
    else:
        return menu()
    
print (menu())

       
