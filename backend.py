import psycopg2
from colorama import Fore
from config import config

connexio = None


def mostrarDescripcioLocalitzacio():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idlocalitzacio = input("Posa la ID de la localització que vols veure: ")
        # SENTENCIA A EXECUTAR
        consulta = " SELECT descripcio FROM localitzacions WHERE id= " + idlocalitzacio + ";"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        print(Fore.BLUE + (answer[0] + "\n"))
        print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError) as error:
        print("Aquesta ID no existeix\n")

    finally:
        if connexio is not None:
            connexio.close()


def crearLocalitzacio():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        lclnom = input("Introdueix el nom de la nova localització: ")
        lcldescripcio = input("Introdueix la descripcio de la nova localització: ")
        lclsortides = input("Introdueix una petita descripció per a la sortida de la nova localització: ")
        # SENTENCIA A EXECUTAR
        consulta = " INSERT INTO localitzacions (nom,descripcio,sortides) VALUES ('" + lclnom + "','" + lcldescripcio + "','" + lclsortides + "');"
        cursor.execute(consulta)
        connexio.commit()
        print("Localització creada")
        print()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error + "\n")

    finally:
        if connexio is not None:
            connexio.close()


def modificarLocalitzacio():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idlocalitzacio = input("Posa la ID de la localització que vols modificar: ")
        consulta = " SELECT FROM localitzacions WHERE id= " + idlocalitzacio + ";"
        if consulta:
            lclnom = input("Introdueix el nou nom de la localització: ")
            lcldescripcio = input("Introdueix la nova descripcio de la localització: ")
            lclsortides = input("Introdueix la nova petita descripció per a la sortida de la localització: ")
            # SENTENCIA A EXECUTAR
            consulta = "DELETE FROM localitzacions WHERE id = " + idlocalitzacio + ";"
            cursor.execute(consulta)
            connexio.commit()
            consulta = " INSERT INTO localitzacions (id,nom,descripcio,sortides) VALUES (" + idlocalitzacio + ",'" + lclnom + "','" + lcldescripcio + "','" + lclsortides + "');"
            cursor.execute(consulta)
            connexio.commit()
            print("Localització modificiada")
            print()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error + "Aquesta ID no existeix\n")

    finally:
        if connexio is not None:
            connexio.close()


def eliminarLocalitzacio():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idlocalitzacio = input("Posa la ID de la localització que vols eliminar: ")

        # SENTENCIA A EXECUTAR
        consulta = "DELETE FROM localitzacions WHERE id = " + idlocalitzacio + ";"
        cursor.execute(consulta)
        connexio.commit()
        print("Localització borrada")
        print()

    except(Exception, psycopg2.DatabaseError) as error:
        print("Aquesta ID no existeix\n")

    finally:
        if connexio is not None:
            connexio.close()


def llistarLocalitzacions():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        # SENTENCIA A EXECUTAR
        consulta = " SELECT * FROM localitzacions;"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        while answer is not None:
            print(answer)
            answer = cursor.fetchone()
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error + "\n")

    finally:
        if connexio is not None:
            connexio.close()


while(True):
    print("1- Mostrar una localització")
    print("2- Crear una localització")
    print("3- Modificar una localització")
    print("4- Eliminar una localització")
    print("5- Llistar totes les localitzacions")
    print("6- Sortir")
    resposta = int(input("Introduiex una opció: "))

    if resposta == 6:
        print("Andusiauu!")
        break

    if resposta == 1:
        mostrarDescripcioLocalitzacio()

    if resposta == 2:
        crearLocalitzacio()

    if resposta == 3:
        modificarLocalitzacio()

    if resposta == 4:
        eliminarLocalitzacio()

    if resposta == 5:
       llistarLocalitzacions()

