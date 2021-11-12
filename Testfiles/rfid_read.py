#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setup(21, GPIO.IN)
while True:
    if GPIO.input(21) == 1:
        print("Bitte Karte zum Speichern auflegen!")
    if GPIO.input(16) == 1:
        print("Bitte Karte zum Löschen auflegen!")

try:
    id, text = reader.read()
    print(id)
finally:
    GPIO.cleanup()
