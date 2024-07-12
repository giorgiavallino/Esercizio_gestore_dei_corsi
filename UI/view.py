import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # Elementi relativi alla pagina in generale
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self._controller = None
        # Elementi grafici
        self._title = None
        self.dd_pd = None
        self.btn_corsi_periodo = None
        self.btn_studenti_periodo = None
        self.txt_codice_corso = None
        self.btn_studenti_corso = None
        self.btn_dettaglio_corso = None
        self.lv_result = None

    def load_interface(self):

        # Titolo
        self._title = ft.Text("Gestore dei corsi", color="blue", size=24)
        self._page.add(self._title)

        # Row 1
        self.dd_pd = ft.Dropdown(label = "Periodo didattico",
                                 hint_text = "Selezionare il periodo didattico",
                                 options = [ft.dropdown.Option(key = "1"), ft.dropdown.Option(key = "2")],
                                 width = 200)
        self.btn_corsi_periodo = ft.ElevatedButton(text = "Corsi del periodo didattico",
                                                   tooltip = "Ottenere i corsi del periodo didattico selezionato",
                                                   on_click = self._controller.get_corsi_periodo)
        self.btn_studenti_periodo = ft.ElevatedButton(text = "Studenti del periodo didattico",
                                                      tooltip = "Ottenere gli studenti iscritti ai corsi del periodo didattico",
                                                      on_click = self._controller.get_studenti_periodo)
        row_01 = ft.Row([self.dd_pd, self.btn_corsi_periodo, self.btn_studenti_periodo],
                        alignment = ft.MainAxisAlignment.CENTER)
        self._page.add(row_01)
        self.update_page()

        # Row 2
        self.txt_codice_corso = ft.TextField(label = "Codice del corso",
                                             hint_text = "Inserire il codice del corso",
                                             width = 400)
        self.btn_studenti_corso = ft.ElevatedButton(text = "Studenti del corso",
                                                    tooltip = "Ottenere gli studenti iscritti al corso selezionato",
                                                    on_click = self._controller.get_studenti_corso)
        self.btn_dettaglio_corso = ft.ElevatedButton(text = "Corso di studio degli studenti",
                                                     tooltip = "Ottenere i corsi di studio degli iscritti al corso selezionato",
                                                     on_click = self._controller.get_dettaglio_corso)
        row_02 = ft.Row([self.txt_codice_corso, self.btn_studenti_corso, self.btn_dettaglio_corso],
                        alignment = ft.MainAxisAlignment.CENTER)
        self._page.add(row_02)
        self.update_page()

        # List view --> è un contenitore di righe, non un campo di testo!
        self.lv_result = ft.ListView(expand = 1,
                                     spacing = 10,
                                     padding = 20,
                                     auto_scroll = True)
        self._page.add(self.lv_result)
        self.update_page()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()