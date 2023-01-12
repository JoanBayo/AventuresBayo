from backend import menuLocalitzacions
from camins import menuCamins
from objectes import menuObjectes
from protagonista import menuProtagonista

while True:
    print("1- Apartat de Localitzacions")
    print("2- Apartat de Camins")
    print("3- Apartat de Objectes")
    print("4- Modificar el Personatge")
    print("5- Sortir")
    resposta = int(input("On vols treballar? "))
    print()

    if resposta == 5:
        print("Andusiauuu!")
        break

    if resposta == 1:
        print("Benvingut al apartat de Localitzacions:")
        menuLocalitzacions()

    if resposta == 2:
        print("Benvingut al apartat de Camins:")
        menuCamins()

    if resposta == 3:
        print("Benvingut al apartat d'Objectes:")
        menuObjectes()

    if resposta == 4:
        print("Edita el teu protagonista al teu gust:")
        menuProtagonista()