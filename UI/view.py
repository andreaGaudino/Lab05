import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        #row 1
        self.menu_corsi = ft.Dropdown(width=700, label="Selezionare un corso")
        self.btn_cerca_iscritti = ft.ElevatedButton("Cerca iscritti")

        row1 = ft.Row([self.menu_corsi, self.btn_cerca_iscritti], alignment=ft.MainAxisAlignment.CENTER)



        #row2
        self.matricola = ft.TextField(label="Matricola")
        self.cognome = ft.TextField(label="Cognome", read_only=True)
        self.nome = ft.TextField(label="Nome", read_only=True)
        row2 = ft.Row([self.matricola, self.cognome, self.nome], alignment=ft.MainAxisAlignment.CENTER)

        #row3
        self.cerca_studente = ft.ElevatedButton("Cerca studente")
        self.cerca_corsi = ft.ElevatedButton("Cerca corsi")
        self.iscrivi = ft.ElevatedButton("Iscrivi")
        row3 = ft.Row([self.cerca_studente, self.cerca_corsi, self.iscrivi], alignment=ft.MainAxisAlignment.CENTER)



        self._page.add(row1,row2, row3)
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
