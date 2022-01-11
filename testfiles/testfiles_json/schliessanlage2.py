import json
from schrittmotor import forward, backwards
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


# def schliessanlage():
while True:
    # universe.json laden und lesen:
    with open("/home/pi/config_dateien/universe.json") as json_file:
        x = json.load(json_file)
        la = len(x["aktoren"])  # Anzahl der gespeicherten Aktoren
        for k in range(0, la):  # Gespeicherte Aktoren werden durchlaufen
            aktor = x["aktoren"][k]["typ"]
            if aktor == "haustuer":  # Benötigter Aktor gefunden
                zustand = x["aktoren"][k]["zustand"]
                zustand = "0"  # Zustand auf "0" gesetzt (Grundzustand)
                with open("/home/pi/config_dateien/universe.json", "w") as json_file:
                    json.dump(x, json_file, indent=4)

    # taster.json öffnen und Zustände der Taster in variablen speichern:
    with open("/home/pi/config_dateien/taster.json") as json_file:
        x = json.load(json_file)
        lt = len(x["taster"])
        for k in range(0, lt):
            taster = x["taster"][k]["name"]
            if taster == "gruen":
                zustandgruen = x["taster"][k]["zustand"]
            if taster == "blau":
                zustandblau = x["taster"][k]["zustand"]

    # Schließanlage funktioniert nur, wenn momentan Karten weder gespeichert, noch gelöscht werden sollen:
    if zustandgruen == "0" and zustandblau == "0":
        id, text = reader.read()
        with open("/home/pi/config_dateien/universe.json") as json_file:
            x = json.load(json_file)
        lk = len(x["karten"])  # Anzahl der gespeicherten Karten
        lb = len(x["benutzer"])  # Anzahl der gespeicherten Benutzer
        la = len(x["aktoren"])  # Anzahl der gespeicherten Aktoren
        for i in range(0, lk):  # Gespeicherte Karten werden durchlaufen
            kartennummer = x["karten"][i]["kartennummer"]
            if kartennummer == id:  # Karte wurde schonmal gespeichert
                kartenid = x["karten"][i]["id"]
                for j in range(0, lb):  # Benutzer dieser Karte finden
                    benutzerkarte = x["benutzer"][j]["kartenid"]
                    if kartenid == benutzerkarte:  # Benutzer gefunden
                        zugang = x["benutzer"][j]["zugang"]
                        if zugang == "ja":  # Benutzer hat Zugang
                            for k in range(0, la):  # Haustür finden
                                aktor = x["aktoren"][k]["typ"]
                                if aktor == "haustuer":  # Haustür gefunden
                                    zustand = x["aktoren"][k]["zustand"]
                                    # Wenn Haustür geschlossen ist, dann öffnen:
                                    if zustand == "0":
                                        backwards(1, int(20))
                                        print("Tür ist geöffnet!")
                                        # Zustand auf "Geöffnet"
                                        (x["aktoren"][k]["zustand"]) = "1"
                                        # Neuen Zustand speichern:
                                        with open(
                                            "/home/pi/config_dateien/universe.json", "w"
                                        ) as json_file:
                                            json.dump(x, json_file, indent=4)
                                    else:
                                        # Wenn Haustür geöffnet ist, dann schließen:
                                        forward(1, int(200))
                                        print("Tür ist geschlossen!")
                                        # Zustand auf "Geschlossen"
                                        (x["aktoren"][k]["zustand"]) = "0"
                                        # Neuen Zustand speichern:
                                        with open(
                                            "/home/pi/config_dateien/universe.json", "w"
                                        ) as json_file:
                                            json.dump(x, json_file, indent=4)
