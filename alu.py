class ALU:

    def __init__(self, akku):
        self.speicher = 0
        self.akku = akku
        
    def addieren(self):
        self.akku.speicher = self.akku.speicher + self.speicher

    def subtrahieren(self):
        self.akku.speicher = self.akku.speicher - self.speicher

    def multiplizieren(self):
        self.akku.speicher = self.akku.speicher * self.speicher

    def dividieren(self):
        self.akku.speicher = self.akku.speicher / self.speicher

    def istNull(self):
        return self.akku.speicher == 0

    def istNichtNull(self):
        return self.akku.speicher <> 0

    def istKleinerGleichNull(self):
        return self.akku.speicher <= 0
