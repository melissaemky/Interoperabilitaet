import json
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def löschen():
    id, text = reader.read()
    # schliessanlage.json laden und lesen:
    with open("/home/pi/config_dateien/schliessanlage.json") as json_file:
        x = json.load(json_file)
    lk = len(x["karten"])  # Anzahl der gespeicherten Karten
    lb = len(x["benutzer"])  # Anzahl der gespeicherten Benutzer
    for i in range(0, lk):  # Gespeicherte Karten werden durchlaufen
        kartennummer = x["karten"][i]["kartennummer"]
        if kartennummer == id:  # Karte wurde schonmal gespeichert
            kartenid = x["karten"][i]["id"]
            for j in range(0, lb):  # Benutzer dieser Karte finden
                benutzerkarte = x["benutzer"][j]["kartenid"]
                if kartenid == benutzerkarte:  # Benutzer gefunden
                    (x["benutzer"][j]["zugang"]) = "nein"  # Zugang verweigern
                    # Aktualisierung in schliessanlage.json zurückschreiben:
                    with open(
                        "/home/pi/config_dateien/schliessanlage.json", "w"
                    ) as json_file:
                        json.dump(x, json_file, indent=4)
                    print("Der Zugang wurde verweigert.")


löschen()
