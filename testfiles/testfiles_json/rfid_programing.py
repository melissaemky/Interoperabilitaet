import json
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
    y = {
        "id": k+1,
        "kartennummer": id
    }
    z = {
        "id": b+1,
        "kartenid": k+1,
        "zugang": "ja"
    }
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
        '''
        else:
            with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                json.dump(y['karten'], z['benutzer'], json_file, indent=4)
                '''


def löschen():
    id, text = reader.read()
    print("Karte gelesen " + str(id))

    with open("/home/pi/config_dateien/universetest.json") as json_file:
        x = json.load(json_file)
    print("Json geladen")  # kann später weg
    lk = len(x['karten'])
    lb = len(x['benutzer'])
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
                    zugang == "nein"
                    print("Zugang auf 'nein' gesetzt")  # kann später weg


with open("/home/pi/config_dateien/taster.json") as json_file:
    x = json.load(json_file)
    print(type(x))
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
    speichern()  # Speichert noch nichts neues
if zustandblau == "1":
    löschen()
