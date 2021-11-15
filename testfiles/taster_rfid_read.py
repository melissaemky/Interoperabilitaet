import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import configparser
import datetime
cfg = configparser.ConfigParser()

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Speichern)


def speichern():
    id, text = reader.read()
    if cfg.has_section(id) == True:
        cfgfile = open(
            "/home/pi/interoperabilitaet/config_dateien/benutzer.ini", 'w')
        cfg.set(str(id), 'zugang', 'gestattet')
        cfg.set(str(id), 'gespeichert am', datetime.now())
        cfg.write(cfgfile)
        cfgfile.close()
        print(id + " Zugang gestattet")
    else:
        cfgfile = open(
            "/home/pi/interoperabilitaet/config_dateien/benutzer.ini", 'w')
        cfg.add_section(str(id))
        cfg.set(str(id), 'zugang', 'gestattet')
        x = datetime.now()
        cfg.set(str(id), 'gespeichert am', str(x))
        cfg.write(cfgfile)
        cfgfile.close()
        print(id + " gespeichert und Zugang gestattet")


def löschen():
    id, text = reader.read()
    if cfg.has_section(id) == True:
        cfgfile = open(
            "/home/pi/interoperabilitaet/config_dateien/benutzer.ini", 'w')
        cfg.set(str(id), 'zugang', 'verweigert')
        x = datetime.now()
        cfg.set(str(id), 'gelöscht am', str(x))
        cfg.write(cfgfile)
        cfgfile.close()
        print(id + " Zugang verweigert")
    else:
        print("Karte noch nie gespeichert!")


while True:
    cfg.read('/home/pi/interoperabilitaet/config_dateien/benutzer.ini')
    if GPIO.input(40) == 0:
        time.sleep(5)
        speichern()
    if GPIO.input(38) == 0:
        time.sleep(5)
        löschen()
