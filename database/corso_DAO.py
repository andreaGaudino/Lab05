# Add whatever it is needed to interface with the DB Table corso
import database.DB_connect
from database.DB_connect import get_connection
from model.corso import Corso


class Corso_dao:
    def get_corsi(self):
        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM corso"""
        cursor.execute(query)
        tabella = []
        for i in cursor:
            tabella.append(Corso(i[0], i[1], i[2], i[3]))

        return tabella
        cursor.close()
        cnx.close()


if __name__=="__main__":
    a= Corso_dao()
    lista=a.get_corsi()
    for e in lista:
        print(e)