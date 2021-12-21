import json
from servo import tuerauf, tuerzu, tuerini
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

with open("/home/pi/config_dateien/universetest.json") as json_file:
    x = json.load(json_file)
    la = len(x['aktoren'])
    for k in range(0, la):
        aktor = (x['aktoren'][k]['typ'])
        if aktor == "haustuer":
            print("Haustür gefunden")  # kann später weg
            zustand = (x['aktoren'][k]['zustand'])
            zustand = "0"
            with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                json.dump(x, json_file, indent=4)

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

if zustandgrün == "0" and zustandblau == "0":
    id, text = reader.read()
    print("Karte gelesen " + str(id))

    with open("/home/pi/config_dateien/universetest.json") as json_file:
        x = json.load(json_file)
    print("Json geladen")  # kann später weg
    lk = len(x['karten'])
    lb = len(x['benutzer'])
    la = len(x['aktoren'])
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
                    print("Benutzer gefunden")  # kann später weg
                    if zugang == "ja":
                        print("Zugang: ja")  # kann später weg
                        for k in range(0, la):
                            aktor = (x['aktoren'][k]['typ'])
                            if aktor == "haustuer":
                                # kann später weg
                                print("Haustür gefunden")
                                zustand = (x['aktoren'][k]['zustand'])
                                if zustand == "0":
                                    # kann später weg
                                    print("Tür war zu, wird geöffnet")
                                    tuerini()
                                    tuerauf()
                                    # Zustand "Türauf"
                                    (x['aktoren'][k]['zustand']) = "1"
                                    # Neuen Zustand speichern
                                    with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                                        json.dump(x, json_file, indent=4)
                                else:
                                    # kann später weg
                                    print("Tür war auf, wird geschlossen")
                                    tuerini()
                                    tuerzu()
                                    # Zustand "Türzu"
                                    (x['aktoren'][k]['zustand']) = "0"
                                    # Neuen Zustand speichern
                                    with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                                        json.dump(x, json_file, indent=4)
