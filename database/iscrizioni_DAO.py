import database.DB_connect
from database.DB_connect import get_connection
from database import corso_DAO, studente_DAO
from model.iscrizione import Iscrizione


class Iscrizioni_dao:

    def get_iscrizioni_corso(self):
        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM iscrizione"""
        cursor.execute(query)
        tabella_corsi = corso_DAO.Corso_dao().get_corsi()
        tabella_studenti = studente_DAO.Studente_dao().get_studenti()
        tabella = []
        self.corso = None
        self.studente = None
        for i in cursor:
            for corso in tabella_corsi:
                if i[1] == corso.codins:
                    self.corso = corso
            for studente in tabella_studenti:
                if i[0] == studente.matricola:
                    self.studente = studente

            tabella.append(Iscrizione(self.corso, self.studente))

        return tabella





