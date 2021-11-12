import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)  # Grüner Taster(Speichern)
GPIO.setup(20, GPIO.IN)  # Blauer Taser(Speichern)

while True:
    if GPIO.input(21) == 0:
        print("Grüner Taster gedrückt")
        time.sleep(10)
    if GPIO.input(20) == 0:
        print("Blauer Taster gedrückt")
        time.sleep(10)
