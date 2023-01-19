import psycopg2
from colorama import Fore
from config import config


def mostrarDescripcioObjectes():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        objid = input("Posa la ID del objecte que vols veure: ")
        # SENTENCIA A EXECUTAR
        consulta = "select * from objectes where id = " + objid + ";"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        print(Fore.BLUE +f'{answer}'+ "\n")
        print(Fore.RESET)

    except Exception as e:
        print(Fore.RED + "Aquesta ID no existeix\n")
        print(Fore.RESET)
        print(e)

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
        objPes = input("Introdueix el pes del nou objecte, es contara en kilograms: ")
        objDescripcio = input("Introdueix la descripcio del nou objecte: ")
        print("Selecciona una resposta amb 1 o 2: "
              "\n1- Si"
              "\n0- No")
        objInventari = input("Aquest objecte està a l'inventari? ")

        # SENTENCIA A EXECUTAR
        consulta = " INSERT INTO objectes (id,idlocalitzacio,object,inventari) VALUES ('" + objId + "','" + objIdLocalitzacio + "',('" + objNom + "','" + objPes + "','" + objDescripcio + "'),'" + objInventari + "');"
        cursor.execute(consulta)
        connexio.commit()
        print(Fore.GREEN + "Objecte creat")
        print(Fore.RESET)

    except Exception as e:
        print(Fore.RED + "El Objecte no s'ha creat correctament\n")
        print(Fore.RESET)
        print (e)

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

            consulta = "DELETE FROM objectes WHERE id = " + idObjecte + ";"
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


def eliminarObjecte():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idObjecte = input("Posa la ID del objecte que vols eliminar: ")

        # SENTENCIA A EXECUTAR
        consulta = "DELETE FROM objectes WHERE id = " + idObjecte + ";"
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
        consulta = " SELECT id,object FROM objectes;"
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
        try:
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

        except:
            print("Aquesta opció no esta disponible")
