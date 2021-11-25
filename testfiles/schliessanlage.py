# Wenn karte vor tür (RFID-Sensor) gehalten wird und Karte in benutzer.ini als zugelassen gilt, dann fürhre funktion tuerauf() aus
# Endlosschleife durch drücken der beiden vorhandenen Knöpfe für gewisse Zeit unterbrechen
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from servo import tuerauf, tuerzu
import configparser
cfg = configparser.ConfigParser()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Löschen)

reader = SimpleMFRC522()

while True:
    if GPIO.input(38) == 0 or GPIO.input(40) == 0:
        time.sleep(30)
    else:
        try:
            id, text = reader.read()
            print(id)
        finally:
            GPIO.cleanup()
        if cfg.has_section(str(id)) == True:
            tuerauf
        else:
            tuerzu
