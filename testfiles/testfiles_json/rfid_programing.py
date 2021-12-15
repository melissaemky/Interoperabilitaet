import json
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def speichern():
    id, text = reader.read()
    print("Karte gelesen " + str(id))

    with open("/home/pi/config_dateien/universetest.json") as json_file:
        x = json.load(json_file)
    print("Json geladen")  # kann später weg
    lk = len(x['karten'])
    k = lk+1
    lb = len(x['benutzer'])
    b = lb+1
    for i in range(0, lk):
        print("in der for schleife")  # kann später weg
        kartennummer = (x['karten'][i]['kartennummer'])
        print(str(i) + "te Kartennummer " +
              str(kartennummer))  # kann später weg
        if kartennummer == str(id):
            print("if abfrage ist wahr")  # kann später weg
            kartenid = (x['karten'][i]['id'])
            print("Kartennummer gefunden")  # kann später weg
            for j in range(0, lb):
                benutzerkarte = (x['benutzer'][j]['kartenid'])
                if kartenid == benutzerkarte:
                    zugang = (x['benutzer'][j]['zugang'])
                    zugang == "ja"
                    print("Zugang auf 'ja' gesetzt")  # kann später weg
        else:
            (x['karten'][k])


def löschen():
    id, text = reader.read()
    print("Karte gelesen " + str(id))

    with open("/home/pi/config_dateien/universetest.json") as json_file:
        x = json.load(json_file)
    print("Json geladen")  # kann später weg


with open("/home/pi/config_dateien/taster.json") as json_file:
    x = json.load(json_file)
    lt = len(x['taster'])
    for k in range(0, lt):
        taster = (x['taster'][k]['name'])
        if taster == "grün":
            print("Grüner taster gefunden")  # kann später weg
            zustandgrün = (x['taster'][k]['zustand'])
        if taster == "blau":
            print("blauer taster gefunden")  # kann später weg
            zustandblau = (x['taster'][k]['zustand'])

if zustandgrün == "1":
    speichern()
if zustandblau == "1":
    löschen()
