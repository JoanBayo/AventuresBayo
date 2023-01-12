import psycopg2
from colorama import Fore
from config import config

connexio = None

def menuProtagonista():
    global connexio
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()


        consulta = "DELETE * FROM protagonista;"
        cursor.execute(consulta)
        objIdLocalitzacio = input("Introdueix la IdLocalització del nou objecte: ")
        objNom = input("Introdueix el nom del nou objecte: ")
        objPes = input("Introdueix el pes del nou objecte, es contara en kilograms: ")
        objDescripcio = input("Introdueix la descripcio del nou objecte: ")
        print("Selecciona una resposta en 1 o 2: "
              "\n1- Si"
              "\n0- No")
        objInventari = input("Aquest objecte està a l'inventari? ")
        # SENTENCIA A EXECUTAR
        consulta = " INSERT INTO objectes (id,idlocalitzacio,object,inventari) VALUES ('" + idObjecte + "','" + objIdLocalitzacio + "',('" + objNom + "','" + objPes + "','" + objDescripcio + "'),'" + objInventari + "');"
        cursor.execute(consulta)
        connexio.commit()
        print(Fore.GREEN + "Objecte creat")
        print(Fore.RESET)

    except Exception as e:
        print(Fore.RED + "Aquesta ID no existeix\n")
        print(Fore.RESET)
        print(e)

    finally:
        if connexio is not None:
            connexio.close()
