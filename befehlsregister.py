class Befehlsregister:

    def __init__(self, datenbus, adressbus):
        self.datenbus = datenbus
        self.adressbus = adressbus
        self.befehl = ""
        self.adresse = ""

    def parse(self):
        if self.befehl.upper() == "LDA":
            if self.adresse[0] == "#":
                self.datenbus.akku.speicher = int(self.adresse[1:])
            elif self.adresse[0] == "(":
                self.datenbus.akku.speicher = int(self.adressbus.speicher.zellen[self.adressbus.speicher.zellen[int(self.adresse)].daten].daten)
            else:
                self.datenbus.akku.speicher = int(self.adressbus.speicher.zellen[int(self.adresse)].daten)
        elif self.befehl.upper() == "STA":
            if self.adresse[0] == "(":
                self.adressbus.speicher.zellen[self.adressbus.speicher.zellen[int(self.adresse)].daten].daten = str(self.datenbus.akku.speicher)
            else:
                self.adressbus.speicher.zellen[int(self.adresse)].daten = str(self.datenbus.akku.speicher)
        elif self.befehl.upper() == "ADD":
            self.datenbus.alu.speicher = int(self.adressbus.speicher.zellen[int(self.adresse)].daten)
            self.datenbus.alu.addieren()
        elif self.befehl.upper() == "SUB":
            self.datenbus.alu.speicher = int(self.adressbus.speicher.zellen[int(self.adresse)].daten)
            self.datenbus.alu.subtrahieren()
        elif self.befehl.upper() == "MUL":
            self.datenbus.alu.speicher = int(self.adressbus.speicher.zellen[int(self.adresse)].daten)
            self.datenbus.alu.multiplizieren()
        elif self.befehl.upper() == "DIV":
            self.datenbus.alu.speicher = int(self.adressbus.speicher.zellen[int(self.adresse)].daten)
            self.datenbus.alu.dividieren()
        elif self.befehl.upper() == "JMP":
            self._jump()
        elif self.befehl.upper() == "JNZ":
            if self.datenbus.alu.istNichtNull():
                self._jump()
        elif self.befehl.upper() == "JZE":
            if self.datenbus.alu.istNull():
                self._jump()
        elif self.befehl.upper() == "JLE":
            if self.datenbus.alu.istKleinerGleichNull():
                self._jump()
        elif self.befehl.upper() == "STP":
            return False
        else:
            raise ValueError ("Nicht unterstuetzter Befehl:" , self.befehl)
        return True

    def _jump(self):
        if self.adresse[0] == "(":
            self.datenbus.befehlszaehler.adresse = int(self.adressbus.speicher.zellen[int(self.adresse)].daten)
        else:
            self.datenbus.befehlszaehler.adresse = int(self.adresse)
