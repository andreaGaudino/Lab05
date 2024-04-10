import flet as ft

from database import corso_DAO, studente_DAO, iscrizioni_DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_btn_iscritti(self, e):
        self.stampa = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        tab = iscrizioni_DAO.Iscrizioni_dao().get_iscrizioni_corso()
        corso = self._view.menu_corsi.value
        tabella_iscritti = []
        for i in tab:
            if i.corso.codins==corso:
                tabella_iscritti.append(i.studente)


        self.stampa.controls.append(ft.Text(f"Ci sono {len(tabella_iscritti)} studenti iscritti al corso"))
        for i in tabella_iscritti:
            self._view.stampa.controls.append(ft.Text(f"{i.nome}, {i.cognome}, ({i.matricola})"))
        self._view.update_page()



