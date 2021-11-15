import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import configparser

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Speichern)

l = []
id = ''

logfile = open('/home/pi/Heizungssteuerung/logfile.txt','a')

cfg = configparser.ConfigParser()
cfg.read('/home/pi/Heizungssteuerung/heizung-config.ini')

heizdauer = cfg.get('Parameter', 'Heizdauer')

cfgfile = open("/home/pi/Heizungssteuerung/heizung-config.ini",'w')
cfg.set('DoNotChange','heizen',str(heizung_status))
cfg.set('DoNotChange','letzteheizperiode', letzte_heizung.strftime("%d/%m/%Y, %H:%M:%S")) 
cfg.write(cfgfile)
cfgfile.close()


def speichern():
    id, text = reader.read()
    l.append(id)


def löschen():
    id, text = reader.read()
    l.remove(id)


while True:
    if GPIO.input(40) == 0:
        time.sleep(5)
        speichern()
        time.sleep(2)
        x = l.pop()
        print(id)
        print(x)
    if GPIO.input(38) == 0:
        time.sleep(5)
        löschen()
        time.sleep(2)
        print(id)
        #print(*l, sep="\n")
