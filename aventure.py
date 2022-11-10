while(True):

    print("1- Crear una nova partida")
    print("2- Continuar una partida")
    print("3- Sortir")
    resposta = int(input("Introdueix una opció: "))

    if resposta == 3:
        print("Andusiauu!")
        break


    if resposta == 1:
        nomUsuari = input("Introdueix el teu nom de jugador: ")
        identificadorUsuari = input("Introdueix l'identificador d'aquesta partida: ")

    if resposta == 2:
        nomUsuari = input("Introdueix el teu nom de jugador: ")
        identificadorUsuari = input("Introdueix l'identificador de la partida que vulguis iniciar: ")