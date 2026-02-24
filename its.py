class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
class Docente(Persona):
    def __init__(self, nome, cognome, materia=None, titolo=None):
        super().__init__(nome, cognome)
        self._materia = materia
        self.titolo = titolo
        self._corsi = []
class Allievo(Persona):
    def __init__(self, nome, cognome, orePresenza=0):
        super().__init__(nome, cognome)
        self._orePresenza = orePresenza
        self._corso = None
class Tutor(Persona):
    def __init__(self, nome, cognome, corso, registro=None):
        super().__init__(nome, cognome)
        self._corso = corso
        self._registro = [] if registro is None else registro
    def appendToRegistro(self, allievo):
        self._registro.append(allievo)
class Corso:
    def __init__(self, dicitura, edizione, dataInizio):
        self._dicitura = dicitura
        self._edizione = edizione
        self._dataInizio = dataInizio
program = Corso("Cyber Defense & System Administrator", "biennio 2025-2027", "che inizierà il 24/11/2025")
doc = Docente("Andrea", "Ribuoli")
tu = Tutor("Cecilia", "Giacchella", program)
nomi_allievi = [
    ("Giovanni", "Artibani"),
    ("Ayoub", "Ben Hassan"),
    ("Marco", "Betti"),
    ("Tommaso", "Bravi"),
    ("Giampaolo", "Buzzi"),
    ("Maxim", "Cognigni"),
    ("Serena", "Di Gianvito"),
    ("Mirko", "Fabbrizi"),
    ("Monica", "Fiocchi"),
    ("Daniele", "Gagliardi"),
    ("Matteo", "Galeazzi"),
    ("Alessio", "Gennari"),
    ("Dulnath Nethdula", "Jayawardana"),
    ("Marco", "Lucarelli"),
    ("Adam", "Madih"),
    ("Federico", "Perotti"),
    ("Giacomo Maria", "Piersantini"),
    ("Federico", "Pruccoli"),
    ("Alessandro", "Rastelli"),
    ("Tomas", "Santi"),
    ("Emanuele", "Senesi"),
    ("Gianluca", "Taddei"),
    ("Raffaele", "Tesei"),
    ("Nicola", "Verdini"),
]
lista_allievi = [Allievo(nome, cognome) for nome, cognome in nomi_allievi]
for a in lista_allievi:
    tu.appendToRegistro(a)
print("Corso:", program._dicitura)
print()
print("Docente:", doc.nome, doc.cognome)
print("Tutor:", tu.nome, tu.cognome)
print()
print("Lista allievi:")
for a in tu._registro:
    print("-", a.cognome, a.nome)