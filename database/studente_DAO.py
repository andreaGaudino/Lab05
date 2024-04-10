# Add whatever it is needed to interface with the DB Table studente
import database.DB_connect
from database.DB_connect import get_connection
from model.studente import Studente


class Studente_dao:
    def get_studenti(self):
        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM studente"""
        cursor.execute(query)
        tabella = []
        for i in cursor:
            tabella.append(Studente(i[0], i[1], i[2], i[3]))
        return tabella
        cursor.close()
        cnx.close()