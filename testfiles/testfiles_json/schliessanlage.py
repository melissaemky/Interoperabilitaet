# Wenn karte vor tür (RFID-Sensor) gehalten wird und Karte in benutzer.ini als zugelassen gilt, dann fürhre funktion tuerauf() aus
# Endlosschleife durch drücken der beiden vorhandenen Knöpfe für gewisse Zeit unterbrechen
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from servo import tuerauf, tuerzu
import json


GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Löschen)

reader = SimpleMFRC522()


while True:
    if 1 == 0:  # GPIO.input(38) == 0 or GPIO.input(40) == 0:
        time.sleep(30)  # Hier fehlt noch speichern und löschen
    else:
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
                                if aktor == "haustür":
                                    # kann später weg
                                    print("Haustür gefunden")
                                    zustand = (x['aktoren'][k]['zustand'])
                                    if zustand == "0":
                                        # kann später weg
                                        print("Tür war zu, wird geöffnet")
                                        tuerauf()
                                        # Zustand "Türauf"
                                        (x['aktoren'][k]['zustand']) = "1"
                                        # Neuen Zustand speichern
                                        with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                                            json.dump(x, json_file, indent=4)
                                    else:
                                        # kann später weg
                                        print("Tür war auf, wird geschlossen")
                                        tuerzu()
                                        # Zustand "Türzu"
                                        (x['aktoren'][k]['zustand']) = "0"
                                        # Neuen Zustand speichern
                                        with open('/home/pi/config_dateien/universetest.json', 'w') as json_file:
                                            json.dump(
                                                x, json_file, indent=4)

    GPIO.cleanup()
