import flet as ft
import database.DB_connect
from database import corso_DAO, studente_DAO, iscrizioni_DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_btn_iscritti(self, e):

        tab = iscrizioni_DAO.Iscrizioni_dao().get_iscrizioni_corso()
        corso = self._view.menu_corsi.value
        if corso is None:
            self._view.create_alert("Selezionare un corso!")

        else:
            tabella_iscritti = []
            for i in tab:
                if i.corso.codins==corso:
                    tabella_iscritti.append(i.studente)

            self._view.stampa.clean()
            self._view.update_page()
            self._view.stampa.controls.append(ft.Text(f"Ci sono {len(tabella_iscritti)} studenti iscritti al corso"))
            for i in tabella_iscritti:
                self._view.stampa.controls.append(ft.Text(f"{i.nome}, {i.cognome}, ({i.matricola})"))
            self._view.update_page()

    def handle_cerca_studente(self,e):
        studente = str(self._view.matricola.value)
        inesistente = True
        if studente=="":
            self._view.create_alert("Seleziona una matricola!")
        else:
            tab = studente_DAO.Studente_dao().get_studenti()
            for stud in tab:
                if str(stud.matricola)==studente:
                    inesistente = False
                    self._view.cognome.value = stud.cognome
                    self._view.nome.value = stud.nome
                    self._view.update_page()
        if inesistente == True:
            self._view.create_alert("Studente non esistente!")
    def handle_cerca_corsi(self, e):
        studente = str(self._view.matricola.value)
        inesistente = True
        self._view.stampa.clean()
        self._view.update_page()
        if studente == "":
            self._view.create_alert("Seleziona una matricola!")

        else:
            tab_iscritti = iscrizioni_DAO.Iscrizioni_dao().get_iscrizioni_corso()
            tab_corsi = []
            for iscrizione in tab_iscritti:
                if str(iscrizione.studente.matricola) == studente:
                    inesistente = False
                    tab_corsi.append(iscrizione.corso)
            self._view.stampa.controls.append(ft.Text(f"Lo studente {studente} è iscritto a {len(tab_corsi)} corsi"))
            for i in tab_corsi:
                self._view.stampa.controls.append(ft.Text(f"{i.nome} ({i.codins})"))
            self._view.update_page()

        if inesistente==True:
            self._view.create_alert("Studente non esistente!")

    def handle_iscrivi(self, e):
        matricola = str(self._view.matricola.value)
        codins = self._view.menu_corsi.value

        if matricola == "" or codins is None:
            self._view.create_alert("Matricola studente o corso incompleti!")
        else:
            cnx = database.DB_connect.get_connection()
            cursor = cnx.cursor()
            query = """INSERT INTO iscrizione
                        (matricola, codins)
                        VALUES(%s, %s)
                        """
            cursor.execute(query, (matricola, codins))
            cnx.commit()
            cursor.close()
            cnx.close()




