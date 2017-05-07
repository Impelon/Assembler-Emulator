from adressbus import Adressbus
from akku import AKKU
from alu import ALU
from befehlsregister import Befehlsregister
from befehlszaehler import Befehlszaehler
from datenbus import Datenbus
from speicher import Speicher

befehlszaehler  = Befehlszaehler()
akku            = AKKU()
alu             = ALU(akku)
speicher        = Speicher(128)
adressbus       = Adressbus(speicher, befehlszaehler)
datenbus        = Datenbus(speicher, alu, akku, befehlszaehler)
befehlsregister = Befehlsregister(datenbus, adressbus)

speicher.vonFestplatteLaden("input.txt")

print speicher.zellen

while True:
    d = datenbus.speicher.zellen[adressbus.befehlszaehler.adresse].daten.split(" ", 1)
    befehlsregister.befehl = d[0]
    if len(d) <= 1:
        befehlsregister.adresse = ""
    else:
        befehlsregister.adresse = d[1]
    datenbus.befehlszaehler.adresse += 1
    if not befehlsregister.parse():
        break
    
speicher.aufFestplatteSpeichern("output.txt")
