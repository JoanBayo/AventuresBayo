import psycopg2
from colorama import Fore
from config import config


def mostrarDescripcioObjectes():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        id = input("Posa la ID del objecte que vols veure: ")
        # SENTENCIA A EXECUTAR
        consulta = " SELECT descripcio FROM objectes WHERE id= " + id + ";"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        print(Fore.BLUE + (answer[0] + "\n"))
        print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError):
        print(Fore.RED + "Aquesta ID no existeix\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()


def crearObjecte():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()
        objId = input("Introdueix la ID del nou objecte: ")
        objIdLocalitzacio = input("Introdueix la IdLocalització del nou objecte: ")
        objNom = input("Introdueix el nom del nou objecte: ")
        objPes = input("Introdueix el pes del nou objecte: ")
        objDescripcio = input("Introdueix la descripcio del nou objecte: ")
        print("Selecciona una resposta: "
              "\n1- Si"
              "\n2- No")
        objInventari = input("Aquest objecte està a l'inventari? ")
        # SENTENCIA A EXECUTAR
        consulta = " INSERT INTO objectes (id,idlocalitzacio,object,inventari) VALUES ('" + objId + "','" + objIdLocalitzacio + "',('" + objNom + "','" + objPes + "','" + objDescripcio + "'),'" + objInventari + "');"
        cursor.execute(consulta)
        connexio.commit()
        print(Fore.GREEN + "Objecte creat")
        print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError):
        print(Fore.RED + "El Objecte no s'ha creat correctament\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()


def modificarObjecte():
    global connexio
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idObjecte = input("Posa la ID del objecte que vols modificar: ")
        consulta = " SELECT FROM objectes WHERE id= " + idObjecte + ";"
        if consulta:
            objId = input("Introdueix la ID del nou objecte: ")
            objIdLocalitzacio = input("Introdueix la IdLocalització del nou objecte: ")
            print("Selecciona una resposta: "
                  "\n1- Si"
                  "\n2- No")
            objInventari = input("Aquest objecte està a l'inventari? ")
            objNom = input("Introdueix el nom del nou objecte: ")
            objPes = input("Introdueix el pes del nou objecte: ")
            objDescripcio = input("Introdueix la descripcio del nou objecte: ")
            # SENTENCIA A EXECUTAR
            consulta = " INSERT INTO objectes (id,idlocalitzacio,object,inventari) VALUES ('" + objId + "','" + objIdLocalitzacio + "',('" + objNom + "','" + objPes + "','" + objDescripcio + "'),'" + objInventari + "');"
            cursor.execute(consulta)
            connexio.commit()
            print(Fore.GREEN + "Objecte creat")
            print(Fore.RESET)
    except(Exception, psycopg2.DatabaseError):
        print(Fore.RED + "Aquesta ID no existeix\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()


def eliminarObjecte():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idObjecte = input("Posa la ID del objecte que vols eliminar: ")

        # SENTENCIA A EXECUTAR
        consulta = "DELETE FROM objectes WHERE id = " + id + ";"
        cursor.execute(consulta)
        connexio.commit()
        print(Fore.GREEN + "Objecte borrada")
        print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError):
        print(Fore.RED + "Aquesta ID no existeix\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()


def llistarObjectes():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        # SENTENCIA A EXECUTAR
        consulta = " SELECT * FROM objectes;"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        while answer is not None:
            print(Fore.BLUE + str(answer))
            answer = cursor.fetchone()
        cursor.close()
        print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError):
        print(Fore.RED + "Encara no hi ha localitzacions\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()


def menuObjectes():
    while (True):
        print("1- Mostrar un objecte")
        print("2- Crear un objecte")
        print("3- Modificar un objecte")
        print("4- Eliminar un objecte")
        print("5- Llistar tots els objectes")
        print("6- Sortir")
        resposta = int(input("Introdueix una opció: "))

        if resposta == 6:
            print("Menu Principal:\n")
            break

        if resposta == 1:
            mostrarDescripcioObjectes()

        if resposta == 2:
            crearObjecte()

        if resposta == 3:
            modificarObjecte()

        if resposta == 4:
            eliminarObjecte()

        if resposta == 5:
            llistarObjectes()

            # Se te que treballar en types, per fer aixo mirar a dungeonofbits, tenim que crear uuna taula objectes que incloura id, id localitzacions i lo type de objectes el qual inclou nom pes i descripcio, per fer tot aixo tenim que modificar molt tot aixo

