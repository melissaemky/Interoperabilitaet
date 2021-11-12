import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)  # Grüner Taster(Speichern)
GPIO.setup(20, GPIO.IN)  # Blauer Taser(Speichern)

l = []


def speichern():
    id, text = reader.read()
    l.append(id)


while True:
    if GPIO.input(21) == 0:
        speichern()
        print(reader)
        time.sleep(2)
    if GPIO.input(20) == 0:
        print("Blauer Taster gedrückt")
        time.sleep(2)
