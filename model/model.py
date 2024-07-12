from database import DAO

class Model:

    # Una soluzione alternativa potrebbe essere quella di memeorizzare tutti i corsi subito
    def __init__(self):
        self.corsi = DAO.get_all_corsi()
    # e di andare a lavorare su questa lista direttamente

    def get_corsi_periodo(self, pd):
        # Soluzione con filtro fatta in Python e da Python
        corsi_periodo = []
        for corso in self.corsi:
           if corso.pd == pd:
               corsi_periodo.append(corso)
        return corsi_periodo

        # Soluzione con filtro fatta nella query
        return DAO.get_corsi_periodo(pd)

    # In questi casi conviene scegliere i due metodi in base alla complessità della query...
    # in questo caso, la soluzione creata attraverso la query è forse la migliore

    def get_numero_studenti(self, pd):
        # Soluzione programmatica con le relazioni
        matricole_iscritti = set() # Si utilizza un set perché gli elementi uguali, ma presenti più volte vengono presi
        # in considerazione una volta sola
        for corso in self.corsi:
            if corso.pd == pd:
                # Se le matricole non sono inizializzate, allora...
                if corso.matricole is None:
                    corso.matricole = DAO.get_matricole_corso(corso.codins)
                matricole_iscritti = matricole_iscritti.union(corso.matricole)
        return len(matricole_iscritti)

        # Soluzione con il join da SQL
        # return DAO.get_corsi_periodo(pd)