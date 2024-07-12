import flet as ft


class Controller:
    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model
        self._pd = None

    def get_corsi_periodo(self, e):
        # pd = self._view.dd_periodo.value si può scrivere così oppure si può inserire un altro metodo il quale ogni
        # qual volta viene cambiato il valore scelto nel menù a tendina esso venga letto --> per fare questo, si
        # utilizza on_change nella dropdown inizializzata nella view
        # Per fare ciò deve essere inizializzata la variabile self._pd, inizialmente uguale a None, nell'init e
        # introdurre il metodo leggi_tendina nel controller
        if self._pd is None:
            self._view.create_alert("Selezionare il periodo didattico!")
            return
        # Il controller, come è appena stato fatto, deve sempre controllare gli input degli utenti!
        corsi = self._model.get_corsi_periodo(self._pd)
        self._view.lv_result.controls.clear()
        self._view.lv_result.controls.append(ft.Text(f"Sono presenti {len(corsi)} corsi nel periodo didattico {self._pd}"))
        for corso in corsi:
            self._view.lv_result.controls.append(ft.Text(corso.__str__()))
        self._view.update_page()

    def leggi_tendina(self, e):
        self._pd = self._view.dd_pd.value
        # Quanto appena scritto, potrebbe essere riformulato anche nel seguente modo: self._pd = e.controls.value

    def get_studenti_periodo(self, e):
        if self._pd is None:
            self._view.create_alert("Selezionare il periodo didattico!")
            return
        numero_studenti = self._model.get_numero_studenti(self._pd)
        self._view.lv_result.controls.clear()
        self._view.lv_result.controls.append(ft.Text(f"Gli studenti iscritti ai corsi dei periodo didattico {self._pd} sono {numero_studenti}"))
        self._view.update_page()

    def get_studenti_corso(self):
        pass

    def get_dettaglio_corso(self):
        pass