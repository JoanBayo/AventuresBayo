from backend import menuLocalitzacions
from camins import menuCamins


while True:
    print("1- Apartat de Localitzacions")
    print("2- Apartat de Camins")
    print("3- Sortir")
    resposta = int(input("On vols treballar? "))
    print()

    if resposta == 3:
        print("Andusiauuu!")
        break

    if resposta == 1:
        print("Benvingut al apartat de Localitzacions:")
        menuLocalitzacions()

    if resposta == 2:
        print("Benvingut al apartat de Camins:")
        menuCamins()