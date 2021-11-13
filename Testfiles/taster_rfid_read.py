import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)  # Grüner Taster(Speichern)
GPIO.setup(40, GPIO.IN)  # Blauer Taser(Speichern)

l = []
x = l.pop()


def speichern():
    id, text = reader.read()
    l.append(id)


while True:
    if GPIO.input(38) == 0:
        speichern()
        print(reader)
        time.sleep(2)
        print(x)
    if GPIO.input(40) == 0:
        print("Blauer Taster gedrückt")
        time.sleep(2)