import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)  # Grüner Taster(Speichern)

while True:
    if GPIO.input(7) == 0:
        os.system("git pull")