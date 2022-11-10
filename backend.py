import psycopg2
from config import config
from termcolor import colored
connexio = None



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
            print(colored(answer[0] + "\n", 'blue'))

        except(Exception, psycopg2.DatabaseError) as error:
            print("Aquesta ID no existeix\n")

        finally:
            if connexio is not None:
                connexio.close()


    if resposta == 2:
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

    # TROBAR LA ID DEL CAM QUE BORRA I GUARDARLI AL NOU CAMP I ACABAR DE FER-HO TOT

    if resposta == 3:
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


    if resposta == 4:
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


 #FER UN WHERE PER TAL DE PRINTEJAR TOTES LES LOCALITZACIONS
    if resposta == 5:
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



