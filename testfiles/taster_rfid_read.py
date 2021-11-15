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
    cfgfile = open(
        "/home/pi/interoperabilitaet/config_dateien/benutzer.ini", 'w')
    cfg.add_section(str(id))
    cfg.write(cfgfile)
    cfgfile.close()


def löschen():
    id, text = reader.read()


while True:
    if GPIO.input(40) == 0:
        time.sleep(5)
        speichern()
        time.sleep(2)
        print(id)
    if GPIO.input(38) == 0:
        time.sleep(5)
        löschen()
        time.sleep(2)
        print(id)
