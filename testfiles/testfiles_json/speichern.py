import json
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
reader = SimpleMFRC522()


def speichern():
    print("Speichern gestartet")
    id, text = reader.read()
    print(id)
    # schliessanlage.json laden und lesen:
    with open("/home/pi/config_dateien/schliessanlage.json") as json_file:
        x = json.load(json_file)
    lk = len(x["karten"])  # Anzahl der gespeicherten Karten
    lb = len(x["benutzer"])  # Anzahl der gespeicherten Benutzer
    z = 0  # Hilfsvariable
    for i in range(0, lk):  # Gespeicherte Karten werden durchlaufen
        kartennummer = x["karten"][i]["kartennummer"]
        if kartennummer == id:  # Karte wurde schonmal gespeichert
            kartenid = x["karten"][i]["id"]
            for j in range(0, lb):  # Benutzer dieser Karte finden
                benutzerkarte = x["benutzer"][j]["kartenid"]
                if kartenid == benutzerkarte:  # Benutzer gefunden
                    (x["benutzer"][j]["zugang"]) = "ja"  # Zugang erlauben
                    # Aktualisierung in schliessanlage.json zurückschreiben:
                    with open(
                        "/home/pi/config_dateien/schliessanlage.json", "w"
                    ) as json_file:
                        json.dump(x, json_file, indent=4)
                    z = 1
                    print("Der Zugang wurde gestattet.")

        if (
            i == lk - 1 and z == 0
        ):  # Alle Karten durchlaufen und keine passende gefunden
            # schliessanlage.json laden, lesen und ergänzen mit x:
            def write_benutzer(
                new_data, filename="/home/pi/config_dateien/schliessanlage.json"
            ):
                with open(filename, "r+") as file:
                    file_data = json.load(file)
                    file_data["benutzer"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)

            # schliessanlage.json laden, lesen und ergänzen mit y:
            def write_karten(
                new_data, filename="/home/pi/config_dateien/schliessanlage.json"
            ):
                with open(filename, "r+") as file:
                    file_data = json.load(file)
                    file_data["karten"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)

            x = {"id": lb, "kartenid": lk, "zugang": "ja"}
            y = {"id": lk, "kartennummer": id}

            write_benutzer(x)
            write_karten(y)
            print("Der Benutzer wurde gespeichert und der Zugang wurde gestattet.")


speichern()
