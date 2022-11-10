import psycopg2
from colorama import Fore
from config import config

connexio = None


def mostraCami():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idCami = input("Posa la ID del camí que vols veure: ")
        # SENTENCIA A EXECUTAR
        consulta = " SELECT * FROM camins WHERE id= " + idCami + ";"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        print(Fore.RED + (answer[0] + "\n"))
        print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError) as error:
        print("Aquesta ID no existeix\n")

    finally:
        if connexio is not None:
            connexio.close()


def crearCami():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        cmiIdOrigen = input("Introdueix la IdOrigen del nou camí: ")
        cmiIdDesti = input("Introdueix la IdDesti del nou camí: ")
        cmiNomOrigen = input("Introdueix el Nom Origen del nou camí: ")
        cmiNomDesti = input("Introdueix el Nom Desti del nou camí: ")
        # SENTENCIA A EXECUTAR
        consulta = " INSERT INTO camins (idOrigen,idDesti,NomOrigen,NomDesti) VALUES ('" + cmiIdOrigen + "','" + cmiIdDesti + "','" + cmiNomOrigen + "''" + cmiNomDesti + "');"
        cursor.execute(consulta)
        connexio.commit()
        print("Camí creat")
        print()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error + "\n")

    finally:
        if connexio is not None:
            connexio.close()


def modificarCami():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idCami = input("Posa la ID del camí que vols modificar: ")
        consulta = " SELECT FROM camins WHERE id= " + idCami + ";"
        if consulta:
            cmiIdOrigen = input("Introdueix la nova IdOrigen del camí: ")
            cmiIdDesti = input("Introdueix la nova IdDesti del camí: ")
            cmiNomOrigen = input("Introdueix el nou Nom Origen del camí: ")
            cmiNomDesti = input("Introdueix el nou Nom Desti del camí: ")
            # SENTENCIA A EXECUTAR
            consulta = " INSERT INTO camins (idOrigen,idDesti,NomOrigen,NomDesti) VALUES ('" + cmiIdOrigen + "','" + cmiIdDesti + "','" + cmiNomOrigen + "''" + cmiNomDesti + "');"
            cursor.execute(consulta)
            connexio.commit()
            print("Camí creat")
            print()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error + "Aquesta ID no existeix\n")

    finally:
        if connexio is not None:
            connexio.close()


def eliminarCami():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idCami = input("Posa la ID del camí que vols eliminar: ")

        # SENTENCIA A EXECUTAR
        consulta = "DELETE FROM camins WHERE id = " + idCami + ";"
        cursor.execute(consulta)
        connexio.commit()
        print("Localització borrada")
        print()

    except(Exception, psycopg2.DatabaseError) as error:
        print("Aquesta ID no existeix\n")

    finally:
        if connexio is not None:
            connexio.close()


def llistarCami():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        # SENTENCIA A EXECUTAR
        consulta = " SELECT * FROM camins;"
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
    print("1- Mostrar una camí")
    print("2- Crear una camí")
    print("3- Modificar una camí")
    print("4- Eliminar una camí")
    print("5- Llistar totes les camins")
    print("6- Sortir")
    resposta = int(input("Introduiex una opció: "))

    if resposta == 6:
        print("Andusiauu!")
        break

    if resposta == 1:
        mostraCami()

    if resposta == 2:
        crearCami()

    if resposta == 3:
        modificarCami()

    if resposta == 4:
        eliminarCami()

    if resposta == 5:
       llistarCami()


