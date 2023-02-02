import psycopg2
from colorama import Fore
from config import config

def updateProtagonistScreen():
    # try:
    #     # PARAMETRES NECESSARIS PER CONECTARNOS A LA NOSTRA BD
    #     params = config()
    #     connexio = psycopg2.connect(**params)
    #     cursor = connexio.cursor()
    #
    #     consulta = "DELETE FROM protagonista;"
    #     cursor.execute(consulta)
    #     nom = input("Introdueix el nom: ")
    #     descripcio = input("Fes una breu descricpió del personatge: ")
    #     sexe = input("Introduiex el sexe del personatge pot ser masculí, femení i altres: ")
    #     edad = input("Introdueix la edad a de ser major de 18 i menor de 99: ")
    #     altura = input("Introdueix l'alçada, els decimals amb un (.) = 1.82: ")
    #     pes = input("Introdueix el pes, els decimals amb un (.) = 70.8: ")
    #     print()
    #     print("Ara posarem els estats del teu personatge, tots han de estar entre 1-20")
    #     forca = input("- Força: ")
    #     resistencia = input("- Rsistencia: ")
    #     destresa = input("- Destresa: ")
    #     print("La salut del teu personatge serà dos cops la seva resistencia")
    #     salut = str(int(resistencia) * 2)
    #
    #     # SENTENCIA A EXECUTAR
    #     consulta = "INSERT INTO protagonista VALUES ('" + nom + "','" + descripcio + "','" + sexe + "'," + edad + "," + altura + "," + pes + "," + forca + "," + destresa + "," + resistencia + "," + salut + ");"
    #     cursor.execute(consulta)
    #     connexio.commit()
    #     print(Fore.GREEN + "Personatge actualitzat perfectament!")
    #     print(Fore.RESET)
    #
    #
    # except Exception as e:
    #     print(e)
    #     print(Fore.RED + "Algun dels valors anteriors no és correcte, mira bé les condicions i torna a provar-ho")
    #     print(Fore.RESET)
    #
    # finally:
    #     if connexio is not None:
    #         connexio.close()

    pass
