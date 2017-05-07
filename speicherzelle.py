class Speicherzelle:

    def __init__(self, daten = ""):
        self.daten = daten

    def __repr__(self):
        return (str(self.__class__.__name__) +
                "(" + repr(self.daten) + ")")
