import csv
from operator import attrgetter
class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)

    def __str__(self):
        # Questo metodo si attiva automaticamente quando fai print(oggetto_strumento)
        return f"Codice {self.id_strumento}: {self.tipo}, {self.marca}, {self.anno_acquisto}, {self.valore:.2f} €"

class Prestito:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.id_prestito = id_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"Prestito {self.id_prestito}: Strumento {self.id_strumento} a {self.cognome_allievo} in data {self.data}"


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}
        self.cont_p = 1


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open (file_path, "r", encoding = "utf-8") as file:
                reader = csv.reader(file)
                for line in reader:
                    id_strumento = line[0]
                    tipo = line[1]
                    marca = line[2]
                    anno = line[3]
                    valore = line[4]

                    # Crea l'oggetto Strumento
                    nuovo_strumento = Strumento(id_strumento, tipo, marca, anno, valore)

                    # Salva lo strumento nel dizionario usando l'ID (es. 'S1') come chiave
                    self.strumenti[id_strumento] = nuovo_strumento

        except FileNotFoundError:
            print(f"File {file_path} non trovato")


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        codice = "S" + str(len(self.strumenti) + 1)
        nuovo_strumento_tastiera = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti[codice] = nuovo_strumento_tastiera
        return nuovo_strumento_tastiera

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        ordinati = sorted(self.strumenti.values(), key=attrgetter("marca"))
        return ordinati
    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception ("strumento non trovato")
        if id_strumento in self.prestiti:
            raise Exception ("lo strumento è già in prestito")
        else:
            id_prestito = "P" +str(self.cont_p)
            self.cont_p += 1
            nuovo_prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)
            self.prestiti[id_prestito] = nuovo_prestito
            return nuovo_prestito
    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            raise Exception(f"Errore: il prestito '{id_prestito}' non esiste.")
            # Rimozione del prestito dal sistema
        self.prestiti.pop(id_prestito, None)
