import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import configparser
cfg = configparser.ConfigParser()

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Speichern)

id = ''


def speichern():
    id, text = reader.read()
    cfg.read('/home/pi/interoperabilitaet/config_dateien/benutzer.ini')
    cfg.add_section(str(id))
    cfg.write(cfg)
    cfg.close()


def löschen():
    id, text = reader.read()
    cfg.read('/home/pi/interoperabilitaet/config_dateien/benutzer.ini')
    cfg.remove_section(str(id))
    cfg.write(cfg)
    cfg.close()


while True:
    if GPIO.input(40) == 0:
        time.sleep(5)
        speichern()
        print(id)
    if GPIO.input(38) == 0:
        time.sleep(5)
        löschen()
        print(id)
