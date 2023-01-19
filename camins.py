import psycopg2
from colorama import Fore
from config import config

connexio = None


def mostraCamiOrigenDesti():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idOrigenCami = input("Posa la ID Origen del camí que vols veure: ")
        idDestiCami = input("Posa la ID Desti del camí que vols veure: ")
        # SENTENCIA A EXECUTAR
        consulta = "SELECT * FROM camins WHERE idorigen = " + idOrigenCami + " and iddesti = " + idDestiCami + ";"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        if answer is not None:
            while answer is not None:
                print(Fore.BLUE + str(answer))
                print(Fore.RESET)
                answer = cursor.fetchone()
            cursor.close()
        else:
            print(Fore.RED + "Aquest camí no existeix\n")
            print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError) as error:
        print(Fore.RED + "Aquest camí no existeix\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()


def mostraCamiOrigen():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idOrigenCami = input("Posa la ID Origen dels camins que vols veure: ")
        # SENTENCIA A EXECUTAR
        consulta = "SELECT * FROM camins WHERE idorigen = " + idOrigenCami + ";"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        if answer is not None:
            while answer is not None:
                print(Fore.BLUE + str(answer))
                print(Fore.RESET)
                answer = cursor.fetchone()
            cursor.close()
        else:
            print(Fore.RED + "Aquest camí no existeix\n")
            print(Fore.RESET)


    except(Exception, psycopg2.DatabaseError) as error:
        print(Fore.RED + "Aquest camí no existeix\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()

def mostraCamiDesti():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idDestiCami = input("Posa la ID Desti dels camins que vols veure: ")
        # SENTENCIA A EXECUTAR
        consulta = "SELECT * FROM camins WHERE iddesti = " + idDestiCami + ";"
        cursor.execute(consulta)
        answer = cursor.fetchone()
        if answer is not None:
            while answer is not None:
                print(Fore.BLUE + str(answer))
                print(Fore.RESET)
                answer = cursor.fetchone()
            cursor.close()
        else:
            print(Fore.RED + "Aquest camí no existeix\n")
            print(Fore.RESET)


    except(Exception, psycopg2.DatabaseError) as error:
        print(Fore.RED + "Aquest camí no existeix\n")
        print(Fore.RESET)

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
        consulta = " INSERT INTO camins (idOrigen,idDesti,NomOrigen,NomDesti) VALUES ('" + cmiIdOrigen + "','" + cmiIdDesti + "','" + cmiNomOrigen + "','" + cmiNomDesti + "');"
        cursor.execute(consulta)
        connexio.commit()
        print(Fore.GREEN + "Camí creat")
        print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError):
        print("Aquesta ID no es troba en la taula localitzacions\n")

    finally:
        if connexio is not None:
            connexio.close()

def modificarCami():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idOrigenCami = input("Posa la ID Origen del camí que vols modificar: ")
        idDestiCami = input("Posa la ID Desti del camí que vols modificar: ")
        consulta = " SELECT FROM camins WHERE idOrigen= " + idOrigenCami + " AND idDesti = " + idDestiCami + ";"
        if consulta:
            cmiNomOrigen = input("Introdueix el nou Nom Origen del camí: ")
            cmiNomDesti = input("Introdueix el nou Nom Desti del camí: ")
            # SENTENCIA A EXECUTAR
            consulta = " DELETE FROM camins WHERE idOrigen= " + idOrigenCami + " AND idDesti = " + idDestiCami + ";"
            cursor.execute(consulta)
            connexio.commit()
            consulta = " INSERT INTO camins (idOrigen,idDesti,NomOrigen,NomDesti) VALUES ('" + idOrigenCami + "','" + idDestiCami + "','" + cmiNomOrigen + "','" + cmiNomDesti + "');"
            cursor.execute(consulta)
            connexio.commit()
            print(Fore.GREEN + "Camí modificat")
            print(Fore.RESET)

    except(Exception, psycopg2.DatabaseError):
        print(Fore.RED + "Aquest camí no existeix\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()


def eliminarCami():
    try:
        # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
        params = config()
        connexio = psycopg2.connect(**params)
        cursor = connexio.cursor()

        idOrigenCami = input("Posa la ID Origen del camí que vols eliminar: ")
        idDestiCami = input("Posa la ID Desti del camí que vols eliminar: ")

        # SENTENCIA A EXECUTAR
        consulta = " DELETE FROM camins WHERE idOrigen= " + idOrigenCami + " AND idDesti = " + idDestiCami + ";"
        cursor.execute(consulta)
        connexio.commit()

        consulta = " SELECT FROM camins WHERE idOrigen= " + idOrigenCami + " AND idDesti = " + idDestiCami + ";"
        cursor.execute(consulta)
        connexio.commit()
        if consulta:
            print(Fore.GREEN + "Localització borrada")
            print(Fore.RESET)
        else:
            print(Fore.RED + "Aquest camí no existeix\n")
            print(Fore.RESET)


    except(Exception, psycopg2.DatabaseError):
        print(Fore.RED + "Aquest camí no existeix\n")
        print(Fore.RESET)

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
            print(Fore.BLUE + str(answer))
            print(Fore.RESET)
            answer = cursor.fetchone()
        cursor.close()

    except(Exception, psycopg2.DatabaseError):
        print(Fore.RED + "Encara no hi ha camins\n")
        print(Fore.RESET)

    finally:
        if connexio is not None:
            connexio.close()

def menuCamins():
    while(True):
        print("1- Mostrar una camí mitjançant el seu Origen i Desti")
        print("2- Mostrar els camí mitjançant el seu Origen ")
        print("3- Mostrar els camí mitjançant el seu Desti")
        print("4- Crear una camí")
        print("5- Modificar una camí")
        print("6- Eliminar una camí")
        print("7- Llistar totes les camins")
        print("8- Sortir")
        try:
            resposta = int(input("Introdueix una opció: "))

            if resposta == 8:
                print("Menu Principal:\n")
                break

            if resposta == 1:
                mostraCamiOrigenDesti()

            if resposta == 2:
                mostraCamiOrigen()

            if resposta == 3:
                mostraCamiOrigen()

            if resposta == 4:
                crearCami()

            if resposta == 5:
                modificarCami()

            if resposta == 6:
                eliminarCami()

            if resposta == 7:
               llistarCami()
        except:
            print("Aquesta opció no esta disponible")


