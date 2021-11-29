import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
from datetime import datetime
import xml.etree.ElementTree as ET
tree = ET.parse('univers.xml')
root = tree.getroot()

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Löschen)


def speichern():
    id, text = reader.read()
    print(root.benutzer(str(id)))
    if root.benutzer(str(id)) == True:
        print("Karte bekannt")
        cfgfile = open(
            "/home/pi/config_dateien/benutzer.ini", 'w')
        cfg.set(str(id), 'zugang', 'gestattet')
        x = datetime.now()
        cfg.set(str(id), 'gespeichert am', str(x))
        cfg.write(cfgfile)
        cfgfile.close()
        print(str(id) + " Zugang gestattet")
    else:
        print("Karte unbekannt")
        cfgfile = open(
            "/home/pi/config_dateien/benutzer.ini", 'w')
        cfg.add_section(str(id))
        cfg.set(str(id), 'zugang', 'gestattet')
        x = datetime.now()
        cfg.set(str(id), 'gespeichert am', str(x))
        cfg.write(cfgfile)
        cfgfile.close()
        print(str(id) + " gespeichert und Zugang gestattet")


def löschen():
    id, text = reader.read()
    print(cfg.has_section(str(id)))
    if cfg.has_section(str(id)) == True:
        cfgfile = open(
            "/home/pi/config_dateien/benutzer.ini", 'w')
        cfg.set(str(id), 'zugang', 'verweigert')
        x = datetime.now()
        cfg.set(str(id), 'gelöscht am', str(x))
        cfg.write(cfgfile)
        cfgfile.close()
        print(str(id) + " Zugang verweigert")
    else:
        print("Karte noch nie gespeichert!")


while True:
    cfg.read('/home/pi/config_dateien/benutzer.ini')
    if GPIO.input(40) == 0:
        time.sleep(1)
        speichern()
    if GPIO.input(38) == 0:
        time.sleep(1)
        löschen()
