from speicherzelle import Speicherzelle

class Speicher:

    def __init__(self, kapazitaet):
        self.zellen = [Speicherzelle() for n in range(kapazitaet)]

    def vonFestplatteLaden(self, pfad):
        pfad = str(pfad)
        try:
            f = open(pfad, "r+")
            try:
                while True:
                    ln = f.readline()
                    if ln == "":
                        break
                    ln = ln.split(" ", 1)
                    self.zellen[int(ln[0])].daten = ln[1][:-1]
            except:
                f.close()
                raise RuntimeWarning("Datei konnte vom Pfad '" + pfad + "' nur bedingt geladen werden. Fehler bei Position " + str(zaehler))
            f.close()
        except:
                raise RuntimeWarning("Pfad '" + pfad + "' konnte nicht zum laden geoeffnet werden.")
        
    def aufFestplatteSpeichern(self, pfad):
        pfad = str(pfad)
        try:
            f = open(pfad, "w+")
            try:
                zaehler = 0
                while zaehler < len(self.zellen):
                    f.write(str(zaehler) + " " + self.zellen[zaehler].daten + "\n")
                    zaehler += 1
            except:
                f.close()
                raise RuntimeWarning("Datei konnte im Pfad '" + pfad + "' nur bedingt gespeichert werden. Fehler bei Position " + str(zaehler))
            f.close()
        except:
            raise RuntimeWarning("Pfad '" + pfad + "' konnte nicht zum speichern geoeffnet werden.")
