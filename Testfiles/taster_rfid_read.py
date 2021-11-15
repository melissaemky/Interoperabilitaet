import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Blauer Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Grüner Taser(Speichern)

l = []


def speichern():
    id, text = reader.read()
    l.append(id)


while True:
    if GPIO.input(40) == 0:
        time.sleep(5)
        speichern()
        print(id)
        time.sleep(2)
        x = l.pop()
        print(x)
    if GPIO.input(38) == 0:
        print("Blauer Taster gedrückt")
        time.sleep(2)
