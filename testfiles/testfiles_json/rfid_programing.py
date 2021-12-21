import json
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def speichern():
    id, text = reader.read()
    print("Karte gelesen " + str(id))
    print(type(id))
    with open("/home/pi/config_dateien/universetest.json") as json_file:
        x = json.load(json_file)
    print("Json geladen")  # kann später weg
    lk = len(x['karten'])
    print("lk " + str(lk))
    lb = len(x['benutzer'])
    print("lb " + str(lb))
    for i in range(0, lk):
        print("in der for schleife")  # kann später weg
        kartennummer = (x['karten'][i]['kartennummer'])
        print("kartennummer " + type(kartennummer))
        print(str(i) + "te Kartennummer " +
              str(kartennummer))  # kann später weg
        if kartennummer == id:
            print("if abfrage ist wahr")  # kann später weg
            kartenid = (x['karten'][i]['id'])
            print("kartenid " + type(kartenid))
            print("Kartennummer gefunden")  # kann später weg
            for j in range(0, lb):
                benutzerkarte = (x['benutzer'][j]['kartenid'])
                if kartenid == benutzerkarte:
                    (x['benutzer'][j]['zugang']) = "ja"
                    with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                        json.dump(x, json_file, indent=4)
                    print("Zugang auf 'ja' gesetzt")  # kann später weg
        else:
            print("Karte existiert noch nicht " + str(id))

            def write_benutzer(new_data, filename='/home/pi/config_dateien/universetest.json'):
                with open(filename, 'r+') as file:
                    file_data = json.load(file)
                    file_data["benutzer"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)

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
            print("Kartennummer gefunden" + kartenid)  # kann später weg
            for j in range(0, lb):
                benutzerkarte = (x['benutzer'][j]['kartenid'])
                if kartenid == benutzerkarte:
                    (x['benutzer'][j]['zugang']) = "nein"
                    with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                        json.dump(x, json_file, indent=4)
                    print("Zugang auf 'nein' gesetzt")  # kann später weg


with open("/home/pi/config_dateien/tastertast.json") as json_file:
    x = json.load(json_file)
    lt = len(x['taster'])
    for k in range(0, lt):
        taster = (x['taster'][k]['name'])
        if taster == "gruen":
            print("Grüner taster gefunden")  # kann später weg
            zustandgruen = (x['taster'][k]['zustand'])
        if taster == "blau":
            print("blauer taster gefunden")  # kann später weg
            zustandblau = (x['taster'][k]['zustand'])

if zustandgruen == "1":
    speichern()
if zustandblau == "1":
    löschen()
