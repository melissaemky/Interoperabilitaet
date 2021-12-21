import json
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def speichern():
    id, text = reader.read()
    print("Timo ist doof")
    # universe.json laden und lesen:
    with open("/home/pi/config_dateien/universetest.json") as json_file:
        x = json.load(json_file)
    lk = len(x['karten'])  # Anzahl der gespeicherten Karten
    lb = len(x['benutzer'])  # Anzahl der gespeicherten Benutzer
    z = 0  # Hilfsvariable
    for i in range(0, lk):  # Gespeicherte Karten werden durchlaufen
        kartennummer = (x['karten'][i]['kartennummer'])
        if kartennummer == id:  # Karte wurde schonmal gespeichert
            kartenid = (x['karten'][i]['id'])
            for j in range(0, lb):  # Benutzer dieser Karte finden
                benutzerkarte = (x['benutzer'][j]['kartenid'])
                if kartenid == benutzerkarte:  # Benutzer gefunden
                    (x['benutzer'][j]['zugang']) = "ja"  # Zugang erlauben
                    # Aktualisierung in universe.json zurückschreiben:
                    with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                        json.dump(x, json_file, indent=4)
                    z = 1

        if i == lk-1 and z == 0:  # Alle Karten durchlaufen und keine passende gefunden
            # universe.json laden, lesen und ergänzen mit x:
            def write_benutzer(new_data, filename='/home/pi/config_dateien/universetest.json'):
                with open(filename, 'r+') as file:
                    file_data = json.load(file)
                    file_data["benutzer"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)

            # universe.json laden, lesen und ergänzen mit y:
            def write_karten(new_data, filename='/home/pi/config_dateien/universetest.json'):
                with open(filename, 'r+') as file:
                    file_data = json.load(file)
                    file_data["karten"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
            x = {
                "id": lb,
                "kartenid": lk,
                "zugang": "ja"
            }
            y = {
                "id": lk,
                "kartennummer": id
            }

            write_benutzer(x)
            write_karten(y)


def löschen():
    id, text = reader.read()
    # universe.json laden und lesen:
    with open("/home/pi/config_dateien/universetest.json") as json_file:
        x = json.load(json_file)
    lk = len(x['karten'])  # Anzahl der gespeicherten Karten
    lb = len(x['benutzer'])  # Anzahl der gespeicherten Benutzer
    for i in range(0, lk):  # Gespeicherte Karten werden durchlaufen
        kartennummer = (x['karten'][i]['kartennummer'])
        if kartennummer == id:  # Karte wurde schonmal gespeichert
            kartenid = (x['karten'][i]['id'])
            for j in range(0, lb):  # Benutzer dieser Karte finden
                benutzerkarte = (x['benutzer'][j]['kartenid'])
                if kartenid == benutzerkarte:  # Benutzer gefunden
                    (x['benutzer'][j]['zugang']) = "nein"  # Zugang verweigern
                    # Aktualisierung in universe.json zurückschreiben:
                    with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                        json.dump(x, json_file, indent=4)


def rfid_programming():
    # taster.json öffnen und Zustände der Taster in variablen speichern:
    with open("/home/pi/config_dateien/taster.json") as json_file:
        x = json.load(json_file)
        lt = len(x['taster'])
        for k in range(0, lt):
            taster = (x['taster'][k]['name'])
            if taster == "gruen":
                zustandgruen = (x['taster'][k]['zustand'])
            if taster == "blau":
                zustandblau = (x['taster'][k]['zustand'])

    # Wenn Grüner/Blauer Taster gedrückt, dann speichern/Löschen ausführen:
    if zustandgruen == "1":
        speichern()
    if zustandblau == "1":
        löschen()
