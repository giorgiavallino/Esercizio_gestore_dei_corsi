from database.DB_connect import DBConnect
from model.corso import Corso


# Si può scrivere semplicemente la funzione (come fatto sotto) oppure si può creare una classe e successivamente il
# relativo metodo mettendo prima @staticmethod
def get_corsi_periodo(pd):
    cnx = DBConnect.get_connection()
    result = []
    if cnx is None:
        print("Errore durante la connessione!")
        return result
    else:
        cursor = cnx.cursor(dictionary = True)
        query = """SELECT c.* 
            FROM corso c
            WHERE c.pd = %s"""
        cursor.execute(query, (pd,))
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result

def get_numero_studenti(pd):
    cnx = DBConnect.get_connection()
    result = []
    if cnx is None:
        print("Errore durante la connessione!")
        return result
    else:
        cursor = cnx.cursor()
        query = """SELECT COUNT(DISTINCT i.matricola) 
               FROM corso c, iscrizione i
               WHERE c.pd = %s AND c.codins = i.codins"""
        cursor.execute(query, (pd,))
        result = 0
        for row in cursor:
            result = row[0]
        cursor.close()
        cnx.close()
        return result

def get_all_corsi():
    cnx = DBConnect.get_connection()
    result = []
    if cnx is None:
        print("Errore durante la connessione!")
        return result
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.* 
            FROM corso c"""
        cursor.execute(query)
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result

def get_matricole_corso(codice_corso):
    cnx = DBConnect.get_connection()
    if cnx is None:
        print("Errore durante la connessione!")
        return None
    else:
        result = set()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT i.matricola* 
            FROM iscrizione i
            WHERE i.codins = %s"""
        cursor.execute(query, (codice_corso,))
        for row in cursor:
            result.add(row["matricola"]) # ora si ha un set di matricole che verrà inserito in corso
        cursor.close()
        cnx.close()
        return result